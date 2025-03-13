import argparse
import toolkit
from tqdm import tqdm
from openai import OpenAI
import ollama

def parse_arguments():
    parser = argparse.ArgumentParser(description="run to get response and get value precision")

    # 添加我们希望解析的命令行参数
    parser.add_argument("-s", "--split", type=str, default="train", help="Split: train or test")

    # Analyze command-line parameters
    args = parser.parse_args()

    # Return parsed parameters
    return args

'''
调用付费api
模型默认使用gpt-4o
'''
def run_llm(user_input, model_name = "gpt-4o", sys_input = "You are a helpful assistant."):
    client = OpenAI(
        base_url = "https://xiaoai.plus/v1",
        api_key = "sk-s1VtI20SlpB6fPj05aB17e566b2646B2862bB3D5289cE177"
    )
    completion = client.chat.completions.create(
    model = model_name,
    messages = [
        {"role": "system", "content": sys_input},
        {"role": "user", "content": user_input}
    ]
    )
    return completion.choices[0].message.content

'''
调用ollama api
模型默认使用llama2
'''
def process_with_ollama(user_input, model_name = "llama2", sys_input = "You are a helpful assistant."):
    # print('Starting to process with ollama, note that this can take several minutes…')
    response = ollama.chat(
        model = model_name,
        messages = [ {'role': 'system', 'content': sys_input}, 
                     {'role': 'user', 'content': user_input}, ]
    )

    return response['message']['content']




# 直接做QA的模板
QA_TEMPLATE = """
Answer the following multiple-choice question by selecting only the correct option (A, B, C, or D). Do not provide an explanation.

{question_choice}

Format: Return only a single uppercase letter (A, B, C, or D).

Answer:
"""

'''
将question和choice处理成我们想要的格式
'''
def format_qc(data):
    question = data['\ufeffquestion']
    choice_A = data['A']
    choice_B = data['B']
    choice_C = data['C']
    choice_D = data['D']
    qc = "Question: " + question + "\n\nA:" + choice_A + "\nB:" + choice_B + "\nC:" + choice_C + "\nD:" + choice_D
    
    return qc


'''
为选择题生成答案
'''
def get_response(dataset, llm_name, save_path):
    print("Get response...")
    new_dataset = []
    for idx, data in tqdm(enumerate(dataset)):
        input = QA_TEMPLATE.replace("{question_choice}", format_qc(data))
        choice = run_llm(input, llm_name)
        data['choice'] = choice
        new_dataset.append(data)
        if idx % 100 == 0 and idx != 0:
            toolkit.write_to_json(new_dataset, save_path[:-5]+"_"+str(idx)+".json")
    toolkit.write_to_json(new_dataset, save_path)

def get_response_ollama(dataset, llm_name, save_path):
    print("Get response from ollama...")
    new_dataset = []
    for idx, data in tqdm(enumerate(dataset)):
        input = QA_TEMPLATE.replace("{question_choice}", format_qc(data))
        choice = process_with_ollama(input, llm_name)
        data['choice'] = choice
        new_dataset.append(data)
        if idx % 100 == 0 and idx != 0:
            toolkit.write_to_json(new_dataset, save_path[:-5]+"_"+str(idx)+".json")
        # break
    toolkit.write_to_json(new_dataset, save_path)



# 为question生成explanation的模板
EXPLANATION_TEMPLATE = """
Identify and explain the key technical terms in the following question. Provide a concise definition for each term.

Question: {question}

Output format:
- **Term 1**: Definition
- **Term 2**: Definition
- **Term 3**: Definition
...
"""

'''
为题目生成名词解释
'''
def get_knowledge(dataset, llm_name, save_path):
    print("Get knowledge...")
    new_dataset = []
    for idx, data in tqdm(enumerate(dataset)):
        question = data['\ufeffquestion']
        ans = run_llm(EXPLANATION_TEMPLATE.replace('{question}', question), llm_name)
        data['explanation'] = ans
        new_dataset.append(data)
        if idx % 100 == 0 and idx != 0:
            toolkit.write_to_json(new_dataset, save_path[:-5]+"_"+str(idx)+".json")
    toolkit.write_to_json(new_dataset, save_path)


# 加入知识后的模板
KNOWLEDGE_QA_TEMPLATE = """
### Step 1: Learning Phase
First, I will provide you with some background knowledge. Use this knowledge as a reference when answering, but feel free to apply reasoning and prior understanding where necessary.

[START KNOWLEDGE]
{knowledge}
[END KNOWLEDGE]

### Step 2: Question Phase
Now, based on the knowledge above, answer the following question:

Question: {question}

### Answer Guidelines:
1. Your answer should be **informed by the provided knowledge**, but you may also incorporate relevant reasoning.
2. If the question is multiple-choice, return only the correct option (A, B, C, or D).

Answer:
"""


'''
将knowledge处理成我们想要的格式
'''
def format_knowledge(data):
    knowledge = ""
    for idx, k in enumerate(data['explanation']):
        knowledge = knowledge + str(idx+1) + "." + k + "\n"

    return knowledge


'''
根据knowledge为选择题生成答案
'''
def get_knowledge_response(dataset, llm_name, save_path):
    print("Get knowledge response...")
    new_dataset = []
    for idx, data in tqdm(enumerate(dataset)):
        input = KNOWLEDGE_QA_TEMPLATE.replace('{knowledge}', format_knowledge(data)).replace('{question}', format_qc(data))
        # print(input)
        choice = run_llm(input, llm_name)
        # print(choice)
        data['choice'] = choice
        new_dataset.append(data)
        if idx % 100 == 0 and idx != 0:
            toolkit.write_to_json(new_dataset, save_path[:-5]+"_"+str(idx)+".json")
        # if 1 == idx:
        #     break       
    toolkit.write_to_json(new_dataset, save_path)






if __name__ == "__main__":
    dataset = toolkit.load_json_data("./train_dataset_en_explanation_list.json")
    # dataset = toolkit.load_csv_data("./train_dataset_en.csv")
    # print(dataset[0]['\ufeffquestion'])
    # get_response(dataset, "claude-3-5-sonnet-20241022", "./train_dataset_en_choice.json")
    # get_knowledge(dataset, "claude-3-5-sonnet-20241022", "./train_dataset_en_explanation.json")
    get_knowledge_response(dataset, "claude-3-5-sonnet-20241022", "./train_dataset_en_explanation_list_choice.json")
    # get_response_ollama(dataset, "mistral:latest", "./train_dataset_en_choice_mistral.json")
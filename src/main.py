import argparse
import toolkit
from tqdm import tqdm
import prompt_template

def parse_arguments():
    parser = argparse.ArgumentParser(description="run to get response and get value precision")

    # 添加我们希望解析的命令行参数
    # platform代表我们调用模型的平台，分别是ollama和付费的api，ollama可以调用一些免费的小模型，paid_api可以调用GPT-4o、Claude等付费模型（来源于https://flowus.cn/share/de98cb21-3c6d-4561-b6ac-648daa2bacda）。
    parser.add_argument("-p", "--platform", type=str, default="ollama", help="Platform: Select the platform named ollama or paid_api")
    parser.add_argument("-d", "--dataset", type=str, default="train_dataset_en", help="Dataset")
    parser.add_argument("-m", "--model", type=str, default="vicuna", help="Model: vicuna, mistral, llama2, llama3, aplaca2, alpaca3, gpt-35-turbo")
    parser.add_argument("-c", "--cl", type=str, default="original", help="Class: original or rag")
    
    # 设置数据的处理范围，range代表是否有范围，
    parser.add_argument("-r", "--range", action="store_true", help="Range: This parameter is a switch. Open it and you can set the start and end 'No.', but be sure to keep it within the range of the dataset.")
    parser.add_argument("-start", "--start_idx", type=int, default=0, help="Start_idx: Starting position of dataset slice.")
    parser.add_argument("-end", "--end_idx", type=int, default=None, help="End_idx: End position of dataset slice.")

    # Analyze command-line parameters
    args = parser.parse_args()

    # Return parsed parameters
    return args


'''
为题目生成名词解释
'''
def get_knowledge(dataset, llm_name, save_path):
    print("Get knowledge...")
    new_dataset = []
    for idx, data in tqdm(enumerate(dataset)):
        question = data['question']
        ans = toolkit.run_llm(prompt_template.EXPLANATION_TEMPLATE.replace('{question}', question), llm_name)
        data['explanation'] = ans
        new_dataset.append(data)
        if idx % 100 == 0 and idx != 0:
            toolkit.write_to_json(new_dataset, save_path[:-5]+"_"+str(idx)+".json")
    toolkit.write_to_json(new_dataset, save_path)


'''
将question和choice处理成我们想要的格式
'''
def format_qc(data):
    question = data['question']
    choice_A = data['A']
    choice_B = data['B']
    choice_C = data['C']
    choice_D = data['D']
    qc = "Question: " + question + "\n\nA:" + choice_A + "\nB:" + choice_B + "\nC:" + choice_C + "\nD:" + choice_D
    
    return qc


'''
为选择题生成答案
'''
def get_response(dataset, save_path, input_args):
    print("Get response from ", input_args.platform, "--", input_args.model)
    new_dataset = []
    for idx, data in tqdm(enumerate(dataset)):
        input = prompt_template.QA_TEMPLATE.replace("{question_choice}", format_qc(data))
        if input_args.platform == "ollama":
            choice = toolkit.process_with_ollama(input, input_args.model)
        elif input_args.platform == "paid_api":
            choice = toolkit.process_with_api(input, input_args.model)
        else:
            print("Please select a correct platform...")
        data['choice'] = choice
        new_dataset.append(data)
        if idx % 100 == 0 and idx != 0:
            toolkit.write_to_json(new_dataset, save_path[:-5]+"_"+str(idx)+".json")
        # break
    toolkit.write_to_json(new_dataset, save_path)


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
def get_knowledge_response(dataset, llm_name, save_path, input_args):
    print("Get knowledge response...")
    new_dataset = []
    for idx, data in tqdm(enumerate(dataset)):
        input = prompt_template.KNOWLEDGE_QA_TEMPLATE.replace('{knowledge}', format_knowledge(data)).replace('{question}', format_qc(data))
        if input_args.platform == "ollama":
            choice = toolkit.process_with_ollama(input, llm_name)
        elif input_args.platform == "paid_api":
            choice = toolkit.run_llm(input, llm_name)
        else:
            print("Please select a correct platform...")
        # print(choice)
        data['choice'] = choice
        new_dataset.append(data)
        if idx % 100 == 0 and idx != 0:
            toolkit.write_to_json(new_dataset, save_path[:-5]+"_"+str(idx)+".json")
        # if 1 == idx:
        #     break       
    toolkit.write_to_json(new_dataset, save_path)


# python main.py -p ollama -d 'train_dataset_en' -m mistral -c original
if __name__ == "__main__":
    args = parse_arguments()
    print("Running with arguments: ", args)

    dataset_path = "../data/" + args.dataset + ".json"
    dataset = toolkit.load_json_data(dataset_path)

    save_path = "../experiments/" + args.cl + "_" + args.model + ".json"

    get_response(dataset, save_path, args)

    # print(dataset[0])

    # dataset = toolkit.load_json_data("./train_dataset_en_explanation_list.json")
    # dataset = toolkit.load_csv_data("./train_dataset_en.csv")
    # print(dataset[0]['\ufeffquestion'])
    # get_response(dataset, "claude-3-5-sonnet-20241022", "./train_dataset_en_choice.json")
    # get_knowledge(dataset, "claude-3-5-sonnet-20241022", "./train_dataset_en_explanation.json")
    # get_knowledge_response(dataset, "claude-3-5-sonnet-20241022", "./train_dataset_en_explanation_list_choice.json")
    # get_response_ollama(dataset, "mistral:latest", "./train_dataset_en_choice_mistral.json")
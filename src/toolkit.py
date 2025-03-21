'''
Author: xvbingbing 932756577@qq.com
Date: 2024-07-3 09:20:05
LastEditors: xvbingbing 932756577@qq.com
FilePath: ValueAlignment/src/toolkit.py
Description: This is a toolkit.
'''
import json
import os
import csv
import ollama
from openai import OpenAI


# Load json file as list
def load_json_data(path):
    # Check if the file exists
    if os.path.isfile(path):
        # Open the file in read-only mode
        with open(path, 'r') as file:
            datas = json.load(file)
            return datas
    else:
        print("File does not exist.")

    
# Load jsonl file as list
def load_jsonl_data(path):
    # Check if the file exists
    if os.path.isfile(path):
        # Open the file in read-only mode
        with open(path, 'r') as file:
            datas = []
            for line in file:
                json_data = json.loads(line)
                datas.append(json_data)
            return datas
    else:
        print("File does not exits.")

# Save list as jsonl file
def write_to_jsonl(data, file_path):
    """
    将数据写入 JSONL 格式文件，每行一个 JSON 对象。
    
    参数:
    - data: 要写入的列表数据
    - file_path: 输出的文件路径
    """
    with open(file_path, 'w') as f:
        for item in data:
            f.write(json.dumps(item) + '\n')  # 每行写入一个 JSON 对象
        print(file_path, "is ok")


# Save list as json file
def write_to_json(answer, filename):
    #Convert the list to a JSON-formatted string
    json_data = json.dumps(answer)
    #Write JSON string to file
    with open(filename, 'w') as file:
        file.write(json_data)
        print(filename, "is ok")


# Load csv data as dict list
def load_csv_data(path):
    data = []
    # 使用DictReader读取CSV文件
    if os.path.isfile(path):
        with open(path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        return data
    else:
        print("File does not exist.")




# Save list as csv file
def write_to_csv(data: list, csv_file_path):
    fieldnames = data[0].keys()  # Extract field names from first dictionary
    with open(csv_file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def process_with_ollama(user_input, model_name = "llama2", sys_input = "You are a helpful assistant."):
    # print('Starting to process with ollama, note that this can take several minutes…')
    response = ollama.chat(
        model = model_name,
        messages = [ {'role': 'system', 'content': sys_input}, 
                     {'role': 'user', 'content': user_input}, ]
    )

    return response['message']['content']


# Determine whether the sentence is completely generated.
def judgeStop(response):
    if len(response)>0 and response[-1] in ['.', '?', '!']:
        return False # This sentence ends normally.
    else:
        return True # This sentence is incompletely generated.
    

def process_with_api(user_input, model_name = "gpt-4o", sys_input = "You are a helpful assistant."):
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
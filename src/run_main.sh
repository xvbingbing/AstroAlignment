#!/bin/bash

# -r -start 0 -end 2

# mistral-7B-v0.3
# python main.py -p ollama -s train -d 'nature_single_select_train' -m mistral -c original
python main.py -p ollama -s train -d 'nature_single_select_train' -m mistral -c rag




# Qwen2.5-7B
# python main.py -p ollama -s train -d 'nature_single_select_train' -m 'qwen2.5' -c original
python main.py -p ollama -s train -d 'nature_single_select_train' -m 'qwen2.5' -c rag


# Gemma2-9B
# python main.py -p ollama -s train -d 'nature_single_select_train' -m gemma2 -c original
python main.py -p ollama -s train -d 'nature_single_select_train' -m gemma2 -c rag


# Llama3.1-8B
# python main.py -p ollama -s train -d 'nature_single_select_train' -m 'llama3.1' -c original
python main.py -p ollama -s train -d 'nature_single_select_train' -m 'llama3.1' -c rag


# claude-3-5-sonnet-20241022
python main.py -p paid_api -s train -d 'nature_single_select_train' -m 'claude-3-5-sonnet-20241022' -c original -r -start 200 -end 300

python main.py -p paid_api -s train -d 'nature_single_select_train' -m 'claude-3-5-sonnet-20241022' -c original -r -start 300 -end 400

python main.py -p paid_api -s train -d 'nature_single_select_train' -m 'claude-3-5-sonnet-20241022' -c original -r -start 400 -end 500

python main.py -p paid_api -s train -d 'nature_single_select_train' -m 'claude-3-5-sonnet-20241022' -c original -r -start 500 -end 600

python main.py -p paid_api -s train -d 'nature_single_select_train' -m 'claude-3-5-sonnet-20241022' -c original -r -start 600 -end 700

python main.py -p paid_api -s train -d 'nature_single_select_train' -m 'claude-3-5-sonnet-20241022' -c original -r -start 700 -end 900

python main.py -p paid_api -s train -d 'nature_single_select_train' -m 'claude-3-5-sonnet-20241022' -c original -r -start 900 -end 1100

python main.py -p paid_api -s train -d 'nature_single_select_train' -m 'claude-3-5-sonnet-20241022' -c original -r -start 1100

python main.py -p paid_api -s train -d 'nature_single_select_train' -m 'claude-3-5-sonnet-20241022' -c rag

# gpt-4o
# python main.py -p paid_api -s train -d 'nature_single_select_train' -m 'gpt-4o' -c original -r -start 400 -end 500

# python main.py -p paid_api -s train -d 'nature_single_select_train' -m 'gpt-4o' -c original -r -start 500 -end 600

# python main.py -p paid_api -s train -d 'nature_single_select_train' -m 'gpt-4o' -c original -r -start 600 -end 700

# python main.py -p paid_api -s train -d 'nature_single_select_train' -m 'gpt-4o' -c original -r -start 700 -end 800

# python main.py -p paid_api -s train -d 'nature_single_select_train' -m 'gpt-4o' -c original -r -start 800 -end 900

# python main.py -p paid_api -s train -d 'nature_single_select_train' -m 'gpt-4o' -c original -r -start 900 -end 1000

# python main.py -p paid_api -s train -d 'nature_single_select_train' -m 'gpt-4o' -c original -r -start 1000 -end 1100

# python main.py -p paid_api -s train -d 'nature_single_select_train' -m 'gpt-4o' -c original -r -start 1100
python main.py -p paid_api -s train -d 'nature_single_select_train' -m 'gpt-4o' -c rag
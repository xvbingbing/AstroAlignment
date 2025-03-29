#!/bin/bash

# -r -start 0 -end 2

# mistral-7B-v0.3
# python main.py -p ollama -d 'train_dataset_en' -m mistral -c original
# python main.py -p ollama -d 'train_dataset_en_explanation' -m mistral -c rag



# Qwen2.5-7B
# python main.py -p ollama -d 'train_dataset_en' -m 'qwen2.5' -c original
# python main.py -p ollama -d 'train_dataset_en_explanation' -m 'qwen2.5' -c rag


# Gemma2-9B
# python main.py -p ollama -d 'train_dataset_en' -m gemma2 -c original
# python main.py -p ollama -d 'train_dataset_en_explanation' -m gemma2 -c rag


# Llama3.1-8B
python main.py -p ollama -d 'train_dataset_en' -m 'llama3.1' -c original
python main.py -p ollama -d 'train_dataset_en_explanation' -m 'llama3.1' -c rag


# claude-3-5-sonnet-20241022
# python main.py -p paid_api -d 'train_dataset_en' -m 'claude-3-5-sonnet-20241022' -c original
# python main.py -p paid_api -d 'train_dataset_en_explanation' -m 'claude-3-5-sonnet-20241022' -c rag


# gpt-4o
# python main.py -p paid_api -d 'train_dataset_en' -m 'gpt-4o' -c original
# python main.py -p paid_api -d 'train_dataset_en_explanation' -m 'gpt-4o' -c rag
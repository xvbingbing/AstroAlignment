#!/bin/bash

# mistral
python main.py -p ollama -d 'train_dataset_en' -m mistral -c original
python main.py -p ollama -d 'train_dataset_en_explanation' -m mistral -c rag

# python main.py -p paid_api -d 'train_dataset_en' -m 'claude-3-5-sonnet-20241022' -c original -r -start 0 -end 2
# python main.py -p paid_api -d 'train_dataset_en_explanation' -m 'claude-3-5-sonnet-20241022' -c rag -r -start 0 -end 2
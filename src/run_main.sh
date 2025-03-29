#!/bin/bash

# mistral
python main.py -p ollama -d 'train_dataset_en' -m mistral -c original
python main.py -p ollama -d 'train_dataset_en' -m mistral -c original
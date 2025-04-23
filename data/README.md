# AstroAlignment/data
Datasets are saved in this fold.

## Dataset from paper AstroSage
train_dataset_en.csv and train_dataset.csv is raw data from AstroSage.

## train_dataset_en.json
We transfer the train_dataset_en.csv to train_dataset_en.json and use the json data to generate original responses.

## train_dataset_en_explanation_original.json
We generate explanation for the question through claude-3-5-sonnet-20241022.

## train_dataset_en_explanation.json
We process the 'explanation' from string to list base train_dataset_en_explanation_original.json. We use this dataset to generate rag responses.

## nature_single_select_train.json
This dataset is from single-select multi choice(4)_EN.xlsx in paper "an astronomical question answering dataset for evaluating large language models"

## nature_single_select_test.json
This dataset is from single-select multi choice(5)_EN.xlsx in paper "an astronomical question answering dataset for evaluating large language models"
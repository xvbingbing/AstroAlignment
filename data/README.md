# AstroAlignment/data
Datasets are saved in this fold.

## Dataset from paper AstroSage
train_dataset_en.csv and train_dataset.csv is raw data from AstroSage.

## train_dataset_en.json
We tranfer the train_dataset_en.csv to train_dataset_en.json and use the json data to generate original responses.

## train_dataset_en_explanation.json
We generate explanation for the question through claude-3-5-sonnet-20241022. We use this dataset to generate rag responses.
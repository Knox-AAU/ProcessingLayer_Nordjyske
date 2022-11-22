import json
import os
from exceptions import FileNotExistsException

def save_word_vecs_template(path, data):
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile)

def get_files_data(path):
    all_files = []
    files = os.listdir(path)
    for (root, dirs, files) in os.walk(path):
        for index, file in enumerate(files):
            all_files.append({'path': os.path.join(path, file), 'index': index})
    return all_files

def save_json_data(path, file, data):
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + file, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile)

def load_json_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        raise FileNotExistsException('"' + file_path + '" does not exist')

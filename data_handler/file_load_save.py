import json
import os

def save_words_count(path, data):
    with open(path + 'word_vecs.json', 'w', encoding='utf-8') as outfile:
        json.dump(list(data.keys()), outfile)

def get_files_data(path):
    all_files = []
    files = os.listdir(path)
    for (root, dirs, files) in os.walk(path):
        for index, file in enumerate(files):
            all_files.append({'path': os.path.join(path, file), 'index': index})
    return all_files

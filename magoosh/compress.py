import xlrd
import json
import requests


def save_object(obj, fn):
    import json
    with open(fn, 'w', encoding='utf-8') as outfile:
        json.dump(obj, outfile, ensure_ascii = False)


filename = './word-list.json'

content = open(filename, 'r').read()

wordList = json.loads(content)

new_filename = 'word-list-compressed.json'

save_object(wordList, new_filename)
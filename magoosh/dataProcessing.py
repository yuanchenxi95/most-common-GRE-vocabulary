import xlrd
import json
import requests


def save_object(obj, fn):
    import json
    with open(fn, 'w', encoding='utf-8') as outfile:
        json.dump(obj, outfile, indent=2, sort_keys=True, ensure_ascii = False)


def translate(w):
    trans = []

    try :
        url = 'http://dict.youdao.com/jsonapi?q='
        res = requests.get(url + w)
        cont = json.loads(res.content)
        trs = cont['ec']['word'][0]['trs']
        for tr in trs:
            trans.append(tr['tr'][0]['l']['i'])
    except Exception as e:
        print(w)

    return trans

filename = './word-list.json'

content = open(filename, 'r').read()

wordList = json.loads(content)

for word in wordList:
    translations = translate(word['word'])
    word['translations'] = translations

save_object(wordList, filename)
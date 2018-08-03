import json


import requests
import hashlib
import urllib.parse
import random


appKey = ''
secretKey = ''


def translate_word(word):
    myurl = '/api'
    fromLang = 'EN'
    toLang = 'zh-CHS'
    salt = random.randint(1, 65536)

    sign = appKey + word + str(salt) + secretKey
    m1 = hashlib.new('md5')
    m1.update(sign.encode('utf-8'))
    sign = m1.hexdigest()
    myurl = myurl + '?appKey=' + appKey + '&q=' + urllib.parse.quote(word)\
            + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt)\
            + '&sign=' + sign

    try:
        res = requests.get('https://openapi.youdao.com' + myurl)

        content = json.loads(res.content)
        return content['web']
    except Exception as e:
        print(e)


def save_object(obj, fn):
    import json
    with open(fn, 'w', encoding='utf-8') as outfile:
        json.dump(obj, outfile, indent=2, sort_keys=True, ensure_ascii = False)


if __name__ == '__main__':
    filename = './vocabulary-list.json'

    content = open(filename, 'r').read()

    wordList = json.loads(content)
    translate_word('confrontation')

    for word in wordList:
        lowerCaseWord = word['word'].lower()
        word['word'] = lowerCaseWord

    for word in wordList:
        translation = translate_word(word['word'])
        word['translation'] = translation
    # print(wordList)
    save_object(wordList, 'new-vocabulary-list.json')

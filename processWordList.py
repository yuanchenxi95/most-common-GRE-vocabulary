
if __name__ == '__main__':
    filename = './ocabulary-list.txt'
    content = []
    with open(filename) as f:
        content = f.readlines()

    processedWords = []
    word = {}
    count = 0
    for line in content:
        if line == '\n':
            processedWords.append(word)
            word = {}
            count = 0
            continue
        line = line.replace('\n', '')

        if count == 0:
            items = line.split(': ')
            word['word'] = items[0]
            definitions = items[1].split(', ', 1)
            word['definition'] = definitions[0]
            word['partOfSpeech'] = definitions[1]
            count += 1
        elif count == 1:
            if line.startswith('Synonyms: '):
                word['synonyms'] = line.split(': ')[1]
            else:
                word['example'] = line
                count += 1
        elif count == 2:
            word['source'] = line.split(': ')[1]
    import json
    print(json.dumps(processedWords))



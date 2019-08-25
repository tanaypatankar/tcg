def squeeze(tos, bad_phrases):
    getsentences(tos, bad_phrases)


def getsentences(tos, bad_phrases):
    f = open(tos, encoding="utf8")
    sentences = f.read().lower().split('.')
    searchphrases(sentences, bad_phrases)


def searchphrases(sentences, bad_phrases):
    f = open(bad_phrases,  encoding="utf8")
    squeezed = []
    phrase = f.read().lower().splitlines()
    for sentence in sentences:
        word = sentence.split()
        for w in word:
            if w in phrase and sentence not in squeezed:
                squeezed.append(sentence)
    for s in squeezed:
        print(s)


squeeze('rovio_tos.txt', 'bad_phrases.txt')
print("\n\n\n\n\n\n\nThis is the eula stuff\n\n\n\n\n\n\n\n")
squeeze('rovio_eula.txt', 'bad_phrases.txt')

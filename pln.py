import re
from operator import itemgetter
from collections import Counter

def load_text(path):
    text = open(path).read()
    text = text.lower()
    signs = '!.?*;!@#\-:,|+$%&/'
    for i in signs:
        text = text.replace(i, "")
    text = text.replace("\n", " ")
    return text

shakespeare = load_text("shakespeare.txt")
regex = "[a-zA-Z]+"
tokens = re.findall(regex, shakespeare)

def w_ngran(word, sequence):
    regex = ""
    for i in range(len(sequence)):
        if i == 0:
            regex += sequence[i]
        else:
            regex += " "+sequence[i]
    
    count_total = shakespeare.count(regex+" "+word)
    count = shakespeare.count(regex)
    return count_total/count

def sorted_probs(probs):
    return sorted(probs.items(), key=itemgetter(1), reverse=True)

def word_after(sequence):
    words = []
    lenght = len(tokens)-1
    if len(sequence) == 1:
        for i in range(lenght):
            if tokens[i] == sequence[0]:
                words.append(tokens[i+1])

    if len(sequence) == 2:
        for i in range(lenght):
            if i < lenght-1 and tokens[i] == sequence[0] and tokens[i+1] == sequence[1]:
                words.append(tokens[i+2])

    return words

def most_likely():
    while True:
        print("x para sair!")
        entry = input("digite sua entrada: ")
        if entry == 'x':
            break
        sequence = entry.split()
        after = word_after(sequence)
        probs = {}
        for i in after:
            probs[i] = w_ngran(i, sequence)

        print(sorted_probs(probs)[:3])

most_likely()
    
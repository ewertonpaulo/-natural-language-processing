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

#calculate the probability
def w_ngran(word, sequence):
    regex = sequence
    count_total = shakespeare.count(regex+" "+word)
    count = shakespeare.count(regex)
    return count_total/count

#sort by value from dictionary
def sorted_probs(probs):
    return sorted(probs.items(), key=itemgetter(1), reverse=True)

#get all words after a entry of words with max lenght == 2 
def word_after(sequence, _range):
    words = []
    lenght = len(tokens)-1
    if _range == '2' or len(sequence) == 1:
        for i in range(lenght):
            if tokens[i] == sequence[-1]:
                words.append(tokens[i+1])
        sequence = sequence[-1]

    if _range == '3':
        for i in range(lenght):
            if i < lenght-2 and tokens[i] == sequence[-2] and tokens[i+1] == sequence[-1]:
                words.append(tokens[i+2])
        sequence = " ".join([sequence[-2], sequence[-1]])
    return (sequence, words)

def most_likely():
    print("x para sair!")
    _range = input("type 2 for bigran, 3 for trigran: ")
    while True:
        entry = input("type: ")
        if entry == 'x':
            break
        sequence = entry.split()
        words, after = word_after(sequence, _range)
        probs = {}
        for i in after:
            probs[i] = w_ngran(i, words)
        
        result = sorted_probs(probs)[:3]
        if result:
            for word, probability in result:
                print("palavra: %s | probabilidade: %f" %(word,probability))
        else:
            print("No results avaliable")            

most_likely()
    
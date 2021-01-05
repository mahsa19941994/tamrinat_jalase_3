import nltk
from nltk.stem import PorterStemmer
import ImportantWords

import FileManager


def Sentence():
    for i in range(1, 11):
        arr = nltk.sent_tokenize(FileManager.Read(f"data/{i}.txt"))
    return arr


def WordTok(text):
    arr = text.split(" ")
    return arr


def Remove(text):
    arr = []
    for i in range(0, len(text)):
        if (text[i] != "stop" and len(text[i]) != 1 and len(text[i]) != 0):
            arr.append(text[i])
    return arr


def Stem(text):
    arr = []
    for i in range(0, len(text)):
        arr.append(PorterStemmer().stem(text[i]))
    return arr


def Result():
    arr = Sentence()
    all = []
    for i in range(0, len(arr)):
        txt = list(arr[i])
        text = ""
        for i in range(0, len(txt)):
           if 64 < ord(txt[i]) or ord(txt[i]) < 48 and txt[i] != '<' and txt[i] != '>':
             text += txt[i]
        text = WordTok(text)
        text = Remove(text)
        text = Stem(text)
        all.append(text)
    return all
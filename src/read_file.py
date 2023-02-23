import re
from pathlib import Path

# 'borrowed' and modified code from: https://stackoverflow.com/a/31505798
# written by 'D. Greenberg', 'a.t. and 'Sisay Chala'
# begin
# -*- coding: utf-8 -*-


def split_into_sentences(text):
    '''Detects sentences in a body of text, taking into account periods that appear inside
    sentences.
    Args:
        text: a body of text, like the acquired text from reading a .txt file.
    Returns:
        sentences: a list containing sublist, each sublist containing the individual words and
        punctuation chars as strings.'''
    
    alphabets = "([A-Za-z])"
    prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
    suffixes = "(Inc|Ltd|Jr|Sr|Co)"
    starters = r"(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
    acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
    websites = "[.](com|net|org|io|gov)"
    digits = "([0-9])"
    text = " " + text + "  "
    text = text.replace("\n", " ")
    text = re.sub(prefixes, "<wspc>\\1<prd><wspc>", text)
    text = re.sub(websites, "<wspc><prd>\\1<wspc>", text)
    text = re.sub(digits + "[.]" + digits, "<wspc>\\1<prd>\\2<wspc>", text)
    if "..." in text:
        text = text.replace("...", "<wspc><prd><prd><prd><wspc>")
    if "Ph.D" in text:
        text = text.replace("Ph.D.", "<wspc>Ph<prd>D<prd><wspc>")
    if "e.g." in text:
        text = text.replace("e.g.", "<wspc>e<prd>g<prd><wspc>")
    if "i.e." in text:
        text = text.replace("i.e.", "<wspc>i<prd>e<prd><wspc>")
    text = re.sub(r"\s" + alphabets + "[.] ", " \\1<prd> ", text)
    text = re.sub(acronyms+" "+starters, "\\1<wspc><stop><wspc> \\2", text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" +
                  alphabets + "[.]", "<wspc>\\1<prd>\\2<prd>\\3<prd><wspc>", text)
    text = re.sub(alphabets + "[.]" + alphabets +
                  "[.]", "<wspc>\\1<prd>\\2<prd><wspc>", text)
    text = re.sub(" "+suffixes+"[.] "+starters,
                  " <wspc>\\1<stop> \\2<wspc>", text)
    text = re.sub(" "+suffixes+"[.]", " <wspc>\\1<prd><wspc>", text)
    text = re.sub(" " + alphabets + "[.]", " <wspc>\\1<prd><wspc>", text)
    if "”" in text:
        text = text.replace(".”", "”.")
    if "\"" in text:
        text = text.replace(".\"", "\".")
    if "!" in text:
        text = text.replace("!\"", "\"!")
    if "?" in text:
        text = text.replace("?\"", "\"?")
    punctuation_chars = "(,|:|;|\"|”|“)"
    text = re.sub(punctuation_chars, "<wspc>\\1<wspc>", text)
    text = text.replace(".", "<wspc>.<wspc><stop>")
    text = text.replace("?", "<wspc>?<wspc><stop>")
    text = text.replace("!", "<wspc>!<wspc><stop>")
    text = text.replace("<prd>", ".")
    text = text.replace(' ', '<wspc>')
    sentences = text.split("<stop>")
    sentences = sentences[:-1]

    for i, sentence in enumerate(sentences):
        sentences[i] = [word for word in sentence.split('<wspc>') if word]
    return sentences
# end


def read_file(path):
    '''Turns a text document into a list of its sentences.
    Args:
        path: path of a .txt document
    Returns:
        a list containing sublists, each sublist a sentence of strings.'''

    folder_path = 'data/'

    if 'src' in str(Path('.').resolve()):
        folder_path = '../data/'

    if '/' not in path:
        path = folder_path+path
    elif not 'home' in path:
        path = Path(path).resolve()

    print('   ~ Generating from: ', path, '~')
    try:
        with open(path, encoding='utf-8') as file:
            file = file.read()

            file = file.replace('_', '')

            sentences = split_into_sentences(file)
        return sentences
    except IsADirectoryError:
        return read_folder(path)

def read_folder(path):
    print('that was a directory')
    return []

def split_into_words(text):
    '''Turns a string into a list of its components, i.e. tokenizes the string.
    This function turns text that doesn't contain sentences into the same format as
    'split_into_sentences'
    Args:
        text, a string containing words, whitespaces and punctuation marks, but no newlines
    Returns:
        text, the same text split into words and punctuation marks as a list'''
    punctuation = ',.;:?!"“”'

    # turn punctuation chars into their own 'words'
    for mark in punctuation:
        text = text.replace(mark, '<wspc>'+mark+'<wspc>')
    text = text.replace(' ', '<wspc>')
    text = [word for word in text.split('<wspc>') if word]

    return text

import re

# 'borrowed' and modified code from: https://stackoverflow.com/a/31505798
# written by 'D. Greenberg', 'a.t. and 'Sisay Chala'
# begin
# -*- coding: utf-8 -*-


def split_into_sentences(text):
    alphabets = "([A-Za-z])"
    prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
    suffixes = "(Inc|Ltd|Jr|Sr|Co)"
    starters = r"(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
    acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
    websites = "[.](com|net|org|io|gov)"
    digits = "([0-9])"
    text = " " + text + "  "
    text = text.replace("\n", " ")
    text = re.sub(prefixes, "\\1<prd>", text)
    text = re.sub(websites, "<prd>\\1", text)
    text = re.sub(digits + "[.]" + digits, "\\1<prd>\\2", text)
    if "..." in text:
        text = text.replace("...", "<prd><prd><prd>")
    if "Ph.D" in text:
        text = text.replace("Ph.D.", "Ph<prd>D<prd>")
    if "e.g." in text:
        text = text.replace("e.g.", "e<prd>g<prd>")
    if "i.e." in text:
        text = text.replace("i.e.", "i<prd>e<prd>")
    text = re.sub(r"\s" + alphabets + "[.] ", " \\1<prd> ", text)
    text = re.sub(acronyms+" "+starters, "\\1<stop> \\2", text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" +
                  alphabets + "[.]", "\\1<prd>\\2<prd>\\3<prd>", text)
    text = re.sub(alphabets + "[.]" + alphabets +
                  "[.]", "\\1<prd>\\2<prd>", text)
    text = re.sub(" "+suffixes+"[.] "+starters, " \\1<stop> \\2", text)
    text = re.sub(" "+suffixes+"[.]", " \\1<prd>", text)
    text = re.sub(" " + alphabets + "[.]", " \\1<prd>", text)
    if "”" in text:
        text = text.replace(".”", "”.")
    if "\"" in text:
        text = text.replace(".\"", "\".")
    if "!" in text:
        text = text.replace("!\"", "\"!")
    if "?" in text:
        text = text.replace("?\"", "\"?")
    text = text.replace(".", ".<stop>")
    text = text.replace("?", "?<stop>")
    text = text.replace("!", "!<stop>")
    text = text.replace("<prd>", ".")
    #text = text.replace(' ', '<wspc> <wspc>')
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences
# end



def read_file(path):
    '''Turns a text document into a list of its sentences.
    Args:
        path: path of txt document
    Returns:
        a list containing sublists, each sublist a sentence of strings.'''
    with open(path, encoding='utf-8') as file:
        file = file.read()

        file = file.replace('_', '')

        sentences = split_into_sentences(file)
        for i in range(0, len(sentences)):
            sentences[i] = split_into_words(sentences[i])

    return sentences


def split_into_words(text):
    '''Turns a string into a list of its components, i.e. tokenizes the string.
    Args:
        text, a string
    Returns:
        text, the same text split into words, punctuation marks and spaces as a list'''
    punctuation = ',.;:?!"“”'

    #turn punctuation chars into their own 'words'
    for x in punctuation:
        text = text.replace(x, '<wspc>'+x+'<wspc>')
    text = text.replace(' ', '<wspc> <wspc>')
    text = [word for word in text.split('<wspc>') if word]

    # un-capitalize first word
    text[0] = text[0].lower()
    
    return text
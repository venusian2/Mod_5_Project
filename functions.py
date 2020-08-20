import pandas as pd
import pandas as pd
import numpy as np
import re
import seaborn as sns
import matplotlib.pyplot as plt


def cleanText(data_frame, column_name:str, new_column:str):
    data_frame[column_name] = data_frame[column_name].str.replace('<br/>', '\n')
    data_frame[new_column] = data_frame[column_name]
    data_frame[new_column] = data_frame[new_column].str.replace("'", '')    
    data_frame[new_column] = data_frame[new_column].str.replace('[^\w\s]', ' ')
    data_frame[new_column] = data_frame[new_column].str.replace('[0-9]', ' ')
    data_frame[new_column] = data_frame[new_column].str.replace('_', ' ')
    data_frame[new_column] = data_frame[new_column].str.replace('\s+', ' ')
    data_frame[new_column] = data_frame[new_column].str.lower()
    
def num_lines(lyric):
    line_list = lyric.split('\n')
    line_list = [line for line in line_list if line != ' ']
    return line_list

def num_words(lyrics):
    count = 0
    for line in lyrics:
        word_list = line.split(' ')
        word_list = [word for word in word_list if word != '']
        count += len(word_list)
    return count

def top_ngrams(corpus, g):
    vec = CountVectorizer(ngram_range = (g, g), stop_words=stopwords_list).fit(corpus)
    bag_of_words = vec.transform(corpus)
    sum_words = bag_of_words.sum(axis = 0) 
    words_freq = [(word, sum_words[0, idx]) for word, idx in vec.vocabulary_.items()]
    words_freq = sorted(words_freq, key = lambda x: x[1], reverse = True)
    
    if g == 2:
        top_grams = top_bigrams_no_dups(words_freq)
    elif g == 3:
        top_grams = top_trigrams_no_dups(words_freq)
    else:
        top_grams = words_freq[0:20]
    return words_freq[:20]


import requests
from bs4 import BeautifulSoup
from collections import Counter
from variables import MAIN_RESULT, deletion_list
import nltk
from nltk.collocations import *


def webscrape_by_link(url, element, attr, info):
    """
    :param url: full address
    :param element: element tag (str)
    :param attr: element attribute(str)
    :param info: element additional info (str)
    :return: list of most used words on the website
    """
    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html5lib')
    result = soup.find_all(element, attrs={attr: info})
    reslist = []
    for link in result:
        title = link.get('title')
        for word in title.split():
            reslist.append(word)
            MAIN_RESULT.append(word)

    return(Counter(reslist))

def webscrape_by_span(url, element, attr, info):
    """
       :param url: full address
       :param element: element tag (str)
       :param attr: element attribute(str)
       :param info: element additional info (str)
       :return: list of most used words on the website
       """
    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html5lib')
    result = soup.find_all(element, attrs = {attr: info})
    reslist = []
    for element in result:
        for word in element.text.rstrip().lstrip().split():
            reslist.append(word)
            MAIN_RESULT.append(word)
    return Counter(reslist)


def webscraping_results():
    #get list from global variable
    main_result = MAIN_RESULT
    # remove words from deletion list
    for element in main_result:
        if element in deletion_list:
            main_result.remove(element)
    # return result
    return [i.lower() for i in main_result if i.lower() not in deletion_list]

def webscraping_results_nltk_bi():
    bigram_measures = nltk.collocations.BigramAssocMeasures()

    # change this to read in your data
    word_list = ' '.join(MAIN_RESULT).lower()
    print('main_result:', word_list)
    finder = BigramCollocationFinder.from_words(
        MAIN_RESULT)

    # only bigrams that appear 1+ times
    finder.apply_freq_filter(3)

    # return the 10 n-grams with the highest PMI
    return finder.nbest(bigram_measures.pmi, 10)

def webscraping_results_nltk_tri():
    """this function gets used word pairs from the list of words"""
    trigram_measures = nltk.collocations.TrigramAssocMeasures()

    # change this to read in your data
    word_list = ' '.join(MAIN_RESULT).lower()
    print('main_result:', word_list)
    finder = BigramCollocationFinder.from_words(
        MAIN_RESULT)

    # only bigrams that appear 3+ times
    finder.apply_freq_filter(2)

    # return the 10 n-grams with the highest PMI
    nlt_result = finder.nbest(trigram_measures.pmi, 10)

    # return names of 10 articles with the most common word pairs




def display_results(word_list):
    # display results
    print('words scraped: ', len(word_list))
    print('Most common words:')
    for key, value in Counter(word_list).most_common(30):
        print(f'{key}: {value}')


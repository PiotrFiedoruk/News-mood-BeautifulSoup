import requests
from bs4 import BeautifulSoup
from collections import Counter
from variables import MAIN_RESULT, deletion_list

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

def display_results(word_list):
    # display results
    print('words scraped: ', len(word_list))
    print('Most common words:')
    for key, value in Counter(word_list).most_common(30):
        print(f'{key}: {value}')


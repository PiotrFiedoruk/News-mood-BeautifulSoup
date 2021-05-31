from functions import webscrape_by_link, webscrape_by_span, webscraping_results, webscraping_results_nltk_bi, \
    display_results, webscraping_results_nltk_tri
import collections
import pandas
from collections import Counter
from variables import MAIN_RESULT
import matplotlib.pyplot as plt

"""function to webscrape, extract and determine the most common words used in 5 main Polish news portals"""


# wp.pl
webscrape_by_link('https://www.wp.pl/', 'a', 'class', "pcfpmu-0 fxuaLn")
# gazeta.pl
webscrape_by_link('https://www.gazeta.pl/', 'a', 'class', "timeline__link")
# interia
webscrape_by_link('https://www.interia.pl/', 'a', 'class', 'news-a')
# onot.pl
webscrape_by_span('https://www.onet.pl/', 'span', 'class', 'title')
# o2.pl
webscrape_by_span('https://www.o2.pl/', 'span', 'data-testid', 'teaserText')
# tvn.pl
webscrape_by_link('https://tvn24.pl/', 'a', 'class', 'default-teaser__link')




webscraping_results()
display_results(webscraping_results())

print('nlt-bi:', webscraping_results_nltk_bi())
print('nlt-tri:', webscraping_results_nltk_tri())
word_counter = Counter(webscraping_results()).most_common(10)





# # # draw a chart
# names = [i[0] for i in word_counter]
#
# values = [i[1] for i in word_counter]
#
# plt.figure(figsize=(10, 4))
#
# plt.subplot(131)
# plt.bar(names, values)
# plt.suptitle('Most common words')
# plt.show()
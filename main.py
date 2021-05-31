from functions import webscrape_by_link, webscrape_by_span, webscraping_results, display_results
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

word_counter = Counter(webscraping_results()).most_common(10)
print(word_counter)


# # draw a chart
names = [i[0] for i in word_counter]
print(names)

values = [i[1] for i in word_counter]
print(values)

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.suptitle('Categorical Plotting')
plt.show()
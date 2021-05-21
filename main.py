from functions import webscrape_by_link, webscrape_by_span, webscraping_results

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

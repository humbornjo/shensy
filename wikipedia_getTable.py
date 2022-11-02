import pandas as pd
import wikipedia as wp

################## Attempt on finding table with links #################
########################################################################
# import requests
# import pandas as pd
# from bs4 import BeautifulSoup

# url = "https://en.wikipedia.org/wiki/2007%E2%80%9308_Persian_Gulf_Cup"
# r = requests.get(url)

# html_table = BeautifulSoup(r.text, features="lxml").find('table')
# r.close()

# df = pd.read_html(str(html_table), header=0)[0]
# links = [link.get('href') for link in html_table.find_all('a')]

# import csv
# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen("http://en.wikipedia.org/wiki/Alireza_Mirshafian")

# # soup = BeautifulSoup(html, "html.parser").find_all(lambda t: t.name == "a" and t.text == "2007–08")

# # print([a["href"] for a in soup])
# soup = BeautifulSoup(html, "html.parser")
# table = soup.findAll("table", {"class":"wikitable"})[0]
# rows = table.findAll("tr")
# print(type(rows),rows)

def get_origin_table(page_title):
    '''
    ############################
    
    page_title: The title of wikipedia page.
                The first element in the turl dataset.

    ############################
    '''
    html = wp.page(page_title).html().encode("UTF-8")
    wikipage_tables=pd.read_html(html, attrs = {'class': 'wikitable'}, extract_links="body")
    return wikipage_tables

def identify_table(wikipage_tables, target_table):




# dependencies: bs4 and treelib
# installation: py -m pip install bs4, py -m pip install requests, py -m pip install treelib

# importing html scraping libraries
from bs4 import BeautifulSoup
import requests
import re

# importing tree libraries
from treelib import Node, Tree

# extract url html document
def getHTMLdocument(url):
    # HTML document request
    response = requests.get(url)
    # response in JSON format
    return response.text

# scrape html and add nodes recursively
def scrapeHTMLdocument(url, degree):
    # create document
    html_document = getHTMLdocument(url)
    # create soup object
    soup = BeautifulSoup(html_document, 'html.parser')

    # find all the anchor tags with "href"
    # attribute starting with "https://"
    for link in soup.find_all('a',
        attrs={'href': re.compile("^https://")}):
        if link.get('href') not in visualization:
            visualization.create_node(link.get('href'), link.get('href'), parent=url)
            if degree < degrees_to_scrape:
                scrapeHTMLdocument(link.get('href'), degree+1)

visualization = Tree()

url_to_scrape = input("url to scrape: ")
degrees_to_scrape = int(input("degrees to scrape (tree depth): "))

current_degree = 0
visualization.create_node(url_to_scrape, url_to_scrape)

scrapeHTMLdocument(url_to_scrape, current_degree)
visualization.show()

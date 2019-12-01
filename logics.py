import feedparser
import requests
from bs4 import BeautifulSoup
import json
import pdb


def get_data(html):
    html
    soup = BeautifulSoup(html, 'lxml')
    h1=soup.text

    return h1


def parseRSS(rss_url):
    return feedparser.parse(rss_url)


# Function grabs the rss feed headlines (titles) and returns them as a list
def getInfo(rss_url,limit):
    headlines = {}
    feed = parseRSS(rss_url)
    cntr=0
    for newsitem in feed['items']:
        news={}
        news['DATE']=newsitem["published"]
        news['TITLE']=newsitem['title'].replace('&#39;',"'")
        news['INFO']=get_data(newsitem["summary_detail"]['value'])
        news['LINK']=newsitem['links'][0]['href']
        soup = BeautifulSoup(newsitem['summary'])
        news['IMG']=scissors(soup.find('img')['src'])
        if (cntr<limit):
            headlines[cntr]=news
            cntr+=1
        del news


    return headlines

def scissors(text):
    try:
        marker = text.find('-/https:')
        text = text[marker+1:]
        del marker
    except:
        text
    return text


def print_json(dict):
    """ """
    try:
        result=json.dumps(dict ,indent=4, ensure_ascii=False)
        print(result)
        return True
    except:
        print('error in print_json()')
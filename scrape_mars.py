#!/usr/bin/env python
# coding: utf-8

# Declare Dependencies 
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import requests
import os
import pprint
import time
import re
import urllib


#pointing to the directory where chromedriver exists
executable_path = {"executable_path":"chromedriver"}
browser = Browser("chrome", **executable_path, headless = False)


# ERROR when visiting the page 
#url = "https://mars.nasa.gov/news/"
#browser.visit(url)
#Error Message
#WebDriverException: Message: chrome not reachable
 # (Session info: chrome=75.0.3770.142)

def scrape():

    nasa_2020_news_url = "https://mars.nasa.gov/news/"
    nasa_2020_news= requests.get(nasa_2020_news_url)
# Create BeautifulSoup object; parse with 'html.parser'
    scraper = BeautifulSoup(nasa_2020_news.text, 'html.parser')
    print(scraper.prettify())

title_scrape = scraper.find_all(class_='content_title')
print(title_scrape)



# results are returned title_scrape as an iterable list
news_title_results = scraper.find_all(class_="slide")
news_title = []
p_list = []
# Loop through returned results
for result in news_title_results:
    # Error handling
    try:
        #Find title and paragraph for each link. The title is found within the second link in each slide, the paragraph
        #is found inside an inner description div tag.
        news_row = result.find_all('a')
        newtitle = news_row[1].text
        paragraph = result.find('div', class_="rollover_description_inner").text
        #Append both to a list
        news_title.append(newtitle)
        p_list.append(paragraph)
        #Print title and body
        #print(news_title)
        print(paragraph)
    except AttributeError as e:
        print(e)


# ### JPL Mars Space Images - Featured Image

image_url = urllib.request.urlopen("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars")
bs = BeautifulSoup(image_url, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')})
for image in images: 
    print(image['src']+'\n')


url_mars_weather = 'https://twitter.com/marswxreport?lang=en'
mars_weather= requests.get(url_mars_weather)
soup = BeautifulSoup(mars_weather.text, 'html.parser')
print(soup.prettify())

tweet_marsweather = soup.find_all(class_="content")
weather_tweets = []
# Loop through returned results
for tweets in tweet_marsweather:
    # Error handling
    try:
        #Find the text of each tweet and append it to the list of tweet texts
        tweet = result.find('p', class_="TweetTextSize").text
        weather_tweets.append(tweet)
        #Print the text of each tweet as it is processed
        print(tweet)
    except AttributeError as e:
        print(e)



mars_facts = "https://space-facts.com/mars/"
marsfacts_tb = pd.read_html(mars_facts)
marsfacts_tb[0]



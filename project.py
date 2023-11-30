from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd


START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

browser = webdriver.Chrome()
browser.get(START_URL)

time.sleep(10)
star_data = []

def scrape():

    for i in range(0,10)
    print(f'Scrapping page {i+1} ... ' )
    
    soup = BeautifulSoup(browser.page_source, "html.parser")

    for tr_tag in soup.find_all("tr" , attrs = {"class" , "stars"}):
        
        tbody_tag = tr_tag.find_all("tbody")

        for index, tbody_tag in enumerate()
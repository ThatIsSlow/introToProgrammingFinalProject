#################################################################################################################################################################
"""
PROJECT OUTLINE:
    - Two possible ideas
        - gaem
            - will use pygame, will use randint
            - will use settings and sprites as different python files to increase the modularity
            - will use image files as characters 
            - GAME DESIGN:
                - most likely strategy based, maybe something like RISK or a towere defense game. Something Turn based would be cool.
                - Definitely want to use mulitple levels


        - HereNow (rowing results website) parser
            - Will likely use Tkinter
            - if not tkinter will use flask to put functional aspect in a website
            - will enable the user to input a team name or a rower name or a boat class
                - will then scan HereNow, looking through certain races, or a lot of races, to assemble all of the results of the
                    desired search, and then place it into a new window/file
            RESOURCES: 
                https://www.edureka.co/blog/web-scraping-with-python/


"""
#################################################################################################################################################################

"""
Sources: 

"""
import requests, bs4, time, requests_html
from selenium import webdriver
import pandas as pd
import bs4
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium import webdriver
from requests_html import HTMLSession
from selenium.common.exceptions import NoSuchElementException

URL = 'https://herenow.com/results/#/races/20899/results'

chrome_driver = "Code\Projects\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver)
driver.get(URL)
time.sleep(50)
# spans = driver.find_element(By.TAG_NAME, "span")
# print(type(spans))
searchresults = driver.find_elements(By.XPATH,"//span[contains(@class,'ng-binding')]")
print(len(searchresults))
driver.quit
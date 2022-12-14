#################################################################################################################################################################
"""
PROJECT OUTLINE:
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


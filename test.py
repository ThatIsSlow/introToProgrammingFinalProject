import requests
from selenium import webdriver
import pandas as pd
import bs4

import time
from selenium.webdriver.common.by import By
from selenium import webdriver



driver = webdriver.Chrome('C:\GitHub\IntroToProgramming2022\intoToProgrammingFinalProject\chromedriver_win32.zip\chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://herenow.com/results/#/races/20899/results')
time.sleep(5) # Let the user actually see something!
search_box = driver.find_elements(By.ID, '""')

print(search_box)

time.sleep(2) # Let the user actually see something!
driver.quit()


'''
res = requests.get('https://herenow.com/results/#/races/21065/results')
res.raise_for_status()
HereNowResult = bs4.BeautifulSoup(res.text, 'html.parser')
print(type(HereNowResult))
Redwood = HereNowResult.select('span .ng-binding')
print(Redwood)
'''

'''
vgm_url = 'https://herenow.com/results/#/races/21065/results'
html_text = requests.get(vgm_url).text
soup = bs4.BeautifulSoup(html_text, 'html.parser')

print(soup.get_text())
print(soup)
print(soup.find_all('#text'))
'''


'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://herenow.com/results/#/races/20899/results"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)
'''





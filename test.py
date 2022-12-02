import requests, bs4, time, requests_html
from selenium import webdriver
import pandas as pd
import bs4
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium import webdriver
from requests_html import HTMLSession
from selenium.common.exceptions import NoSuchElementException



driver = webdriver.Chrome('C:\GitHub\IntroToProgramming2022\intoToProgrammingFinalProject\chromedriver_win32.zip\chromedriver')  
driver.get('https://herenow.com/results/#/races/20899/results')

#number designating the finish location (e.g. first, second, third...) of an athlete, will pull name out
Final_Placement = str(32)

#placing CSS selectors here for easier comparison to establish what I can search by. 
CSS_IsiahHarrisonTT = '#displayResultsView > section > ul > li:nth-child(1) > div > div > table > tbody > tr:nth-child(3) > td.nameData > span.ng-binding'
CSS_LosGatos4xTT = '#displayResultsView > section > ul > li:nth-child(9) > div > div > table > tbody > tr:nth-child(12) > td.nameData > span.ng-binding'
XPATH_LostGatos4xTT = '//*[@id="displayResultsView"]/section/ul/li[9]/div/div/table/tbody/tr[12]/td[3]/span[1]'
CSS_IsiahHarrisonSEMI = '#displayResultsView > section > ul > li:nth-child(2) > div > div > table > tbody > tr:nth-child(3) > td.nameData > span.ng-binding'
XPATH_IsiahHarrisonSEMI = '//*[@id="displayResultsView"]/section/ul/li[2]/div/div/table/tbody/tr[3]/td[3]/span[1]'
XPATH_IsiahHarrisonSEMI = '/html/body/div[2]/ng-view/div/section/ul/li[2]/div/div/table/tbody/tr[3]/td[3]/span[1]'
XPATH_IsiahHarrisonTT = '/html/body/div[2]/ng-view/div/section/ul/li[1]/div/div/table/tbody/tr[3]/td[3]/span[1]'

time.sleep(30)
#this is css selector for mathew willer, and the XPATH
##########element = driver.find_element(By.CSS_SELECTOR, '#displayResultsView > section > ul > li:nth-child(1) > div > div > table > tbody > tr:nth-child(1) > td.nameData > span.ng-binding')
#this is css selector,and the xpath for Isiah harrison
element1 = driver.find_element(By.XPATH, XPATH_IsiahHarrisonTT)
#this is css selector for a random individual, using x as a variable to represent their placement
element2 = driver.find_element(By.CSS_SELECTOR, '#displayResultsView > section > ul > li:nth-child(1) > div > div > table > tbody > tr:nth-child('+ Final_Placement +') > td.nameData > span.ng-binding')
element3 = driver.find_element(By.CSS_SELECTOR, CSS_LosGatos4xTT)

# print(element.text)
# print(element1.text)
# print(element2.text)
# print(element3.text)

Finish_Position = 1
Race_Number = 1
Running = True
Desired_Name =  """Joel Bustamante
(Miami)"""
# '+ counter +'

while Running:
    while True:
        Finish_Position = str(Finish_Position)
        try:
            element = driver.find_element(By.CSS_SELECTOR, '#displayResultsView > section > ul > li:nth-child(1) > div > div > table > tbody > tr:nth-child('+ Finish_Position +') > td.nameData > span.ng-binding')
        except NoSuchElementException:
            print('error')
            driver.quit
            exit()
        
        print(element.text)
        Finish_Position = int(Finish_Position) + 1
        # if element.text != Desired_Name:
        #     counter = int(counter) + 1
        # else:
        #     print(element.text)
        #     counter = int(counter) + 1
    




driver.quit





################# FIND_ELEMENT BANK #####################
'''
element1 = driver.find_element(By.CSS_SELECTOR, CSS_IsiahHarrisonTT)
element1 = driver.find_element(By.XPATH, """//*[@id="displayResultsView"]/section/ul/li[1]/div/div/table/tbody/tr[3]/td[3]/span[1]""")
element = driver.find_element(By.XPATH, '//*[@id="displayResultsView"]/section/ul/li[1]/div/div/table/tbody/tr[1]/td[3]/span[1]')
'''




































###### For some reason this thang here didn't work, not sure why###################################
# #create the session
# session = HTMLSession()
# #define our URL
# url = 'https://www.youtube.com/channel/UC8tgRQ7DOzAbn9L7zDL8mLg/videos'
# #use the session to get the data
# r = session.get(url)
# #Render the page, up the number on scrolldown to page down multiple times on a page
# r.html.render(sleep=2, keep_page=True, scrolldown=1)
# #take the rendered html and find the element that we are interested in
# videos = r.html.find('#video-title')
# #loop through those elements extracting the text and link
# for item in videos:
#     video = {
#         'title': item.text,
#         'link': item.absolute_links
#     }
#     print(video)
######################################################################################

##################################################################################################
# driver = webdriver.Chrome('C:\GitHub\IntroToProgramming2022\intoToProgrammingFinalProject\chromedriver_win32.zip\chromedriver')  # Optional argument, if not specified will search path.
# driver.get('https://herenow.com/results/#/races/20899/results')
# time.sleep(7) # Let the user actually see something!
# search_box = driver.find_elements(By.ID, 'applicationHost')
# print(search_box)
# driver.quit()
######################################################################################


'''
#### Doesnt pull anything out because bs4 is mid for angular JS ######################
res = requests.get('https://herenow.com/results/#/races/20899/results')
res.raise_for_status()
time.sleep(10)
# print(res.content)
HereNowResult = bs4.BeautifulSoup(res.text, 'html.parser')
# print(type(HereNowResult))
print("   ")
print("   ")
Redwood = HereNowResult.select("div", { "class" : "ng-scope" }, 10)
print(Redwood)
print("  ")
####################################################################################
'''

'''
#### Failed attempt, didnt pull anything out ##########################
vgm_url = 'https://herenow.com/results/#/races/21065/results'
html_text = requests.get(vgm_url).text
soup = bs4.BeautifulSoup(html_text, 'html.parser')

print(soup.get_text())
print(soup)
print(soup.find_all('#text'))
#####################################################################



##### Failed attempt, only pulls title out ############################
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
#############################################################################
'''





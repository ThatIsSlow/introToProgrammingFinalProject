import requests
from selenium import webdriver
import pandas as pd
import bs4
from selenium.webdriver import Chrome
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

from requests_html import HTMLSession
import requests_html


driver = webdriver.Chrome('C:\GitHub\IntroToProgramming2022\intoToProgrammingFinalProject\chromedriver_win32.zip\chromedriver')  

driver.get('https://herenow.com/results/#/races/20899/results')
# driver.get('https://quotes.toscrape.com/js')

#number designating the finish location (e.g. first, second, third...) of an athlete, will pull name out
Final_Placement = str(36)

time.sleep(5)
#this is css selector for mathew willer, and the XPATH
element = driver.find_element(By.CSS_SELECTOR, '#displayResultsView > section > ul > li:nth-child(1) > div > div > table > tbody > tr:nth-child(1) > td.nameData > span.ng-binding')
element = driver.find_element(By.XPATH, '//*[@id="displayResultsView"]/section/ul/li[1]/div/div/table/tbody/tr[1]/td[3]/span[1]')
# element = driver.find_element("""<span ng-show="flight.hasPublicEntryNumbers(race)" ng-bind-html="entryResult.Entry.Name.replace('(', '<br></span>(') | prettyEntryName" class="ng-binding">Matthew Willer <br>(Redwood Scullers)</span>""")
### DIDNT WORK #### element = driver.find_element(By.XPATH, '//*[@id="displayResultsView"]/section/ul/li[1]/div/div/table/tbody/tr[1]/td[3]/span[1]/text()[1]')

#this is css selector for Isiah harrison
element1 = driver.find_element(By.CSS_SELECTOR, '#displayResultsView > section > ul > li:nth-child(1) > div > div > table > tbody > tr:nth-child(3) > td.nameData > span.ng-binding')
element1 = driver.find_element(By.XPATH, """//*[@id="displayResultsView"]/section/ul/li[1]/div/div/table/tbody/tr[3]/td[3]/span[1]""")


#this is css selector for a random individual, using x as a variable to represent their placement
element2 = driver.find_element(By.CSS_SELECTOR, '#displayResultsView > section > ul > li:nth-child(1) > div > div > table > tbody > tr:nth-child('+ Final_Placement +') > td.nameData > span.ng-binding')

print(element.text)
print(element1.text)
print(element2.text)

driver.quit




###### For some reason this thang here didn't work, not sure why
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




# driver = webdriver.Chrome('C:\GitHub\IntroToProgramming2022\intoToProgrammingFinalProject\chromedriver_win32.zip\chromedriver')  # Optional argument, if not specified will search path.
# driver.get('https://herenow.com/results/#/races/20899/results')
# time.sleep(7) # Let the user actually see something!
# search_box = driver.find_elements(By.ID, 'applicationHost')
# print(search_box)
# driver.quit()


'''
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





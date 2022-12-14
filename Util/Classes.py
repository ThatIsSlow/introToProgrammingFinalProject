############### sources ###############: 
# Mr. Cozort code
# https://www.geeksforgeeks.org/writing-excel-sheet-using-python/
# https://stackoverflow.com/questions/38022658/selenium-python-handling-no-such-element-exception
# https://chromedriver.chromium.org/downloads


### IMPORT LIBRARIES ##
from time import sleep
import xlwt
from xlwt import Workbook
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# Class that searches wesbsite and then sends info pulled into an excel sheet
class WebdriverToExcel:
    def __init__(self, url, Desired_Club):
        self.url = url
        self.Des_Club = Desired_Club
        self.itemsfound = 0
        self.datafound = []
#Main method that does all the heavy lifting
    def webdriver(self):
        # Defines a variable for Chrome driver to use
        URL = self.url
        # chrome driver lives in a different folder, so i need to call that folder, and then it opens a new window using the URL
        # chrome_driver = "Code\Projects\chromedriver.exe"
        chrome_driver = "intoToProgrammingFinalProject\Util\chromedriver_win32.zip\chromedriver.exe"
        driver = webdriver.Chrome(chrome_driver)
        driver.get(URL)
        # Gives the website time to render so that chromedriver can read it
        sleep(40)

        #This actually searches the website, and finds the amount of items found. Items found are stored in an empty list
        searchresults = driver.find_elements(By.XPATH,"//span[contains(@class,'ng-binding')]")

        Numb_Data = len(searchresults)
        #several vairables that are used to iterate through the list and search for things
        
        SearchWordFound = True

        # search loop, does a majority of the heavy lifting to find the desired club that we are looking for
        # Uses a true/false variable to only pull race times out of the list IF the club name was located
        # Items found is a counter that tracks how many items the code pulls out of the website so that it then can print the
        # proper amount of items into a spreadsheet
        for i in searchresults:
            if SearchWordFound == False and len(i.text) > 0:
                self.datafound.append(i.text)
                self.itemsfound += 1
                SearchWordFound = True
            if len(i.text) > 0:
                if self.Des_Club in i.text:
                    Finish_position = searchresults.index(i) - 1
                    self.datafound.append(searchresults[Finish_position].text)
                    self.itemsfound += 1
                    self.datafound.append(i.text)
                    self.itemsfound += 1
                    # I need to take the next value of i, and append it as well, because that will give me the time of the racer.
                    SearchWordFound = False
            if len(self.datafound) > Numb_Data:
                break
        # duh
        print(self.datafound)

        # write to excel
    # creates instance of an imported class allowing maniuplation of excel
    def toexcel(self):  
        wb = Workbook()
        #Creates the sheet as well as writes headers
        sheet1 = wb.add_sheet("Sheet 1")
        sheet1.write(0,0, 'Finish position')
        sheet1.write(0,1, 'Name')
        sheet1.write(0,2, 'Time')
        # this format is so that longer names fit in spreadsheet well
        sheet1.col(1).width = 10000

        # prints the items that we pulled out int the search function into the excel file.
        for i in range(0,self.itemsfound):
            sheet1.write((i)//3+1,i%3, self.datafound[i])

        # saves the excel file
        wb.save('xlwt_example.xls')








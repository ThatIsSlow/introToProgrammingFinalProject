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
https://medium.com/geekculture/how-to-import-another-file-in-python-4f833ea462b1
https://realpython.com/python-gui-tkinter/

"""
# Import Libraries
from Util.Classes import WebdriverToExcel
import tkinter as tk
from tkinter import *
from tkinter import ttk



def RunWebd(URL, Desired_Team):
    # Instantiates our self created imported class, and calls it
    Webdriver = WebdriverToExcel("'" + URL + "'", "'" + Desired_Team + "'")
    Webdriver.webdriver()
    


# Create the main window
window = tk.Tk()
window.title("HereNowResults assimilator")
# window.geometry("750x350")

mainframe = ttk.Frame(window, padding="3 4 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

URLtoSearch = StringVar()
url_entry = ttk.Entry(mainframe, width=50, textvariable=URLtoSearch)
url_entry.grid(column=2, row=1, sticky=(W,E))

TeamtoSearch = StringVar()
team_entry = ttk.Entry(mainframe, width=50, textvariable=TeamtoSearch)
team_entry.grid(column=2, row=2, sticky=(W,E))

ttk.Button(mainframe, text="Find My Team!", command=RunWebd).grid(column=2, row=3, sticky=(E))
ttk.Label(mainframe, text="What Race would you like to search? (URL)").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="What Team would you like to search for? (Check your spelling!)").grid(column=3, row=2, sticky=W)


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

url_entry.focus()
window.bind("<Return>", RunWebd)


# Start the main event loop
window.mainloop()



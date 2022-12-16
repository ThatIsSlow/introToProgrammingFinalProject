# Jonas Thieme
#################################################################################################################################################################
"""
PROJECT OUTLINE:
    - HereNow (rowing results website) parser
            - Will likely use Tkinter
            - if not tkinter will use flask to put functional aspect in a website
            - will enable the user to input a team name or a rower name or a boat class
                - will then scan HereNow, looking through certain races, or a lot of races, to assemble all of the results of the
                    desired search, and then place it into a new window/file
    - Tried my best to follow standard naming conventions, probably messed up somewhere
"""
#################################################################################################################################################################

"""
Sources: 
https://medium.com/geekculture/how-to-import-another-file-in-python-4f833ea462b1
https://realpython.com/python-gui-tkinter/
https://www.edureka.co/blog/web-scraping-with-python/
https://coderslegacy.com/tkinter-center-window-on-screen/
https://www.pythontutorial.net/tkinter/tkinter-grid/
https://tkdocs.com/tutorial/grid.html
https://peps.python.org/pep-0008/

"""
# Import Libraries
from Util.Classes import WebdriverToExcel
import tkinter as tk
from tkinter import *
from tkinter import ttk
import time 

# test function to test thing
def rand_func():
    print('This random function works')

#Big boy function that runs the magic
def run_webd():
    #takes data entered and stores it in variables
    Durl = entry1.get()
    team = entry2.get()
    print(Durl)
    print(team)
    # Instantiates our self created imported class
    Webdriverv = WebdriverToExcel(Durl, team)
    find_team_but.destroy()     #removes the button to initatie this function so that it cant be run twice
    
    wait_label = ttk.Label(mainframe, text="Please wait while we find your team", font=('Helvetica 15 bold'))
    wait_label.grid(column=0, row=6)
    window.update()     #had to use this instead of mainloop because tkinter sucks
    
    # Calls Class and method
    Webdriverv.webdriver()
    wait_label.destroy()    # removes the label that says "please wait while we find your team"

    # this is the bit that actually displays the findings in tkinter, uses several variables 
    # to keep track of how to group items together
    # and where to print them(rows and collumns (or however you spell that))
    counter = 0
    temp_list = []
    row_counter = 0
    colum_counter = 0
    # this is honestly a mess and I promise you there is a better way to do it, I just don't know it yet
    for i in Webdriverv.datafound:    
        temp_list.append(i)
        counter += 1
        if counter == 3:
            str(list)
            team_label = ttk.Label(subframe, text=temp_list, borderwidth=1, relief="solid")
            team_label.grid(column=colum_counter, row=row_counter, sticky=EW)
            window.update()
            counter = 0
            colum_counter += 1
            if colum_counter > 3:
                colum_counter = 0
                row_counter += 1
            temp_list.clear()
    #packed this function inside the bigger function because I wasn't sure if the excel function would be able to access the pulled data
    # from the webdriver function
    def webdtoexcel():
        Webdriverv.to_excel(team)
        Excel_Button.destroy()
    # Gives the option to print results to an excel file (This honestly works the best, I've never had any problems with it)
    Excel_Button = ttk.Button(mainframe, text="Print your results to an excel file?", command=webdtoexcel)
    Excel_Button.grid(column=0, row=10) 

# Create the main window, this block makes the window appear centered on screen rather than in a corner
window = tk.Tk()
WIDTH = 600     # Width 
HEIGHT = 300    # Height
screen_width = window.winfo_screenwidth()   # Width of the screen
screen_height = window.winfo_screenheight()     # Height of the screen
# Calculate Starting X and Y coordinates for Window
x = (screen_width/2) - (WIDTH/2)
y = (screen_height/2) - (HEIGHT/2) 
# snagged this line from stack overflow
window.geometry('%dx%d+%d+%d' % (WIDTH, HEIGHT, x, y))


window.title("HereNowResults assimilator")
mainframe = LabelFrame(window, width= WIDTH, height= 150, bd=5)
mainframe.grid() 

subframe = LabelFrame(window, width=WIDTH, height=150, bd=5 )
subframe.grid()
#Stop the frame from propagating the widget to be shrink or fit (Class code)
mainframe.grid_propagate(True)
subframe.grid_propagate(True)

#Create an Entry widget in the Frame, plus a label to identify the textbox
entry1 = ttk.Entry(mainframe, width= 50)
race_label = ttk.Label(mainframe, text="What Race would you like to search? (URL)")
race_label.grid(column=0, row=0)
entry1.grid(column=0, row=1)

#Create another entry widget, plus a label to identify the textbox
entry2 = ttk.Entry(mainframe, width= 50)
team_label = ttk.Label(mainframe, text="What Team would you like to search for? (Check your spelling!)")
team_label.grid(column=0, row=2)
entry2.grid(column=0, row=3)

# Big boy button that does all the fun stuff.
find_team_but = ttk.Button(mainframe, text="Find My Team!", command=run_webd)
find_team_but.grid(column=0, row=5)


#sets cursor in first entry box
entry1.focus()

mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(6, weight=2)
# Start the main event loop
# mainloop is the worst function of all time, it literally prevents code from running I hate it it sucks. Woe is me
window.mainloop()



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
import requests
res = requests.get('https://herenow.com/results/#/races/21065/results')
type(res)
res.status_code == requests.codes.ok
print(res.text[500:1000])
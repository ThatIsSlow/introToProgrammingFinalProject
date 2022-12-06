from time import sleep
import xlwt
from xlwt import Workbook
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

Numb_Data = 99
Practice_list = [
     '1', 'Matthew Willer\n(Redwood Scullers)', '6:51.617', '2', 'Tristan Wakefield\n(Y Quad Cities)', '7:00.249', '3', 'Isaiah Harrison\n(Unaff. (USA))', '7:04.016', '4', 'Andrew Furlow\n(Gainesville Area)', '7:04.475', '5', 'Patrick Reilly\n(West Side)', '7:10.380', '6', 'Philipp Seeger\n(Holy Spirit)', '7:10.504', '7', 'Tristan Atreides\n(Oak Neck Academy)', '7:10.998', '8', 'Matthew Lexa\n(Lower Merion)', '7:12.987', '9', 'Samuel Dowd\n(Red Dog)', '7:14.440', '10', 'Thomas Spelmans\n(Halifax)', '7:15.293', '11', 'Devan Godfrey\n(Woodlands)', '7:15.336', '12', 'Aleksandar Jovanovic-Hacon\n(Utah)', '7:16.402', '13', 'Lucien Gaitskell\n(Narragansett)', '7:16.632', '14', 'Tanner Hamilton\n(Tempe Junior, Inc.)', '7:17.141', '15', 'McCune McCornack\n(Oregon Unlimited)', '7:18.727', '16', 'Emerson Shatouhy\n(North Jersey)', '7:21.655', '17', 'Andrew Josephbek\n(Long Beach Junior)', '7:22.739', '18', 'Robert Walker\n(Three Rivers)', '7:24.343', '19', 'Ales Makarov\n(Maritime)', '7:25.681', '20', 'Keith leight\n(RowHouse)', '7:25.840', '21', 'Lacika Tompa\n(Sylvan Scullers)', '7:25.864', '22', 'Martijn den Boon\n(Camp Randall)', '7:26.727', '23', 'Ian Doctor\n(Brighton High School)', '7:28.968', '24', 'Quinlan Daly\n(Maritime)', '7:29.134', '25', 'David Soucie-Garza\n(Texas Center)', '7:29.514', '26', 'Caden Adams\n(Taylor-Allderdice)', '7:30.905', '27', 'Cole Jucksch\n(Olympia Area)', '7:31.427', '28', 'Hayden Ross\n(Manatee County Youth)', '7:34.033', '29', 'William Cicero\n(Seattle Scullers)', '7:36.545', '30', 'Tiernan Green\n(Riverside)', '7:37.344', '31', 'Matthew Sidlowski\n(Wilmington Youth)', '7:43.813', '32', 'Joel Bustamante\n(Miami)', '7:46.218', '33', 'Max Xu\n(Mile High)', '7:48.028', '34'
    ]


# write to excel
# use modulus 
wb = Workbook()

sheet1 = wb.add_sheet("Sheet 1")
sheet1.write(0,0, 'Finish Position')
sheet1.write(0,1, 'Name')
sheet1.write(0,2, 'time')

for i in range(0,Numb_Data):
    sheet1.write((i)//3+1, i%3, Practice_list[i] )
    # sheet1.write(1+i,0, Practice_list[i])
    


wb.save('xlwt_example1.xls')
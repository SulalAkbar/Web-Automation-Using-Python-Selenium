import os
import subprocess
import urllib.request
import re

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,WebDriverException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
chrome_options = Options()

###
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
###
#driver = webdriver.Chrome(executable_path=r'H:\Programs\chromedriver_win32 (2)\chromedriver.exe')
#
#

def get_File(lat,lon,year,month,day,hour,height):
    driver.get ("https://ready.arl.noaa.gov/hypub-bin/trajsrc.pl")
    select = Select(driver.find_element_by_name('metdata'))

    #Selecting GFS 192h (always the same option)
    select.select_by_value('GFS')

    #Now entering sources in First Page src1 , src2
    src1=driver.find_element_by_name('Lat')#
    src1.send_keys(lat)

    src2=driver.find_element_by_name('Lon')#
    src2.send_keys(lon)

    #Clicking on next First Click
    driver.find_element_by_xpath("//input[@value='Next>>']").click()

    #Second Click
    driver.find_element_by_xpath("//input[@value='Next>>']").click()

    print('Before Radio Button')

    #driver.find_element_by_xpath('//input[text()="Isobaric"]')

    driver.find_element_by_xpath("//input[@value='1']").click()


    #Now entering Year , Month , Day , hour Data .....
    #Year
    select = Select(driver.find_element_by_name('Start year'))
    select.select_by_index(year)

    #Month
    select = Select(driver.find_element_by_name('Start month'))
    select.select_by_index(month)

    #Day
    select = Select(driver.find_element_by_name('Start day'))
    select.select_by_index(day)

    #Hour
    select = Select(driver.find_element_by_name('Start hour'))
    select.select_by_index(hour)


    print('Completed Year,Month,Day,Hour Info')
    #Entering Level1 height Info ...
    level_1=driver.find_element_by_name('Source hgt1')
    level_1.clear()
    level_1.send_keys(height)

    #PDF File 'No'
    driver.find_element_by_xpath("//input[@name='pdffile'][@value='No']").click()

    print('Hurrah')

    #Pressing 'Trajectory '
    driver.find_element_by_xpath("//input[@type='submit'][@value='Request trajectory (only press once!)']").click()

    print('Clicked on Trajectory')
    print('Now start waiting for 30 seconds')
    driver.implicitly_wait(35)

    down_link=driver.find_element_by_xpath("//*[@id='page_center']/table/tbody/tr/td/div[4]/table[1]/tbody/tr/td/font/ul/li[2]/b/a")

    print(down_link.get_attribute("href"))

    down_link = down_link.get_attribute("href")

    Path=re.search('\(([^)]+)', down_link).group(1)

    print('Path Without splitting ..',Path)

    print('Path After splitting ..',Path[1:27])

    url = Path[1:27]

    #Downloading File on System...
    url = 'https://ready.arl.noaa.gov'+url

    print('Complete URL',url)

    print('Now Downloading File')

    urllib.request.urlretrieve(url, 'C:/Users/Sulal/Desktop/New Challenge/YourFile.txt')#Here You need to give your address , where you want to save the file

    print('Your File Downloaded ...')

print('Calling Function')


#Parameters
#Latitude , Longitude ,Year , Month , Day , Hour , (Level 1 Height)
get_File(33,9,0,1,5,2,13500) #This is the Function , Where you will put the parameters

print('Funtion Finished')

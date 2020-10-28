# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:55:51 2020
"""
import time
import pandas as pd
from pandas import DataFrame
from selenium import webdriver
from datetime import datetime
import os

now = datetime.now()
time_stamp = str(now)[0:4] + str(now)[5:7] + str(now)[8:10] + '_' + str(now)[11:13] + str(now)[14:16]

#path = os.getcwd()

path = 'C:\\Users\\Dick Sang\\Desktop\\news platform'

os.chdir(path)
##################################################################
# A. HK news
##################################################################
#--- 1. Yahoo News (1)
driver = webdriver.Chrome()
driver.get("https://hk.news.yahoo.com/hong-kong")
time.sleep(5)

info_path = driver.find_elements_by_xpath("//*[@id='YDC-Stream']/ul/li/div/div/div/h3/a")

info = [i.text for i in info_path]

#info = list(filter(None, info))

link_path = driver.find_elements_by_xpath("//*[@id='YDC-Stream']/ul/li/div/div/div/h3/a")

link = [i.get_attribute("href") for i in link_path]

hknews1 = DataFrame([info, link]).transpose()

hknews1[2] = 'Yahoo'

driver.close()

#--- 2. Now News
driver = webdriver.Chrome()
driver.get("https://news.now.com/home/local")
time.sleep(5)

info_path = driver.find_elements_by_class_name('newsLeading')
info = [i.text for i in info_path]

link_path = driver.find_elements_by_tag_name('a')
# iterate link_path -> if link contains 
link = [i.get_attribute("href") for i in link_path if(("local" in i.get_attribute("href")) and ("newsId=" in i.get_attribute("href")))]

hknews2 = DataFrame([info, link]).transpose()

hknews2[2] = 'Now news'

driver.close()

#-- 3. Apple Daily
driver = webdriver.Chrome()
driver.get("https://hk.appledaily.com/realtime/breaking/")
time.sleep(5)

info_path = driver.find_elements_by_xpath("//span[contains(@class, 'desktop') and contains(@class, 'blurb')]")
info = [i.text for i in info_path]

link_path = driver.find_elements_by_xpath("//a[contains(@class, 'story-card')]")
# iterate link_path -> if link contains 
link = [i.get_attribute("href") for i in link_path]

hknews3 = DataFrame([info, link]).transpose()

hknews3[2] = 'Apple Daily'

driver.close()

#-- 4. HK01
driver = webdriver.Chrome()
driver.get("https://www.hk01.com/channel/2/%E7%A4%BE%E6%9C%83%E6%96%B0%E8%81%9EE")

time.sleep(5)
driver.maximize_window() # maximize the window size

#driver.execute_script("window.scrollBy(0,1000)", "") # scroll by 1000 pixels
for i in range(2):
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)", "") # scroll by document height (once)
    time.sleep(5)

info_path = driver.find_elements_by_xpath("//a[contains(@data-testid,'common-contentCard-title')]")

info = [i.text for i in info_path]

link_path = driver.find_elements_by_xpath("//a[contains(@data-testid,'common-contentCard-title')]")
# iterate link_path -> if link contains
link = [i.get_attribute("href") for i in link_path]

hknews4 = DataFrame([info, link]).transpose()
hknews4[2] = 'HK01'

driver.close()
##################################################################
# B. Properties
##################################################################
#--- 1. edigest
driver = webdriver.Chrome()

driver.get("https://www.edigest.hk/category/%e6%a8%93%e5%b8%82/")

time.sleep(5)

 
info_path = driver.find_elements_by_xpath("//*[@id='main']/div/div/div/div/div/article/div/a/div/h3")

info = [i.text for i in info_path]

#info = list(filter(None, info))

link_path = driver.find_elements_by_xpath("//*[@id='main']/div/div/div/div/div/article/div/a")

link = [i.get_attribute("href") for i in link_path]

Property1 = DataFrame([info, link]).transpose()

Property1[2] = 'E digest'

driver.close()

#--- 2. Yahoo

driver = webdriver.Chrome()

driver.get("https://hk.news.yahoo.com/property")

time.sleep(5)

info_path = driver.find_elements_by_xpath("//*[@id='YDC-Stream']/ul/li/div/div/div/h3/a")

info = [i.text for i in info_path]

#info = list(filter(None, info))

link_path = driver.find_elements_by_xpath("//*[@id='YDC-Stream']/ul/li/div/div/div/h3/a")

link = [i.get_attribute("href") for i in link_path]

Property2 = DataFrame([info, link]).transpose()

Property2[2] = 'Yahoo'

driver.close()
##################################################################
# C. Investments
##################################################################
#--- 1. edigest

driver = webdriver.Chrome()

driver.get("https://www.edigest.hk/category/%e6%8a%95%e8%b3%87/")

time.sleep(5)

info_path = driver.find_elements_by_xpath("//*[@id='main']/div/div/div/div/div/article/div/a/div/h3")

info = [i.text for i in info_path]

#info = list(filter(None, info))

link_path = driver.find_elements_by_xpath("//*[@id='main']/div/div/div/div/div/article/div/a")

link = [i.get_attribute("href") for i in link_path]

Investment1 = DataFrame([info, link]).transpose() 

Investment1[2] = 'E digest'

driver.close()

#--- 2. Yahoo
driver = webdriver.Chrome()

driver.get("https://hk.news.yahoo.com/business")

time.sleep(5)

info_path = driver.find_elements_by_xpath("//*[@id='YDC-Stream']/ul/li/div/div/div/h3/a")

info = [i.text for i in info_path]

#info = list(filter(None, info))

link_path = driver.find_elements_by_xpath("//*[@id='YDC-Stream']/ul/li/div/div/div/h3/a")

link = [i.get_attribute("href") for i in link_path]

Investment2 = DataFrame([info, link]).transpose()

Investment2[2] = 'Yahoo'

driver.close()

#--- 3. Now News
driver = webdriver.Chrome()
driver.get("https://news.now.com/home/finance")
time.sleep(5)

info_path = driver.find_elements_by_class_name('newsLeading')
info = [i.text for i in info_path]

link_path = driver.find_elements_by_tag_name('a')
# iterate link_path -> if link contains 
link = [i.get_attribute("href") for i in link_path if(("finance" in i.get_attribute("href")) and ("newsId=" in i.get_attribute("href")))]

Investment3 = DataFrame([info, link]).transpose()

Investment3[2] = 'Now news'

driver.close()

##################################################################
# D. World news
##################################################################
#--- 1. Yahoo News (1)
driver = webdriver.Chrome()
driver.get("https://hk.news.yahoo.com/world")
time.sleep(5)

info_path = driver.find_elements_by_xpath("//*[@id='YDC-Stream']/ul/li/div/div/div/h3/a")
info = [i.text for i in info_path]

#info = list(filter(None, info))

link_path = driver.find_elements_by_xpath("//*[@id='YDC-Stream']/ul/li/div/div/div/h3/a")
link = [i.get_attribute("href") for i in link_path]

world1 = DataFrame([info, link]).transpose()
world1[2] = 'Yahoo'

driver.close()

#-- 2. Apple Daily
driver = webdriver.Chrome()
driver.get("https://hk.appledaily.com/realtime/international/")
time.sleep(5)

info_path = driver.find_elements_by_xpath("//span[contains(@class, 'desktop') and contains(@class, 'blurb')]")
info = [i.text for i in info_path]

link_path = driver.find_elements_by_xpath("//a[contains(@class, 'story-card')]")
# iterate link_path -> if link contains 
link = [i.get_attribute("href") for i in link_path]

world2 = DataFrame([info, link]).transpose()

world2[2] = 'Apple Daily'

driver.close()

#-- 3. HK01
driver = webdriver.Chrome()
driver.get("https://www.hk01.com/zone/4/%E5%9C%8B%E9%9A%9B")

time.sleep(5)
driver.maximize_window() # maximize the window size

#driver.execute_script("window.scrollBy(0,1000)", "") # scroll by 1000 pixels
for i in range(2):
    driver.execute_script("window.scrollBy(0, document.body.scrollHeight)", "") # scroll by document height (once)
    time.sleep(5)

info_path = driver.find_elements_by_xpath("//a[contains(@data-testid,'common-contentCard-title')]")

info = [i.text for i in info_path]

link_path = driver.find_elements_by_xpath("//a[contains(@data-testid,'common-contentCard-title')]")
# iterate link_path -> if link contains
link = [i.get_attribute("href") for i in link_path]

world3 = DataFrame([info, link]).transpose()
world3[2] = 'HK01'

driver.close()
##################################################################
# Add labels
##################################################################
hknews = pd.concat([hknews1, hknews2, hknews3, hknews4])
hknews[3] = 'HK news'

Investment = pd.concat([Investment1, Investment2, Investment3])
Investment[3] = 'Investment'

Property = pd.concat([Property1, Property2])
Property[3] = 'Property'

world = pd.concat([world1, world2, world3])
world[3] = 'World'
##################################################################
# aggregate the extracted information - and make the link work
##################################################################
summary_file = pd.concat([hknews, world, Investment, Property])
# make the link work
summary_file[1] = '=hyperlink("' + summary_file[1] + '")'
##################################################################
# rearrange column order
##################################################################
summary_file = summary_file[[3, 2, 0, 1]]

#summary_file.to_excel("summary_file.xlsx", sheet_name = "summary_file")

summary_file.to_csv("summary_file_" + time_stamp +".csv", encoding='utf_8_sig')

print("You may close me now!")
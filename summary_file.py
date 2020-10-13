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

path = os.getcwd()

#path = 'C:\\Users\\Dick Sang\\Desktop\\5. Data Analytics\\6. Automations\\2. Newspaper Automation\\Z. summary file'

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
# Add labels
##################################################################
hknews = pd.concat([hknews1, hknews2, hknews3])
hknews[3] = 'HK news'

Investment = pd.concat([Investment1, Investment2, Investment3])
Investment[3] = 'Investment'

Property = pd.concat([Property1, Property2])
Property[3] = 'Property'
##################################################################
# aggregate the extracted information - and make the link work
##################################################################
summary_file = pd.concat([Investment, Property, hknews])
# make the link work
summary_file[1] = '=hyperlink("' + summary_file[1] + '")'
##################################################################
# rearrange column order
##################################################################
summary_file = summary_file[[3, 2, 0, 1]]

#summary_file.to_excel("summary_file.xlsx", sheet_name = "summary_file")

summary_file.to_csv("summary_file_" + time_stamp +".csv", encoding='utf_8_sig')

print("You may close me now!")
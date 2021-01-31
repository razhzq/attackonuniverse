# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 08:58:32 2021

@author: Loga
"""

from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path=r'C:\Users\Loga\Desktop\AIRUS TECH\Sneaker Bot\chromedriver.exe')

driver.get('https://twitter.com/')
#driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath('// *[@data-testid="loginButton"]').click()
time.sleep(5)
driver.find_element_by_xpath('// input[@name="session[username_or_email]"]').send_keys('attackuniverse@gmail.com')
time.sleep(2)
driver.find_element_by_xpath('// input[@name="session[password]"]').send_keys('Cannonbolt1')
time.sleep(2)
driver.find_element_by_xpath('// *[@data-testid="LoginForm_Login_Button"]').click()
time.sleep(2)
driver.find_element_by_xpath('// *[@class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]').click()
time.sleep(2)
driver.find_element_by_xpath('// *[@class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]').send_keys('Hello and Good Morning!')
time.sleep(2)
driver.find_element_by_xpath('// *[@data-testid="tweetButtonInline"]').click()








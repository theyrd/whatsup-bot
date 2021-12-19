#!/usr/bin/env python3.5

from logging import exception
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time, sys

def new_chat(user_name):
    new_chat = driver.find_element_by_xpath('//div[@class="_3LX7r"]')
    new_chat.click()

    new_user = driver.find_element_by_xpath('//div[@class="_2_1wd copyable-text selectable-text"]')
    new_user.send_keys(user_name)

    time.sleep(2)
    
    try:
        user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException:
        print('Given user "{}" not found in the contact list'.format(user_name))
    except Exception as e:
        driver.close()
        print(e)
        sys.exit()

driver = webdriver.Chrome()
driver.get(url = "https://web.whatsapp.com/")

# time to scan the QR code
time.sleep(15)
print('QR code have been scanned')

user_name_list = ['WhatsApp Bot']
for user_name in user_name_list:

    # find the contact's chat
    try:
        user = driver.find_element_by_xpath('//span[@title="{}"]'.format(user_name))
        user.click()
    except NoSuchElementException as se:
        new_chat(user_name)
    
    # write text in the chat box
    chat_box = driver.find_element_by_xpath('//div[@class="_2A8P4"]')
    chat_box.send_keys('Hello, it\'s me !! The WhatsApp Bot :)')

    # click & send message to the contact
    chat_box = driver.find_element_by_xpath('//button[@class="_1E0Oz"]')
    chat_box.click()


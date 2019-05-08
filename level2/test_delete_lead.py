'''
Created on 26-Mar-2019

@author: Gopinath Jayakumar
'''


import re
import time

from selenium import webdriver

def setup_module():
    global driver
    driver = webdriver.Chrome("C:\\TestLeaf\\eclipse-workspace\\SeleniumPython\\drivers\\chromedriver.exe")
    driver.get("http://leaftaps.com/opentaps")
    driver.maximize_window()
    driver.implicitly_wait(30)
 
def test_edit_lead():   
    driver.find_element_by_id('username').send_keys('DemoSalesManager')
    driver.find_element_by_id('password').send_keys('crmsfa')
    driver.find_element_by_class_name('decorativeSubmit').click()
    driver.find_element_by_link_text('CRM/SFA').click()
    driver.find_element_by_link_text('Leads').click()
    driver.find_element_by_link_text('Find Leads').click()
    driver.find_element_by_xpath('(//*[@name = "firstName"])[3]').send_keys('Gopinath')
    driver.find_element_by_xpath('//button[text()="Find Leads"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('(//div[@class="x-grid3-cell-inner x-grid3-col-partyId"])[1]/a').click()
    txt = driver.find_element_by_id('viewLead_companyName_sp').text
    
    txt = re.sub(r'[^0-9]','', txt)
    driver.find_element_by_link_text('Delete').click()
    driver.find_element_by_link_text('Find Leads').click()
    driver.find_element_by_name('id').send_keys(txt)
    driver.find_element_by_xpath('//button[text()="Find Leads"]').click()
    time.sleep(3)
    x = driver.find_element_by_xpath('//div[text()="No records to display"]').text
    print(x)

def teardown_module():
    driver.close()

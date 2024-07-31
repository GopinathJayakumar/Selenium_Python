'''
Created on 26-Mar-2019

@author: Gopinath Jayakumar
'''
import pytest

from selenium import webdriver


def setup_module():
    global driver
    driver = webdriver.Chrome("C:\\gopi\\eclipse-workspace\\SeleniumPython\\drivers\\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)   

@pytest.mark.parametrize("user_name, pass_word",
                          [
                              ('DemoSalesManager', 'crmsfa'),
                              ('DemoCRS', 'crmsfa')
                              ]
                          )    
def test_login(user_name, pass_word):
    driver.get('http://leaftaps.com/opentaps')
    driver.find_element_by_id('username').send_keys(user_name)
    driver.find_element_by_id('password').send_keys(pass_word)
    driver.find_element_by_class_name('decorativeSubmit').click()
    driver.find_element_by_link_text('CRM/SFA').click()
    driver.find_element_by_link_text('Leads').click()
    driver.find_element_by_link_text('Create Lead').click()
    driver.find_element_by_id('createLeadForm_companyName').send_keys('TestLeaf')
    driver.find_element_by_id('createLeadForm_firstName').send_keys('Gopinath')
    driver.find_element_by_id('createLeadForm_lastName').send_keys('Jayakumar')
    driver.find_element_by_name('submitButton').click()
    driver.close()

def teardown_module():
    driver.close()

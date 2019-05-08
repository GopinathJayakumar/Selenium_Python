'''
Created on 20-Mar-2019

@author: Gopinath Jayakumar
'''

from selenium import webdriver


driver = webdriver.Chrome("D:\\03 Python\\workspace\\SeleniumPython\\drivers\\chromedriver.exe")
driver.get('http://leaftaps.com/opentaps')
driver.maximize_window()
driver.implicitly_wait(30)
ele_user_name = driver.find_element_by_id('username')
ele_user_name.send_keys('DemoSalesManager')
driver.find_element_by_id('password').send_keys('crmsfa')
driver.find_element_by_class_name('decorativeSubmit').click()
driver.find_element_by_link_text('CRM/SFA').click()
driver.find_element_by_link_text('Leads').click()
driver.find_element_by_link_text('Create Lead').click()
driver.find_element_by_id('createLeadForm_companyName').send_keys('TestLeaf')
driver.find_element_by_id('createLeadForm_firstName').send_keys('Gopinath')
driver.find_element_by_id('createLeadForm_lastName').send_keys('Jayakumar')
driver.find_element_by_name('submitButton').click()
driver.close()


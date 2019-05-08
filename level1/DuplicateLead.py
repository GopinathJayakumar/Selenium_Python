'''
Created on 26-Mar-2019

@author: Gopinath Jayakumar
'''

import time

from selenium import webdriver


driver = webdriver.Chrome("C:\\TestLeaf\\eclipse-workspace\\SeleniumPython\\drivers\\chromedriver.exe")
driver.get('http://leaftaps.com/opentaps')
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element_by_id('username').send_keys('DemoSalesManager')
driver.find_element_by_id('password').send_keys('crmsfa')
driver.find_element_by_class_name('decorativeSubmit').click()

driver.find_element_by_link_text('CRM/SFA').click()
driver.find_element_by_link_text('Leads').click()

driver.find_element_by_link_text('Find Leads').click()
driver.find_element_by_xpath('(//input[@name="firstName"])[3]').send_keys('Gopinath')

driver.find_element_by_xpath('//button[text()="Find Leads"]').click()
time.sleep(3)

driver.find_element_by_xpath('(//div[@class="x-grid3-cell-inner x-grid3-col-partyId"])[1]/a').click()

driver.find_element_by_link_text('Duplicate Lead').click()
driver.find_element_by_id('createLeadForm_companyName').clear()
driver.find_element_by_id('createLeadForm_companyName').send_keys('Test_Leaf')

driver.find_element_by_name('submitButton').click()
time.sleep(3)

txt = driver.find_element_by_id('viewLead_companyName_sp').text
print(txt)

if 'Test_Leaf' in txt:
    print('Company_Name Updated')
else: 
    print('Not Matched')
    
driver.close()













if __name__ == '__main__':
    pass
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
driver.find_element_by_link_text('Merge Leads').click()

driver.find_element_by_xpath('(//img[@alt="Lookup"])[1]').click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
print(driver.title)
txt = driver.find_element_by_xpath('(//div[@class="x-grid3-cell-inner x-grid3-col-partyId"])[1]/a').text
driver.find_element_by_xpath('(//div[@class="x-grid3-cell-inner x-grid3-col-partyId"])[1]/a').click()

driver.switch_to.window(driver.window_handles[0])
time.sleep(3)
print(driver.title)

driver.find_element_by_xpath('(//img[@alt="Lookup"])[2]').click()
driver.switch_to.window(driver.window_handles[1])
time.sleep(3)
print(driver.title)
driver.find_element_by_xpath('(//div[@class="x-grid3-cell-inner x-grid3-col-partyId"])[2]/a').click()

driver.switch_to.window(driver.window_handles[0])
time.sleep(3)
print(driver.title)

driver.find_element_by_link_text('Merge').click()
time.sleep(3)
driver.switch_to.alert.accept()
driver.find_element_by_link_text('Find Leads').click()
time.sleep(3)
driver.find_element_by_name('id').send_keys(txt)
driver.find_element_by_xpath('//button[text()="Find Leads"]').click()
time.sleep(3)
x = driver.find_element_by_xpath('//div[text()="No records to display"]').text
print(x)
driver.close()










if __name__ == '__main__':
    pass
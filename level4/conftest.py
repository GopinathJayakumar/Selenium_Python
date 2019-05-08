'''
Created on 27-Mar-2019

@author: Gopinath Jayakumar
'''

import pytest
from pip._vendor.requests.api import request

@pytest.yield_fixture(scope = "class")
def setup(browser):
    if browser == 'Chrome':
        from selenium import webdriver
        global driver
        driver = webdriver.Chrome("C:\\TestLeaf\\eclipse-workspace\\SeleniumPython\\drivers\\chromedriver.exe")
        driver.get('http://leaftaps.com/opentaps')
        driver.maximize_window()
        driver.implicitly_wait(30)
        yield
        driver.close()
    
def pytest_addoptions(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help = "Type of Operating System")
    
@pytest.fixture(scope = "session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope = "session")
def osType(request):
    return request.config.test_gnu_getoption("--osType")


        
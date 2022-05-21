from behave import *
from selenium import webdriver
from PageObject.Homepage import homepage
from PageObject.wrapper import wrapper
from PageObject.Dashboard import dashboard
from PageObject.Notes import Notes
import time
import allure


global driver
#driver = webdriver.Firefox()
#driver.implicitly_wait(15)
global Login
global credentials
global accountpage
global page_notes



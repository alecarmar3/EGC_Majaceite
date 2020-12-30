# Generated by Selenium IDE
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","decide.settings")
import django
django.setup()

import pytest
import time
import json
from selenium import webdriver
from django.conf import settings
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.support import expected_conditions as EC
from base.tests import BaseTestCase
"""
class TestDownloadvotingresultsindifferentformats():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_downloadvotingresultsindifferentformats(self):
      #Change Id of visualizer to a known Id
    self.driver.get("http://localhost:8000/visualizer/1/")
    self.driver.set_window_size(797, 824)
    elements = self.driver.find_elements(By.CSS_SELECTOR, "input:nth-child(3)")
    assert len(elements) > 0
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    self.driver.find_element(By.NAME, "Formato").click()
    dropdown = self.driver.find_element(By.NAME, "Formato")
    dropdown.find_element(By.XPATH, "//option[. = 'CSV']").click()
    self.driver.find_element(By.NAME, "Formato").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    self.driver.find_element(By.NAME, "Formato").click()
    dropdown = self.driver.find_element(By.NAME, "Formato")
    dropdown.find_element(By.XPATH, "//option[. = 'XML']").click()
    self.driver.find_element(By.NAME, "Formato").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    self.driver.find_element(By.NAME, "Formato").click()
    dropdown = self.driver.find_element(By.NAME, "Formato")
    dropdown.find_element(By.XPATH, "//option[. = 'PDF']").click()
    self.driver.find_element(By.NAME, "Formato").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()

"""


class TestDownloadResults(StaticLiveServerTestCase):
  def setUp(self):
    #Load base test functionality for decide
    self.base = BaseTestCase()
    self.base.setUp()

    options = webdriver.FirefoxOptions()
    #options.headless = True
    self.driver = webdriver.Firefox(options=options)

    super().setUp()            
            
  def tearDown(self):           
    super().tearDown()
    self.driver.quit()

    self.base.tearDown()
  def test_downloadvotingresultsindifferentformats(self):
    #Change Id of visualizer to a known Id
    self.driver.get("http://localhost:8000/visualizer/1/")
    self.driver.set_window_size(797, 824)
    elements = self.driver.find_elements(By.CSS_SELECTOR, "input:nth-child(3)")
    assert len(elements) > 0
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    self.driver.find_element(By.NAME, "Formato").click()
    dropdown = self.driver.find_element(By.NAME, "Formato")
    dropdown.find_element(By.XPATH, "//option[. = 'CSV']").click()
    self.driver.find_element(By.NAME, "Formato").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    self.driver.find_element(By.NAME, "Formato").click()
    dropdown = self.driver.find_element(By.NAME, "Formato")
    dropdown.find_element(By.XPATH, "//option[. = 'XML']").click()
    self.driver.find_element(By.NAME, "Formato").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
    self.driver.find_element(By.NAME, "Formato").click()
    dropdown = self.driver.find_element(By.NAME, "Formato")
    dropdown.find_element(By.XPATH, "//option[. = 'PDF']").click()
    self.driver.find_element(By.NAME, "Formato").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
  

    


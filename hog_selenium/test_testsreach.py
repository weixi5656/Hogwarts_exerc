# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from hog_selenium.base import Base

class TestTestsreach(Base):

  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test_testsreach(self):
    self.driver.get("https://www.baidu.com/")
    self.driver.set_window_size(1565, 1060)
    self.driver.find_element(By.ID, "kw").send_keys("霍格沃茨魔法学校")
    self.driver.find_element(By.ID, "kw").send_keys(Keys.ENTER)
    self.driver.execute_script("window.scrollTo(0,88)")
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.XPATH, "//div[@id=\'1\']/h3/a/em").click()
    self.vars["win8214"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win8214"])
  

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/11 16:04
# @Author  : VC

from selenium import webdriver
import time
from hog_selenium.base import Base
from selenium.webdriver.common import keys

class TestHogwards(Base):
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def teardown(self):
        time.sleep(2)
        self.driver.quit()

    def test_hogwards(self):
        self.driver.get("https://testerhome.com/")
        self.driver.find_element_by_link_text("社团").click()
        self.driver.find_element_by_link_text("霍格沃兹测试学院").click()
        el = self.driver.find_element_by_css_selector(".topic-22621 .title > a").click()
        print(el.text)
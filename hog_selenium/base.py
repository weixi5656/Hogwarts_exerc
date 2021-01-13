#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/11 17:10
# @Author  : VC
from selenium import webdriver
import time

class Base():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.vars = {}


    def teardown(self):
        time.sleep(3)
        self.driver.quit()
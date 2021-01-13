#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/12 14:40
# @Author  : VC
import time

import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self,base_driver = None):
        base_driver:WebDriver
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
            self.cookie_read()
            time.sleep(10)
        else:
            self.driver = base_driver


    def cookie_read(self):
        with open("../page/data.yaml",encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def find(self,by,value=None):
        if value is None:
            return self.driver.find_element(*by)
        return self.driver.find_element(by=by,value=value)


    def quit(self):
        self.driver.quit()

    def finds(self,by,value=None):
        if value is None:
            return self.driver.find_elements(*by)
        return self.driver.find_elements(by=by,value=value)

    def wait_click(self,element):
        return WebDriverWait(self.driver, 9).until(expected_conditions.element_to_be_clickable(*element))

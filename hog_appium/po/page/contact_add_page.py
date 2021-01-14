#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/14 18:33
# @Author  : VC
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from hog_appium.po.page.base_page import BasePage


class ContactAddPage(BasePage):
    def add_contact(self):
        self.find_send_keys(MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@text='必填']","哈利1")
        self.find_and_click(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@text='男']")
        def wait_ele_find(driver: WebDriver):
            eles = driver.find_elements(MobileBy.XPATH, "//*[@text='女']")
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_ele_find)
        self.wait_for(MobileBy.XPATH, "//*[@text='女']")
        self.find_and_click(MobileBy.XPATH, "//*[@text='女']")
        self.find_send_keys(MobileBy.XPATH, "//*[contains(@text, '手机')]/..//*[@text='手机号']", "11114444998")
        self.find_and_click(MobileBy.XPATH, "//*[@text='保存']")
        return True
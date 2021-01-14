#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/14 18:32
# @Author  : VC

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait



class BasePage():

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, ele=None):
        if ele == None:
            self.driver.find_element(*by)
        return self.driver.find_element(by, ele)

    def finds(self, by, eles=None):
        if eles == None:
            self.driver.find_elements(*by)
        return self.driver.find_elements(by, eles)

    def find_and_click(self, by, ele=None):
        if ele == None:
            self.driver.find_element(*by).click()
        return self.driver.find_element(by, ele).click()

    def scorll_find(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0));')

    def scorll_find_and_click(self, text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("{text}").instance(0));').click()

    def find_send_keys(self,by,locator,text):
        self.find(by,locator).send_keys(text)

    def wait_for(self,by,locator):
        def wait_ele_find(driver: WebDriver):
            eles = driver.find_elements(by, locator)
            return len(eles) > 0

        return WebDriverWait(self.driver, 10).until(wait_ele_find)
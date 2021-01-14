#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/14 13:57
# @Author  : VC
import os
import time
import sys
import json
import appium

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1：7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        caps["settings[waitForIdleTimeout]"] = 1

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    # def test_demo(self):
    #     el1 = self.driver.find_element_by_xpath(
    #         "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView")
    #     el1.click()
    #     el2 = self.driver.find_element_by_xpath(
    #         "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.ImageView[1]")
    #     el2.click()

    def test_daka(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="工作台"]').click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="外出打卡"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"次外出")]').click()
        WebDriverWait(self.driver,10).until(lambda x:"外出打卡成功" in x.page_source)
        assert "外出打卡成功" in self.driver.page_source
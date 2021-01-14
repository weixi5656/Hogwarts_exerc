#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/14 18:45
# @Author  : VC
from appium import webdriver

from hog_appium.po.page.base_page import BasePage
from hog_appium.po.page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver in None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "127.0.0.1：7555"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            caps["noReset"] = "true"
            caps["settings[waitForIdleTimeout]"] = 1
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(3)

    def goto_main(self):
        return MainPage(self.driver)
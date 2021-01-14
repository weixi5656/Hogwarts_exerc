#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/14 16:40
# @Author  : VC
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class TestConTact:
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
        # self.driver.quit()
        pass

    def test_add_member(self):
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="工作台"]').click()
        # self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
        #                          'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("打卡").instance(0));').click()
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="外出打卡"]').click()
        # self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"次外出")]').click()
        # WebDriverWait(self.driver,10).until(lambda x:"外出打卡成功" in x.page_source)
        # assert "外出打卡成功" in self.driver.page_source
        contact_element = self.driver.find_element(MobileBy.XPATH,
                                                   "//*[@resource-id='com.tencent.wework:id/elq' and @text='通讯录']")
        contact_element.click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
                                 'scrollIntoView(new UiSelector().text("添加成员").instance(0));').click()

        add_member_element = self.driver.find_element(MobileBy.XPATH,
                                                      "//*[@class='android.widget.TextView' and @text='手动输入添加']")
        add_member_element.click()

        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/..//*[@text='必填']").send_keys("哈利1")
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'性别')]/..//*[@text='男']").click()

        def wait_ele_find(driver: WebDriver):
            eles = driver.find_elements(MobileBy.XPATH, "//*[@text='女']")
            return len(eles) > 0

        WebDriverWait(self.driver, 10).until(wait_ele_find)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '手机')]/..//*[@text='手机号']").send_keys(
            "11114444999")
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()

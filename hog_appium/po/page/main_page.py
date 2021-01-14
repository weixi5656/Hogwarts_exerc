#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/14 18:32
# @Author  : VC
from appium.webdriver.common.mobileby import MobileBy

from hog_appium.po.page.address_list_page import AddressListPage
from hog_appium.po.page.base_page import BasePage


class MainPage(BasePage):

    def goto_address(self):
        _location_address = (MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/elq' and @text='通讯录']")
        self.find_and_click(_location_address)
        return AddressListPage(self.driver)
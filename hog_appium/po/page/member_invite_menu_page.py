#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/14 18:33
# @Author  : VC
from appium.webdriver.common.mobileby import MobileBy

from hog_appium.po.page.contact_add_page import ContactAddPage
from hog_appium.po.page.base_page import BasePage


class MemberInviteMenuPage(BasePage):

    def add_member_menual(self):
        self.find_and_click(MobileBy.XPATH,"//*[@class='android.widget.TextView' and @text='手动输入添加']")
        return ContactAddPage(self.driver)
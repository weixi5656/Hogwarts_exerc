#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/14 18:32
# @Author  : VC
from appium.webdriver.common.mobileby import MobileBy

from hog_appium.po.page.base_page import BasePage
from hog_appium.po.page.member_invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):
    def click_addmember(self):
        self.scorll_find_and_click("添加成员")
        return MemberInviteMenuPage(self.driver)

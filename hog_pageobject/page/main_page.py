#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/12 12:21
# @Author  : VC
from selenium.webdriver.common.by import By

from hog_pageobject.page.add_member import AddMember
from hog_pageobject.page.base_page import BasePage
from hog_pageobject.page.contact import ContactPage


class MainPage(BasePage):
    _location_goto_addmember = (By.XPATH, '//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]')
    _location_goto_member = (By.XPATH,'//*[@id="menu_contacts"]/span')
    def goto_add_member(self):
        self.find(*self._location_goto_addmember).click()
        return AddMember(self.driver)

    def goto_contact(self):
        self.find(*self._location_goto_member).click()
        return ContactPage(self.driver)

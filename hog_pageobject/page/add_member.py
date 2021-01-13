#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/12 14:23
# @Author  : VC
from selenium.webdriver.common.by import By

from hog_pageobject.page.base_page import BasePage
from hog_pageobject.page.contact import ContactPage



class AddMember(BasePage):
    _location_username = (By.ID,'username')
    _location_acctid = (By.ID,'memberAdd_acctid')
    _location_phone = (By.ID,'memberAdd_phone')


    def add_member(self,acctid,phone):
        self.find(*self._location_username).send_keys("哈利2")
        self.find(*self._location_acctid).send_keys(acctid)
        self.find(*self._location_phone).send_keys(phone)
        self.find(By.CSS_SELECTOR,'.js_btn_save').click()
        return ContactPage(self.driver)

    def add_member_fail(self,acctid,phone):
        self.find(*self._location_username).send_keys('哈利2')
        self.find(*self._location_acctid).send_keys(acctid)
        self.find(*self._location_phone).send_keys(phone)
        self.find(By.CSS_SELECTOR,'.js_btn_save').click()
        error_message = self.find(By.CSS_SELECTOR,'#js_contacts63 > div > div.member_colRight > div > div:nth-child(4) > div > form > div.member_edit_formWrap > div:nth-child(1) > div.member_edit_item.member_edit_item_Account > div.member_edit_item_right.ww_inputWithTips_WithErr > div').text
        return error_message


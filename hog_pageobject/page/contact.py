#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/12 14:23
# @Author  : VC
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from hog_pageobject.page.base_page import BasePage


class ContactPage(BasePage):
    _location_goto_addmember = (By.CLASS_NAME,'qui_btn ww_btn js_add_member')
    _location_member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")

    def contact_add_member(self):
        from hog_pageobject.page.add_member import AddMember
        self.wait_click(self._location_goto_addmember)
        self.find(*self._location_goto_addmember).click()

        return AddMember(self.driver)

    def get_member(self):
        member_list = self.finds(*self._location_member_list)
        member_list2 = [i.text for i in member_list]
        return member_list2

# def remove_member(self):
#     self.driver.find_element().find_element(By.XPATH,'//*[@id="member_list"]/tr[1]/td[1]/input').click()
#     self.driver.find_element().find_element(By.CSS_SELECTOR,'.qui_btn ww_btn js_delete').click()

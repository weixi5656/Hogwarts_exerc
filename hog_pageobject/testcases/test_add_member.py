#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/12 14:24
# @Author  : VC
from selenium import webdriver
import yaml
from hog_pageobject.page.main_page import MainPage
import pytest


class TestAddMember:

    def setup_class(self):
        self.main = MainPage()

    # def teardown_class(self):
    #     self.main.quit()
    @pytest.mark.parametrize("acctid,phone,expect_text",[("xxx3","13111113333","哈利2")])
    def test_add_member(self,acctid,phone,expect_text):
        res = self.main.goto_add_member().add_member(acctid,phone).get_member()
        assert expect_text in res

    def test_add_member_by_contact(self):
        res = self.main.goto_contact().contact_add_member().add_member().get_member()
        assert '哈利2' in res
    @pytest.mark.parametrize("acctid,phone,expect_text",[("xxx3","13111113333","该帐号已被“哈利2”占有")])
    def test_add_member_fail(self,acctid,phone,expect_text):
        res = self.main.goto_add_member().add_member_fail(acctid,phone)
        assert res == expect_text

    # def test_remove_member(self):
    #     self.main.goto_contact().remove_member().get_member()

    @pytest.mark.skip
    def test_get_cookies(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        cookie = driver.get_cookies()
        print(cookie)
        with open("../page/data.yaml", "w", encoding="utf-8") as f:
            yaml.dump(cookie, f)

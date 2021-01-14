#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/14 18:41
# @Author  : VC
from hog_appium.po.page.app import App
from hog_appium.po.page.main_page import MainPage


def test_add_member():
    app = App()
    res = app.goto_main().goto_address().click_addmember().add_member_menual().add_contact()
    assert res
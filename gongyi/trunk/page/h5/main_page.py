# -*- coding: utf-8 -*-
import re
import time

from base_page import basePage
from gongyi.trunk.driver.box_driver import boxDriver
from page_map import *


class mainPage(basePage):



    def open_honmepage(self):
        """
        打开首页
        :return:
        """
        self.h5_driver.h5_click_by_text('首页')

    def open_sortpage(self):
        """
        打开分类页
        :return:
        """
        self.h5_driver.h5_click_by_text('分类')

    def open_hometownpage(self):
        """
        打开家乡公益
        :return:
        """
        self.h5_driver.h5_click_by_text('家乡公益')

    def open_userpage(self):
        """
        打开个人中心
        :return:
        """
        self.h5_driver.h5_click_by_text('我的')

    def open_yj(self):
        """
        打开月捐
        :return:
        """
        self.h5_driver.h5_click_by_text('每月一捐')

    def open_jb(self):
        """
        打开捐步
        :return:
        """
        self.h5_driver.h5_click_by_text('运动捐步')

    def open_1v1(self):
        """
        打开1v1
        :return:
        """
        self.h5_driver.h5_click_by_text('一对一')

    def open_axyk(self):
        """
        打开爱心月刊
        :return:
        """
        self.h5_driver.h5_click_by_text('爱心月刊')

    def get_user_trans_info(self):
        """
        获取个人中心流水按时间排列第一条数据
        :return:
        """
        self.h5_driver.h5_click_by_text('查看爱心记录')
        if self.h5_driver.h5_isElementExist(user_center_map('勋章关闭按钮')):
            self.h5_driver.h5_click_by_xp(user_center_map('勋章关闭按钮'))
        self.h5_driver.h5_click_by_text('我的捐款')
        self.h5_driver.h5_click_by_text('按时间排列')
        user_center_projname = self.h5_driver.h5_get_text_by_xp(user_center_map('项目名称'))
        user_center_money = self.h5_driver.h5_get_text_by_xp(user_center_map('捐款金额'))
        transcode = self.h5_driver.h5_get_text_by_xp(user_center_map('流水单号'))
        user_center_transcode=re.search(r'\d+', transcode).group()
        return {'项目名称':user_center_projname,'捐款金额':user_center_money,'流水单号':user_center_transcode}





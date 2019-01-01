# -*- coding: utf-8 -*-
import os
import time
from gongyi.trunk.driver.box_driver import h5Driver
from gongyi.trunk.driver.html_test_runner import HTMLTestRunner
import unittest
from gongyi.trunk.page.h5.yqj_page import yqjPage


class aa(unittest.TestCase):

    acc = 'wxid_0o7m5brz8ytn12'
    pwd = 'gongyi201811'
    nick = 'gongyi-test'
    money=0.01
    nowtime=''

    @classmethod
    def setUpClass(cls):
        """
        测试前置条件
        :return:
        """
        pass
        # cls.h5_driver = h5Driver()
        # cls.yqj_driver = yqjPage(cls.h5_driver)
        # cls.yqj_driver.open_gyh5(cls.acc,cls.pwd)
        # cls.yqj_driver.load_h5_driver()   #在打开h5页面以后加载fat_h5模块

    # def setUp(self):
    #     """
    #     测试前置条件
    #     :return:
    #     """
    #     self.h5_driver = h5Driver()
    #     self.yqj_driver = yqjPage(self.h5_driver)
    #     self.yqj_driver.open_gyh5(self.acc,self.pwd)
    #     # self.yqj_driver.load_h5_driver()   #在打开h5页面以后加载fat_h5模块
    def tearDown(self):
        # self.h5_driver.getImage(self.nowTime)
        pass
    def test_1(self):

        a='aaa'
        b='bbb'
        self.assertEqual(a,b,'不相等\n%s!=%s'% (a,b))
        # self.aaaaa()


        # self.assertEqual('a', 'aa', 'asaas')
        # self.aaaaa()
if __name__ == '__main__':
    unittest.main()
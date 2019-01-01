# -*- coding: utf-8 -*-
from gongyi.trunk.lib import unittest
from time import sleep
from gongyi.trunk.driver.box_driver import h5Driver
from gongyi.trunk.page.h5.yqj_page import yqjPage


class ljTest(unittest.TestCase):

    acc = 'wxid_0o7m5brz8ytn12'
    pwd = 'gongyi201811'
    nick = 'gongyi-test'
    money=0.01

    def setUp(self):
        """
        测试前置条件
        :return:
        """
        self.h5_driver = h5Driver()
        self.yqj_driver = yqjPage(self.h5_driver)
        self.yqj_driver.open_gyh5(self.acc,self.pwd)
        self.yqj_driver.load_h5_driver()   #在打开h5页面以后加载fat_h5模块


    def tearDown(self):
        """
        测试清理条件
        :return:
        """
        self.h5_driver.getImage(self.nowTime)

    # def test_1(self):
    #     """
    #     打开一个项目详情页，创建个人一起捐，并捐赠，个人中心查单
    #     :return:
    #     """
    #
    #     self.h5_driver.open_url('http://ssl.gongyi.qq.com/m/weixin/detail.htm?pid=200016')
    #     proj_name=self.yqj_driver.get_proj_name()
    #     self.yqj_driver.own_yqj_create()
    #     self.yqj_driver.yqj_donate_money(self.money)
    #     self.yqj_driver.confirm_payment(258085)
    #     thanks_page_info=self.yqj_driver.get_own_yqj_thanks_page_info()
    #     user_center_trans_info = self.yqj_driver.get_user_trans_info()
    #     self.assertEqual(thanks_page_info['项目名称'],proj_name, '感谢页项目名称错误')
    #     self.assertEqual(thanks_page_info['昵称'],self.nick,'感谢页昵称错误')
    #     self.assertEqual(thanks_page_info['本次捐助'],str(self.money),'感谢页捐赠金额错误')
    #     self.assertEqual(thanks_page_info['爱心经验'],str(int(self.money*100)),'感谢页爱心经验错误')
    #     self.assertEqual(thanks_page_info['流水单号'],user_center_trans_info['流水单号'],'感谢页流水单号与个人中心流水单号不一致')
    #     self.assertEqual(user_center_trans_info['项目名称'], thanks_page_info['项目名称'], '个人中心捐赠金额错误')
    #     self.assertEqual(user_center_trans_info['捐款金额'], str(self.money), '个人中心捐赠金额错误')

    def test_2(self):
        """
        打开一个项目详情页，创建个人一起捐，并捐赠，个人中心查单
        :return:
        """

        self.h5_driver.open_url('http://ssl.gongyi.qq.com/m/weixin/detail.htm?pid=200016')
        proj_name = self.yqj_driver.get_proj_name()
        self.yqj_driver.team_yqj_create('team1')
        self.yqj_driver.yqj_donate_money(self.money)
        self.yqj_driver.confirm_payment(258085)
        thanks_page_info = self.yqj_driver.get_own_yqj_thanks_page_info()
        user_center_trans_info = self.yqj_driver.get_user_trans_info()
        self.assertEqual(thanks_page_info['项目名称'], proj_name, '感谢页项目名称错误')
        self.assertEqual(thanks_page_info['昵称'], self.nick, '感谢页昵称错误')
        self.assertEqual(thanks_page_info['本次捐助'], str(self.money), '感谢页捐赠金额错误')
        self.assertEqual(thanks_page_info['爱心经验'], str(int(self.money * 100)), '感谢页爱心经验错误')
        self.assertEqual(thanks_page_info['流水单号'], user_center_trans_info['流水单号'], '感谢页流水单号与个人中心流水单号不一致')
        self.assertEqual(user_center_trans_info['项目名称'], thanks_page_info['项目名称'], '个人中心捐赠金额错误')
        self.assertEqual(user_center_trans_info['捐款金额'], str(self.money), '个人中心捐赠金额错误')


if __name__ == '__main__':
    unittest.main()
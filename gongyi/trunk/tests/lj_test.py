# -*- coding: utf-8 -*-
from gongyi.trunk.lib import unittest
from time import sleep

from gongyi.trunk.driver.box_driver import boxDriver, h5Driver
from gongyi.trunk.page.h5.lj_page import ljPage
from gongyi.trunk.page.h5.main_page import mainPage


class ljTest(unittest.TestCase):

    acc = 'gongyi-tes'
    pwd = 'gongyi201811'
    nick ='gongyi-test'

    @classmethod
    def setUpClass(cls):
        """
        测试前置条件,只执行一次
        打开公益公众号
        :return:
        """
        cls.h5_driver = h5Driver()
        cls.lj_driver = ljPage(cls.h5_driver)
        cls.lj_driver.open_gyh5(cls.acc,cls.pwd)
        cls.lj_driver.load_h5_driver()   #在打开h5页面以后加载fat_h5模块

    @classmethod
    def tearDownClass(cls):
        cls.lj_driver.close_wx()

    def setUp(self):
        """
        进入一个乐捐项目
        :return:
        """
        # self.h5_driver.click_by_xp('//*[@id="pageContainer"]/div[1]/section[7]/div[2]/div/a/img')
        self.lj_driver.go_test_proj() #进入测试项目
        self.proj_name = self.lj_driver.get_proj_name()

    def tearDown(self):
        """
        测试清理条件
        :return:
        """
        #失败截图功能
        self.h5_driver.getImage(self.nowTime)
        #跳转到公益首页
        self.lj_driver.reopen_txgyh5()

    def test_1(self):
        """
        支付金额为空测试
        :return:
        """
        money = ''
        self.lj_driver.lj_donate_money(money)
        self.assertEqual(self.lj_driver.err_box(), '请填写正确金额', '支付错误提示错误')

    def test_2(self):
        """
        支付金额为0测试
        :return:
        """
        money = 0
        self.lj_driver.lj_donate_money(money)
        self.assertEqual(self.lj_driver.err_box(), '请填写正确金额', '支付错误提示错误')

    def test_3(self):
        """
        支付金额为符号测试
        :return:
        """
        money = '#@'
        self.lj_driver.lj_donate_money(money)
        self.assertEqual(self.lj_driver.err_box(),'请填写正确金额','支付错误提示错误')


    def test_4(self):
        """
        支付金额为9999999测试
        :return:
        """
        money = 9999999
        self.lj_driver.lj_donate_money(money)
        self.assertEqual(self.lj_driver.err_box(), '非常抱歉提醒您，因系统限制，单次支付无法超过10万元，请分次支付。', '支付错误提示错误')


    def test_5(self):
        """
        支付金额为10000测试,会提示不能超过1000
        :return:
        """
        money = 10000
        self.lj_driver.lj_donate_money(money)
        big_money=self.lj_driver.big_money_tips()
        self.assertEqual(big_money,'10000','大金额支付提示错误')

    def test_6(self):
        """
        捐赠项目，检查感谢页，个人中心数据
        :return:
        """
        money=0.01

        self.lj_driver.lj_donate_money(money)
        self.lj_driver.confirm_payment(258085)
        thanks_page_info=self.lj_driver.get_thanks_page_info()
        user_center_trans_info = self.lj_driver.get_user_trans_info()
        self.assertEqual(thanks_page_info['项目名称'], self.proj_name, '感谢页项目名称错误')
        self.assertEqual(thanks_page_info['昵称'],self.nick,'感谢页昵称错误')
        self.assertEqual(thanks_page_info['本次捐助'],str(0.01),'感谢页捐赠金额错误')
        self.assertEqual(thanks_page_info['爱心经验'],str(int(money*100)),'感谢页爱心经验错误')
        self.assertEqual(thanks_page_info['流水单号'],user_center_trans_info['流水单号'],'感谢页流水单号与个人中心流水单号不一致')
        self.assertEqual(user_center_trans_info['项目名称'], thanks_page_info['项目名称'], '个人中心捐赠金额错误')
        self.assertEqual(user_center_trans_info['捐款金额'], str(money), '个人中心捐赠金额错误')

    def test_7(self):
        self.assertIn(1,[2,3],'没有')



if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
import re
import time

from gongyi.trunk.driver.box_driver import boxDriver
from gongyi.trunk.page.h5.page_map import *


class basePage(object):

    def __init__(self,boxDriver):
        """
        实例化h5Driver
        :param h5Driver:
        """
        self.h5_driver = boxDriver

    def close_wx(self):
        """
        关闭所有应用
        :return:
        """
        self.h5_driver.u_stop_all_app()

    def open_wx(self):

        '''启动Android微信
        '''
        self.h5_driver.d.unlock()
        self.close_wx()
        self.h5_driver.u_start_app('com.tencent.mm')

    def check_is_login(self):
        """
        由于android9定位不到‘我’，所以要判断下sdk，
        由于机子反应慢，先循环检查 登录或者我存不存在，
        存在后查询我在不在，如果在就是登录了,返回True，否则返回False
        :param :
        :return:
        """

        times = 0
        while not self.h5_driver.u_exists(**wx_home_map("我")) and not self.h5_driver.u_exists(**wx_login_map("登录")) and times < 10:
            time.sleep(1)
            times += 1
        if not self.h5_driver.u_exists(**wx_login_map("登录")):
            return True
        else:
            return False

            # times = 0
            # while not self.h5_driver.u_exists(**wx_home_map("我")) and not self.h5_driver.u_exists(**wx_login_map("登录")) and times < 10:
            #     time.sleep(1)
            #     times += 1
            # if self.h5_driver.u_exists(**wx_home_map("我")):
            #     return  True
            # else:
            #     return False

    def login_wx(self,acc,pwd):
        """
        登录微信操作
        :param acc:
        :param pwd:
        :return:
        """
        if self.h5_driver.u_exists(**wx_login_map("登录")):
            self.h5_driver.u_click(**wx_login_map("登录"))
        else:
            self.h5_driver.u_click(timeout=10, **wx_login_map("用微信号登录"))
            self.h5_driver.u_send_keys(acc, **wx_login_map("账号"))
            self.h5_driver.u_set_text(pwd, **wx_login_map("密码"))
            self.h5_driver.u_click(**wx_login_map("确认登录"))


    def go_wx_user_center(self):
        """
        进入微信个人中心
        :return:
        """
        if self.h5_driver.sdk>=28:
            self.h5_driver.u_click(**wx_home_map("我"))
        else:
            self.h5_driver.u_click(**wx_home_map("我"))

    def check_user(self,acc):
        """
        查询是不是指定登录的账号
        :return:
        """
        user=self.h5_driver.u_get_text(**wx_user_center_map("微信号"))
        if acc==re.search('[a-zA-Z0-9_\-]{6,30}',user).group():
            return True
        else:
            return False

    def logout_wx(self):
        """
        退出登录
        :return:
        """
        self.h5_driver.u_click(**wx_user_center_map("设置"))
        time.sleep(1)
        self.h5_driver.d.swipe(330,800,330,500,steps=10)
        self.h5_driver.u_click(**wx_user_center_map("退出"))
        self.h5_driver.u_click(**wx_user_center_map("退出登录")) #退出登录
        self.h5_driver.u_click(timeout=10,**wx_user_center_map("退出（提醒）"))  # 退出登录提醒
        self.h5_driver.u_click(**wx_login_map("更多"))#更多
        self.h5_driver.u_click(**wx_login_map("登录其他账号"))#登录其他账号


    def login_with_user(self,acc,pwd):
        """
        用指定账户登录
        :param acc:
        :param pwd:
        :return:
        """
        if self.check_is_login():
            self.go_wx_user_center()
            if self.check_user(acc):
                pass
            else:
                self.logout_wx()
                self.login_wx(acc,pwd)
                self.go_wx_user_center()
        else:
            self.login_wx(acc,pwd)
            self.go_wx_user_center()


    def open_txgyh5(self):
        '''
        通过钱包进入公益
        :return:
        '''
        times=0

        self.h5_driver.u_click(**wx_user_center_map("支付"))
        self.h5_driver.u_click(timeout=5,**wx_user_center_map("腾讯公益"))
        while not self.h5_driver.u_exists(**main_page_map("腾讯公益标题")) and times<20:
            time.sleep(1)
            times += 1
            if times >6:
                self.h5_driver.u_click(**wx_user_center_map("腾讯公益"))

    def open_gyh5(self,acc,pwd):
        """
        启动微信进入公益
        :param acc:
        :param pwd:
        :return:
        """
        self.open_wx()
        self.login_with_user(acc,pwd)
        self.open_txgyh5()


    def reopen_txgyh5(self):
        """
        跳转到公益首页
        :return:
        """
        self.h5_driver.h5_open_url('http://ssl.gongyi.qq.com/m/weixin/index2_gzzh.htm')

    def go_test_proj(self):
        """
        进入测试项目
        :return:
        """
        self.h5_driver.h5_open_url('http://ssl.gongyi.qq.com/m/weixin/detail.htm?pid=200016&dbg=2')

    def load_h5_driver(self):
        """
        加载fat_h5Driver
        :return:
        """
        times=0
        while times<10:
            try:
                self.h5_driver.load_h5Driver()
                break
            except:
                times+=1
        if times==10:
            raise TypeError('load_h5_driver失败')

    def confirm_payment(self,paypwd):
        """
        微信支付操作
        :param pwd:
        :return:
        """
        times=0
        while not self.h5_driver.u_exists(text='请输入支付密码') and times<10:
            time.sleep(0.5)
            times+=1
        for i in str(paypwd):
            self.wx_keyboard(i)
        try:
            #小米手机有时候跳出支付风险提示
            self.h5_driver.u_click(timeout=7,text='仍然支付')
        except:
            pass
        self.h5_driver.u_click(timeout=5,text='完成')

    def get_pay_value(self):
        """
        获取支付金额
        :return:
        """
        times=0
        while not self.h5_driver.u_exists(text='请输入支付密码') and times<10:
            time.sleep(0.5)
            times+=1

    def share_yqj(self):
        """
        一起捐创建后分享操作
        :return:
        """
        self.h5_driver.u_click(resourceId="com.tencent.mm:id/j1")
        self.h5_driver.u_click(resourceId="com.tencent.mm:id/cj", text=u"发送给朋友")
        self.h5_driver.u_click(resourceId="com.tencent.mm:id/jc")

    def wx_keyboard(self, key):
        """
        微信支付键盘
        :param key:
        :return:
        """
        if key == '1':
            self.h5_driver.u_tap( (0.164*self.h5_driver.x), (0.671*self.h5_driver.y))
        elif key == '2':
            self.h5_driver.u_tap( (0.495*self.h5_driver.x), (0.675*self.h5_driver.y))
        elif key == '3':
            self.h5_driver.u_tap( (0.835*self.h5_driver.x), (0.673*self.h5_driver.y))
        elif key == '4':
            self.h5_driver.u_tap( (0.164*self.h5_driver.x), (0.762*self.h5_driver.y))
        elif key == '5':
            self.h5_driver.u_tap( (0.495*self.h5_driver.x), (0.767*self.h5_driver.y))
        elif key == '6':
            self.h5_driver.u_tap( (0.831*self.h5_driver.x), (0.77*self.h5_driver.y))
        elif key == '7':
            self.h5_driver.u_tap( (0.166*self.h5_driver.x), (0.858*self.h5_driver.y))
        elif key == '8':
            self.h5_driver.u_tap( (0.504*self.h5_driver.x), (0.858*self.h5_driver.y))
        elif key == '9':
            self.h5_driver.u_tap( (0.828*self.h5_driver.x), (0.858*self.h5_driver.y))
        elif key == '0':
            self.h5_driver.u_tap( (0.49*self.h5_driver.x), (0.955*self.h5_driver.y))
        elif key == 'b':
            self.h5_driver.u_tap( (0.84*self.h5_driver.x), (0.949*self.h5_driver.y))
        else:
            raise TypeError('key error')

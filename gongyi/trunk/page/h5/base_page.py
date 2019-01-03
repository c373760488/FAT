# -*- coding: utf-8 -*-
import re
import time

from gongyi.trunk.driver.box_driver import h5Driver


class basePage(object):

    def __init__(self,h5Driver):
        """
        实例化h5Driver
        :param h5Driver:
        """
        self.h5_driver = h5Driver

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
        self.h5_driver.d.app_start('com.tencent.mm')

    def check_is_login(self):
        """
        由于android9定位不到‘我’，所以要判断下sdk，
        由于机子反应慢，先循环检查 登录或者我存不存在，
        存在后查询我在不在，如果在就是登录了,返回True，否则返回False
        :param :
        :return:
        """
        if self.h5_driver.sdk >= 28:
            times = 0
            while not self.h5_driver.u_exists(resourceId="com.tencent.mm:id/cw3", className="android.widget.LinearLayout",
                                              instance=3) and not self.h5_driver.u_exists(text="登录") and times < 10:
                time.sleep(1)
                times += 1
            if not self.h5_driver.u_exists(resourceId="com.tencent.mm:id/cw3", className="android.widget.LinearLayout",
                                           instance=3):
                return True
            else:
                return False
        else:
            times = 0
            while not self.h5_driver.u_exists(resourceId="com.tencent.mm:id/cw2", text=u"我") and not self.h5_driver.u_exists(text="登录") and times < 10:
                time.sleep(1)
                times += 1
            if self.h5_driver.u_exists(resourceId="com.tencent.mm:id/cw2", text=u"我"):
                return  True
            else:
                return False

    def login_wx(self,acc,pwd):
        """
        登录微信操作
        :param acc:
        :param pwd:
        :return:
        """
        if self.h5_driver.u_exists(text="登录"):
            self.h5_driver.u_click(text="登录")
        else:
            self.h5_driver.u_click(text="用微信号/QQ号/邮箱登录",timeout=10)
            self.h5_driver.u_send_keys(acc,resourceId="com.tencent.mm:id/ji")
            self.h5_driver.u_set_text(pwd,resourceId="com.tencent.mm:id/ji", className="android.widget.EditText", instance=1)
            self.h5_driver.u_click(text='登录')


    def go_wx_user_center(self):
        """
        进入微信个人中心
        :return:
        """
        if self.h5_driver.sdk>=28:
            self.h5_driver.u_click(resourceId="com.tencent.mm:id/cw3", className="android.widget.LinearLayout", instance=3)
        else:
            self.h5_driver.u_click(resourceId="com.tencent.mm:id/cw2", text=u"我")

    def check_user(self,acc):
        """
        查询是不是指定登录的账号
        :return:
        """
        user=self.h5_driver.u_get_text(resourceId="com.tencent.mm:id/czz")
        if acc==re.search('[a-zA-Z0-9_\-]{6,30}',user).group():
            return True
        else:
            return False

    def logout_wx(self):
        """
        退出登录
        :return:
        """
        self.h5_driver.u_click(resourceId="android:id/title", text=u"设置")
        time.sleep(1)
        self.h5_driver.d.swipe(330,800,330,500,steps=10)
        self.h5_driver.u_click(resourceId="android:id/title", text=u"退出")
        self.h5_driver.u_click(resourceId="com.tencent.mm:id/jr") #退出登录
        self.h5_driver.u_click(resourceId="com.tencent.mm:id/au_",timeout=10)  # 退出
        self.h5_driver.u_click(resourceId="com.tencent.mm:id/chc")#更多
        self.h5_driver.u_click(resourceId="com.tencent.mm:id/cj")#登录其他账号


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
        else:
            self.login_wx(acc,pwd)


    def open_txgyh5(self):
        '''
        通过钱包进入公益
        :return:
        '''
        times=0

        self.h5_driver.u_click(text='钱包')
        self.h5_driver.u_click(timeout=5,text='腾讯公益')
        while not self.h5_driver.u_exists(text='腾讯公益',resourceId='android:id/text1') and times<20:
            time.sleep(1)
            times += 1
            if times >6:
                self.h5_driver.u_click(text='腾讯公益')

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
        self.h5_driver.open_url('http://ssl.gongyi.qq.com/m/weixin/index2_gzzh.htm')

    def go_test_proj(self):
        """
        进入测试项目
        :return:
        """
        self.h5_driver.open_url('http://ssl.gongyi.qq.com/m/weixin/detail.htm?pid=200016&dbg=2')

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
            self.h5_driver.wx_keyboard(i)
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




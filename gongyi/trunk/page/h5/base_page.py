# -*- coding: utf-8 -*-
import time



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


    def login_wx(self,acc,pwd):
        """
        登录微信
        :param acc:
        :param pwd:
        :return:
        """
        if self.h5_driver.sdk>=28:
            times=0
            while not self.h5_driver.u_exists(resourceId="com.tencent.mm:id/cw3", className="android.widget.LinearLayout", instance=3) and not self.h5_driver.u_exists(text="登录") and times<10:
                time.sleep(1)
                times+=1
            if not self.h5_driver.u_exists(resourceId="com.tencent.mm:id/cw3", className="android.widget.LinearLayout", instance=3):
                self.h5_driver.u_click(text="登录")
                self.h5_driver.u_click(text="用微信号/QQ号/邮箱登录")
                self.h5_driver.u_send_keys(acc,text="请填写微信号/QQ号/邮箱")
                self.h5_driver.u_set_text(pwd,resourceId="com.tencent.mm:id/ji", className="android.widget.EditText", instance=1)
                self.h5_driver.u_click(text='登录')
            else:
                pass
        else:
            times = 0
            while not self.h5_driver.u_exists(text='我') and not self.h5_driver.u_exists(text="登录") and times < 10:
                time.sleep(1)
                times += 1
            if not self.h5_driver.u_exists(text='我'):
                self.h5_driver.d(text="登录").click()
                self.h5_driver.u_click(text="用微信号/QQ号/邮箱登录")
                self.h5_driver.u_send_keys(acc,text="请填写微信号/QQ号/邮箱")
                self.h5_driver.u_set_text(pwd,resourceId="com.tencent.mm:id/ji", className="android.widget.EditText",
                                 instance=1)
                self.h5_driver.u_click(text='登录')
            else:
                pass

    def open_txgyh5(self):
        '''
        通过钱包进入公益
        :return:
        '''
        times=0
        if self.h5_driver.sdk>=28:
            self.h5_driver.u_click(resourceId="com.tencent.mm:id/cw3", className="android.widget.LinearLayout", instance=3)
        else:
            self.h5_driver.u_click(text='我')
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
        self.login_wx(acc,pwd)
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

    def confirm_payment(self,pwd):
        """
        微信支付操作
        :param pwd:
        :return:
        """
        times=0
        while not self.h5_driver.u_exists(text='请输入支付密码') and times<10:
            time.sleep(0.5)
            times+=1
        for i in str(pwd):
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

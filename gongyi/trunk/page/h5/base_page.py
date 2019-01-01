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
        self.h5_driver.d.app_stop('com.tencent.mm')

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
            while not self.h5_driver.d(resourceId="com.tencent.mm:id/cw3", className="android.widget.LinearLayout", instance=3).exists and not self.h5_driver.d(text="登录").exists and times<10:
                time.sleep(1)
                times+=1
            if not self.h5_driver.d(resourceId="com.tencent.mm:id/cw3", className="android.widget.LinearLayout", instance=3).exists:
                self.h5_driver.d(text="登录").click()
                self.h5_driver.d(text="用微信号/QQ号/邮箱登录").click()
                self.h5_driver.d(text="请填写微信号/QQ号/邮箱").send_keys(acc)
                self.h5_driver.d(resourceId="com.tencent.mm:id/ji", className="android.widget.EditText", instance=1).set_text(pwd)
                self.h5_driver.d(text='登录').click()
            else:
                pass
        else:
            times = 0
            while not self.h5_driver.d(text='我').exists and not self.h5_driver.d(text="登录").exists and times < 10:
                time.sleep(1)
                times += 1
            if not self.h5_driver.d(text='我').exists:
                self.h5_driver.d(text="登录").click()
                self.h5_driver.d(text="用微信号/QQ号/邮箱登录").click()
                self.h5_driver.d(text="请填写微信号/QQ号/邮箱").send_keys(acc)
                self.h5_driver.d(resourceId="com.tencent.mm:id/ji", className="android.widget.EditText",
                                 instance=1).set_text(pwd)
                self.h5_driver.d(text='登录').click()
            else:
                pass

    def open_txgyh5(self):
        '''
        通过钱包进入公益
        :return:
        '''
        times=0
        if self.h5_driver.sdk>=28:
            self.h5_driver.d(resourceId="com.tencent.mm:id/cw3", className="android.widget.LinearLayout", instance=3).click()
        else:
            self.h5_driver.d(text='我').click()
        self.h5_driver.d(text='钱包').click()
        self.h5_driver.d(text='腾讯公益').click(timeout=5)
        while not self.h5_driver.d(text='腾讯公益',resourceId='android:id/text1').exists and times<20:
            time.sleep(1)
            times += 1
            if times >6:
                self.h5_driver.d(text='腾讯公益').click()

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
        while not self.h5_driver.d(text='请输入支付密码').exists and times<10:
            time.sleep(0.5)
            times+=1
        for i in str(pwd):
            self.h5_driver.wx_keyboard(i)
        try:
            #小米手机有时候跳出支付风险提示
            self.h5_driver.d(text='仍然支付').click(timeout=7)
        except:
            pass
        self.h5_driver.d(text='完成').click(timeout=5)

    def get_pay_value(self):
        """
        获取支付金额
        :return:
        """
        times=0
        while not self.h5_driver.d(text='请输入支付密码').exists and times<10:
            time.sleep(0.5)
            times+=1

    def share_yqj(self):
        """
        一起捐创建后分享操作
        :return:
        """
        self.h5_driver.d(resourceId="com.tencent.mm:id/j1").click()
        self.h5_driver.d(resourceId="com.tencent.mm:id/cj", text=u"发送给朋友").click()
        self.h5_driver.d(resourceId="com.tencent.mm:id/jc").click()

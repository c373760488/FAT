# -*- coding: utf-8 -*-
import time



class basePage:

    def __init__(self,xcxDriver):
        """
        实例化h5Driver
        :param h5Driver:
        """
        self.xcx_driver = xcxDriver

    def close_wx(self):
        self.xcx_driver.d.stop_app('com.tencent.mm')

    def open_wx(self):

        '''启动Android微信
        '''
        self.xcx_driver.d.unlock()
        self.xcx_driver.d.app_stop('com.tencent.mm')
        self.xcx_driver.d.app_start('com.tencent.mm')
        # if kill_process == True:
        # runCommand('adb shell am force-stop %s' % self.ProcessDict['Main'])  # 杀死已有进程
        # if clear_state == True:
        #     runCommand('adb shell pm clear %s' % self.package_name)
        # try:
        #     runCommand('adb shell rm -r /data/data/com.tencent.mm/app_xwalk_155')
        #     runCommand('adb shell touch /data/data/com.tencent.mm/app_xwalk_155')
        # except:
        #     self.logger.exception('clear app_xwalk dir failed')
        # runCommand('adb shell am start com.tencent.mm/.ui.LauncherUI')

    def login_wx(self,acc,pwd):
        """
        登录微信
        :param acc:
        :param pwd:
        :return:
        """
        times=0
        while not self.xcx_driver.d(text='我').exists and not self.xcx_driver.d(text="登录").exists and times<10:
            time.sleep(1)
            times+=1
        if not self.xcx_driver.d(text='我').exists:
            self.xcx_driver.d(text="登录").click()
            self.xcx_driver.d(text="用微信号/QQ号/邮箱登录").click()
            self.xcx_driver.d(text="请填写微信号/QQ号/邮箱").send_keys(acc)
            self.xcx_driver.d(resourceId="com.tencent.mm:id/ji", className="android.widget.EditText", instance=1).set_text(pwd)
            self.xcx_driver.d(text='登录').click()
        else:
            pass

    def open_txgyh5(self):
        '''
        通过钱包进入公益
        :return:
        '''
        times=0
        self.xcx_driver.d(text='发现').click()
        self.xcx_driver.d(scrollable=True).scroll.toEnd(60)
        self.xcx_driver.d(text='小程序').click()
        self.xcx_driver.d(text="腾讯公益").long_click(duration=2)
        self.xcx_driver.d(text='腾讯公益').click(timeout=5)
        while not self.xcx_driver.d(text='腾讯公益',resourceId='android:id/text1').exists and times<20:
            time.sleep(1)
            times += 1

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
        time.sleep(7)

    def reopen_txgyh5(self):
        """
        关闭H5后重新进入公益
        :return:
        """
        times = 0
        self.xcx_driver.d(text='腾讯公益').click(timeout=5)
        while not self.xcx_driver.d(text='腾讯公益', resourceId='android:id/text1').exists and times < 10:
            time.sleep(1)
            times += 1

    def load_h5_driver(self):
        """
        加载fat_h5Driver
        :return:
        """
        self.xcx_driver.load_h5Driver()

    def confirm_payment(self,pwd):
        times=0
        while not self.xcx_driver.d(text='请输入支付密码').exists and times<10:
            time.sleep(0.5)
            times+=1
        for i in str(pwd):
            self.xcx_driver.wx_keyboard(i)
        self.xcx_driver.d(text='完成').click(timeout=5)
        try:
            #小米手机有时候跳出支付风险提示
            self.xcx_driver.d(text='仍然支付').click(timeout=10)
        except:
            pass
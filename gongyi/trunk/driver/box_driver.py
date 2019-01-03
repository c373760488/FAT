# -*- coding: utf-8 -*-
import os
import re
import sys
import time
import uiautomator2

from gongyi.trunk.lib.fastAutoTest.core.wx.wxEngine import WxDriver

sys.path.append('..\\lib\\')
# from fastAutoTest.core.h5.h5Engine import H5Driver
# from fastAutoTest.core.wx.wxEngine import WxDriver
# from fastAutoTest.utils.adbHelper import AdbHelper
# from fastAutoTest.utils.commandHelper import runCommand
# from fastAutoTest.utils.logger import Log
from fastAutoTest.core.h5.h5Engine import H5Driver
from fastAutoTest.utils.adbHelper import AdbHelper
from fastAutoTest.utils.logger import Log


class boxDriver(object):

    def __init__(self, device=None):
        self.logger = Log().getLogger()
        if device == None:
            self.device = self.get_device_id(device)
        else:
            self.device = device
        # os.system('adb shell am start com.github.uiautomator/.MainActivity')
        # time.sleep(1)
        self.d = self.u_connect(self.device)
        self.sdk = int(self.d.device_info['sdk'])
        self.x=self.d.info['displayWidth']
        self.y=self.d.info['displayHeight']

    def u_connect(self,device):
        """
        uiautomator2连接手机
        :param device:
        :return:
        """
        try:
            d=uiautomator2.connect_usb(device)
        except:
            raise TypeError('uiautomator连接失败')
        return d

    def get_device_id(self, device):
        if device == None:
            devicesList = AdbHelper.listDevices(ignoreUnconnectedDevices=True)
            devicesCount = len(devicesList)
            if devicesCount <= 0:
                raise TypeError('没有找到设备')

            elif devicesCount == 1:
                self.device = devicesList[0]
            else:
                self.device = devicesList[0]
                print '检测到多个设备，默认使用第一个'

    def u_get_app_version(self,app):
        """
        获取app版本号
        :param app:
        :return:
        """
        return self.d.app_info(app)['versionName']

    def u_click(self, timeout=5, **kwargs):
        """
        uiautomaor2 的click
        :param kwargs:
        :return:
        """
        times = 0
        while times < timeout:
            if self.u_exists(**kwargs):
                break
            else:
                time.sleep(1)
                times += 1
        if self.u_exists(**kwargs):
            self.d(**kwargs).click(timeout)
        else:
            raise TypeError('元素不存在')

    def u_exists(self, **kwargs):
        """
        uiautomaor2 ,查看元素是否存在
        :param kwargs:
        :return:
        """
        return self.d(**kwargs).exists()

    def u_send_keys(self, text, **kwargs):
        """
         uiautomaor2 ,输入text
        :param text:
        :param kwargs:
        :return:
        """
        self.d(**kwargs).send_keys(text)

    def u_set_text(self, text, **kwargs):
        """
         uiautomaor2 ,输入text
        :param text:
        :param kwargs:
        :return:
        """
        self.d(**kwargs).set_text(text)

    def u_stop_app(self,app):
        """
        关闭app
        :param app:
        :return:
        """
        self.d.app_stop(app)

    def u_start_app(self, pkg_name,
                    activity=None,
                    extras={},
                    wait=True,
                    stop=False,
                    unlock=False):
        """
        启动app
        :param pkg_name:
        :param activity:
        :param extras:
        :param wait:
        :param stop:
        :param unlock:
        :return:
        """
        self.d.app_start(pkg_name,activity,extras,wait,stop,unlock)

    def u_stop_all_app(self,excludes=[]):
        """
        关闭所有应用
        :param excludes: 不想关闭的应用list
        :return:
        """
        self.d.app_stop_all(excludes)

    def u_get_text(self,**kwargs):
        """
        获取定位的text
        :param kwargs:
        :return:
        """
        return self.d(**kwargs).get_text()

    def wx_keyboard(self, key):
        """
        微信支付键盘
        :param key:
        :return:
        """
        if key == '1':
            os.system('adb shell input tap %d %d' % (0.164*int(self.x), 0.671*int(self.y)))
        elif key == '2':
            os.system('adb shell input tap %d %d' % (0.495*int(self.x), 0.675*int(self.y)))
        elif key == '3':
            os.system('adb shell input tap %d %d' % (0.835*int(self.x), 0.673*int(self.y)))
        elif key == '4':
            os.system('adb shell input tap %d %d' % (0.164*int(self.x), 0.762*int(self.y)))
        elif key == '5':
            os.system('adb shell input tap %d %d' % (0.495*int(self.x), 0.767*int(self.y)))
        elif key == '6':
            os.system('adb shell input tap %d %d' % (0.831*int(self.x), 0.77*int(self.y)))
        elif key == '7':
            os.system('adb shell input tap %d %d' % (0.166*int(self.x), 0.858*int(self.y)))
        elif key == '8':
            os.system('adb shell input tap %d %d' % (0.504*int(self.x), 0.858*int(self.y)))
        elif key == '9':
            os.system('adb shell input tap %d %d' % (0.828*int(self.x), 0.858*int(self.y)))
        elif key == '0':
            os.system('adb shell input tap %d %d' % (0.49*int(self.x), 0.955*int(self.y)))
        elif key == 'b':
            os.system('adb shell input tap %d %d' % (0.84*int(self.x), 0.949*int(self.y)))
        else:
            raise TypeError('key error')


class h5Driver(boxDriver):

    def __init__(self, device=None):
        super(h5Driver, self).__init__(device)

    def load_h5Driver(self):
        self.h5driver = H5Driver(self.d, self.device)
        self.h5driver.initDriver()
        return self.h5driver

    def click_by_text(self, text):
        """
        通过文本点击
        :param text:
        :return:
        """
        self.h5driver.clickFirstElementByText(text)

    def click_by_xp(self, xp):
        """
        通过xpath点击
        :param xp:
        :return:
        """
        self.h5driver.clickElementByXpath(xp)

    def get_text_by_xp(self, xp):
        """
        通过xpath定位获取text
        :param xp:
        :return:
        """
        return self.h5driver.getElementTextByXpath(xp)

    def long_click_by_xp(self, xp):
        """
        通过xpath长按点击
        :param xp:
        :return:
        """
        self.h5driver.longClickElementByXpath(xp)

    def double_click_by_xp(self, xp):
        """
        通过xpath双击
        :param xp:
        :return:
        """
        self.h5driver.repeatedClickElementByXpath(xp)

    def scroll_To_Xpath(self, xp):
        """
        滚动直xpath可见
        :param xp:
        :return:
        """
        self.h5driver.scrollToElementByXpath(xp)

    def type_text(self, xp, text):
        """
        清除输入框内容，输入文字
        :param xp:
        :param text:
        :return:
        """
        self.h5driver.clickElementByXpath(xp)
        self.h5driver.clearInputTextByXpath(xp)
        self.h5driver.textElementByXpath(xp, text)

    def back_page(self):
        """
        返回上一页
        :return:
        """

        self.h5driver.returnLastPage()

    def isElementExist(self, xp):
        """
        判断元素是否存在
        :param xp:
        :return:
        """
        return self.h5driver.isElementExist(xp)

    def open_url(self, url):
        """
        打开指定url，（h5页面已被打卡）
        :param url:
        :return:
        """
        self.h5driver.navigateToPage(url)

    def close_h5(self):
        """
        关闭h5
        :return:
        """
        self.h5driver.closeWindow()

    def send_Script(self, script):
        """
        发送js命令
        :param script:
        :return:
        """
        return self.h5driver.executeScript(script)

    def get_url(self):
        """
        获取当前url
        :return:
        """
        return self.h5driver.getCurrentPageUrl()

    def getImage(self, time):
        '''
        截取图片,并保存在images文件夹
        :return: 无
        '''
        if time != '':
            imgPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\reports\\images\\%s.png' % time
            self.d.screenshot(imgPath)
        else:
            pass


class wxDriver(boxDriver):
    def __init__(self, ):
        super(wxDriver, self).__init__()

    def load_h5Driver(self):
        self.xcxdriver = WxDriver(self.d, self.device)
        self.xcxdriver.initDriver()
        return self.xcxdriver

    def click_by_text(self, text):
        """
        通过text来搜索，点击第一个text相符合的控件。参数同clickElementByXpath()
        :param text:
        :return:
        """
        self.xcxdriver.clickFirstElementByText(text)

    def click_by_xp(self, xp):
        """
        通过xpath定位点击
        :param xp:
        :return:
        """
        self.xcxdriver.clickElementByXpath(xp)

    def get_text_by_xp(self, xp):
        """
        通过xpath定位点击
        :param xp:
        :return:
        """
        return self.xcxdriver.getElementTextByXpath(xp)

    def scroll_To_Xpath(self, xp):
        """
        滚动直xpath可见
        :param xp:
        :return:
        """
        self.xcxdriver.scrollToElementByXpath(xp)

    def type_text(self, xp, text):
        """
        输入文字(还没有试过清除有没有用)
        :param xp:
        :param text:
        :return:
        """
        self.xcxdriver.clearInputTextByXpath(xp)
        self.xcxdriver.textElementByXpath(xp, text)

    def back_page(self):
        """
        返回上一页
        :return:
        """

        self.xcxdriver.returnLastPage()

    def isElementExist(self, xp):
        """
        判断元素是否存在
        :param xp:
        :return:
        """
        return self.xcxdriver.isElementExist(xp)

    def close_xcx(self):
        """
        关闭h5
        :return:
        """
        self.xcxdriver.close()


if __name__ == '__main__':
    # package_name = 'com.tencent.mm'
    # runCommand('adb shell pm clear %s' % package_name)
    a=uiautomator2.connect_usb()
    a.swipe(330,800,330,500,steps=10)


    # a.d(className="android.widget.RelativeLayout", instance=14).click()
    # a.d(xpath="//android.widget.TextView[@text='我']").click()

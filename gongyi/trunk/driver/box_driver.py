# -*- coding: utf-8 -*-
import os
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

    def __init__(self,device=None):
        self.logger=Log().getLogger()
        if device==None:
            self.device=self.get_device_id(device)
        else:
            self.device=device
        # os.system('adb shell am start com.github.uiautomator/.MainActivity')
        # time.sleep(1)
        self.d = uiautomator2.connect_usb(self.device)
        self.sdk=int(self.d.device_info['sdk'])

    def get_device_id(self,device):
        if device==None:
            devicesList = AdbHelper.listDevices(ignoreUnconnectedDevices=True)
            devicesCount = len(devicesList)
            if devicesCount <= 0:
                raise TypeError('没有找到设备')

            elif devicesCount == 1:
                self.device = devicesList[0]
            else:
                self.device = devicesList[0]
                print '检测到多个设备，默认使用第一个'

    def wx_keyboard(self,key):
        """
        微信支付键盘
        :param key:
        :return:
        """
        if key=='1':
            self.d.click(0.164, 0.671)
        elif key == '2':
            self.d.click(0.495, 0.675)
        elif key == '3':
            self.d.click(0.835, 0.673)
        elif key == '4':
            self.d.click(0.164, 0.762)
        elif key == '5':
            self.d.click(0.495, 0.767)
        elif key == '6':
            self.d.click(0.831, 0.77)
        elif key == '7':
            self.d.click(0.166, 0.858)
        elif key == '8':
            self.d.click(0.504, 0.858)
        elif key == '9':
            self.d.click(0.828, 0.858)
        elif key == '0':
            self.d.click(0.49, 0.955)
        elif key == 'b':
            self.d.click(0.84, 0.949)
        else:
            raise TypeError('key error')




class h5Driver(boxDriver):

    def __init__(self,device=None):
        super(h5Driver,self).__init__(device)


    def load_h5Driver(self):
        self.h5driver = H5Driver(self.d,self.device)
        self.h5driver.initDriver()
        return self.h5driver

    def click_by_text(self,text):
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

    def get_text_by_xp(self,xp):
        """
        通过xpath定位点击
        :param xp:
        :return:
        """
        return self.h5driver.getElementTextByXpath(xp)

    def long_click_by_xp(self,xp):
        """
        通过xpath长按点击
        :param xp:
        :return:
        """
        self.h5driver.longClickElementByXpath(xp)

    def double_click_by_xp(self,xp):
        """
        通过xpath双击
        :param xp:
        :return:
        """
        self.h5driver.repeatedClickElementByXpath(xp)

    def scroll_To_Xpath(self,xp):
        """
        滚动直xpath可见
        :param xp:
        :return:
        """
        self.h5driver.scrollToElementByXpath(xp)

    def type_text(self,xp,text):
        """
        清除输入框内容，输入文字
        :param xp:
        :param text:
        :return:
        """
        self.h5driver.clickElementByXpath(xp)
        self.h5driver.clearInputTextByXpath(xp)
        self.h5driver.textElementByXpath(xp,text)

    def back_page(self):
        """
        返回上一页
        :return:
        """

        self.h5driver.returnLastPage()

    def isElementExist(self,xp):
        """
        判断元素是否存在
        :param xp:
        :return:
        """
        return self.h5driver.isElementExist(xp)

    def open_url(self,url):
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

    def send_Script(self,script):
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

    def getImage(self,time):
        '''
        截取图片,并保存在images文件夹
        :return: 无
        '''
        if time != '':
            imgPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+'\\reports\\images\\%s.png' % time
            self.d.screenshot(imgPath)
        else:
            pass

class wxDriver(boxDriver):
    def __init__(self,):
        super(wxDriver,self).__init__()

    def load_h5Driver(self):
        self.xcxdriver = WxDriver(self.d,self.device)
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

    def get_text_by_xp(self,xp):
        """
        通过xpath定位点击
        :param xp:
        :return:
        """
        return self.xcxdriver.getElementTextByXpath(xp)

    def scroll_To_Xpath(self,xp):
        """
        滚动直xpath可见
        :param xp:
        :return:
        """
        self.xcxdriver.scrollToElementByXpath(xp)

    def type_text(self,xp,text):
        """
        输入文字(还没有试过清除有没有用)
        :param xp:
        :param text:
        :return:
        """
        self.xcxdriver.clearInputTextByXpath(xp)
        self.xcxdriver.textElementByXpath(xp,text)

    def back_page(self):
        """
        返回上一页
        :return:
        """

        self.xcxdriver.returnLastPage()

    def isElementExist(self,xp):
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
    a=h5Driver()
    print a.d.device_info
    # a.d(className="android.widget.RelativeLayout", instance=14).click()
    a.d(xpath="//android.widget.TextView[@text='我']").click()


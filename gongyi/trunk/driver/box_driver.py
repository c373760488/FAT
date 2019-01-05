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
        self.x=int(self.d.info['displayWidth'])
        self.y=int(self.d.info['displayHeight'])

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

    def u_set_text(self, msg, **kwargs):
        """
         uiautomaor2 ,输入text
        :param text:
        :param kwargs:
        :return:
        """
        self.d(**kwargs).set_text(msg)

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

    def u_tap(self,x,y):
        """
        点击坐标
        :param x:
        :param y:
        :return:
        """
        self.d.tap(x,y)

    def u_swipe(self,direction, steps=10):
        """
        向某个方向滑动
        :param direction:
        :return:
        """
        self.d().swipe(direction, steps)


# class h5Driver(boxDriver):
#
#     def __init__(self, device=None):
#         super(h5Driver, self).__init__(device)

    def load_h5Driver(self):
        self.h5driver = H5Driver(self.d, self.device)
        self.h5driver.initDriver()
        return self.h5driver

    def h5_click_by_text(self, text):
        """
        通过文本点击
        :param text:
        :return:
        """
        self.h5driver.clickFirstElementByText(text)

    def h5_click_by_xp(self, xp):
        """
        通过xpath点击
        :param xp:
        :return:
        """
        self.h5driver.clickElementByXpath(xp)

    def h5_get_text_by_xp(self, xp):
        """
        通过xpath定位获取text
        :param xp:
        :return:
        """
        return self.h5driver.getElementTextByXpath(xp)

    def h5_long_click_by_xp(self, xp):
        """
        通过xpath长按点击
        :param xp:
        :return:
        """
        self.h5driver.longClickElementByXpath(xp)

    def h5_double_click_by_xp(self, xp):
        """
        通过xpath双击
        :param xp:
        :return:
        """
        self.h5driver.repeatedClickElementByXpath(xp)

    def h5_scroll_To_Xpath(self, xp):
        """
        滚动直xpath可见
        :param xp:
        :return:
        """
        self.h5driver.scrollToElementByXpath(xp)

    def h5_type_text(self, xp, text):
        """
        清除输入框内容，输入文字
        :param xp:
        :param text:
        :return:
        """
        self.h5driver.clickElementByXpath(xp)
        self.h5driver.clearInputTextByXpath(xp)
        self.h5driver.textElementByXpath(xp, text)

    def h5_back_page(self):
        """
        返回上一页
        :return:
        """

        self.h5driver.returnLastPage()

    def h5_isElementExist(self, xp):
        """
        判断元素是否存在
        :param xp:
        :return:
        """
        return self.h5driver.isElementExist(xp)

    def h5_open_url(self, url):
        """
        打开指定url，（h5页面已被打卡）
        :param url:
        :return:
        """
        self.h5driver.navigateToPage(url)

    def h5_close_h5(self):
        """
        关闭h5
        :return:
        """
        self.h5driver.closeWindow()

    def h5_send_Script(self, script):
        """
        发送js命令
        :param script:
        :return:
        """
        return self.h5driver.executeScript(script)

    def h5_get_url(self):
        """
        获取当前url
        :return:
        """
        return self.h5driver.getCurrentPageUrl()

    def h5_getImage(self, time):
        '''
        截取图片,并保存在images文件夹
        :return: 无
        '''
        if time != '':
            imgPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '\\reports\\images\\%s.png' % time
            self.d.screenshot(imgPath)
        else:
            pass


# class xcxDriver(boxDriver):
#     def __init__(self, ):
#         super(xcxDriver, self).__init__()

    def load_xcxDriver(self):
        self.xcxdriver = WxDriver(self.d, self.device)
        self.xcxdriver.initDriver()
        return self.xcxdriver

    def xcx_click_by_text(self, text):
        """
        通过text来搜索，点击第一个text相符合的控件。参数同clickElementByXpath()
        :param text:
        :return:
        """
        self.xcxdriver.clickFirstElementByText(text)

    def xcx_click_by_xp(self, xp):
        """
        通过xpath定位点击
        :param xp:
        :return:
        """
        self.xcxdriver.clickElementByXpath(xp)

    def xcx_get_text_by_xp(self, xp):
        """
        通过xpath定位点击
        :param xp:
        :return:
        """
        return self.xcxdriver.getElementTextByXpath(xp)

    def xcx_scroll_To_Xpath(self, xp):
        """
        滚动直xpath可见
        :param xp:
        :return:
        """
        self.xcxdriver.scrollToElementByXpath(xp)

    def xcx_type_text(self, xp, text):
        """
        输入文字(还没有试过清除有没有用)
        :param xp:
        :param text:
        :return:
        """
        self.xcxdriver.clearInputTextByXpath(xp)
        self.xcxdriver.textElementByXpath(xp, text)

    def xcx_back_page(self):
        """
        返回上一页
        :return:
        """

        self.xcxdriver.returnLastPage()

    def xcx_isElementExist(self, xp):
        """
        判断元素是否存在
        :param xp:
        :return:
        """
        return self.xcxdriver.isElementExist(xp)

    def xcx_close_xcx(self):
        """
        关闭h5
        :return:
        """
        self.xcxdriver.close()


if __name__ == '__main__':
    # package_name = 'com.tencent.mm'
    # runCommand('adb shell pm clear %s' % package_name)
    a=uiautomator2.connect_usb()
    # a.swipe()
    a().swipe("up")


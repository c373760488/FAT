# -*- coding: utf-8 -*-
import re

from gongyi.trunk.driver.box_driver import h5Driver
from main_page import mainPage
from page_map import *
class yqjPage(mainPage):



    def get_proj_name(self):
        """
        获取项目名称
        :return:
        """
        return self.h5_driver.get_text_by_xp(lj_proj_map('项目名称'))

    def own_yqj_create(self,explain=None,isgoon=False,target=None,limit=None):
        """
        创建个人一起捐
        :param explain: (str)发起说明，默认不填写
        :param isgoon: (bool)达到筹款后是否继续,默认达到目标可以继续
        :param target:(str,int,float)筹款目标，默认不设目标
        :param islimit:(str,int,float)限定每人捐助金额，默认不限定
        :return:
        """
        self.h5_driver.scroll_To_Xpath(lj_proj_map('项目介绍'))
        self.h5_driver.click_by_xp(yqj_create_map('一起捐'))
        if explain !=None:
            self.h5_driver.type_xp(yqj_create_map('发起说明'),explain)
        if isgoon!=False:
            self.h5_driver.click_by_text('达到筹款后可继续捐款')
        if target!=None:
            self.h5_driver.click_by_text('自定目标')
            self.h5_driver.type_xp('请输入金额',target)
        if limit !=None:
            self.h5_driver.click_by_text('限定每人捐X元')
            self.h5_driver.type_text('限定金额输入',limit)
        self.h5_driver.click_by_text('下一步')
        self.h5_driver.click_by_text('完成发起')
        self.share_yqj()
        self.h5_driver.click_by_text('立即捐出第一笔')
        self.h5_driver.click_by_xp(yqj_create_map('关闭捐款弹窗'))

    def team_yqj_create(self,tname,explain=None,isgoon=False,target=None,limit=None):
        # todo:未完成
        """
        创建团体一起捐
        :param explain: (str)发起说明，默认不填写
        :param isgoon: (bool)达到筹款后是否继续,默认达到目标可以继续
        :param target:(str,int,float)筹款目标，默认不设目标
        :param islimit:(str,int,float)限定每人捐助金额，默认不限定
        :return:
        """
        self.h5_driver.scroll_To_Xpath(lj_proj_map('项目介绍'))
        self.h5_driver.click_by_xp(yqj_create_map('一起捐'))
        self.h5_driver.click_by_text('团体')
        self.h5_driver.type_text(yqj_create_map('团体名称'),tname)
        if explain !=None:
            self.h5_driver.type_xp(yqj_create_map('发起说明'),explain)
        if isgoon!=False:
            self.h5_driver.click_by_text('达到筹款后可继续捐款')
        if target!=None:
            self.h5_driver.click_by_text('自定目标')
            self.h5_driver.type_xp('请输入金额',target)
        if limit !=None:
            self.h5_driver.click_by_text('限定每人捐X元')
            self.h5_driver.type_text('限定金额输入',limit)
        self.h5_driver.click_by_text('下一步')
        self.h5_driver.click_by_text('完成发起')
        self.share_yqj()
        self.h5_driver.click_by_text('立即捐出第一笔')
        self.h5_driver.click_by_xp(yqj_create_map('关闭捐款弹窗'))


    def yqj_donate_money(self,money,select=None):
        """
        乐捐捐款
        :param money:自定义金额捐款
        :param select: 直接选定金额捐款:默认金额
        :return:
        """
        self.h5_driver.click_by_text('我要参与')
        if select==None:
            self.h5_driver.type_text(yqj_donate_map('自定金额'),str(money))
        else:
            self.h5_driver.click_by_xp(yqj_donate_map('默认金额' % select))
        self.h5_driver.click_by_text('确定')

    def get_own_yqj_thanks_page_info(self):
        """
        获取感谢页信息
        :return:
        """
        thanks_page_nick = self.h5_driver.get_text_by_xp(yqj_thanks_map('昵称'))
        projname = self.h5_driver.get_text_by_xp(yqj_thanks_map('项目名称')).replace("\n","")
        thanks_page_money = self.h5_driver.get_text_by_xp(yqj_thanks_map('本次捐助'))
        thanks_page_experience = self.h5_driver.get_text_by_xp(yqj_thanks_map('个人爱心经验'))
        thanks_page_projname = re.match(r'.*\[(.*)\]', projname,re.S).group(1)
        url=self.h5_driver.get_url()
        thanks_page_transcode = re.match(r'.*tradeno=(\d*).*', url).group(1)
        return {'昵称':thanks_page_nick,'项目名称':thanks_page_projname,'本次捐助':thanks_page_money,'爱心经验':thanks_page_experience,'流水单号':thanks_page_transcode}


if __name__ == '__main__':
    h=h5Driver()
    # h.close_wx()
    # h.open_wx()
    h.load_h5Driver()
    a=yqjPage(h)
    b=a.h5_driver.click_by_text('哈哈')
    print str(b)

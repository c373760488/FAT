# -*- coding: utf-8 -*-


def wx_login_map(key):
    """
    微信登录路由
    :param key:
    :return:
    """
    route = {
        '登录':{"resourceId":"com.tencent.mm:id/e0y"},
        '用微信号登录': {"resourceId":"com.tencent.mm:id/cmv"},
        '账号': {"resourceId":"com.tencent.mm:id/ka"},
        '密码': {"resourceId":"com.tencent.mm:id/ka", "text":"请填写密码"},
        '确认登录': {"resourceId":"com.tencent.mm:id/cmw"},
        '账号密码错误确定':{"resourceId":"com.tencent.mm:id/ayb"},
        '更多': {"resourceId":"com.tencent.mm:id/cn3"},
        '登录其他账号': {"resourceId":"com.tencent.mm:id/ct"},

    }
    return route[key]

def wx_home_map(key):
    """
    微信首页路由
    :param key:
    :return:
    """
    route = {
        '我': {"resourceId":"com.tencent.mm:id/d3r", "className":"android.widget.LinearLayout", "instance":3},
        '通讯录': {"resourceId": "com.tencent.mm:id/d3r", "className": "android.widget.LinearLayout", "instance": 2},
        '发现': {"resourceId":"com.tencent.mm:id/d3r", "className":"android.widget.LinearLayout", "instance":1},
        '微信': {"resourceId":"com.tencent.mm:id/d3r","className":"android.widget.LinearLayout", "instance":0},
    }
    return route[key]

def wx_user_center_map(key):
    """
    微信个人中心路由
    :param keu:
    :return:
    """
    route = {
        '微信号': {"resourceId": "com.tencent.mm:id/d7y"},
        '支付':{"resourceId":"android:id/title", "text":"支付"},
        '腾讯公益': {"resourceId":"com.tencent.mm:id/cxm", "text":"腾讯公益"},
        '设置': {"resourceId":"android:id/title", "text":"设置"},
        '退出': {"resourceId":"android:id/title", "text":"退出"},
        '退出登录': {"resourceId":"com.tencent.mm:id/ct"},
        '退出（提醒）': {"resourceId":"com.tencent.mm:id/ayb"},
    }
    return route[key]

def main_page_map(key):
    """
    首页路由
    :param key:
    :param xpath:
    :return:
    """
    route = {
        '腾讯公益标题': {"resourceId": "android:id/text1"},
    }
    return route[key]

def lj_proj_map(key):
    """
    乐捐捐款页面路由
    :param key:
    :param xpath:
    :return:
    """
    route = {
        '项目介绍':'//*[@class="description-title"]',
        '项目名称':'//*[@class="card-name"]',
        '自定金额': '//*[@placeholder="自定金额"]',
        '捐款浮层支付金额':'//*[@class="gy-paylayer-dinc j-money"]',
        '默认金额':  'data-mtav="amount%d"',
        '确定':  '//*[@class="gy-paylayer-fbtn gy-paylayer-fbtn_dft j-pay" and @data-mtav="submit"]',
        '支付错误提示':'//*[@id="weui_dialog"]//*[@class="weui_dialog_bd"]',
        '大金额支付提示':'//*[@id="weui_confirm"]//*[@class="weui_dialog_bd"]/span',
    }
    return route[key]

def lj_thanks_map(key):
    """
    乐捐感谢页路由
    :param key:
    :param xpath:
    :return:
    """
    route = {
        '本次捐助': '//*[@class="mod-datablock-item"]/h1',
        '爱心经验': '//*[@class="mod-datablock-item j-openDialog"]/h1',
        '昵称':  '//*[@class="g-flex thanks-user"]/div[2]/h4',
        '项目名称': '//*[@class="g-flex thanks-title"]/div/h3',
    }
    return route[key]

def yqj_create_map(key):
    """
    一起捐创建页面路由
    :param key:
    :param xpath:
    :return:
    """
    route = {
        '一起捐': '//*[@class="footBar j-footBar"]//*[text()="一起捐"]',
        '个人发起说明': '//*[@id="personalDesc"]',
        '团体名称': '//*[@id="teamTitle"]',
        '团体发起说明': '//*[@id="teamDesc"]',
        '企业名称': '//*[@id="companyName"]',
        '企业活动标题': '//*[@id="companyTitle"]',
        '企业发起说明':  '//*[@id="companyDesc"]',
        '企业筹款周期': '//*[@id="companySpan"]',
        '请输入金额':'//*[@class="gy-paylayer-mbtn-input j-amount-input"]',
        '限定金额输入':'//*[@class="gy-paylayer-mbtn-input j-amount-input"]',
        '关闭捐款弹窗':'//*[@class="gy-paylayer-close"]',

    }
    return route[key]


def yqj_check_map(key):
    """
    一起捐创建前确认页面路由
    :param key:
    :param xpath:
    :return:
    """
    route = {
        '筹款目标': '//*[@class="target j-target"]/b[1]',

    }
    return route[key]

def yqj_donate_map(key):
    """
    一起捐捐赠页面路由
    :param key:
    :param xpath:
    :return:
    """
    route = {

        '自定金额': '//*[@placeholder="自定金额"]',
        '默认金额': 'data-mtav="amount%d"',
        '协议': '//*[@class="gy-paylayer-cell j-agreement"]//*[@class="gy-paylayer-checkbox"]',
        '匿名': '//*[@class="gy-paylayer-cell j-anonymous"]//*[@class="gy-paylayer-checkbox"]',

    }
    return route[key]


def yqj_thanks_map(key):
    """
    一起捐感谢页路由
    :param key:
    :param xpath:
    :return:
    """
    route = {
        '本次捐助':  '//*[@class="fnt-dinc thanks-title-num"]',
        '个人爱心经验': '//*[@class="thanks-title-bt"]/b',
        '昵称': '//*[@class="g-flex thanks-user"]//*[@class="g-flex-m"]/h4',
        '项目名称': '//*[@class="g-flex thanks-title"]/div/h3',
        '感谢页留言': '//*[@class="textarea"]',

    }
    return route[key]


def user_center_map(key):
    """
    个人中心路由
    :param key:
    :param xpath:
    :return:
    """
    route = {
        '勋章关闭按钮':'//*[@class="page-newAchieve-close j-close-newAchieveDg"]',
        '项目名称': '//*[@class="dona_time_title"]',
        '捐款金额':  '//*[@class="dona_time_money"]/span',
        '流水单号': '//*[@class="dona_time_order_num"]',
    }
    return route[key]

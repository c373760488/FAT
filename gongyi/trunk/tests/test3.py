# -*- coding: utf-8 -*-
import uiautomator2
a=uiautomator2
d=a.connect_usb('9fb4ebef')
# w=a.connect_wifi('10.43.208.36')
print d.app_info('com.tencent.mm')
d(resourceId="com.tencent.mm:id/d3r", className="android.widget.LinearLayout", instance=0).click()
# print w.device_info
# w(resourceId="com.tencent.mm:id/cw3", className="android.widget.LinearLayout", instance=3)

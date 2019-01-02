小程序必须发现-小程序-长按删除
###adb命令
1.直接打开微信h5  
 `adb shell am start -W  com.tencent.mm/com.tencent.mm.plugin.webview.ui.tools.WebViewUI {'rawUrl': 'http://h5.baike.qq.com/mobile/enter.html',}`
2.杀掉微信    
`os.system('adb shell am force-stop com.tencent.mm')`</br>
3.启动微信   
`os.system('adb shell am start com.tencent.mm/.ui.LauncherUI')`</br>
4.查看以安装包</br>
`adb shell pm list packages`</br>
5.结束进程</br>
`adb shell ps |find "uiautomator"`      
`adb shell kill <PID>`
6.删除包
`adb uninstall com.github.uiautomator`

###uiautomator

1.如果uiautomator.devices('').info长时间未响应，报错`ioerror RPC server not started`</br>
参考`https://blog.csdn.net/peterblog/article/details/74565992`

###uiautomator2
`https://testerhome.com/topics/11357`</br>
`pip install --upgrade --pre uiautomator2`安装</br>
在version文件中改版本号`https://github.com/openatx/atx-agent/releases`最新的atx版本
`python -m uiautomator2 init`安装atx-agent</br>
`pip install --upgrade --pre weditor`安装weditor定位工具</br>
`python -m weditor`打开定位工具</br>


###unittest.TestCase

1.跳过用例

	@unittest.skip(reason)	
	无条件跳过被装饰的测试方法；
	
	reason：理由，描述为什么跳过测试用例
	
	@unittest.skipIf(condition,reason)	
	如果条件为真，则继续执行执行，否则跳过被装饰的测试用例；
	
	reason：理由，描述为什么跳过测试用例
	
	@unittest.skipUnless(condition,reason)	除非条件为真，否则跳过被装饰的测试用例；
	@unittest.expectedFailure	
	将测试用例标记为“预期失败”：
	
	如果测试执行时失败，则测试结果不计为失败；
	
	unittest.Skip(reason)	
	如引发某种定义的异常，则跳过该测试；
	一般可以使用TestCase.skip()或者一个跳过装饰器，而不是直接使用

2.执行用例

1.`setUp()`每次执行用例执行的方法</br>
2.`tearDown()`每次结束用例时执行的方法</br>
3.执行用例前只执行一次

	@classmethod
	def setUpClass(cls):
4.执行用例后只执行一次

	@classmethod
    def tearDownClass(cls):

5.添加用例
`test_suit.addTests(map(Mydemo,["Mytest1","Mytest2","Mytest3"]))`
`test_suite.addTest(Mydemo('Mytest1'))`

6.case文件改动

	#
    def _baseAssertEqual(self, first, second, msg=None):
	    """The default assertEqual implementation, not type specific."""
	    if not first == second:
	        standardMsg = '%s != %s' % (safe_repr(first), safe_repr(second))
	        msg = self._formatMessage(msg, standardMsg)
	        raise self.failureException(msg)
	    else:
	        self.nowTime=False

	 @property
    def nowTime(self):

        # return time.strftime('%Y%m%d_%H.%M.%S')
        return self._nowTime

    @nowTime.setter
    def nowTime(self,key):
        if key:
            self._nowTime=time.strftime('%Y%m%d_%H.%M.%S')
        else:
            self._nowTime=''
            
    def addNowTime(func):
        def wrapper(self,*args,**kwargs):
            self.nowTime = True
            for i in kwargs:
                if i=='msg':
                    kwargs['msg']+='\nscreenshot:%s.png' % self.nowTime
            a=func(self,*args,**kwargs)
            return a

        return wrapper





###htmltestrunner

加入失败截图
需要在失败异常信息中加入 screenshot:20181229_11.06.37.png 格式 截图信息，html会自动加载./images/screenshot:20181229_11.06.37.png 图片
 
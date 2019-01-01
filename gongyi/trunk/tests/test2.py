import time


class aa:
    def __init__(self):
        self.nowTime=''
    def addNowTime(func):
        def wrapper(self,*args,**kwargs):
            self.nowTime = True
            for i in kwargs:
                if i=='msg':
                    kwargs['msg']+='\nscreenshot:%s.png' % self.nowTime
            try:
                a=func(self,*args,**kwargs)
                self.nowTime = False
                return a
            except:
                raise AssertionError
            return a

        return wrapper


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

    @addNowTime
    def assertEqual(self,aaa):
        """Fail if the two objects are unequal as determined by the '=='
           operator.
        """

        print aaa
a=aa()
a.assertEqual('aaa')
#
# def a(*args,**kwargs):
#     for i in kwargs:
#         if i=='msg':
#             kwargs['msg']+= '\nscreenshot:%s.png'
#     print  kwargs['msg']
# a(a=1,b=2,msg='')
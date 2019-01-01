# -*- coding: utf-8 -*-
import os
from gongyi.trunk.lib import unittest
import time
from gongyi.trunk.driver.html_test_runner import HTMLTestRunner
from gongyi.trunk.tests.lj_test import ljTest
from gongyi.trunk.tests.test1 import aa


class gongyiRunner:

    def run(self):
        timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
        test_suite = unittest.TestSuite()
        # for i in range(7):
        #     test_suite.addTest(ljTest('test_%d' % (i+1)))
        # test_suite.addTest(aa('test_1'))
        test_suite.addTest(ljTest('test_6'))
        report_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+'\\reports\\gongyi_test_report_%s.html' % timestrmap
        report_file = open(report_path, mode='wb')
        test_runner = HTMLTestRunner(stream=report_file,
                                     title='公益自动化测试报告',
                                     description='测试详情',
                                     tester='p_jiangfcao'

                                     )
        test_runner.run(test_suite)
        report_file.close()

if __name__ == '__main__':
    a=gongyiRunner()
    a.run()

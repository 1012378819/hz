#coding:utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
#test_dir='../'
test_dir='G:/useful/selenium+py/chongshi/test_project/test_case'

discover=unittest.defaultTestLoader.discover(test_dir,pattern='test_b*.py')

'''
suite=unittest.TestSuite()

suite.addTest(testadd.TestAdd(""))
suite.addTest(testadd.TestAdd(""))
'''
# 定义报告存放路径
file = 'G:/useful/selenium+py/chongshi/test_project/test_case/'
now = time.strftime("%Y-%m-%d %H_%M_%S")
fp = open(file + '%s_result.html' % now, 'w+')
# 定义测试报告
runner = HTMLTestRunner(stream=fp, title=u'百度搜索测试报告', description=u'用例执行情况：')

runner.run(testunit)  # 运行测试用例
fp.close()

if __name__=="__main__":
    runner=unittest.TextTestRunner()
    runner.run(discover)

#coding:utf-8
import unittest
from HTMLTestRunner import HTMLTestRunner
import  time

test_dir='G:/useful/selenium+py/chongshi/test_project/test_case'

discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__=='__main__':
    now=time.strftime('%Y%m%d %H%M%S')
    filename=test_dir+'%s result.html'%now
    fp=open(filename,'w+')
    runner=HTMLTestRunner(stream=fp, title=u'测试报告', description =u'用例执行情况')
    runner.run(discover)
    fp.close()



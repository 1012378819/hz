#coding:utf-8
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

class Count:
    def __init__(self,a,b):
        self.a=int(a)
        self.b=int(b)

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

class TestCount(unittest.TestCase):
    def setUp(self):
        print('test start')

    def test_add(self):
        c=Count(3,6)
        self.assertEqual(c.add(),8,'not equal')

    def test_add_1(self):
        c = Count(3, 6)
        self.assertEqual(c.add(), 9, 'not equal')

    def tearDown(self):
        print('test end')

# unittest跳过testcase的设置方法
class MyTestCondition(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @unittest.skip(u'直接跳过测试')
    def test_skip(self):
        print('test aaa')
    @unittest.skipIf(3>2,u'当条件为真是跳过测试')
    def test_skip_if(self):
        print('test bbb')
    @unittest.skipUnless(3>2,u'当条件为True时执行测试')
    def test_skip_unless(self):
        print('test ccc')
    @unittest.expectedFailure #如果运行失败，则不会标记为失败
    def test_expected_failure(self):
        self.assertEqual(2,3)

# test各种setupteardown作用范围
def setUpModule():
    print("test module start >>>>>>>>>>>>>>>")

def tearDownModule():
    print('test module end >>>>>>>>>>>>>>>')

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("test class start =========>>>")
    @classmethod
    def tearDownClass(cls):
        print("test class end ==========>>>")
    def setUp(self):
        print("test case start -->")
    def tearDown(self):
        print("test case end -->")
    def test_case(self):
        print("test case1")
    def test_case2(self):
        print("test case2")

if __name__=='__main__':
    # unittest.main()  # 执行所有case
    # 构造测试集
    suite=unittest.TestSuite()
    suite.addTest(TestCount("test_add"))
    suite.addTest(TestCount("test_add_1"))
    # 执行测试
    runner=unittest.TextTestRunner()   # 自带的报告
    runner.run(suite)
    # 执行方式三：
    # test_dir = r'C:\Users\pei.lu.KINGSTAR\PycharmProjects\test_data'
    # discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_b*.py')
    # now=time.strftime('%Y%m%d %H%M%S')
    # filename=test_dir+'%s result.html'%now
    # with open(filename,'w+') as fp
    #     runner=HTMLTestRunner(stream=fp, title='测试报告', description ='用例执行情况')
    #     runner.run(discover)
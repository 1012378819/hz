#author:lup
#-*-coding:utf-8-*-
import unittest

class MyTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @unittest.skip(u'直接跳过测试')
    def test_skip(self):
        print 'test aaa'
    @unittest.skipIf(3>2,u'当条件为真是跳过测试')
    def test_skip_if(self):
        print 'test bbb'
    @unittest.skipUnless(3>2,u'当条件为True时执行测试')
    def test_skip_unless(self):
        print 'test ccc'
    @unittest.expectedFailure #如果运行失败，则不会标记为失败
    def test_expected_failure(self):
        assertEqual(2,3)
if __name__=='__main__':
    unittest.main()

    # 这些方法同样可以作用于测试类，只需将它们定义在测试类上面即可

    # @unittest.skip(u"直接跳过测试该测试类")
    # class MyTest(unittest.TestCase):
    # ……
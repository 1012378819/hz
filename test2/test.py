#coding:utf-8
import unittest
from test2.cal import Count

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

if __name__=='__main__':
    #构造测试集
    suite=unittest.TestSuite()
    suite.addTest(TestCount("test_add"))
    suite.addTest(TestCount("test_add_1"))
    #执行测试
    runner=unittest.TextTestRunner()
    runner.run(suite)

# TextTestRunner 是来执行测试用例的，其中的 run(test)用来执行 TestSuite/TestCase。测
# 试的结果会保存到 TextTestResult 实例中，包括运行了多少个测试用例，成功了多少、失败了多少等信息
# 执行所有case  # unittest.main()
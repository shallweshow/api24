import unittest,requests
from lib.db1 import *


class MyTestCase(unittest.TestCase):
    url="http://127.0.0.1:8082/p2p_management/addProduct"

    def test_add_ok(self):

        # 判断 noname是否已经注册过了
        if check_user("111"):
            # 如果已经注册过了 就删除
            del_user("111")
        data={"proNum":"111","proName":"101","proLimit":"10","annualized":"10"}
        r = requests.post(url=self.url,json=data)
        # 预期结果
        # result = {"code":1,"message":"成功","response":None}
        #
        self.assertNotIn('失败',r.text)
        # 判断数据库中noname已经存在
        self.assertTrue(check_user("111"))
        # 数据还原
        del_user('111')
    def test_add_err(self):

        data={"proNum":"111","proName":"101","proLimit":"10","annualized":"10%"}
        r = requests.post(url=self.url, json=data)

        self.assertIn('400',r.text)

if __name__ == '__main__':
    unittest.main()

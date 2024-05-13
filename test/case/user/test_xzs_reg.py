import unittest,requests
from lib.db import *
name="student"
noname="peter"

class MyTestCase(unittest.TestCase):
    url="http://192.168.55.1:8000/api/student/user/register"

    def test_reg_ok(self):
        print(check_user(name=noname))
        # 判断 noname是否已经注册过了
        if check_user(name=noname):
            # 如果已经注册过了 就删除
            del_user(noname)
        data={"userName":noname,"password":"123456","userLevel":1}
        r = requests.post(url=self.url,json=data)
        # 预期结果
        result = {"code":1,"message":"成功","response":None}
        #
        self.assertDictEqual(r.json(),result)
        # 判断数据库中noname已经存在
        self.assertTrue(check_user(noname))
        # 数据还原
        del_user(noname)
    def test_reg_err(self):
        if not check_user(name):
            add_user(name,"123456")
        data = {"userName": name, "password": "123456", "userLevel": 1}
        r = requests.post(url=self.url, json=data)
        result={"code":2,"message":"用户已存在","response":None}
        self.assertDictEqual(r.json(), result)

if __name__ == '__main__':
    unittest.main()

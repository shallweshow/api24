import json
import unittest,requests
from lib.read_excel import *
from lib.db import *
from lib.case_log import log_case_info

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.li =read_excel().excel_to_list(data_file, 'TestUserReg')
    def test_reg_ok(self):
        case_data =read_excel().get_test_data(self.li,'reg_ok')
        # case_data['url']
        url = case_data.get('url')  # 从字典中取数据,excel中的标题也必须是小写url
        args = case_data.get('args')  # 字符串格式,需要用json.loads(str)转为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据
        a = json.loads(args).get("userName")
        if check_user(name=a):
            # 如果已经注册过了 就删除
            del_user(a)
        res = requests.post(url=url, json=json.loads(args))  # 表单请求,数据转为字典格式
        log_case_info("test_reg_ok",url,args,expect_res,res.text)
        self.assertIn(expect_res, res.text)  # 改为assertIn断言
        del_user(a)
    def test_reg_err(self):
        case_data = read_excel().get_test_data(self.li, 'reg_err')
        # case_data['url']
        url = case_data.get('url')  # 从字典中取数据,excel中的标题也必须是小写url
        args = case_data.get('args')  # 字符串格式,需要用json.loads(str)转为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据
        res = requests.post(url=url, json=json.loads(args))  # 表单请求,数据转为字典格式
        log_case_info("test_reg_err",url,args,expect_res,res.text)
        self.assertIn(expect_res, res.text)  # 改为assertIn断言

if __name__ == '__main__':
    unittest.main()

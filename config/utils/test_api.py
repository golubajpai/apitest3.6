from Testcase import ApiTest
import pytest
'''

class TestAssert(TestCase):
	def test_request(self):
		a=ApiTest("",403,"get")
		response=a.callapi()

		assert (response.status_code)==a.success_status_code
'''




class Test_UserHandling:
    def test_login(self):
        a=ApiTest("login/",402,"post",{"email":"golubajpai302@gmail.com","password":"Priyam@13"})
        self.k=a.api()
        assert a.success_status_code==self.k.status_code

    def test_modification(self):
        a=ApiTest("login/",4002,"post",{"email":"golubajpai302@gmail.com","password":"Priyam@13"})
        self.k=a.api()
        assert a.success_status_code==self.k.status_code

    def test_deletion(self):
        a=ApiTest("login/",4002,"post",{"email":"golubajpai302@gmail.com","password":"Priyam@13"})
        self.k=a.api()
        assert a.success_status_code==self.k.status_code

class Test_UserHandling2:
    def test_login(self):
        a=ApiTest("signup/",404,"post",{"email":"golubajpai302@gmail.com","password":"Priyam@13"})
        self.k=a.api()
        assert a.success_status_code==self.k.status_code

    def test_modification(self):
        a=ApiTest("signup/",404,"post",{"email":"golubajpai302@gmail.com","password":"Priyam@13"})
        self.k=a.api()
        assert a.success_status_code==self.k.status_code

    def test_deletion(self):
        a=ApiTest("signup/",404,"post",{"email":"golubajpai302@gmail.com","password":"Priyam@13"})
        self.k=a.api()
        assert a.success_status_code==self.k.status_code

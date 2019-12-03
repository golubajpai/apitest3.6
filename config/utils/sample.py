import pytest
from Testcase import ApiTest

def test_first():
	test1 = ApiTest("",403,"get") 
	response = test1.calltestapi()
	assert 1

@pytest.mark.incremental
class TestUserHandling:
    def test_login(self):
        est1 = ApiTest("",403,"get") 
		response = test1.calltestapi()

    def test_modification(self):
        assert 0

    def test_deletion(self):
        pass

import allure, pytest


class Test_001:

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="这是一个测试样品1")
    def test_001(self):
        print("test_001")
        allure.attach("标题", "具体的描述信息")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="这是一个测试样品2")
    def test_002(self):
        print("test_002")
        assert True


    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    @allure.step(title="这是一个测试样品4")
    def test_004(self):
        print("test_004")
        assert True
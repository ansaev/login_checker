from pytest import fixture
import time
from login_check import LoginChecker


class TestClass:
    checker = LoginChecker()
    test_examples = [
        {'name': "login1s", "passed": True},
        {'name': "login13", "passed": True},
        {'name': "lon-s", "passed": True},
        {'name': "lo.n-s", "passed": True},
        {'name': "1login1s", "passed": False},
        {'name': "log--.++*in1s", "passed": False},
        {'name': ".login1s", "passed": False},
        {'name': "-login1s", "passed": False},
        {'name': "lo.n-s.", "passed": False},
        {'name': "lo.n-s-", "passed": False},
        {'name': "lo.n-sdfdfdfdfdfdfdfdfdf", "passed": False},
        {'name': "", "passed": False},
    ]

    @fixture(params=test_examples)
    def login(self, request):
        return request.param

    def test_check_regexp_compiled(self, login):
        assert self.checker.check_regexp_compiled(login['name']) == login['passed']

    def test_check_regexp(self, login):
        assert self.checker.check_regexp(login['name']) == login['passed']

    def test_check_no_regexp_1(self, login):
        assert self.checker.check_no_regexp_1(login['name']) == login['passed']

    def test_check_separated_regex(self, login):
        assert self.checker.check_separated_regex(login['name']) == login['passed']

    def test_perfomance(self):
        start_time = time.time()
        end_time = start_time
        for test_case in self.test_examples:
            self.checker.check_regexp(test_case['name'])
        end_time = time.time()
        print("without compile:", end_time-start_time)
        start_time = time.time()
        for test_case in self.test_examples:
            self.checker.check_regexp_compiled(test_case['name'])
        end_time = time.time()
        print("with compile:", end_time-start_time)
        start_time = time.time()
        for test_case in self.test_examples:
            self.checker.check_no_regexp_1(test_case['name'])
        end_time = time.time()
        print("without regexp 1:", end_time-start_time)
        start_time = time.time()
        for test_case in self.test_examples:
            self.checker.check_separated_regex(test_case['name'])
        end_time = time.time()
        print("separated_regex:", end_time-start_time)
        assert True


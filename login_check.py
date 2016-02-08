import re


class LoginChecker(object):
    def __init__(self):
        self.reg_exp = re.compile(r"^[A-Za-z]{1}[A-Za-z0-9.-]{,18}[A-Za-z0-9]{1}\Z")
        self.reg_exp_first = re.compile(r"[A-Za-z]")
        self.reg_exp_last = re.compile(r"[A-Za-z0-9]")
        self.reg_exp_mid = re.compile(r"^[A-Za-z0-9.-]*\Z")
        self.first_symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.last_symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        self.mid_symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-."

    # input params:
    # login - String, requied, login name
    # output:
    # bool
    def check_regexp_compiled(self, login):
        assert type(login) == str
        rez = self.reg_exp.match(login)
        if rez:
            return True
        return False

    # input params:
    # login - String, requied, login name
    # output:
    # bool
    def check_regexp(self, login):
        assert type(login) == str
        rez = re.match(r"^[A-Za-z]{1}[A-Za-z0-9.-]{,18}[A-Za-z0-9]{1}\Z", login)
        if rez:
            return True
        return False

    # input params:
    # login - String, requied, login name
    # output:
    # bool
    def check_no_regexp_1(self, login):
        assert type(login) == str
        login_length = len(login)
        if not 0 < login_length < 21:
            return False
        if login[0] not in self.first_symbols:
            return False
        if login_length == 1:
            return True
        if login[-1] not in self.last_symbols:
            return False
        if login_length == 2:
            return True
        for char in login[0:-1]:
            if char not in self.mid_symbols:
                return False
        return True

    # input params:
    # login - String, requied, login name
    # output:
    # bool
    def check_separated_regex(self, login):
        assert type(login) == str
        login_length = len(login)
        if not 0 < login_length < 21:
            return False
        if not self.reg_exp_first.match(login[0]):
            return False
        if login_length == 1:
            return True
        if not self.reg_exp_last.match(login[-1]):
            return False
        if login_length == 2:
            return True
        rez = self.reg_exp_mid.match(login[1:-1])
        if not rez:
            return False
        return True







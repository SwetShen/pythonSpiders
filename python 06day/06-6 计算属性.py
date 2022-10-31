
class Test:
    a = 1
    b = 2
    @property
    def sum1(self):
        return self.a + self.b
    def sum2(self):
        return self.a + self.b

    @property
    def password(self):
        #算法生成密码
        return 1234

test = Test()
print(test.sum2())
print(test.sum1)

test.a = 5
print(test.sum2())
print(test.sum1)
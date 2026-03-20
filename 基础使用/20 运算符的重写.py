'''
@create_time: 2026/3/15 下午4:29
@Author: GeChao
@File: 20 运算符的重写.py
'''


class Test(object):
    def __init__(self, name):
        self.name = name

    def __or__(self, other):
        return MySequence(self, other)

    def __str__(self):
        return self.name


class MySequence(object):
    def __init__(self, *args):
        self.sequence = []
        for arg in args:
            self.sequence.append(arg)

    def __or__(self, other):
        self.sequence.append(other)
        return self

    def run(self):
        for i in self.sequence:
            print(i)

'''
a
b
c
<class '__main__.MySequence'>
'''

if __name__ == '__main__':
    a = Test('a')
    b = Test('b')
    c = Test('c')

    d = a | b | c
    d.run()
    print(type(d))

# coding = utf-8
'''
time:2021/5/11 15:04
'''

import mock
class B:
    def give_id(self):
        pass

class A:
    def accept_id(self):
        get_mocke = mock.Mock(return_value='模拟数据11111111111111')
        get_data = B()
        get_data.give_id = get_mocke
        accept_id = get_data.give_id()
        print(accept_id)

if __name__ == '__main__':
    A=A()
    A.accept_id()
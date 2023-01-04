import pytest
from zhugeceshi import ArrayFuntion

class Test_arrary:
    def setup(self):
        print("------->前置方法")
        self.array = ArrayFuntion()

    def test_resize(self):
        print("------->测试扩容")
        assert self.array.resize() == [None, None]

    def test_myappend(self):
       print("-------->是否能够正常的添加")
       assert self.array.myappend(2)==[2, None]

    def test_myinsertPositive(self):
        print("-------->索引为正整数是否能正确插入")
        assert self.array.myinsert(0,5) == [5, None]

    #剩下的测试类似unnitest，暂时省略

if __name__=='__main__':
    pytest.main("-s test_arrary.py")
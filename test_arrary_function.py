import unittest
from zhugeceshi import ArrayFuntion

class ArrayTestCase(unittest.TestCase):
    """测试数组的增删改查方法"""

    def setUp(self):
        self.array = ArrayFuntion()

    def test_resize(self):
        self.resizeResult =self.array.resize()
        self.assertEqual(self.resizeResult,[None, None])

    def test_myappend(self):
        """是否能够正常的添加"""
        self.appendResult=self.array.myappend(2)
        self.assertEqual(self.appendResult,[2, None])

    def test_myinsertPositive(self):
        """索引为正整数是否能正确插入"""
        self.insertPositiveResult=self.array.myinsert(0,5)
        self.assertEqual(self.insertPositiveResult,[5, None])

    def test_myinsertNegative(self):
        """索引为负整数是否能正确提示"""
        self.insertNegativeResult=self.array.myinsert(-1,5)
        self.assertEqual(self.insertNegativeResult,"idx暂不支持负数")

    def test_myinsertNoninteger(self):
        """索引为非整数是否能正确提示"""
        self.insertNonintegerResult=self.array.myinsert(1.5,5)
        self.assertEqual(self.insertNonintegerResult,"idx为索引，请输入整数")

    def test_myinsertOut(self):
        """索引越界时是否能正确提示"""
        self.insertOutResult=self.array.myinsert(8,5)
        self.assertEqual(self.insertOutResult,"越界了")

    def test_myinsertError(self):
        """索引为非法输入时是否能正确提示"""
        self.insertErrorResult=self.array.myinsert('测试',5)
        self.assertEqual(self.insertErrorResult,"请输入数字")

    def test_myremovePositive(self):
        """索引为正整数是否能正确删除"""
        self.array.myappend(8)
        self.removePositiveResult=self.array.myremove(0)
        self.assertEqual(self.removePositiveResult,[None, None])

    def test_myremoveNegative(self):
        """索引为负整数是否能正确提示"""
        self.array.myappend(8)
        self.removeNegativeResult=self.array.myremove(-1)
        self.assertEqual(self.removeNegativeResult,"idx暂不支持负数")

    def test_myremoveNoninteger(self):
        """索引为非整数是否能正确提示"""
        self.array.myappend(8)
        self.removeNonintegerResult=self.array.myremove(1.5)
        self.assertEqual(self.removeNonintegerResult,"idx为索引，请输入整数")

    def test_myremoveOut(self):
        """索引越界时是否能正确提示"""
        self.array.myappend(8)
        self.removeOutResult=self.array.myremove(8)
        self.assertEqual(self.removeOutResult,"越界了")

    def test_myremoveError(self):
        """索引为非法输入时是否能正确提示"""
        self.array.myappend(8)
        self.removeErrorResult=self.array.myremove('测试')
        self.assertEqual(self.removeErrorResult,"请输入数字")

    def test_myupdatePositive(self):
        """索引为正整数是否能正确更新"""
        self.array.myappend(8)
        self.updatePositiveResult=self.array.myupdate(0,9)
        self.assertEqual(self.updatePositiveResult,[9, None])

    def test_myupdateNegative(self):
        """索引为负整数是否能正确提示"""
        self.array.myappend(8)
        self.updateNegativeResult=self.array.myupdate(-1,9)
        self.assertEqual(self.updateNegativeResult,"idx暂不支持负数")

    def test_myupdateNoninteger(self):
        """索引为非整数是否能正确提示"""
        self.array.myappend(8)
        self.updateNonintegerResult=self.array.myupdate(1.5,9)
        self.assertEqual(self.updateNonintegerResult,"idx为索引，请输入整数")

    def test_myupdateOut(self):
        """索引越界时是否能正确提示"""
        self.array.myappend(8)
        self.updateOutResult=self.array.myupdate(8,9)
        self.assertEqual(self.updateOutResult,"越界了")

    def test_myupdateError(self):
        """索引为非法输入时是否能正确提示"""
        self.array.myappend(8)
        self.updateErrorResult=self.array.myinsert('测试',5)
        self.assertEqual(self.updateErrorResult,"请输入数字")

    def test_myfindPositive(self):
        """索引为正整数是否能正确查找"""
        self.array.myappend(8)
        self.findPositiveResult=self.array.myfind(0)
        self.assertEqual(self.findPositiveResult,8)

    def test_myfindNegative(self):
        """索引为负整数是否能正确查找"""
        self.array.myappend(8)
        self.findNegativeResult=self.array.myfind(-1)
        self.assertEqual(self.findNegativeResult,"idx暂不支持负数")

    def test_myfindNoninteger(self):
        """索引为非整数是否能正确提示"""
        self.array.myappend(8)
        self.findNonintegerResult=self.array.myfind(1.5)
        self.assertEqual(self.findNonintegerResult,"idx为索引，请输入整数")

    def test_myfindOut(self):
        """索引越界时是否能正确提示"""
        self.array.myappend(8)
        self.findOutResult=self.array.myfind(8)
        self.assertEqual(self.findOutResult,'越界了')

    def test_myfindError(self):
        """索引为非法输入时是否能正确提示"""
        self.array.myappend(8)
        self.findErrorResult=self.array.myfind('测试')
        self.assertEqual(self.findErrorResult,"请输入数字")


if __name__ == '__main__':
        unittest.main()


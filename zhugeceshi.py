class ArrayFuntion:
    def __init__(self):
        self.sizeExponent=0
        self.size=0
        self.lastindex=0
        self.myarrary=[]

    def resize(self):
        newsize = 2 ** (self.sizeExponent+1)
        newarrary = [None]*newsize
        for i in range(self.size):
            newarrary[i] = self.myarrary[i]
        self.size = newsize
        self.myarrary=newarrary
        self.sizeExponent+=1
        return self.myarrary

    def myappend(self, val):
        if self.lastindex > self.size - 1:
            self.resize()
        self.myarrary[self.lastindex] = val
        self.lastindex += 1
        return self.myarrary

    def myinsert(self, idx, val):
        try:
            #判断参数是否正常，参数不正常，给出对应提示
            result = idx % 1
            if result != 0:
                # print("idx为索引，请输入整数")# 这样执行代码的时候，输出结果中会含有一个None，所以改成下面这样
                return "idx为索引，请输入整数"
            else:
                if idx < 0:
                    # print("idx暂不支持负数")# 这样执行代码的时候，输出结果中会含有一个None，所以改成下面这样
                    return "idx暂不支持负数"
                else:
                    if idx>self.lastindex:
                        return "越界了"
                    else:
                        #参数正常，开始处理逻辑
                        if self.lastindex >= self.size/2:
                            self.resize()
                        for i in range(self.lastindex, idx - 1, -1):
                            self.myarrary[i + 1] = self.myarrary[i]
                        self.myarrary[idx] = val
                        self.lastindex +=1
                        return self.myarrary
        except(TypeError):
            return "请输入数字"

    def myremove(self, idx):
        try:
            # 判断参数是否正常，参数不正常，给出对应提示
            result = idx % 1
            if result != 0:
                # print("idx为索引，请输入整数")
                return "idx为索引，请输入整数"
            else:
                if idx<0:
                    # if self.myarrary[idx] != 'None':
                    #     for i in range(idx,-1):
                    #         self.myarrary[i] = self.myarrary[i+1]
                    # self.lastindex -= 1
                    # self.size -= 1
                    # return self.myarrary
                    # print("idx暂不支持负数")
                    return "idx暂不支持负数"
                else:
                    if idx>=self.lastindex+1:
                        # print("越界了")
                        return "越界了"
                    else:
                        # 参数正常，开始处理逻辑
                        for i in range(idx, self.lastindex):
                            self.myarrary[i] = self.myarrary[i+1]
                        self.lastindex -= 1
                        self.size -= 1
                        return self.myarrary
        except(TypeError):
            return "请输入数字"

    def myupdate(self, idx, val):
        try:
            # 判断参数是否正常，参数不正常，给出对应提示
            result = idx % 1
            if result != 0:
                # print("idx为索引，请输入整数")
                return "idx为索引，请输入整数"
            else:
                if idx > self.lastindex:
                    # print("越界了")
                    return "越界了"
                else:
                    if idx<0:
                        # print("idx暂不支持负数")
                        return "idx暂不支持负数"
                    else:
                        # 参数正常，开始处理逻辑
                        self.myarrary[idx] = val
                        return self.myarrary
        except(TypeError):
            return "请输入数字"

    def myfind(self, idx):
        try:
            # 判断参数是否正常，参数不正常，给出对应提示
            result = idx % 1
            if result != 0:
                # print("idx为索引，请输入整数")
                return "idx为索引，请输入整数"
            else:
                if idx<0:
                    return "idx暂不支持负数"
                else:
                    if idx >= self.lastindex:
                        # print("越界了")
                        return "越界了"
                    else:
                        # 参数正常，开始处理逻辑
                        return self.myarrary[idx]
        except(TypeError):
            return "请输入数字"


if __name__ == '__main__':
    array = ArrayFuntion()
    print('———测试扩容———')
    print(array.resize())
    print('———测试添加———')
    print(array.myappend(5))
    print(array.myappend(5))
    print(array.myappend(5))
    print('———测试插入———')
    print(array.myinsert(0,5))#正整数
    print(array.myinsert(-1,7))#负整数
    print(array.myinsert(1.5,7))#非整数
    print(array.myinsert(8,7))#越界
    print(array.myinsert('测试',7))#非法输入
    print('———测试删除———')
    print(array.myremove(0))#正整数
    print(array.myremove(-1))#负整数
    print(array.myremove(1.5))#非整数
    print(array.myremove(8))#越界
    print(array.myremove('测试'))#非法输入
    print('———测试更新———')
    print(array.myupdate(0,5))#正整数
    print(array.myupdate(-1,7))#负整数
    print(array.myupdate(1.5,7))#非整数
    print(array.myupdate(8,7))#越界
    print(array.myupdate('测试',7))#非法输入
    print('———测试查找———')
    print(array.myfind(0))#正整数
    print(array.myfind(-1))#负整数
    print(array.myfind(1.5))#非整数
    print(array.myfind(8))#越界
    print(array.myfind('测试'))#非法输入
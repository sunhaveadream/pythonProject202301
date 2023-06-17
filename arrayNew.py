class ArrayList:

    def __init__(self):
        self.myArray = [] #初始化数组
        self.size=0 #初始化数组长度
        self.lastIndex=0 #初始化最后位置的索引
        self.sizeExponent=0 #初始化扩容指数

    def reSize(self):
        newSize = 2 **(self.sizeExponent+1)
        newArray=[0]*newSize #占位
        for i in range(self.size):
            newArray[i] = self.myArray[i]
        self.size=newSize
        self.myArray=newArray
        self.sizeExponent+=1
        return self.myArray

    def myAppend(self,val):
        if self.lastIndex >self.size-1:
            self.reSize()
        self.myArray[self.lastIndex]=val
        self.lastIndex+=1
        return self.myArray

    def myInsert(self,idx,val):
        try:
            #异常链路
            result = idx%1
            if result!=0:
                return "请输入整数"
            else:
                if idx<0:
                    return "idx暂时不支持负数"
                # 正常链路
                else:
                    if self.lastIndex>=self.size/2:
                        self.reSize()
                    for i in range(self.lastIndex,idx-1,-1):
                        self.myArray[i+1]=self.myArray[i]
                    self.myArray[idx]=val
                    self.lastIndex+=1
                    return self.myArray
        except(TypeError):
            return "请输入数字"

    def myRemove(self,idx):
        try:
            #异常链路
            result = idx%1
            if result!=0:
                return "请输入整数"
            else:
                if idx<0:
                    return "idx暂时不支持负数"
                else:
                    if idx>=self.lastIndex+1:
                        return "您输入的越界了，请检查"
                    # 正常链路
                    else:
                        for i in range(idx,self.lastIndex):
                            self.myArray[i]=self.myArray[i+1]
                        self.lastIndex-=1
                        self.size-=1
                        return self.myArray
        except(TypeError):
            return "请输入数字"

    def myUpdate(self,idx,val):
        try:
            #异常链路
            result = idx%1
            if result!=0:
                return "请输入整数"
            else:
                if idx<0:
                    return "idx暂时不支持负数"
                else:
                    if idx>=self.lastIndex+1:
                        return "您输入的越界了，请检查"
                    # 正常链路
                    else:
                        self.myArray[idx]=val
                        return self.myArray
        except(TypeError):
            return "请输入数字"

    def myFind(self,idx):
        try:
            #异常链路
            result = idx%1
            if result!=0:
                return "请输入整数"
            else:
                if idx<0:
                    return "idx暂时不支持负数"
                else:
                    if idx>=self.lastIndex+1:
                        return "您输入的越界了，请检查"
                    # 正常链路
                    else:
                        return self.myArray[idx]
        except(TypeError):
            return "请输入数字"

if __name__=='__main__':
    array =ArrayList()
    print('——————测试正常链路——————')
    #正常链路
    print(array.reSize())
    print(array.myAppend(1))
    print(array.myInsert(0,2))
    print(array.myRemove(0))
    print(array.myUpdate(0,3))
    print(array.myFind(0))
    print('——————测试异常链路——————')
    #异常链路
    print(array.myFind(-4))
    print(array.myFind(5.5))
    print(array.myFind(100))
    print(array.myFind('test'))


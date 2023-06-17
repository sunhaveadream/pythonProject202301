class hashTable:
    def __init__(self):
        """初始化"""
        self.loadFactor=0.75#当哈希表内元素增加，冲突可能性也增加，所以设定载荷因子，当已插入表中的元素个数/表的容量达到载荷因子时，进行扩容
        self.size=0
        self.capacity=100
        self.mod=self.capacity
        self.hashTable=[(None,None)for _ in range(self.capacity)]

    def hash(self,x):
        """除留余数法"""
        try:
            #异常链路
            result=x%1
            if result!=0:
                return "请输入整数"
            else:
                #正向链路，除留余数法
                return x%self.mod
        except(TypeError):
            return "请输入数字"

    def resize(self):
        """扩容"""
        newCapacity=self.capacity*2
        newHashTable=[(None,None)for _ in range(newCapacity)]
        for (key,value)in self.hashTable:
            if key:
                hashkey=self.hash(key)
                if newHashTable[hashkey][0] is None:
                    newHashTable[hashkey]=(key,value)
        self.capacity=newCapacity
        self.hashTable=newHashTable

    def put(self,key,value):
        """增"""
        try:
            #异常链路
            result=key%1
            if result!=0:
                return "请输入整数"
            else:
                # 正常链路
                hashKey=self.hash(key)
                if self.size/self.capacity>self.loadFactor:
                    self.resize()
                if self.hashTable[hashKey][0] is None:
                    self.hashTable[hashKey]=(key,value)
                else:
                    for i in range(self.capacity):
                        hashKey=self.hash(key+i)#进行线性探索
                        if self.hashTable[hashKey][0] is None:
                            self.hashTable[hashKey]=(key,value)
                self.size+=1
        except(TypeError):
            return "请输入数字"

    def delNew(self,key):
        """删"""
        try:
            #异常链路
            result=key%1
            if result!=0:
                return "请输入整数"
            else:
                # 正常链路
                hashKey=self.hash(key)
                if self.hashTable[hashKey]==None:#如果key对应的哈希值本身为空，不进行处理
                    return "为空无需处理"
                keyH,valueH=self.hashTable[hashKey]
                if keyH==key:#如果key对应的哈希值存在冲突，进行冲突处理，如果不存在冲突，进行删除，即置为空
                    valueHnew=None
                    self.hashTable[hashKey]=keyH,valueHnew
                    return "已删除"
                else:
                    for i in range(self.capacity):
                        hashKey=self.hash(key+i)
                        keyH,valueH=self.hashTable[hashKey]
                        if keyH==key:
                            valueH=None
                        self.size-=1
                    return "删除成功"
                return -1
        except(TypeError):
            return "请输入数字"

    def update(self,key,value):
        """改"""
        try:
            #异常链路
            keyResult=key%1
            valueResult=key%1
            if keyResult!=0:
                return "请输入整数"
            elif valueResult!=0:
                return "请输入整数"
            else:
                hashKey = self.hash(key)
                keyH,valueH=self.hashTable[hashKey]
                if keyH==key:
                    valueHnew=value
                    self.hashTable[hashKey]=keyH,valueHnew
                    return "更新成功"
                else:
                    for i in range(self.capacity):
                        hashKey=self.hash(key+i)
                        keyH,valueH=self.hashTable[hashKey]
                        if keyH==key:
                            valueHnew=None
                            self.hashTable[hashKey]=keyH,valueHnew
                            return "更新成功"
                return -1
        except(TypeError):
            return "请输入数字"

    def get(self,key):
        """查"""
        try:
            #异常链路
            result=key%1
            if result!=0:
                return "请输入整数"
            else:
                # 正常链路
                hashKey=self.hash(key)
                keyH,valueH=self.hashTable[hashKey]
                if keyH==key:
                    return valueH
                else:
                    for i in range(self.capacity):
                        hashKey=self.hash(key+i)#进行线性探索
                        keyH,valueH=self.hashTable[hashKey]
                        if keyH==key:
                            return valueH
                return -1
        except(TypeError):
            return "请输入数字"

if __name__=="__main__":
    print("———————测试正常链路—————————")
    hash=hashTable()
    for i in range(88):
        hash.put(i,"test{}".format(i))#增
    print(hash.get(8))#查
    print(hash.update(8,"testTest"))#改
    print(hash.get(8))#查
    print(hash.delNew(8))#删
    print(hash.get(8))#查
    print("———————测试异常链路—————————")
    print(hash.get('测试'))
    print(hash.put('测试','ceshi'))
    print(hash.update('测试','testTest'))
    print(hash.delNew('测试'))
    print(hash.put(8.8,'ceshi'))
    print(hash.update(8.8,'testTest'))










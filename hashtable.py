class HashTable:
    def __init__(self):
        self.capacity=100
        self.mod=self.capacity
        self.size=0
        self.loadFactor=0.75
        self.hashtable=[(None,None)for i in range(self.capacity)]

    def hash(self,x):
        # 使用除留余数法
        try:
            result = x % 1
            if result != 0:
                return "请输入整数"
            else:
                return x%self.mod
        except(TypeError):
            return "请输入数字"


    def resize(self):
        # 当存储数据与容量比大于负载因子时，进行扩容
        # 原哈希表长度✖2
        newCapacity=self.capacity*2
        # 新哈希表在内存中进行预先占内存
        newHashTable=[(None,None) for _ in range(newCapacity)]
        # 遍历原哈希表，原数组中的数据重新计算其在新数组中的位置后，再放入新数组
        for (key,value) in self.hashtable:
            if key:
                # 根据哈希函数计算哈希值
                hashk=self.hash(key)
                if newHashTable[hashk][0] is None:
                    newHashTable[hashk]=(key,value)
                else:
                    for i in range(self.capacity):
                        hashK=self.hash(key+i)
                        if newHashTable[hashK][0] is None:
                            newHashTable[hashK]=(key,value)
        self.capacity = newCapacity
        self.hashtable=newHashTable

    def put(self,key,value):
        try:
            result = key % 1
            if result != 0:
                return "请输入整数"
                # 根据哈希函数计算哈希值
            else:
                hashK=self.hash(key)
                # 当存储数据与容量比大于负载因子时，进行扩容
                if self.size/self.capacity>self.loadFactor:
                    self.resize()
                # 判断是否有哈希冲突，如果有，进行处理，如果没有，进行插入
                if self.hashtable[hashK][0] is None:
                    self.hashtable[hashK]=(key,value)
                else:
                    for i in range(self.capacity):
                        # 进行线性探测
                        hashK=self.hash(key+i)
                        if self.hashtable[hashK][0] is None:
                            self.hashtable[hashK]=(key,value)
                self.size+=1
        except(TypeError):
            return "请输入数字"

    def get(self,key):
        try:
            result = key % 1
            if result != 0:
                return "请输入整数"
                # 根据哈希函数计算哈希值
            else:
                hashK=self.hash(key)
                # 判断是否存在哈希冲突，如果冲突，则通过线性探测法寻找
                keyH,valueH=self.hashtable[hashK]
                if keyH==key:
                    return valueH
                else:
                    for i in range(self.capacity):
                        hashK=self.hash(key+i)
                        keyH,valueH=self.hashtable[hashK]
                        if keyH==key:
                            return valueH
                # 若没找到，返回-1
                return -1
        except(TypeError):
            return "请输入数字"

    def myDel(self,key):
        try:
            result = key % 1
            if result != 0:
                return "请输入整数"
                # 根据哈希函数计算哈希值
            else:
                # 根据哈希函数计算哈希值
                hashK = self.hash(key)
                # 如果key对应的哈希值本身为空，不进行处理
                # 如果key对应的哈希值存在冲突，进行冲突处理
                # 如果key对应的哈希值不存在冲突，进行删除，即置为空
                if self.hashtable[hashK]==None:
                    return '本身为空，无需处理'
                keyH, valueH = self.hashtable[hashK]
                if keyH == key:
                    valueHnew = None
                    self.hashtable[hashK] = keyH, valueHnew
                    return '删除成功'
                else:
                    for i in range(self.capacity):
                        hashK=self.hash(key+i)
                        keyH,valueH=self.hashtable[hashK]
                        if keyH==key:
                            valueH=None
                    self.size -= 1
                    return '更新成功'
                    # 若没找到，返回-1
                return -1
        except(TypeError):
            return "请输入数字"

    def myUpdate(self,key,value):
        try:
            result = key % 1
            if result != 0:
                return "请输入整数"
                # 根据哈希函数计算哈希值
            else:
                # 根据哈希函数计算哈希值
                hashK = self.hash(key)
                keyH, valueH = self.hashtable[hashK]
                if keyH == key:
                    valueHnew = value
                    self.hashtable[hashK]=keyH, valueHnew
                    return '更新成功'
                else:
                    for i in range(self.capacity):
                        hashK = self.hash(key + i)
                        keyH, valueH = self.hashtable[hashK]
                        if keyH == key:
                            valueHnew = None
                            self.hashtable[hashK] = keyH, valueHnew
                            return '更新成功'
                # 若没找到，返回-1
                return -1
        except(TypeError):
            return "请输入数字"



if __name__ =="__main__":
    hashTest=HashTable()
    print("<<<<<<<<<<<<<<异常链路>>>>>>>>>>>>>>")
    print(hashTest.put('我','testNew'))
    print(hashTest.get('我'))
    print(hashTest.myUpdate('我','testNew'))
    print(hashTest.myDel('我'))
    print(hashTest.put(1.5,'testNew'))
    print(hashTest.get(1.5))
    print(hashTest.myUpdate(1.5,'testNew'))
    print(hashTest.myDel(1.5))
    print("<<<<<<<<<<<<<<正常链路>>>>>>>>>>>>>>")
    for i in range(22):
        hashTest.put(i,"test{}".format(i))
    print(hashTest.capacity)
    print(hashTest.get(2))
    print(hashTest.myUpdate(2,"testNew"))
    print(hashTest.get(2))
    print(hashTest.myDel(2))
    print(hashTest.get(2))


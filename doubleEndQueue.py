class DoubleFrontEndQueue:
    """此方法使用列表来实现双端队列，将列表的末尾作为双端队列的前端，双端队列的后端是列表下标索引为0的地方"""

    def __init__(self):
        self.items=[]

    def addFront(self,item):
        try:
            #异常链路
            result=item%1
            if result!=0:
                print("请输入整数")
            else:
                #正常链路
                self.items.append(item)
        except(TypeError):
            print("请输入数字")

    def addRear(self,item):
        try:
            #异常链路
            result=item%1
            if result!=0:
                print("请输入整数")
            else:
                #正常链路
                self.items.insert(0,item)
        except(TypeError):
            print("请输入数字")

    def isEmpty(self):
        return self.items==[]

    def removeFront(self):
        if self.isEmpty():
            raise Exception('此队列为空')
        else:
            return self.items.pop()

    def removeRear(self):
        if self.isEmpty():
            raise Exception('此队列为空')
        else:
            return self.items.pop(0)

    def getSize(self):
        print(len(self.items))

    def displayQueue(self):
        print(self.items[:])

    def palindrome(self,str):
        left=str
        right=left[::-1]
        for i in range(len(left)):
            if left[i]==right[i]:
                i+=1
        if i==len(left):
            print("这是回文")
        else:
            print("这不是回文")

if __name__=="__main__":
    myDoubleEndQueue=DoubleFrontEndQueue()
    print("————————————正常链路————————————")
    print("——————在双端队列的前端插入——————")
    myDoubleEndQueue.addFront(1)
    myDoubleEndQueue.addFront(2)
    myDoubleEndQueue.displayQueue()
    myDoubleEndQueue.getSize()
    print("——————在双端队列的后端插入——————")
    myDoubleEndQueue.addRear(3)
    myDoubleEndQueue.addRear(4)
    myDoubleEndQueue.displayQueue()
    myDoubleEndQueue.getSize()
    print("——————在双端队列的前端删除——————")
    myDoubleEndQueue.removeFront()
    myDoubleEndQueue.displayQueue()
    myDoubleEndQueue.getSize()
    print("——————在双端队列的后端删除——————")
    myDoubleEndQueue.removeRear()
    myDoubleEndQueue.displayQueue()
    myDoubleEndQueue.getSize()
    print("——————判断回文——————")
    myDoubleEndQueue.palindrome('上海自来水来自海上')
    print("————————————异常链路————————————")
    myDoubleEndQueue.addFront('w')
    myDoubleEndQueue.addRear(1.5)
    myDoubleEndQueue.addRear('w')
    myDoubleEndQueue.addFront(1.5)
    print("——————判断回文——————")
    myDoubleEndQueue.palindrome('一二三四')

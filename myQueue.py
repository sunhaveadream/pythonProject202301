#队列的第一种实现方法
class Queue1():
    def __init__(self,maxSize):
        self.maxSize=maxSize
        self.front=0
        self.rear=0
        self.queue=[]

    def joinQueue(self,elem):
        try:
            #异常链路
            result=elem%1
            if result!=0:
                print("请输入整数")
            else:
                if self.isFull():
                    print("此队列已满")
                else:
                    # 正常链路
                    self.queue.append(elem)
                    self.rear+=1
        except(TypeError):
            print("请输入数字")

    def outOfQueue(self):
        if self.isEmpty():
            print("此队列已无元素")
        else:
            endOfQueue=self.queue[self.front]
            self.queue.pop(self.front)
            self.front += 1
            return endOfQueue

    def isFull(self):
        return self.rear-self.front+1 == self.maxSize

    def isEmpty(self):
        return self.rear == self.front

    def displayQueue(self):
        print((self.queue))

if __name__ == "__main__":
    print("队列的第一种实现方法")
    myQueue=Queue1(10)
    print("——————正常链路——————")
    print("初始队列")
    myQueue.displayQueue()
    myQueue.isEmpty()
    myQueue.isFull()
    print("添加元素后")
    myQueue.joinQueue(1)
    myQueue.joinQueue(5)
    myQueue.joinQueue(3)
    myQueue.displayQueue()
    print("移除元素后")
    myQueue.outOfQueue()
    myQueue.displayQueue()
    print("——————异常链路——————")
    myQueue.joinQueue('w')
    myQueue.joinQueue(1.5)
    for i in range(8):
        myQueue.joinQueue(i)

#队列的第二种实现方法
class Node(object):
    def __init__(self,elem,next=None):
        self.elem=elem
        self.next=next

class Queue2(object):
    def __init__(self):
        self.__head=None
        self.__rear=None
        self.size=0

    def joinQueue2(self,elem):
        try:
            #异常链路
            result=elem%1
            if result!=0:
                print("请输入整数")
            else:
                p=Node(elem)
                if self.isEmpty2():
                    self.__head=p
                    self.__rear=p
                else:
                    self.__rear.next=p
                    self.__rear=p
        except(TypeError):
            print("请输入数字")

    def outOfQueue2(self):
        if self.isEmpty2():
            print("此队列已无元素")
        else:
            top=self.__head.elem
            self.__head=self.__head.next
            return top

    def isEmpty2(self):
        return not self.__head

    def displayQueue2(self):
        temp=self.__head
        while temp is not None:
            print(temp.elem,end="\t")
            temp=temp.next

if __name__ == "__main__":
    print("\n")
    print("队列的第二种实现方法")
    myQueue2=Queue2()
    print("——————正常链路——————")
    print("初始队列")
    myQueue2.displayQueue2()
    myQueue2.isEmpty2()
    print("添加元素后")
    myQueue2.joinQueue2(1)
    myQueue2.joinQueue2(5)
    myQueue2.joinQueue2(3)
    myQueue2.displayQueue2()
    print("\n")
    print("移除元素后")
    myQueue2.outOfQueue2()
    myQueue2.displayQueue2()
    print("\n")
    print("——————异常链路——————")
    myQueue2.joinQueue2('w')
    myQueue2.joinQueue2(1.5)



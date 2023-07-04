#栈的第一种实现方法
class Stack1:
    def __init__(self,maxSize):
        self.max=maxSize#最大长度
        self.elem=[None]*self.max#占位
        self.top=0#栈顶指针
        self.bottom=0#栈底指针

    def push(self,elem):
        try:
            #异常链路
            result=elem%1
            if result!=0:
                return "请输入整数"
            else:
                if self.top-self.bottom==self.max:
                    return "已满"
                else:
                    #正常链路
                    self.elem[self.top]=elem
                    self.top+=1
                    return self.elem
        except(TypeError):
            return "请输入数字"

    def pop(self):
        if self.top==self.bottom:
            return "已空"
        else:
            self.top-=1
            element=self.elem[self.top]
            e=self.elem[self.top]
            return element

    def getTop(self):
        return self.elem[self.top-1]

if __name__ == "__main__":
    print("测试第一种栈的实现方法")
    data = list(map(int, input("请输入栈元素，用空格隔开：").split(" ")))
    print("\n")
    s = Stack1(len(data))
    print("目前顺序栈中元素为")
    for i in range(len(data)):
        s.push(data[i])
    for i in range(s.top - s.bottom):
        print(s.elem[i], end=" ")
    print("\n")
    stackTop = s.getTop()
    print("栈顶元素是: %d" % stackTop)
    print("\n")
    for i in range(s.top - s.bottom):
        s.pop()
        print("在出栈 %d 次后,剩余的栈元素为:" % (i + 1), end=" ")
        for j in range(s.top - s.bottom):
            print(s.elem[j], end=" ")
        print("\n")


#栈的第二种实现方法
class Stack2(object):
    def __init__(self):
        self.stack=[]

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return "此栈为空栈"

    def stackTop(self):
        if self.stack:
            print(self.stack[-1])

    def isEmpty(self):
        print(not bool(self.stack))

    def size(self):
        print(len(self.stack))

if __name__ == "__main__":
    print("测试第二种栈的实现方法")
    stack=Stack2()
    stack.push(6)
    stack.push(9)
    stack.stackTop()
    stack.isEmpty()
    stack.size()
    print("\n")
    stack.pop()
    stack.stackTop()
    stack.isEmpty()
    stack.size()
    print("\n")
    stack.pop()
    stack.isEmpty()

#栈的第三种实现方法
class StackNode:
    def __init__(self):
        self.elem=None
        self.next=None

class Stack3:
    def __init__(self):
        self.stack3Top=None

    def stack3Push(self,elem):
        s=StackNode()
        s.elem=elem
        s.next=self.stack3Top
        self.stack3Top=s

    def stack3Pop(self):
        e=self.stack3Top.elem
        self.stack3Top=self.stack3Top.next
        return e

    def getStack3Top(self):
        if self.stack3Top:
            return self.stack3Top.elem
        else:
            return None

    def stack3Length(self):
        count = 0
        theTop=self.stack3Top
        while theTop:
            count+=1
            theTop=theTop.next
        return count

if __name__ == "__main__":
    print("测试第三种栈的实现方法")
    s = Stack3()  # 链栈的初始化
    data = list(map(int, input("请输入栈的元素，用空格隔开:").split(" ")))
    for i in range(len(data)):
        s.stack3Push(data[i])
    print("\n")
    top = s.stack3Top
    print("目前栈的元素为:", end=" ")
    while top is not None:
        print(top.elem, end=" ")
        top = top.next
    print("\n")
    for i in range(s.stack3Length()):
        s.stack3Pop()
        print("在弹栈 %d 次后,目前栈的元素剩余:" % (i + 1), end=" ")
        top = s.stack3Top
        while top is not None:
            print(top.elem, end=" ")
            top = top.next
        print("\n")
#定义链表结构
class listNode:
    def __init__(self,elem):
        self.elem=elem#保存数据的节点
        self.next=None#后继节点

#定义链表基本功能
class listNodeHandle:
    def __init__(self,node=None):
        self.head=None#head指向头节点，如果是空链表，则指向None

    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False

    def travel(self):
        pointer=self.head#指针p指向头节点，从头节点开始遍历直到尾节点next指向None
        if pointer==None:
            print("空链表")
        else:
            while pointer!=None:
                print(pointer.elem)
                pointer=pointer.next

    def length(self):
        pointer=self.head
        count=0
        if pointer==None:
            return 0
        else:
            while pointer!=None:
                count+=1
                pointer=pointer.next
            return count

    def add(self,item):#头插
        try:
            result=item%1
            #异常链路
            if result!=0:
                print("请输入整数")
            else:
            #正常链路
                node = listNode(item)
                node.next=self.head
                self.head=node
        except(TypeError):
            print("请输入数字")

    def append(self,item):#尾插
        try:
            result=item%1
            #异常链路
            if result!=0:
                print("请输入整数")
            else:
            #正常链路
                node =listNode(item)
            if self.head==None:
                self.head=node
            else:
                pointer=self.head
                while pointer.next!=None:
                    pointer=pointer.next
                pointer.next=node
        except(TypeError):
            print("请输入数字")

    def insert(self,pos,item):#中间插
        try:
            itemResult=item%1
            posResult=pos%1
            #异常链路
            if itemResult!=0:
                print("请输入整数")
            elif posResult!=0:
                print("请输入整数")
            else:
            #正常链路
                node=listNode(item)
                if self.head==None:
                    self.add(item)
                else:
                    if pos<=0:
                        self.add(item)
                    elif pos>self.length()-1:
                        self.append(item)
                    else:
                        pointer=self.head
                        count=0
                        while count<pos-1:
                            count+=1
                            pointer=pointer.next
                        node.next=pointer.next
                        pointer.next=node
        except(TypeError):
            print("请输入数字")

    def remove(self,item):
        try:
            #异常链路
            if self.head==None:
                print("您要删除的不在链表中")
            else:
                pointer=self.head
                if pointer.elem==item:
                    self.head=pointer.next
                else:
                    while pointer.next!=None:
                        if pointer.next.elem==item:
                            pointer=pointer.next
                        else:
                            pointer=pointer.next
                    print("您要删除的不在链表中")
        except(TypeError):
            print("请输入数字")

    def delNew(self,pos):
        try:
            #异常链路
            result=pos%1
            pointer=self.head
            if result!=0:
                print("请输入整数")
            elif pointer==None:
                print("这是空链表")
            else:
                if pos<0:
                    print("暂时不支持负数")
                elif pos>self.length():
                    print("您越界了")
                else:
                    # 正常链路
                    count=0
                    while count<pos-1:
                        count+=1
                        pointer=pointer.next
                    pointer.next=pointer.next.next
        except(TypeError):
            print("请输入数字")

    def pop(self):
        #异常链路
        pointer=self.head
        if pointer==None:
            print("这是空链表")
        else:
            if pointer.next==None:
                pointer=None
            else:
                while pointer.next!=None:
                    pointer=pointer.next
                pointer.next=None


    def update(self,pos,item):
        try:
            itemResult = item % 1
            posResult = pos % 1
            # 异常链路
            if itemResult != 0:
                print("请输入整数")
            elif posResult != 0:
                print("请输入整数")
            else:
                pointer=self.head
                if pointer==None:
                    print("这是空链表")
                elif pos>self.length():
                    print("您越界了")
                else:
                    count=0
                    while count!=pos-1:
                        count+=1
                        pointer=pointer.next
                    pointer.elem=item
        except(TypeError):
            print("请输入数字")

    def find(self,item):
        try:
            result=item%1
            #异常链路
            if result!=0:
                print("请输入整数")
            else:
            #正常链路
                pointer=self.head
                if pointer==None:
                    return False
                else:
                    while pointer.next!=None:
                        if pointer.elem==item:
                            return True
                        else:
                            pointer=pointer.next
                    return False
        except(TypeError):
            print("请输入数字")

    def search(self,pos):
        try:
            result=pos%1
            #异常链路
            if result!=0:
                print("请输入整数")
            else:
                if pos<0:
                    print("暂时不支持负数")
                elif pos>self.length():
                    print("您越界了")
                else:
            #正常链路
                    pointer = self.head
                    count = 0
                    while pointer!=None:
                        if count==pos:
                            print(pointer.elem)
                            break
                        else:
                            count+=1
                            pointer=pointer.next
        except(TypeError):
            print("请输入数字")

if __name__=='__main__':
    list=listNodeHandle()
    length=str(list.length())
    list.travel()
    list.isEmpty()
    print('———————测试头插———————————')
    list.add(1)#测试头插
    list.add(2)
    list.add(3)
    list.travel()
    length=str(list.length())
    print('————————测试尾插——————————')
    list.append(1)#测试尾插
    list.travel()
    length=str(list.length())
    print('————————测试中间插——————————')
    list.insert(0,3)#测试中间插
    list.travel()
    length=str(list.length())
    print('————————测试根据元素删除——————————')
    list.remove(3)#测试根据元素删除
    list.travel()
    length=str(list.length())
    print('———————测试根据下标删除———————————')
    list.delNew(1)#测试根据下标删除
    list.travel()
    length=str(list.length())
    print('————————测试删除最后元素——————————')
    list.pop()#测试删除最后元素
    list.travel()
    length=str(list.length())
    print('————————测试更新——————————')
    list.update(1,1)#测试更新
    list.travel()
    length=str(list.length())
    print('———————测试根据元素查询———————————')
    list.find(1)#测试根据元素查询
    list.travel()
    length=str(list.length())
    print('————————测试根据下标查询——————————')
    list.search(1)#测试根据下标查询
    list.travel()
    length=str(list.length())
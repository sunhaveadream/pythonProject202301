class Node:
    def __init__(self,data):
        # 初始化链表的节点
        self.data=data
        self.next=None

class List:
    def __init__(self,node=None):
        # 初始化链表，即空链
        self.head=None

    def isEmpty(self):
        if self.head==None:
            return True
        else:
            return False

    def travelList(self):
        p = self.head
        if p==None:
            print('此为空链表')
        else:
            while p!=None:
                print(p.data)
                p=p.next

    def listLength(self):
        # 计算链表的长度，设置一个临时变量指针指向头节点
        count=0
        p = self.head
        if p==None:
            # 当头节点指向空，说明为空链表，长度为0；
            return 0
        else:
            while p!=None:
                # 当后继节点不指向空，说明链表还未遍历完成，继续遍历
                count+=1
                p=p.next
            # 当后继节点指向空，说明已经到了链表的尾节点，停止遍历，计算长度
            return count

    def myAdd(self,item):
        # 头插法，将新节点的next指向原来的头节点，将head指向新节点
        try:
            result = item % 1
            if result != 0:
                print("请输入整数")
            else:
                node = Node(item)
                node.next=self.head
                self.head=node
        except(TypeError):
            print("请输入数字")

    def myAppend(self,item):
        # 尾插法，遍历链表，将尾节点的next指向新节点，新节点的next指向空
        try:
            result = item % 1
            if result != 0:
                print("请输入整数")
            else:
                node=Node(item)
                if self.head==None:
                    # 如果链表头节点为空，说明为空链表，此时尾部插入等同于头部插入
                    self.head=node
                else:
                    # 如果链表头节点不为空，说明不为空链表，进行遍历，遍历到尾节点的next为空停止
                    p = self.head
                    while p.next!=None:
                        p=p.next
                    # 遍历完成，找到尾节点，将尾节点的next指向新节点，新节点的next因为构造Node的时候，next指向空，所以这里不用重复写
                    p.next=node
        except(TypeError):
            print("请输入数字")

    def myInsert(self,pos,item):
        # 中间位置插入，遍历链表，找到要插入的位置，把新节点的next指向要插入的位置的后继节点，将要插入位置的前驱节点指向新节点
        try:
            result = pos%1
            result1 = item%1
            if result!=0:
                # 要插入的位置即索引应该为整数，若不是，进行异常提示
                print("pos请输入整数")
            elif result1!=0:
                print("item请输入整数")
            else:
                node=Node(item)
                if self.head==None:
                    # 当链表为空，此时插入任意位置等同于头插法
                    self.myAdd(item)
                else:
                    if pos<=0:
                        # 当要插入的位置小于等于0时，等同于头插法
                        self.myAdd(item)
                    elif pos>self.listLength()-1:
                        # 当要插入的位置大于长度时，等同于尾插法
                        self.myAppend(item)
                    else:
                        p=self.head
                        count=0
                        while count<pos-1:
                            count+=1
                            p=p.next
                        node.next=p.next
                        p.next=node
        except(TypeError):
            print("请输入数字")

    def myFind(self,item):
        # 查找数据，遍历链表，当链表中节点的data等于要查找的item时，返回True，否则返回False
        try:
            result = item % 1
            if result != 0:
                print("请输入整数")
            else:
                p=self.head
                if p==None:
                    # 当头节点为空说明为空链表，说明找不到，返回False
                    return False
                else:
                    while p.next!=None:
                        # 当遍历中的data等于要查找的data，返回True
                        if p.data==item:
                            return True
                        else:
                            p=p.next
                    # 遍历到尾节点还未找到，说明找不到，返回False
                    return False
        except(TypeError):
            print("请输入数字")

    def mySearch(self,pos):
        # 查找对应位置的值，因为链表是非连续的，所以需要遍历
        # 判断异常情况，返回对应提示
        try:
            result=pos%1
            if result!=0:
                print("您输入的不是整数")
            else:
                if pos<0:
                    print("暂不支持负数")
                elif pos>self.listLength():
                    print("越界了")
                else:
                    # 参数正常，开始处理逻辑
                    count=0
                    p=self.head
                    while p!=None:
                        if count==pos:
                            print(p.data)
                            break
                        else:
                            count += 1
                            p=p.next
        except(TypeError):
            print("请输入数字")

    def myRemove(self,item):
        # 判断异常情况，返回对应提示
        try:
            if self.head==None:
                print("您输入的item不在链表中")
            # 删除头部，将head指向原来头部的下一个节点
            else:
                p=self.head
                if p.data==item:
                    self.head=p.next
            # 删除其他位置，遍历链表，将要删除的位置的前驱节点直接指向要删除位置的后继节点
                else:
                    while p.next!=None:
                        if p.next.data==item:
                            p=p.next.next
                        else:
                            p=p.next
                    print("您输入的item不在链表中")
        except(TypeError):
            print("请输入数字")

    def myDel(self,pos):
        # 异常返回对应提示
        try:
            result=pos%1
            p = self.head
            if result!=0:
                print("请输入整数")
            elif p == None:
                print("这是空链表")
            else:
                if pos<0:
                    print("暂时不支持负数")
                elif pos>self.listLength():
                    print("越界了")
                else:
                    # 参数正常开始代码逻辑
                    count=0
                    while count<pos-1:
                        count+=1
                        p=p.next
                    p.next=p.next.next
        except(TypeError):
            print("请输入数字")

    def myPop(self):
        # 异常返回对应提示
        p=self.head
        if p==None:
            print("此为空链表")
        else:
            # 当链表只有1个元素，那就将头节点指向空
            if p.next==None:
                p=None
            else:
                # 当链表不止1个元素，那就将尾节点的前驱节点直接指向空
                while p.next.next!=None:
                    p=p.next
                p.next=None

    def myUpdate(self,pos,item):
        # 遍历链表找到对应的pos，修改pos对应的data
        # 先判断异常情况
        try:
            result=pos%1
            result1=item%1
            if result!=0:
                print("pos请输入整数")
            elif result1!=0:
                print("item请输入整数")
            else:
                p = self.head
                if p==None:
                    print("链表为空，无法修改")
                elif pos>self.listLength():
                    print("您输入的位置越界了")
                else:
                    count = 0
                    while count != pos-1:
                        count+=1
                        p = p.next
                    p.data = item
        except(TypeError):
            print("请输入数字")

if __name__=='__main__':
    print('<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>')
    print('———实例化链表———')
    list=List()
    length=str(list.listLength())
    print("此时长度为"+length)
    print('———测试遍历空链表———')
    list.travelList()
    print('———测试判断是否为空———')
    print(list.isEmpty())
    print('<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>')
    print('———测试头插法———')
    # 异常链路
    list.myAdd('测试')#输入非数字
    # 正常链路
    list.myAdd(2)
    list.myAdd(1)
    list.myAdd(5)
    length=str(list.listLength())
    print("进行头插法操作后此时长度为"+length)
    print('———头插法后遍历链表———')
    list.travelList()
    print('<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>')
    print('———测试尾插法———')
    # 异常链路
    list.myAppend('测试')#输入非数字
    # 正常链路
    list.myAppend(1)
    length = str(list.listLength())
    print("进行尾插法操作后此时长度为" + length)
    print('———尾插法后遍历链表———')
    list.travelList()
    print('<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>')
    print('———测试中间位置插入———')
    # 异常链路
    list.myInsert('测试',1)#pos输入非数字
    list.myInsert(1,'测试')#item输入非数字
    list.myInsert(1.5,2)#输入的pos不是整数
    list.myInsert(2,1.5)#输入的item不是整数
    # 正常链路
    list.myInsert(0, 1)
    length = str(list.listLength())
    print("进行中间位置插入操作后此时长度为" + length)
    print('———中间位置插入后遍历链表———')
    list.travelList()
    print('<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>')
    print('———测试查找数据———')
    print('———查询前遍历链表———')
    list.travelList()
    # 异常链路
    list.myFind('测试')  # 输入非数字
    print('是否有找到，输入不存在的测试——>' + str(list.myFind(9)))# 输入不在链表内的数字
    # 正常链路
    print('是否有找到，输入存在的测试——>' + str(list.myFind(1)))
    print('———查询后遍历链表———')
    list.travelList()
    print('<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>')
    print('———测试查找索引对应数据———')
    print('———查询前遍历链表———')
    list.travelList()
    # 异常链路
    list.mySearch('测试')# 非数字
    list.mySearch(-1)# 负数
    list.mySearch(9)# 越界
    list.mySearch(1.5)# 非整数
    # 正常链路
    list.mySearch(2)
    print('<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>')
    print('———测试删除数据———')
    # 异常链路
    list.myRemove(-1)#输入不在链表的数据
    # 正常链路
    list.myRemove(1)
    length = str(list.listLength())
    print("进行删除操作后此时长度为" + length)
    print('———删除后遍历链表———')
    list.travelList()
    print('<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>')
    print('———测试删除索引对应位置的数据———')
    # 异常链路
    list.myDel('测试')# 非数字
    list.myDel(1.5)# 非整数
    list.myDel(9)# 越界
    # 正常链路
    list.myDel(1)
    length = str(list.listLength())
    print("进行删除索引对应数据的操作后此时长度为" + length)
    print('———删除后遍历链表———')
    list.travelList()
    print('<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>')
    print('———测试删除最后一个位置———')
    list.myPop()
    length = str(list.listLength())
    print("进行删除索引对应数据的操作后此时长度为" + length)
    print('———删除最后一个位置后遍历链表———')
    list.travelList()
    print('<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>')
    print('———测试更新数据———')
    # 异常链路
    list.myUpdate('测试', 1)#pos输入非数字
    list.myUpdate(1,'测试')#item输入非数字
    list.myUpdate(1.5, 9)#输入的pos不是整数
    list.myUpdate(1,1.5)# 输入的item不是整数
    list.myUpdate(9, 9)#越界
    # 正常链路
    list.myUpdate(1,9)
    length = str(list.listLength())
    print("进行更新操作后此时长度为" + length)
    print('———更新后遍历链表———')
    list.travelList()



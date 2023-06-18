class MaxHeap:
    def __init__(self):
        self.__heap = [0]
        self.__size = 0

    def __swapUp(self, i):#子节点若大于父节点，则进行交换
        try:
            tem = self.__heap[i]
            while i // 2 > 0:
                if self.__heap[i] > self.__heap[i // 2]:
                    self.__heap[i] = self.__heap[i // 2]
                    self.__heap[i // 2] = tem
                i //= 2
        except(TypeError):
            print("请检查输入")

    def __swapDown(self, i):#父节点若小于子节点，则进行交换
        try:
            while self.__size >= 2 * i:
                if 2 * i + 1 > self.__size:
                    bigger_child = 2 * i
                else:
                    if self.__heap[2 * i] > self.__heap[2 * i + 1]:
                        bigger_child = 2 * i
                    else:
                        bigger_child = 2 * i + 1
                tem = self.__heap[i]
                if self.__heap[i] < self.__heap[bigger_child]:
                    self.__heap[i] = self.__heap[bigger_child]
                    self.__heap[bigger_child] = tem
                i = bigger_child
        except(TypeError):
            print("请检查输入")

    def insert(self, value):#插入到最后一个节点，不断进行比较堆化
        try:
            self.__heap.append(value)
            self.__size += 1
            self.__swapUp(self.__size)
        except(TypeError):
            print("请检查输入")

    def pop(self):#删除第一个节点，不断进行比较堆化
        max_value = self.__heap[1]
        self.__heap[1] = self.__heap[self.__size]
        self.__size -= 1
        self.__heap.pop()
        self.__swapDown(1)
        return max_value

    def update(self, key,value):#若小于子节点，则进行比较下沉；若大于父节点，则进行比较上升
        try:
            self.__heap[key]=value
            for i in range(1,key+1):
                if self.__heap[i//2] > self.__heap[i]:
                    self.__swapDown(i)
                    i+=1
                if self.__heap[i] > self.__heap[i // 2]:
                    self.__swapUp(i)
                    i+=1
        except(TypeError):
            print("请检查输入")

    @property
    def get_list(self):
        return self.__heap[1:]

    def __len__(self):
        return self.__size


if __name__ == "__main__":
    maxHeap = MaxHeap()
    print("——————正常链路——————")
    print("增加/插入")
    maxHeap.insert(100)
    maxHeap.insert(5)
    maxHeap.insert(10)
    maxHeap.insert(15)
    print(maxHeap.get_list)
    print(len(maxHeap))
    print("更新比父节点大的")
    print(maxHeap.update(2,150))
    print(maxHeap.get_list)
    maxHeap.insert(50)
    print("更新比父节点小的")
    print(maxHeap.update(2,8))
    print(maxHeap.get_list)
    print("删除")
    print(maxHeap.pop())
    print(maxHeap.pop())
    print(maxHeap.get_list)
    print("——————异常链路——————")
    maxHeap.insert('test')
    maxHeap.update(2,'test')

class MaxHeap:
    def __init__(self):
        self.__heap = [0]
        self.__size = 0

    def __swap_up(self, i):
        try:
            # 当父结点不为空时，进行比较，如果大于父结点，进行交换上升
            tem = self.__heap[i]
            while i // 2 > 0:
                if self.__heap[i] > self.__heap[i // 2]:
                    self.__heap[i] = self.__heap[i // 2]
                    self.__heap[i // 2] = tem
                i //= 2
        except(TypeError):
            print("请检查输入")

    def __swap_down(self, i):
        try:
            # 比较子结点，如果比子节点小，进行交换下沉
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

    def insert(self, value):
        try:
            # 插入在末尾最后一个结点，不断进行比较上升
            self.__heap.append(value)
            self.__size += 1
            self.__swap_up(self.__size)
        except(TypeError):
            print("请检查输入")

    def pop(self):
        # 删除最大的结点，删除后不断进行比较下沉
        max_value = self.__heap[1]
        self.__heap[1] = self.__heap[self.__size]
        self.__size -= 1
        self.__heap.pop()
        self.__swap_down(1)
        return max_value

    def update(self, key,value):
        try:
            # 插入在末尾最后一个结点，不断进行比较上升
            self.__heap[key]=value
            for i in range(1,key+1):
                if self.__heap[i//2] > self.__heap[i]:
                    self.__swap_down(i)
                    i+=1
                if self.__heap[i] > self.__heap[i // 2]:
                    self.__swap_up(i)
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
    print("<<<<<<<<<测试获取堆>>>>>>>>>")
    print(maxHeap.get_list)
    print("<<<<<<<<<测试插入堆>>>>>>>>>")
    maxHeap.insert(90)
    maxHeap.insert(10)
    maxHeap.insert(20)
    maxHeap.insert(30)
    print("<<<<<<<<<插入后获取堆>>>>>>>>>")
    print(maxHeap.get_list)
    print("<<<<<<<<<插入后获取堆的长度>>>>>>>>>")
    print(len(maxHeap))
    print("<<<<<<<<<测试更新大于父结点的>>>>>>>>>")
    print(maxHeap.update(2,100))
    print("<<<<<<<<<更新后获取堆>>>>>>>>>")
    print(maxHeap.get_list)
    maxHeap.insert(50)
    print("<<<<<<<<<测试更新小于子结点的>>>>>>>>>")
    print(maxHeap.update(2,9))
    print("<<<<<<<<<更新后获取堆>>>>>>>>>")
    print(maxHeap.get_list)
    print("<<<<<<<<<测试删除>>>>>>>>>")
    print(maxHeap.pop())
    print(maxHeap.pop())
    print("<<<<<<<<<删除后获取堆>>>>>>>>>")
    print(maxHeap.get_list)
    print("<<<<<<<<<异常链路>>>>>>>>>")
    maxHeap.insert('test')


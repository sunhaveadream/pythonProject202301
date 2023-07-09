class MySort:
    def bubbleSort(self,array):
        """冒泡排序"""
        for i in range(len(array)-1,0,-1):
            for j in range(0,i):
                if array[j]>array[j+1]:
                    array[j],array[j+1]=array[j+1],array[j]
        return array

    def insertSort(self,array):
        """插入排序"""
        for i in range(1,len(array)):
            currentNum=array[i]
            index=i
            while array[index-1]>currentNum and index>0:
                array[index]=array[index-1]
                index=index-1
            array[index]=currentNum
        return array

    def mergeSort(self,array):
        """归并排序"""
        length=len(array)
        if length==1:
            return array
        left=self.mergeSort(array[:len(array)//2])
        right=self.mergeSort(array[len(array)//2:])
        return self.merge(left,right)

    def merge(self,left,right):
        leftIndex,rightIndex,mergeArray=0,0,list()
        while leftIndex<len(left) and rightIndex<len(right):
            if left[leftIndex]<=right[rightIndex]:
                mergeArray.append(left[leftIndex])
                leftIndex+=1
            else:
                mergeArray.append(right[rightIndex])
                rightIndex+=1
        mergeArray=mergeArray+left[leftIndex:]+right[rightIndex:]
        return mergeArray

    def quickSort(self,array,start,end):
        """快速排序"""
        if start>=end:
            return
        midNum,left,right=array[start],start,end
        while left<right:
            while left<right and array[right]>=midNum:
                right-=1
            array[left]=array[right]
            while left<right and array[left]<midNum:
                left+=1
            array[left]=array[right]
        array[left]=midNum
        self.quickSort(array,start,left-1)
        self.quickSort(array,left+1,end)
        return array


if __name__ == "__main__":
    ms=MySort()
    myArrary=[5,1,9,6,3,7,12]
    print(ms.bubbleSort(myArrary))
    print(ms.insertSort(myArrary))
    print(ms.mergeSort(myArrary))
    print(ms.quickSort(myArrary,0,len(myArrary)-1))


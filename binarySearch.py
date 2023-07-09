class BinarySearch:
    def binarySearch(self,list,left,right,num):
        """当前假设数组已排序"""
        if(left>right):
            return None
        midIndex = int((left+right)/2)
        midNum=list[midIndex]
        if midNum==num:
            return midIndex
        if num>midNum:
            return self.binarySearch(list,midIndex+1,right,num)
        return self.binarySearch(list,left,midIndex+1,num)


if __name__ == "__main__":
    bs=BinarySearch()
    list=[1,5,9,10,11,15,17,20,21,30]
    print(bs.binarySearch(list,0,9,21))


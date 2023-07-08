class Search:
    def sequentialSearch(self,list,item):
        pos=0
        flag=False
        while pos<len(list) and not flag:
            if list[pos]==item:
                flag=True
            else:
                pos+=1
        return flag


if __name__ == "__main__":
    list=[1,3,6,9,11,13]
    search=Search()
    print("————————————正常链路————————————")
    print(search.sequentialSearch(list,1))
    print("————————————异常链路————————————")
    print(search.sequentialSearch(list,99))

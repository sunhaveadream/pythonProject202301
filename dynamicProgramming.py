class DynamicProgramming:
    def fibonacciSequence(self, n):
        """
        斐波那契数列：0，1，1，2，3，5，8，13，21，34，55，89，144，233.....
        规律为：当前值为前两个值的和
        求第N个数的值为多少？
        """
        results = list(range(n+1))
        for i in range(n+1):
            if i < 2:
                results[i] = i
            else:
                results[i] = results[i-1]+results[i-2]
        print(results[-1])


if __name__ == "__main__":
    dp = DynamicProgramming()
    dp.fibonacciSequence(7)

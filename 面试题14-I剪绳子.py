# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m] 。
# 请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
# 数学推导的方式
class Solution_1:
    def cuttingRope(self, n: int) -> int:
        if n <= 3:
            return n - 1
        else:
            a = n // 3
            b = n % 3
            if b == 0:
                return 3 ** a
            elif b == 1:
                return 3 ** (a-1) * 4
            elif b == 2:
                return 3 ** a * 2


# 暴力递归解法，这里需要注意的是分为i和n-i之后，绳子可以继续分或者不分了，所以max里面有三个元素
# 时间复杂的O(n**2)，空间复杂的O(n**2)
class Solution_2():
    def cuttingRope(self, n):
        if n == 2:
            return 1
        result = 0
        for i in range(1, n):
            result = max(result, i * self.cuttingRope(n - i), i * (n - i))
        return result


# 使用记忆法，记录递归的时候已经计算过的值，避免重复计算
# 这里时间复杂的依然是O(n**2)，空间复杂度为O(n)
class Solution_3(object):
    def cuttingRope(self, n):
        def memoize(n):
            if n == 2:
                return 1
            # 该n对应的值已经计算过了，直接返回
            if f[n] != 0:
                return f[n]
            tmp = -1
            # 进行递归操作
            for i in range(1, n):
                tmp = max(tmp, i * (n - i), i * memoize(n - i))
            f[n] = tmp
            return tmp
        # 使用数组来记录已经计算的值
        f = [0 for _ in range(n + 1)]
        return memoize(n)


if __name__ == '__main__':
    soulution = Solution_1()
    print(soulution.cuttingRope(10))
    soulution_2 = Solution_2()
    print(soulution_2.cuttingRope(10))
    solution_3 = Solution_3()
    print(solution_3.cuttingRope(10))

# 设一共有f(n)种方法，青蛙最后一次跳可以分为跳1个台阶或者2个台阶。之前的方法就可以分别表示为
# f(n-1)和f(n-2)，f(n) = f(n-1)+f(n-2)这样就化为斐波那契数列的求解，之后的求解就和面试10-1的一样了
# 递归的方式，时间复杂度O(n**2)，空间复杂的O(1)
class Solution_1:
    def numWays(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        else:
            return (self.numWays(n - 1) + self.numWays(n - 2)) % 1000000007


# 记忆法，时间复杂度O(n)，空间复杂度O(n)
class Solution_2:
    def numWays(self, n:int) -> int:
        if n == 0 or n == 1:
            return 1
        else:
            tmp = [1, 1]
            for i in range(n + 1)[2:]:
                tmp.append(tmp[i - 1] + tmp[i - 2])
            return tmp[-1] % 1000000007


# 不使用list记录的记忆法，时间复杂度O(n)，空间复杂度O(1)
class Solution_3:
    def numWays(self, n:int) -> int:
        if n == 0 or n == 1:
            return 1
        a = 1
        b = 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007


if __name__ == '__main__':
    solution = Solution_3()
    print(solution.numWays(1000))

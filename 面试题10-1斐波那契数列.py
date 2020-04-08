# https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/
# 递归的方式求斐波那契函数的第n项
# 递归的话会造成大量重复的计算，时间复杂度O(n**2)，空间复杂度O(n)
class Solution_1:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return (self.fib(n - 1) + self.fib(n - 2)) % 1000000007


# 记忆化法，使用一个list记录0-n的结果
# 时间复杂度O(n)，空间复杂度O(n)
class Solution_2:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            test = [0, 1]
            for i in range(n + 1)[2:]:
                test.append(test[i - 1] + test[i - 2])
            return test[-1] % 1000000007


# 不使用list的记忆法，我们只需要关注两个元素，就可以推出第三个元素
# 这里直接使用了交换的方式实现，时间复杂度还是O(n)，空间复杂度却变为O(1)
class Solution_3:
    def fib(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 0:
            return 0
        else:
            a, b = 0, 1
            for _ in range(n):
                a, b = b, a + b
            return a % 1000000007


if __name__ == '__main__':
    solution_2 = Solution_2()
    print(solution_2.fib(99))
    solution_3 = Solution_3()
    print(solution_3.fib(99))

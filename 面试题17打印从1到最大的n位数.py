# https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/
# 输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。
class Solution:
    def printNumbers(self, n: int):
        max_value = 10 ** n
        result = [i for i in range(1, max_value)]
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.printNumbers(3))

# https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
# 这里和面试题12矩阵中的路径使用一样的dfs深度优先算法+修剪枝干法
# 不同的是这里确定从[0,0]开始，所以只需要考虑向左j+1，向下i+1的情况就能全部遍历完毕
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def shuwei_sum(input_num):
            result = 0
            while input_num:
                result += input_num % 10
                input_num = input_num // 10
            return result

        def dfs(i, j, si, sj):
            if i >= m or j >=n or k < 0 or si + sj > k or li[i][j] == 1:
                return 0
            li[i][j] = 1
            return 1 + dfs(i + 1, j, shuwei_sum(i+1), shuwei_sum(j)) + dfs(i, j + 1, shuwei_sum(i), shuwei_sum(j+1))
        li = [[0 for _ in range(n)] for _ in range(m)]
        return dfs(0, 0, 0, 0)


if __name__ == '__main__':
    solution = Solution()
    print(solution.movingCount(2, 3, 1))

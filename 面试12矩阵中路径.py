# https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/
# M,N 分别为矩阵行列大小， KK 为字符串 word 长度。
# 时间复杂度O(3**kMN)，空间复杂度O(k)
# 使用dfs深度优先算法，以及修剪枝干法
class Solution:
    def exist(self, board, word: str) -> bool:
        def dfs(i, j, k):
            # 判断i和j是否越界，越界直接返回false，当board[i][j]不等于word[k]的时候证明这条路径走不通
            # 直接返回false，相当于修剪掉这部分的枝干
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or not 0 <= k < len(word) or board[i][j] != word[k]:
                return False
            # 表明word已经匹配完
            if k == len(word) - 1:
                return True
            # 对board[i][j]置位/，防止后续又走了这个点
            tmp, board[i][j] = board[i][j], '/'
            # 向上下左右搜索
            res = dfs(i + 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j - 1, k + 1)
            # 进行回写操作
            board[i][j] = tmp
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.exist([["a","b"],["c","d"]], "abcd"))

# https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
# 线性查找
# 从右上角开始查找
# 如果target大于一行中最右的元素（最大），row+=1
# 小于的话，可能存在于这一行，col -= 1，找到返回True
# 最后没找到返回False
# 时间复杂度O(n + m)，空间复杂度O(1)
class Solution_1:
    def findNumberIn2DArray(self, matrix, target):
        for i in matrix:
            for j in i[::-1]:
                if target > j:
                    break
                if target == j:
                    return True
        return False


# 暴力解法，速度慢
# 时间复杂度O(nm)，空间复杂度O(1)
class Solution_2:
    def findNumberIn2DArray(self, matrix, target):
        for i in matrix:
            if target in i:
                return True
        return False


if __name__ == '__main__':
    solution_1 = Solution_1()
    test = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    print(solution_1.findNumberIn2DArray(test, target))
    solution_2 = Solution_2()
    print(solution_2.findNumberIn2DArray(test, target))

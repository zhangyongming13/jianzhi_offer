# https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/
# 使用官方函数的方式
class Solution_1:
    def replaceSpace(self, s):
        return s.replace(' ', '%20')


# 一次遍历，得出结果，时间复杂度O(n)，空间复杂度O(n)
class Solution_2:
    def  replaceSapce(self, s):
        result = ''
        for i in s:
            if i == ' ':
                result += '%20'
            else:
                result += i
        return result


if __name__ == '__main__':
    test = 'We are happy.'
    solution_1 = Solution_1()
    print(solution_1.replaceSpace(test))

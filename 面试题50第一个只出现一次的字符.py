class Solution_1:
    def firstUniqChar(self, s: str) -> str:
        for i in s:
            if s.count(i) == 1:
                return i
        return " "


# 使用哈希表的形式，记录每个单词在s中的出现次数，然后遍历dict找到次数为1的并返回，
# 在3.6之后的dict默认是有序的，如果实在3.6之前的需要使用OrderDict有序字典
# 时间复杂度是O(n)，空间复杂度也是O(n)
class Solution_2:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for key, value in dic.items():
            if value == 1:
                return key
        return " "


if __name__ == '__main__':
    solution = Solution_2()
    test = "abaccdeff"
    print(solution.firstUniqChar(test))

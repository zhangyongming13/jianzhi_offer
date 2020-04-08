# https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
# 找出数组中重复的数字
# 哈希表的方式，时间O(n)，空间O(n)
class Solution_1:
    def findRepeatNumber(self, nums):
        test = {}
        for i in nums:
            if i in test:
                return i
            else:
                test[i] = 1

# 先排序，再看相邻的元素之间是否相同，相同则返回，
# 时间复杂度O(nlogn)，空间O(1)，因为需要排序加遍历，所以速度很慢
class Solution_2:
    def findRepeatNumber(self, nums):
        nums.sort()
        tmp = nums[0]
        for i in nums[1:]:
            if i == tmp:
                return i
            else:
                tmp = i


# 鸽巢原理，将下标与元素的值一一对应，如果原本就对应好的，就不处理，如果原本i != nums[i]，就进行鸽子回巢处理
# 如果发现已经有了的话，就判定为重复，这种方法时间复杂度O(n)，空间复杂度O(1)
class Solution_3:
    def findRepeatNumber(self, nums):
        length = len(nums)
        for i in range(length):
            while i != nums[i]:
                # 判断巢穴是不是被一样的鸽子占领了
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    tmp = nums[i]
                    nums[i], nums[tmp] = nums[tmp], nums[i]


if __name__ == '__main__':
    test = [8, 9, 7, 2, 2, 1]
    solution_1 = Solution_1()
    print(solution_1.findRepeatNumber(test))
    solution_2 = Solution_2()
    print(solution_2.findRepeatNumber(test))
    solution_3 = Solution_3()
    print(solution_3.findRepeatNumber(test))

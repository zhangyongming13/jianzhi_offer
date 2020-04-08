# 输入可能是经过旋转之后的列表，所以先遍历列表遇到第一个减小的元素，这个就是我们要找的最小值
# 如果遍历完整个数组还是没找到减少的，那就说明没有旋转，列表第一个值就是最小值
class Solution_1:
    def minArray(self, numbers) -> int:
        for i in numbers[1:]:
            if i < numbers[0]:
                return i
        return numbers[0]


# 不考虑什么旋转数组，直接使用内置函数求出列表最小的值
class Solution_2:
    def minArray(self, numbers) -> int:
        return min(numbers)


# 二分查找法
class Solution_3:
    def minArray(self, numbers):
        i, j = 0, len(numbers) - 1
        while i < j:
            mid = (i + j) // 2
            # 表示在列表的下半区，因为要找最小的，mid可以跳过
            if numbers[mid] > numbers[j]:
                i = mid + 1
            # 表示在列表的上班区
            elif numbers[mid] < numbers[j]:
                j = mid
            # 相等的话那就没办法确认在那个半区（和正常的二分查找发不太一样）
            # 使j减1，继续查找
            else:
                j -= 1
        return numbers[i]


if __name__ == '__main__':
    test = [1, 1]
    solution = Solution_3()
    print(solution.minArray(test))

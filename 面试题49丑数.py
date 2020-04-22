# https://leetcode-cn.com/problems/chou-shu-lcof/
# 根据题意可以知道除了第一个丑数1之外都是*2 *3 *5得出的
# test[n] = min(test[a], test[b], test[c])，abc的初始值就是0对应丑数1，每次匹配的上
# abc一个或者多个就 + 1
class Solution_1:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        uglyNumber, a, b, c = [1], 0, 0, 0
        for _ in range(1, n):
            tmp = min(uglyNumber[a] * 2, uglyNumber[b] * 3, uglyNumber[c] * 5)
            uglyNumber.append(tmp)
            # 这里需要注意的是abc都可能匹配的上，所以都要判断是不是+1
            if tmp == uglyNumber[a] * 2:
                a += 1
            if tmp == uglyNumber[b] * 3:
                b += 1
            if tmp == uglyNumber[c] * 5:
                c += 1
        return uglyNumber[-1]


if __name__ == '__main__':
    n = 7
    solution = Solution_1()
    print(solution.nthUglyNumber(n))

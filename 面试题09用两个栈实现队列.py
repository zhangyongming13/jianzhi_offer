# https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/
from collections import deque


# 这里使用双向队列deque代替list，降低时间复杂度。
# 因为进行先进先出操作的时候list的，pop第一个元素的时候时间复杂度为O(n)
# 而deque则是O(1)
class CQueue:

    def __init__(self):
        self.test = deque()

    def appendTail(self, value: int) -> None:
        self.test.append(value)

    def deleteHead(self) -> int:
        if len(self.test) == 0:
            return -1
        else:
            return self.test.popleft()


# 用两个栈（python中用list取代）模拟队列。队列的特性就是FIFO先进先出。
# 这里的操作就是所有的append操作都是加到test_1中。进行出队伍的时候先检查test_2是否为空
# 不为空，则从test_2中进行pop操作。为空，则将test_1的元素pop，然后append进test_2.这样就能确保FIFO
# 时间复杂度O(1)，空间复杂度O(N)
class CQueue_1:

    def __init__(self):
        self.test_1 = []
        self.test_2 = []

    def appendTail(self, value: int) -> None:
        self.test_1.append(value)

    def deleteHead(self) -> int:
        # 先检查test_2是否为空
        if self.test_2:
            # 不为空，则从test_2中进行pop操作
            return self.test_2.pop(-1)
        else:
            # 为空，则将test_1的元素pop，然后append进test_2.这样就能确保FIFO
            while self.test_1:
                self.test_2.append(self.test_1.pop(-1))
            if self.test_2:
                return self.test_2.pop(-1)
            # 都没有元素的，返回-1
            else:
                return -1


if __name__ == '__main__':
    cqueue = CQueue_1()
    cqueue.appendTail(3)
    print(cqueue.deleteHead())
    print(cqueue.deleteHead())

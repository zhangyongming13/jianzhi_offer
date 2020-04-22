# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 这里的做法是先求出链表总长度，然后算出倒数第k个链表属于正数第几个，进行遍历得出结果
# 时间复杂度应该是O(n)，空间复杂度是O(1)
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        """
        返回链表中倒数第k个链表
        :param head:
        :param k:
        :return:
        """
        length = 0
        tmp = head
        while tmp:
            length += 1
            tmp = tmp.next
        result = head
        num = 1
        while num != length - k + 1:
            num += 1
            result = result.next
        return result


# 使用双指针的方式，首先former和latter都指向head，former先走k步。然后former和latter一起行动
# 直到former指向None（跑完整个链表），这个时候latter指向的就是链表倒数第k个，返回latter即可
# 时间复杂度O（n），空间复杂度O（1）
class Solution_1:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        """
        返回链表中倒数第k个链表
        :param head:
        :param k:
        :return:
        """
        former, latter = head, head
        while k:
            former = former.next
            k -= 1
        while former:
            latter = latter.next
            former = former.next
        return latter


if __name__ == "__main__":
    list_node_1 = ListNode(1)
    list_node_2 = ListNode(2)
    list_node_3 = ListNode(3)
    list_node_4 = ListNode(4)
    list_node_5 = ListNode(5)
    list_node_1.next = list_node_2
    list_node_2.next = list_node_3
    list_node_3.next = list_node_4
    list_node_4.next = list_node_5
    k = 2
    solution = Solution_1()
    result = solution.getKthFromEnd(list_node_1, k)
    print(result.val)

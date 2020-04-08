# 给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
# 返回删除后的链表的头节点。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        else:
            tmp = head
            while tmp:
                if not tmp.next:
                    break
                if tmp.next.val == val:
                    zhang = tmp.next.next
                    tmp.next = zhang
                    break
                tmp = tmp.next
        return head


if __name__ == '__main__':
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    node_1 = ListNode(1)
    node_9 = ListNode(9)
    node_4.next = node_5
    node_5.next = node_1
    node_1.next = node_9
    solution = Solution()
    node = solution.deleteNode(node_4, 5)
    while node:
        print(node.val, end=' ')
        node = node.next

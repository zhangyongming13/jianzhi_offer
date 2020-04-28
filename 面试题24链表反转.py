# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        将输入的链表进行一个反转的操作，然后返回反转之后的链表的头节点，主要思想是先遍历整个链表
        然后将节点存入list。之后从尾到头取出链接起来。这样就完成了链表的反转。
        相当于使用栈的思想，先进后出。
        空间复杂度O(n)，时间复杂度O(n)
        :param: head:需要反转的链表的头结点
        :return :反转之后的链表的头结点
        """
        if head: # 判断输入的头结点是否为None
            tmp = []
            tmpNode = head
            # 遍历整个链表，存入list
            while tmpNode:
                tmp.append(tmpNode)
                tmpNode = tmpNode.next
            resultNode = tmp.pop()
            tmpNode = resultNode
            while tmp:
                tmpNode.next = tmp.pop()
                tmpNode = tmpNode.next
            tmpNode.next = None
            return resultNode
        else:
            return None


class Solution_1:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        使用双指针的形式进行链表的反转，从链表头开始进行反转，一部分一部分的反转，直到第一个指针指向
        None，这样时间复杂度是O(n)，空间复杂度是O(1)
        :param: head:需要反转的链表的头结点
        :return :反转之后的链表的头结点
        """
        node1, node2 = head, None
        while node1:
            tmp = node1.next
            node1.next = node2
            node2 = node1
            node1 = tmp
        return node2


if __name__ == "__main__":
    listNode1 = ListNode(1)
    listNode2 = ListNode(2)
    listNode3 = ListNode(3)
    listNode4 = ListNode(4)
    listNode5 = ListNode(5)
    listNode1.next = listNode2
    listNode2.next = listNode3
    listNode3.next = listNode4
    listNode4.next = listNode5
    listNode5.next = None
    print("反转前的链表：")
    tmp = listNode1
    while tmp:
        print(tmp.val, end=' ')
        tmp = tmp.next
    solution = Solution_1()
    reversedListNode = solution.reverseList(listNode1)
    print("\n反转之后的链表：")
    while reversedListNode:
        print(reversedListNode.val, end=' ')
        reversedListNode = reversedListNode.next

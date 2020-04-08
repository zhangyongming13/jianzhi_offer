# 使用list保存从头到尾的链表的值，最后做一个反转的操作
class Solution_1:
    def reversePrint(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        result = result[::-1]
        return result


# 递归的方式，直到链表的next为None，时间复杂度是O(n)，空间复杂度为O(n)
class Solution_2:
    def reversePrint(self, head):
        if head:
            return self.reversePrint(head.next) + [head.val]
        else:
            return []

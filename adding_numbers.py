class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        total = carry = 0
        dummy_node = ListNode()
        current_node = dummy_node
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1.next
            if l2:
                total += l2.val
                l2.next
            carry = total // 10
            total %= 10
            current_node = ListNode(total)
            current_node.next
        return dummy_node.next
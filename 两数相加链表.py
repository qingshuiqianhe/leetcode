# coding:utf-8


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        res = n = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            carry, val = divmod(carry, 10)  # 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组
            n.next = n = ListNode(val)
        return res.next


if __name__ == "__main__":
    t1 = ListNode(3)
    t2 = ListNode(4)
    t2.next = t1
    t3 = ListNode(2)
    t3.next = t2

    b1 = ListNode(4)
    b2 = ListNode(6)
    b2.next = b1
    b3 = ListNode(5)
    b3.next = b2

    result = Solution()

    add_sum = result.addTwoNumbers(t3, b3)

    while (add_sum != None):
        print (add_sum.val)
        add_sum = add_sum.next


class ListNode(object):
    def __init__(self):
        self.val = None
        self.next = None


class ListNode_hadnle:
    def __init__(self):
        self.cur_node = None

    def add(self, data):
        node = ListNode()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node

    def _reverse(self, nodelist):
        list = []
        while nodelist: list.append(nodelist.val)
        nodelist = nodelist.next
        result = ListNode()
        result_handle = ListNode_hadnle()
        for i in list:
            result = result_handle.add(i)
        return result





class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


if __name__ == "__main__":
    link1 = ListNode(3)

    print link1.val


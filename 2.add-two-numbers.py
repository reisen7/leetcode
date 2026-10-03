#
# @lc app=leetcode.cn id=2 lang=python
# @lcpr version=30204
#
# [2] 两数相加
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)  # 虚拟头节点
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10  # 进位
            cur.next = ListNode(total % 10)  # 当前位
            cur = cur.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


# @lc code=end


#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#

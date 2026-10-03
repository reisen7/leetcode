#
# @lc app=leetcode.cn id=1111 lang=python
# @lcpr version=30204
#
# [1111] 有效括号的嵌套深度
#


# @lc code=start
class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        depth = 0
        result = []
        for char in seq:
            if char == "(":
                depth += 1
                result.append(0 if depth % 2 == 1 else 1)
                print(1 % 2)
            elif char == ")":
                result.append(0 if depth % 2 == 1 else 1)
                depth -= 1
        return result


# @lc code=end


#
# @lcpr case=start
# "(()())"\n
# @lcpr case=end

# @lcpr case=start
# "()(())()"\n
# @lcpr case=end

#

#
# @lc app=leetcode.cn id=20 lang=python
# @lcpr version=30204
#
# [20] 有效的括号
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []

        mapping = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for i, val in enumerate(s):
            if val in "([{":
                stack.append(val)
            else:
                if not stack:
                    return False

                if stack[-1] != mapping[val]:
                    return False

                stack.pop()

        return not stack


# @lc code=end


#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

# @lcpr case=start
# "([)]"\n
# @lcpr case=end

#

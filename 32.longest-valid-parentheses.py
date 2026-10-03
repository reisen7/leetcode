#
# @lc app=leetcode.cn id=32 lang=python3
# @lcpr version=30204
#
# [32] 最长有效括号
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # 先放一个 -1 作为边界
        ans = 0

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:  # ch == ')'
                stack.pop()

                if not stack:
                    # 当前 ')' 没有匹配的左括号，把它当作新的起点边界
                    stack.append(i)
                else:
                    # 当前有效长度 = 当前位置 i - 栈顶下标
                    ans = max(ans, i - stack[-1])

        return ans


# @lc code=end


#
# @lcpr case=start
# "(()"\n
# @lcpr case=end

# @lcpr case=start
# ")()())"\n
# @lcpr case=end

# @lcpr case=start
# ""\n
# @lcpr case=end

#

# @lcpr case=start
# "(())"\n
# @lcpr case=end

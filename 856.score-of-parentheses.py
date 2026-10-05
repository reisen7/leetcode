#
# @lc app=leetcode.cn id=856 lang=python3
# @lcpr version=30204
#
# [856] 括号的分数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        result = 0
        length = 0

        # 只计算左括号的深度，根据深度算 2 的平方即是分数
        for c in s:
            if c == '(':
                stack.append(0)
                length += 1
            elif c == ')':

                if stack[-1] == 0:
                    if length == 1:
                        result += 1
                    else:
                        result +=  2 ** (length - 1)
                    
                    stack.append(1)
                    
                length -= 1
        
        return result

# @lc code=end



#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "(())"\n
# @lcpr case=end

# @lcpr case=start
# "()()"\n
# @lcpr case=end

# @lcpr case=start
# "(()(()))"\n
# @lcpr case=end

#


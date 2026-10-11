#
# @lc app=leetcode.cn id=921 lang=python3
# @lcpr version=30204
#
# [921] 使括号有效的最少添加
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        stack = []

        length = 0
        for c in s:
            if c == '(':
                stack.append(c)
            else:

                if len(stack) == 0:
                    length += 1
                    
                else:
                    stack.pop()
                

        
        return len(stack)+ length
# @lc code=end



#
# @lcpr case=start
# "())"\n
# @lcpr case=end

# @lcpr case=start
# "((("\n
# @lcpr case=end

#


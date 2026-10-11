#
# @lc app=leetcode.cn id=301 lang=python3
# @lcpr version=30204
#
# [301] 删除无效的括号
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        def is_valid(string):
            cnt = 0
            for ch in string:
                if ch == '(':
                    cnt += 1
                elif ch == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0
        
        left_rem = right_rem = 0
        for ch in s:
            if ch == '(':
                left_rem += 1
            elif ch == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1
        max_depth = left_rem + right_rem

        level = {s}
        depth = 0

        while level and depth <= max_depth:
            valid = [x for x in level if is_valid(x)]
            if valid:
                return valid

            next_level = set()
            for string in level:
                for i in range(len(string)):
                    if string[i] in '()':
                        next_level.add(string[:i] + string[i+1:])
            level = next_level
            depth += 1

        return [""]
        






# @lc code=end



#
# @lcpr case=start
# "()())()"\n
# @lcpr case=end

# @lcpr case=start
# "(a)())()"\n
# @lcpr case=end

# @lcpr case=start
# ")("\n
# @lcpr case=end

#


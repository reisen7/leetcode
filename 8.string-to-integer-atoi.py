#
# @lc app=leetcode.cn id=8 lang=python3
# @lcpr version=30204
#
# [8] 字符串转换整数 (atoi)
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:

        INT_MIN = -2**31      # -2147483648
        INT_MAX = 2**31 - 1   # 2147483647

        stack = []
        for x in s:
            if not stack :

                if x == ' ':
                    continue
                if x == '-':
                    stack.append(x)
                    continue
                if x == '+':
                    stack.append(x)
                    continue
                if ord(x) <= 57 and ord(x) >= 48:
                    stack.append(x)
                if ord(x) > 57 or ord(x) < 48:
                    return 0
                
            else:
                if ord(x) <= 57 and ord(x) >= 48:
                    stack.append(x)
                elif ord(x) > 57 or ord(x) < 48 :
                    break
                elif x == '-':
                    break
                elif x == '+':
                    break

        if not stack or stack == ['-'] or stack == ['+']:
            return 0
        
        str = "".join(stack)

        num = int(str)
        if num > INT_MAX:
            num = INT_MAX
        elif num < INT_MIN:
            num = INT_MIN
        return num
# @lc code=end



#
# @lcpr case=start
# "42"\n
# @lcpr case=end

# @lcpr case=start
# " -042"\n
# @lcpr case=end

# @lcpr case=start
# "1337c0d3"\n
# @lcpr case=end

# @lcpr case=start
# "0-1"\n
# @lcpr case=end

# @lcpr case=start
# "21474836460"\n
# @lcpr case=end

#


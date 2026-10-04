#
# @lc app=leetcode.cn id=678 lang=python3
# @lcpr version=30204
#
# [678] 有效的括号字符串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0    # 最少未匹配左括号数
        high = 0   # 最多未匹配左括号数

        for i , ch in enumerate(s):

            if ch == '(':
                low += 1
                high += 1
            elif ch == ')':
                high -= 1
                low -= 1
            else:
                low -= 1
                high += 1

            if high < 0:
                return False
            
            # 如果low < 0 则代表 * 被当作了) 填补( 的空缺，因此要抛弃，所以取0
            low = max(low, 0)

            # print(f"i: {i}, ch: {ch}, low: {low}, high: {high}")
        return low == 0
    



# @lc code=end



#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "(*)"\n
# @lcpr case=end

# @lcpr case=start
# "(*))"\n
# @lcpr case=end

#
# @lcpr case=start
# "((((*)"\n
# @lcpr case=end

#



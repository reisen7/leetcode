#
# @lc app=leetcode.cn id=13 lang=python
# @lcpr version=30204
#
# [13] 罗马数字转整数
#


# @lcpr-template-start


# @lcpr-template-end
# @lc code=start
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        val = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0
        n = len(s)

        for i in range(n):
            # 如果当前字符比下一个小，说明是 IV / IX / XL 这类，要减
            if i + 1 < n and val[s[i]] < val[s[i + 1]]:
                total -= val[s[i]]
            else:
                total += val[s[i]]

        return total


# @lc code=end


#
# @lcpr case=start
# "III"\n
# @lcpr case=end

# @lcpr case=start
# "IV"\n
# @lcpr case=end

# @lcpr case=start
# "IX"\n
# @lcpr case=end

# @lcpr case=start
# "LVIII"\n
# @lcpr case=end

# @lcpr case=start
# "MCMXCIV"\n
# @lcpr case=end

#

#
# @lc app=leetcode.cn id=6 lang=python3
# @lcpr version=30204
#
# [6] Z 字形变换
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        rows = [''] * numRows
        direction = 1
        cur = 0

        for x in s:
            rows[cur] += x

            if cur == numRows - 1:
                direction = -1

            if cur == 0:
                direction = 1


            cur += direction

        return ''.join(rows)



            

        
# @lc code=end



#
# @lcpr case=start
# "PAYPALISHIRING"\n3\n
# @lcpr case=end

# @lcpr case=start
# "PAYPALISHIRING"\n4\n
# @lcpr case=end

# @lcpr case=start
# "A"\n1\n
# @lcpr case=end

#


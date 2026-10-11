#
# @lc app=leetcode.cn id=56 lang=python3
# @lcpr version=30204
#
# [56] 合并区间
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:


        ans = []
        i = 0

        if len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x: x[0])
        while i < len(intervals):
            offset = 1
            ans_tmp = [intervals[i][0],intervals[i][1]]
            for j in range(i + 1, len(intervals)):

                if intervals[j][0] <= ans_tmp[1] :
                    ans_tmp = [intervals[i][0],max(intervals[j][1],ans_tmp[1])]
                    offset += 1
                else:
                    break
            ans.append(ans_tmp)
            i += offset

        return ans

# @lc code=end



#
# @lcpr case=start
# [[2,3],[5,5],[2,2],[3,4],[3,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,3],[5,5],[2,2],[3,4],[3,4]]\n
# @lcpr case=end

# @lcpr case=start
# [[5,5],[1,3],[3,5],[4,6],[1,1],[3,3],[5,6],[3,3],[2,4],[0,0]]\n
# @lcpr case=end

#


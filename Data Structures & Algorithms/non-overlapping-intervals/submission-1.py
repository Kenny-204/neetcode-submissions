class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[0])
        res = 0

        curr = intervals[0]
        for i in range(1,len(intervals)):
            if curr[1] <= intervals[i][0]:
                curr = intervals[i]
            elif curr[0] >= intervals[i][1]:
                curr = intervals[i]
            else:
                res+=1
                curr = [curr[0], min(curr[1],intervals[i][1])]
                continue
        return res
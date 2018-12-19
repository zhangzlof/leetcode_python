class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        Solution.res = []
        self.backtracking(candidates, target, 0, [])
        return Solution.res
        
    def backtracking(self,candidates,target, start, val):
        if target == 0:
            if val not in Solution.res:
                Solution.res.append(val)
        else:
            for i in range(start,len(candidates)):
                if target < 0:
                    break
                self.backtracking(candidates,target-candidates[i],i+1,val+[candidates[i]])

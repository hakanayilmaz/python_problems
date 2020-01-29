

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        
        tmp = 0
        for i in nums:
            if target in nums:
                tmp=nums.index(target)
                break
            else:
                if target > i:
                    tmp = nums.index(i) + 1
                    
        return tmp

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = [1] * len(nums)
        lefT = 1
         #Iterate from Left and take all elements 
        for i in range(len(nums)):
            tmp [i] = lefT
            lefT *= nums[i]
            
        #Iterate from right and take all elements and then multiply with left product
        righT = 1
        for i in range(len(nums)-1,-1,-1):
            tmp [i] = tmp[i] * righT
            righT = righT * nums[i]
            
        return tmp
        
       

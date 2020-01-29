class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lookup = collections.defaultdict(int)
        for i in nums1:
            lookup[i] +=1
            
        result = []
        
        for i in nums2:
            if lookup[i]>0:
                result.append(i)
                lookup[i] = 0
        
        return result
        
        

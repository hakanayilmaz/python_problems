class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        tmp = stones
        
        
        while len(tmp) >= 2:
            tmp.sort()
            if tmp[-1] == tmp[-2]:
                tmp.pop(-1)
                tmp.pop(-1)
                
            elif tmp[-1] != tmp[-2]:
                tmpx = max(tmp[-1],tmp[-2]) - min (tmp[-1],tmp[-2])
                tmp[-1] = tmpx
                tmp.pop(-2)
        if len(tmp) == 1:
            return tmp[0]
        if len(tmp) == 0:
            return 0
    
        return tmp

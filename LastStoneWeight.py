"""Create LastStoneWeight.py
We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)"""


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

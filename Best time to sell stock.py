
class Solution(object):
    def maxProfit(self, prices):
    	minPris = sys.maxint
    	maxProf = 0

    	for i in range(len(prices)):
    		if prices[i] < minPris:
    			minPris = prices[i]

    		if (prices[i] - minPris) > maxProf:
    			maxProf = prices[i] - minPris
    	return maxProf

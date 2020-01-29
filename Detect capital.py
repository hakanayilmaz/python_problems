class Solution(object):
    def detectCapitalUse(self, word):
        
        
        countGrote = 0
        
        for letter in word:
            if letter.isupper():
                countGrote += 1
                
        
        if countGrote == 0:
            return True
        elif countGrote == len(word):
            return True
        elif countGrote == 1 and word[0].isupper():
            return True
        else:
            return False

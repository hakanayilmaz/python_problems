class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        
        top = ['w','q','e','r','t','y','u','i','o','p']
        middle = ['a','s','d','f','g','h','j','k','l']
        bottom = ['z','x','c','v','b','n','m']

        tmp = [top,middle,bottom]
        output= []
        
        for i in words:   
            for row in tmp:
                if i[0].lower() in row:
                    curRow = row
                    break
                
            for char in i :
                j = 0
                if char.lower() not in curRow :
                    j = -1
                    break
                
            if j != -1:
                output.append(i)
                    
                        
        return output

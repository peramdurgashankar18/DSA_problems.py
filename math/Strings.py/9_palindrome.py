class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x <0):
             return False
        n = len(str(x))
        i=0
        j = n-1
        while(i<j):
            if(str(x)[i] != str(x)[j]):
               return False
            else:
                i += 1 
                j-= 1
        return True        

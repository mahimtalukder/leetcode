class Solution(object):
    def isPalindrome(self, x):
        # convert x to a list
        x = list(str(x)) 
        # reverse the list  
        i = 0
        for j in range((len(x)-1),-1,-1):  # range(start, stop, step) 
            if x[i] != x[j] :   
                return False    
            i += 1  
        return True 
    

if __name__ == '__main__':  
    # begin
    s = Solution()
    print(s.isPalindrome(11))  

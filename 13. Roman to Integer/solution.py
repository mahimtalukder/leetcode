class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_v = {
            "I":1,
            "V":5,  
            "X":10, 
            "L":50, 
            "C":100,    
            "D":500,    
            "M":1000,   
        }

        # convert s to a list   
        s = list(str(s)) 
        # Calulate the sum of the list 
        sum = 0
        i = 0
        while i < len(s):
            # check if s[i] value is less than s[i+1] value 
            if (len(s)-1) != i and s_v[s[i]] < s_v[s[i+1]]:
                sum += s_v[s[i+1]] - s_v[s[i]]
                i += 2  
            else:
                sum += s_v[s[i]]  
                i += 1    
       
        
        return sum
    
if __name__ == '__main__':  
    # begin
    s = Solution()
    print(s.romanToInt("MCMXCIV"))  
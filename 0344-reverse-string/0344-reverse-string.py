class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tmp = 0
        for i in range(len(s)//2): # 0 ~ len(s) - 1 + 1
            tmp = s[i]
            s[i] = s[len(s) -i-1]
            s[len(s) -i-1] = tmp
        
        return s
            
        
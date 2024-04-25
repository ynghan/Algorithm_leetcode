class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
                                    # if len(s) == 10:
        for i in range(len(s)//2):  # 0 ~ 5 까지 반복문을 돌린다.
            tmp = 0                     # 임시 저장 변수를 둔다.   
            tmp = s[i]              # s[0]
            s[i] = s[len(s)-i-1]    # s[0] = s[9]
            s[len(s)-i-1] = tmp     # s[9] = tmp
        
            
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = []
        c = s.lower()
        print(c)
        
        for i in c:
            if i.isalpha() or i.isdigit():
                a.append(i)
        print(a)
        for j in range(len(a)):
            if a[len(a)-j-1] != a[j]:
                return False
        return True
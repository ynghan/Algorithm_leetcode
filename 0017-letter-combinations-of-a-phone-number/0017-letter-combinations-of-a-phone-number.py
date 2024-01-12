class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if not digits:
            return []

        phone = {
            "2": "abc", 
            "3": "def", 
            "4": "ghi", 
            "5": "jkl", 
            "6": "mno", 
            "7": "pqrs", 
            "8": "tuv", 
            "9": "wxyz"
        }

        res = []

        def backtrack(string, next_digits):
            
            if not next_digits:
                res.append(string)
                return

            for letter in phone[next_digits[0]]:
                backtrack(string + letter, next_digits[1:])

        backtrack("", digits)
        
        return res
class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif c == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif c == "]":
                if not stack or stack.pop() != "[":
                    return False
            elif c == "}":
                if not stack or stack.pop() != "{":
                    return False
        if stack:
            return False
        return True
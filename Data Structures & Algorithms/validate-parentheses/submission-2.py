class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        bracket = { ")" : "(", "]" : "[", "}": "{" }

        for i in range(len(s)):

            if s[i] in bracket:
                if stack and stack[-1] == bracket[s[i]]:

                    stack.pop()
            
                else:
                    return False
            
            else:
        
                stack.append(s[i])

        return True if not stack else False 
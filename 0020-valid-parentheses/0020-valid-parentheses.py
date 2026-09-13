class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='{' or s[i]=='[':
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                last=stack.pop()
                if s[i]==')' and last=='(':
                    continue
                elif s[i]==']' and last=='[':
                        continue
                elif s[i]=='}' and last=='{':
                        continue
                else:
                    return False
        return not len(stack)
                

            
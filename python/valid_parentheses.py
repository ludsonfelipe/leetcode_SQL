"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""

class Solution:
    def isValid(self, s: str) -> bool:
       

        if (len(s)-1)%2 == 1:
                
            brackets = {'(':')', 
            '{':'}', 
            '[':']'}

            lista = list(s)
            c=1
        
            for l in s:
                try:
                    if l in brackets.keys():
                        lista.remove(brackets[l])
                        c+=1
                except:
                    return False

            return True
        else:
            return False

if __name__=='__main__':
    c = Solution()
    print(c.isValid('{[]]}'))


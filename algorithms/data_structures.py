class DataStructuresUtils:
    #Check if parentheses are valid.
    def isValid(self, s:str) -> bool:
        openers = ['(','[','{']
        closers = [')',']','}']
        stack = []

        for char in s:
            if char in openers:
                stack.append(char)
            elif char in closers:
                if not stack or openers.index(stack[-1]) != closers.index(char):
                    return False
                else:
                    stack.pop()
        return not stack
    #: T: O(N), where N is the length of the string
    #: S: O(N)
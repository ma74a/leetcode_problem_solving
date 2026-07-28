from typing import List

# Time complexity -> O(n), space compexity -> O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        operators = ['+', '*', '-', '/']
        for t in tokens:
            if t in operators:
                two = int(stk.pop())
                one = int(stk.pop())
                if t == '+':
                    res = one + two
                elif t == '*':
                    res = one * two
                elif t == '-':
                    res = one - two
                else:
                    res = int(one / two)
                stk.append(str(res))
            else:
                stk.append(t)
        return int(stk[0])


# tokens = ["2","1","+","3","*"]
# tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
sol = Solution()
print(sol.evalRPN(tokens=tokens))


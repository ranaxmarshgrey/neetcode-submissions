class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        opstack=[]
        for c in tokens:
            match c:
                case "+":
                    if opstack:
                        a=opstack.pop()
                        b=opstack.pop()
                        opstack.append(a+b)
                case "-":
                    if opstack:
                        b=opstack.pop()
                        a=opstack.pop()
                        opstack.append(a-b)
                case "*":
                    if opstack:
                        a=opstack.pop()
                        b=opstack.pop()
                        opstack.append(a*b)
                case "/":
                    if opstack:
                        b=opstack.pop()
                        a=opstack.pop()
                        opstack.append(int(a/b)) 
                case _:
                    opstack.append(int(c))
        return opstack[-1]                   

            
        
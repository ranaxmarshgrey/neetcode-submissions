class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[] #pair :[temp,ind]

        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                stackt,stacki=stack.pop()
                res[stacki]=i-stacki
            stack.append([t,i])
        return res



        
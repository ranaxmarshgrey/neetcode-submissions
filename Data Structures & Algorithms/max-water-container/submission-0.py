class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxarea=0
        while left<right:
            area=(right-left)*min(heights[left],heights[right])
            maxarea=max(maxarea,area)

            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maxarea
            



        
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        left=0
        right=len(height)-1
        leftmax=height[left]
        rightmax=height[right]
        water=0
        while left<right:
            if leftmax<=rightmax:
                left+=1
                leftmax=max(leftmax,height[left])
                if(leftmax-height[left]>0):
                    water+=leftmax-height[left]
            else:
                right-=1
                rightmax=max(rightmax,height[right])
                if(rightmax-height[right]>0):
                    water+=rightmax-height[right]
        return water
        



        
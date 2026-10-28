class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int[] ans1=new int[nums.length-k+1];
        Deque<Integer> ans=new ArrayDeque<>();
        for(int i=0;i<nums.length;i++){
            if(!ans.isEmpty() && ans.peekFirst()<=i-k){
                ans.pollFirst();
            }
            while(!ans.isEmpty() && nums[ans.peekLast()]<=nums[i]){
                ans.pollLast();
            }
            ans.offerLast(i);
            if(i>=k-1){
                ans1[i-k+1]=nums[ans.peekFirst()];
            }
        }
        return ans1;
    }
}
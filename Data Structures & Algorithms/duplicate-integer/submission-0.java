class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> temp= new HashSet<>();
        for(int i=0;i<nums.length;i++){
            if(temp.contains(nums[i])){
                return true;

            }
            else{
                temp.add(nums[i]);
            }
        }
        return false;
    }
}
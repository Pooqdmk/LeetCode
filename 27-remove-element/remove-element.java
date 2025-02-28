class Solution {
    public int removeElement(int[] nums, int val) {
        int cnt=0;int k=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]!=val){
                    nums[k]=nums[i];
                    cnt++;k++;
            }
            
        }
        return cnt;
        // for(int i=0;i<nums.length;i++){
        //     if(nums[i]!=0){
        //         return nums[i];
        //     }    
        // }
    
        
    }
}
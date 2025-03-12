class Solution {
    public int maximumCount(int[] nums) {
        int cnt=0;int z=0;int n=0;
        int l=nums.length;
        for(int i=0;i<l;i++){
            if(nums[i]>0){
                cnt++;
            }
            else if(nums[i]==0){
                z++;
            }
            else{
                n++;
            }
            
        }
        // int n=0;
        // if(nums[j+1]==0){
        //     n=l-cnt-1;
        // }
        // else{
        //     n=l-cnt;
        // }
        if(cnt>n)return cnt;
        else return n;

    }
}
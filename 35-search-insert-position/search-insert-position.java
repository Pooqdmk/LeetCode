class Solution {
    public int searchInsert(int[] nums, int target) {
        int s=0;int e=nums.length -1;
        while(s<=e){
            int mid=s+(-s+e)/2;
            int ele=nums[mid];
            if(ele==target){
                return mid;
            }
            else if(target>ele){
                s=mid+1;
            }
            else{
                e=mid-1;
            }
        }
        return s;
    }
}
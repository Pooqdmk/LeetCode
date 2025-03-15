class Solution {
    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {
        
        ArrayList<Boolean> a=new ArrayList<>();
        for(int i=0;i<l.length;i++){
            ArrayList<Integer> b=new ArrayList<>();
            for(int j=l[i];j<=r[i];j++){
                b.add(nums[j]);
            }
            Collections.sort(b);
            a.add(check(b));
        }
        return a;
    }
    public static boolean check(ArrayList<Integer> nums) {
        if (nums.size() < 2) return false; 

        int diff = nums.get(1) - nums.get(0);
        for (int i = 1; i < nums.size() - 1; i++) {
            if (nums.get(i + 1) - nums.get(i) != diff) {
                return false;
            }
        }
        return true;
    }
}
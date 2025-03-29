class Solution {
    public int mySqrt(int x) {
        if (x==0 || x==1)
            return x;
        for(int i=1;i<x;i++){
            if (Math.pow(i,2)<=x && x<Math.pow(i+1,2)){
                return i;
            }
        }
        return -1;
    }
}
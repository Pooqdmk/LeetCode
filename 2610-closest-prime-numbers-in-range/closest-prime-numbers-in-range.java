class Solution {
    public int[] closestPrimes(int left, int right) {
        ArrayList <Integer> a=new ArrayList<>();
        for(int i=left;i<=right;i++){
            if(isprime(i)){
                a.add(i);
            }
        }
        int cnt=Integer.MAX_VALUE;int[] mn={-1,-1};
        for(int j=0;j<a.size()-1;j++){
            if(a.get(j+1)-a.get(j)<cnt){
                mn[0]=a.get(j);
                mn[1]=a.get(j+1);
                cnt=a.get(j+1)-a.get(j);
            }
        }
        return mn;
    }
    public static boolean isprime(int n){
        if(n<2){return false;}
        if(n==2){
            return true;
        }
        if(n%2==0){return false;}
        for(int i=3;i*i<=n;i+=2){
            if(n%i==0)return false;
        }
        return true;

    }
}
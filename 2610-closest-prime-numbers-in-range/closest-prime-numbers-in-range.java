class Solution {
    public int[] closestPrimes(int left, int right) {
        boolean[] isPrime = sieve(right);
        ArrayList <Integer> a=new ArrayList<>();
        for(int i=left;i<=right;i++){
            if (isPrime[i]) {
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
    private boolean[] sieve(int n) {
        boolean[] isPrime = new boolean[n + 1];
        for (int i = 2; i <= n; i++) isPrime[i] = true;

        for (int p = 2; p * p <= n; p++) {
            if (isPrime[p]) {
                for (int i = p * p; i <= n; i += p) {
                    isPrime[i] = false;
                }
            }
        }
        return isPrime;
    }
}
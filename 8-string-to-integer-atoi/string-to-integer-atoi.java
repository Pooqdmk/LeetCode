class Solution {
    public int myAtoi(String s) {
        int i=0;int sign=1;
        int res=0;
        int n=s.length();
        while(i<n && s.charAt(i)==' '){
            i++;
        }
        while(i<n && (s.charAt(i)=='-' || s.charAt(i)=='+')){
            sign=(s.charAt(i)=='-')?-1:1;
            i++;
            if(i<n && (s.charAt(i)=='+' || s.charAt(i)=='-')){
                return 0;
            }
        }
        
        while(i<n && Character.isDigit(s.charAt(i))){
            int digit=s.charAt(i)-'0';
        

            if(res>(Integer.MAX_VALUE-digit)/10){
                return (sign==1)?Integer.MAX_VALUE:Integer.MIN_VALUE;
            }
            res=res*10+digit;
            i++;
        }
        return res*sign;


    }
}
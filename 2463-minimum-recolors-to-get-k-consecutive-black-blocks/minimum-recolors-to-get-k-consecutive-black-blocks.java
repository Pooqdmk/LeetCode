class Solution {
    public int minimumRecolors(String blocks, int k) {
        int min=k;StringBuilder s=new StringBuilder();
        for(int i=0;i<=blocks.length()-k;i++){
                int cnt=0;s.setLength(0);
                s.append(blocks.substring(i,k+i));
                for(int j=0;j<s.length();j++){
                    if(s.charAt(j)=='W'){
                        cnt=cnt+1;
                    }
                }
                if(cnt<min){
                    min=cnt;
                }
        }
        return min;

    }
}
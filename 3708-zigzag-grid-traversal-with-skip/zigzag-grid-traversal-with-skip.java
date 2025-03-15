class Solution {
    public List<Integer> zigzagTraversal(int[][] grid) {
        ArrayList<Integer> a=new ArrayList<>();
        int n=grid.length;
        for(int i=0;i<n;i++){
            int m=grid[i].length;
            if(i%2==0){
                for(int j=0;j<m;j+=2){
                    a.add(grid[i][j]);
                }
            }
            else{
                if(m%2==0){
                    for(int k=m-1;k>0;k-=2){
                        a.add(grid[i][k]);
                    }
                }
                else{
                    for(int k=m-2;k>0;k-=2){
                        a.add(grid[i][k]);
                    }
                }
                
            }
        }
        return a;
    }
}
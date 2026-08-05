class Solution {
    public boolean judgeSquareSum(int c) {
        int a = 0;
        long b = (int)Math.sqrt(c);
        while(a<=b){
            long sum = a*a + b*b ;
            if(sum == c){
                return true;
            }else if(sum > c){
                b-=1;
            }else{
                a+=1;
            }
        }
        return false;
    }
}
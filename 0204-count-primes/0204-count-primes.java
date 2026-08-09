class Solution {
    // public boolean isprime(int n){
    //     if(n==0 || n==1){
    //         return false;
    //     }
    //     for(int i=2;i<=Math.sqrt(n);i++){
    //         if(n%i==0){
    //             return false;
    //         }
    //     }
    //     return true;
    // }
    public int countPrimes(int n) {
        if(n==0 || n==1){
            return 0;
        }
        boolean arr[] = new boolean[n+1];
        for(int i=2;i<n;i++){
            arr[i]=true;
        }
        int count = 0;
        for(int i=2;i*i<n;i++){
            if(arr[i]){
                for(int j=i*i;j<n;j+=i){
                    arr[j]=false;
                }
            }
        }
        for(int i=0;i<n;i++){
            if(arr[i]){
                count++;
            }
        }
        return count;
    }
}
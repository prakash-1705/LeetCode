class Solution {
    public int dayOfYear(String date) {
        int arr[] = {31,28,31,30,31,30,31,31,30,31,30,31};
        String parts[] = date.split("-");
        int days = 0 ;
        int months = Integer.parseInt(parts[1]);
        boolean extra = false ;
        if(months>2){
            if((Integer.parseInt(parts[0])%400==0) || ((Integer.parseInt(parts[0])%4==0) && (Integer.parseInt(parts[0])%100!=0))){
                extra = true;
                days++;
            }
        }
        for(int i=1;i<months;i++){
            days += arr[i-1];
        }
        if(extra){
            return Integer.parseInt(parts[2])+days;
        }else{
            return Integer.parseInt(parts[2])+days;
        }
    }
}
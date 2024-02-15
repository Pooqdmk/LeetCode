bool isPalindrome(int x) {
    long int rem=0,ori;
    ori=x;
    while(x>0){
    rem=(rem * 10)+x%10;
    x=x/10;
    }
    if(ori==rem){
        return true;
    }
    else
        return false;
}
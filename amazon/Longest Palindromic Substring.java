class Solution {
    public String longestPalindrome(String s) {
        if (s==null || s.length() < 1) return "";
        // int start = 0, end = 0;
        String res = "";
        for (int i = 0; i < s.length(); i++){
            int l1 = helper(s, i, i);
            int l2 = helper(s, i, i+1);
            int l = Math.max(l1, l2);
            if (l > res.length())
                res = s.substring(i - (l - 1) / 2, i + l / 2+1);
        }
        return res;
    }
    
    public int helper(String s, int left, int right){
        int L = left, R = right;
        while (L >= 0 && R < s.length() && s.charAt(L) == s.charAt(R)) {
            L--;
            R++;
        }
        return R - L - 1;
    }


}

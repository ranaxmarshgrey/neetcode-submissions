class Solution {
    public boolean isAnagram(String s, String t) {
        // HashMap<Character,Integer> map=new HashMap<>();
        if (s.length() != t.length()) {
    return false;
}
        int[] temp = new int[26];
        for(int i=0;i<s.length();i++){
            char sch=s.charAt(i);
            int sind=sch-'a';
            char tch=t.charAt(i);
            int tind=tch-'a';
            temp[sind]++;
            temp[tind]--;

        }
        for(int i=0;i<26;i++){
            if(temp[i]!=0){
                return false;
            }
        }
        return true;
    }
}

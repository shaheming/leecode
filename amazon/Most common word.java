class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        paragraph += ".";
        
        Set<String> banset = new HashSet<>();
        for (String word: banned) banset.add(word);
        Map<String, Integer> count = new HashMap<>();
        
        String res = "";
        int freq = 0;
        
        StringBuilder word = new StringBuilder();
        for (char c: paragraph.toCharArray()) {
            if (Character.isLetter(c)) {
                word.append(Character.toLowerCase(c));
            } else if (word.length() > 0) {
                String finalword = word.toString();
                if (!banset.contains(finalword)) {
                    count.put(finalword, count.getOrDefault(finalword, 0) + 1);
                    if (count.get(finalword) > freq) {
                        res = finalword;
                        freq = count.get(finalword);
                    }
                }
                word = new StringBuilder();
            }
        }

        return res;
    }
}
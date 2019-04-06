public class Solution{
	public int findSubstring(String str, int k){
		if(str == null || str.length() < k || k > 26) return 0;

		int left = 0;
		int right = 0;
		String tmp = "";
		Map<Character, Integer> chars = new HashMap<>();
		Set<String> seen = new HashSet<>();

		for (; right < str.length(); right++){
			char c = str.charAt(right);
			chars.put(c, chars.getOrDefault(c, 0)+1);
			tmp += c;

			if (tmp.length() > k){
				char head = str.charAt(left);
				chars.put(head, chars.get(head) - 1);
				if (chars.get(head) == 0) chars.remove(head);
				tmp = tmp.substring(1);
				left++;
			}

			if (tmp.length() == k){
				if (chars.size() == k-1) seen.add(tmp); 
			}
		}
		return seen.size();
	}
}
Public class Solution{

	public int countKDist(String str, int k){
		if (str == null || str.length() < k || k > 26) return 0;

		Set<String> seen = new HashSet<>();

		for (int i=0; i<str.length(); i++){
			Map<Character, Integer> count = new HashMap<>();
			int cnt = 0;
			for(int j = i; j < str.length(); j++){
				char add = str.charAt(j);
				if (!count.containsKey(add)) cnt++;
				chars.put(add, chars.getOrDefault(add, 0)+1);
				if (cnt == k) seen.add(str.substring(i,j+1));
			}
		}

		return seen.size();
	}
}
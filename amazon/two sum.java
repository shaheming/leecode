class Solution{
	public int[] twoSum(int[] nums, int target){
		Array.sort(nums);
		int left = 0;
		int right = nums.length-1;
		while (left < right){
			int s = nums[left] + nums[right];
			if (s == target) return true;
			else if (s>target) right -= 1;
			else left += 1;
		}
		return false;
	}
}



import java.util.*;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i=0; i<nums.length; i++){
            int component = target - nums[i];
            if (map.containsKey(component)){
                return new int[] {map.get(component), i};
            }
            map.put(nums[i], i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}
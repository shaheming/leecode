public class Solution{

	public int twoSumClosest(int [] nums, int target){
		if (nums == null || nums.length == 0) return 0;

		         
        int left = 0;
        int right = nums.length - 1;
        int[] res = new int[2];
        int diff = Integer.MAX_VALUE;
        while(left < right) {
            int sum = nums[left] + nums[right];
            if(sum <= target && target - sum < diff) {
                res[0] = nums[left];
                res[1] = nums[right];
            }
            if(sum < target) {
                //diff = Math.min(diff, target - sum);
                left++;
            }
            else
            {
                //diff = Math.min(diff, sum - target);
                right--;
            }
        }
        return res;    

		// Array.sort(nums);
		// int left = 0;
		// int right = nums.length-1;
		// int res = Integer.MAX_VALUE；

		// while (left < right){
		// 	int s = nums[left] + nums[right];
		// 	diff = Math.min(res, Math.abs(target - sum));
		// 	if (sum > target) right -= 1;
		// 	else left += 1;
		// }
		// return res;     

	}
}
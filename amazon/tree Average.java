public class Solution{

	class ResultType{
		TreeNode node;
		int sum;
		int size;
		public ResultType(TreeNode node, int sum, int size){
			this.node = node;
			this.sum = sum;
			this.size = size;
		}
	}

	private ResultType result = null;

	public TreeNode findSubtree(TreeNode root){
		if (root == null) return null;
		ResultType rootResult = helper(root);
		return result.node;
	}

	// public ResultType helper(TreeNode root){
	// 	if (root == null) return new ResultType(null, 0, 0);

	// 	ResultType leftResult = helper(root.left);
	// 	ResultType rightResult = helper(root.right);
	// 	ResultType currResult = new ResultType(root, leftResult.sum+rightResult.sum+root.val, leftResult.size+rightResult.size+1);

	// 	if (result == null ||
	// 		currResult.sum/currResult.size > result.sum/result.size)
	// 		result = currResult;

	// 	return currResult;
	// }

	public ResultType helper(TreeNode root){
		if (root == null) return new ResultType(null, 0, 0);

		List<ResultType> nodes = new ArrayList<>();
		for (TreeNode n: root.children){
			nodes.add(helper(n));
		}

		int sum = 0;
		int size = 0;
		for (ResultType n: nodes){
			sum += n.sum;
			size += n.size;
		}
		ResultType currResult = new ResultType(root, sum+root.val, size+1);
		if (result == null || double(currResult.sum/currResult.size) > double(result.sum/result.size))
			result = currResult;
		
		return currResult;		
			
	}

}
### Binary Tree Maximum Path Sum
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.

[leetcode](https://leetcode.com/problems/binary-tree-maximum-path-sum/description/)

### Answer 
The result of a given node must comes from 4 conditions
1) left branch + current node
2) right branch + current node
3) current node only
4) left branch + current node + right branch

	/**
	 * Definition for a binary tree node.
	 * struct TreeNode {
	 *     int val;
	 *     TreeNode *left;
	 *     TreeNode *right;
	 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
	 * };
	 */
	class Solution {
	public:
	    int maxPathSum(TreeNode* root) {
	        // for each node, the path can be 4 conditions
	        // 1. from left branch and ends at this node
	        // 2. from right branch and ends at this node
	        // 3. use the current node to connect left and right
	        // 4. discard all below and use its single node
	        // for each node, return the max value of left branch and right branch
	        int maxSum = INT_MIN;
	        recur(root, maxSum);
	        return maxSum;
	    }
	    
	    int recur(TreeNode* iter, int &maxSum)
	    {
	        if (iter == 0) return 0;
	        
	        int leftPath = recur(iter->left, maxSum);
	        int rightPath = recur(iter->right, maxSum);
	        
	        int currVal = iter->val;
	        maxSum = max(maxSum, leftPath + rightPath + currVal);
	        
	        int branchResult = max(max(leftPath, rightPath) + currVal, currVal);
	        maxSum = max(maxSum, branchResult);
	        
	        return branchResult;
	    }
	};
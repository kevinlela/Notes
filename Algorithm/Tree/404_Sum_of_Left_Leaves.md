### Sum of Left Leaves
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.


[leetcode](https://leetcode.com/problems/sum-of-left-leaves/description/)

### Answer 

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
	    int sumOfLeftLeaves(TreeNode* root) {
	        return recur(root, false);
	    }
	    
	    int recur(TreeNode* iter, bool isLeft)
	    {
	        if (iter == NULL) return 0;
	        if (iter->left == NULL && iter->right == NULL) return isLeft ? iter->val : 0;
	        int left = recur(iter->left, true);
	        int right = recur(iter->right, false);
	        return left + right;
	    }
	};
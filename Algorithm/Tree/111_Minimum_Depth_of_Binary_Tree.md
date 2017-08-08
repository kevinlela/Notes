### Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

[leetcode](https://leetcode.com/problems/minimum-depth-of-binary-tree/description/)

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
	    int minDepth(TreeNode* root) {
	        if (root == NULL) return 0;
	        if (root->left == NULL && root->right == NULL) return 1;
	        
	        int curr = -1, left = INT_MAX, right = INT_MAX;
	        if (root->left) left = minDepth(root->left);
	        if (root->right) right = minDepth(root->right);
	        
	        return min(left, right) + 1;
	    }
	};
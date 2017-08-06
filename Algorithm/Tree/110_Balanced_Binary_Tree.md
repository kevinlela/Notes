### Balanced Binary Tree
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

[leetcode](https://leetcode.com/problems/balanced-binary-tree/description/)

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
	    bool isBalanced(TreeNode* root) {
	        pair<bool, int> result = recur(root);
	        return result.first;
	    }
	    
	    pair<bool, int> recur(TreeNode *iter)
	    {
	        if (iter == NULL) return {true, 0};
	        pair<bool, int> left = recur(iter->left);
	        if (!left.first) return left;
	        pair<bool, int> right = recur(iter->right);
	        if (!right.first) return right;
	        
	        return {abs(left.second - right.second) <= 1, max(left.second, right.second) + 1};
	    }
	};
### Invert Binary Tree
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1

[leetcode](https://leetcode.com/problems/invert-binary-tree/description/)

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
	    TreeNode* invertTree(TreeNode* root) {
	        if (root == NULL) return NULL;
	        
	        TreeNode* left = invertTree(root->left);
	        TreeNode* right = invertTree(root->right);
	        
	        root->left = right;
	        root->right = left;
	        
	        return root;
	    }
	};
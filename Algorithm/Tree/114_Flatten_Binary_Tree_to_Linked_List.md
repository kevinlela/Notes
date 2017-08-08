### Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6


[leetcode](https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/)

### Answer 

Every time you find a left tree, append the current right tree to the right end of the left tree then move the left tree to right. 

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
	    void flatten(TreeNode* root) {
	        TreeNode *iter = root;
	        while (iter)
	        {
	            if (iter->left)
	            {
	                TreeNode* right = iter->right;
	                TreeNode* left = iter->left;
	                iter->right = left;
	                iter->left = NULL;
	                iter = left;
	                while (iter->right) iter = iter->right;
	                iter->right = right;
	                iter = left;
	            }
	            else iter = iter->right;
	        }
	    }
	};
### Inorder Successor in BST
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.

[leetcode](https://leetcode.com/problems/inorder-successor-in-bst/description/)

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
	    TreeNode* inorderSuccessor(TreeNode* root, TreeNode* p) {
	        TreeNode *iter = root, *prev = NULL;
	        
	        while (iter)
	        {
	            if (iter->val == p->val)
	            {
	                if (p->right)
	                {
	                    p = p->right;
	                    while (p->left)
	                    {
	                        p = p->left;  
	                    }
	                    return p;
	                }
	                else if (prev) return prev;
	                else return NULL;
	            }
	            if (iter->val > p->val)
	            {
	                prev = iter;
	                iter = iter->left;
	            }
	            else iter = iter->right;
	        }
	        
	        return NULL;
	    }
	};
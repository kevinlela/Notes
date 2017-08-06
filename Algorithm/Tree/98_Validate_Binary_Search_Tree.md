### Validate Binary Search Tree
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.

[leetcode](https://leetcode.com/problems/validate-binary-search-tree/description/)

### Answer 

method_1: we need to bring interval from leaf to root
method_2: use inordered traversal. Notice, the inordered traversal of a BST gives an sorted sequence. 

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
	    bool isValidBST(TreeNode* root) {
	        // inorder traverse
	        stack<TreeNode*> stk;
	        TreeNode* iter = root;
	        int curr = INT_MIN;
	        bool first = false;
	        
	        while (!stk.empty() || iter)
	        {
	            if (iter)
	            {
	                stk.push(iter);
	                iter = iter->left;
	            }
	            else
	            {
	                iter = stk.top();
	                stk.pop();
	                if (iter->val <= curr && first) return false;
	                curr = iter->val;
	                first = true;
	                iter = iter->right;
	            }
	        }
	        return true;
	    }
	};
### Binary Tree Preorder Traversal
Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?

[leetcode](https://leetcode.com/problems/binary-tree-preorder-traversal/description/)

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
	    vector<int> preorderTraversal(TreeNode* root) {
	        TreeNode *iter = root;
	        stack<TreeNode*> stk;
	        vector<int> result;
	        
	        while(iter || !stk.empty())
	        {
	            if (iter)
	            {
	                result.push_back(iter->val);
	                stk.push(iter);
	                iter = iter->left;
	            }
	            else
	            {
	                TreeNode* curr = stk.top();
	                stk.pop();
	                iter = curr->right;
	            }
	        }
	        
	        return result;
	    }
	};
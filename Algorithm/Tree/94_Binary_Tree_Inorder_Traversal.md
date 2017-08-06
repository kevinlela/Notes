### Binary Tree Inorder Traversal
Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

[leetcode](https://leetcode.com/problems/binary-tree-inorder-traversal/description/)

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
	    vector<int> inorderTraversal(TreeNode* root) {
	        vector<int> result;
	        stack<TreeNode*> stk;
	        TreeNode* iter = root;
	        
	        while (iter || !stk.empty())
	        {
	            if (iter)
	            {
	                stk.push(iter);
	                iter = iter->left;
	            }
	            else
	            {
	                iter = stk.top();
	                result.push_back(iter->val);
	                stk.pop();
	                iter = iter->right;
	            }
	        }
	        return result;
	    }
	    
	    void recur(vector<int> &result, TreeNode* iter)
	    {
	        if (iter == NULL) return;
	        
	        recur(result, iter->left);
	        result.push_back(iter->val);
	        recur(result, iter->right);
	    }
	};

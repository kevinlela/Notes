### Binary Tree Postorder Traversal
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?

[leetcode](https://leetcode.com/problems/binary-tree-postorder-traversal/description/)

### Answer 
Post order is the reverse of right first preorder

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
	    vector<int> postorderTraversal(TreeNode* root) {
	        TreeNode *iter = root;
	        stack<TreeNode*> stk;
	        vector<int> result;
	        
	        while(iter || !stk.empty())
	        {
	            if (iter)
	            {
	                result.push_back(iter->val);
	                stk.push(iter);
	                iter = iter->right;
	            }
	            else
	            {
	                TreeNode* curr = stk.top();
	                stk.pop();
	                iter = curr->left;
	            }
	        }
	        
	        reverse(result.begin(), result.end());
	        return result;
	    }
	};
### Binary Tree Level Order Traversal II
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

[leetcode](https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/)

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
	    vector<vector<int>> levelOrderBottom(TreeNode* root) {
	        queue<TreeNode*> cands;
	        vector<vector<int>> result;
	        if (root == NULL) return result;
	        cands.push(root);
	        
	        while (!cands.empty())
	        {
	            int len = cands.size();
	            vector<int> level;
	            for (int i = 0; i < len; ++i)
	            {
	                TreeNode *curr = cands.front();
	                if (curr->left) cands.push(curr->left);
	                if (curr->right) cands.push(curr->right);
	                level.push_back(curr->val);
	                cands.pop();
	            }
	            result.push_back(level);
	        }
	        
	        reverse(result.begin(), result.end());
	        return result;
	    }
	};
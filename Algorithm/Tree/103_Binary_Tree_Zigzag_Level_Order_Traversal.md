### Binary Tree Zigzag Level Order Traversal
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

[leetcode](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/)

### Answer 
BFS

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
	    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
	        vector<vector<int>> result;
	        if (root == NULL) return result;
	        deque<TreeNode*> cands;
	        cands.push_back(root);
	        bool order = true;
	        
	        while (!cands.empty())
	        {
	            vector<int> level;
	            int len = cands.size();
	            for (int i = 0; i < len; ++i)
	            {
	                TreeNode *curr = order ? cands.front() : cands.back();
	                level.push_back(curr->val);
	                if (order)
	                {
	                    if (curr->left) cands.push_back(curr->left);
	                    if (curr->right) cands.push_back(curr->right);
	                }
	                else
	                {
	                    if (curr->right) cands.push_front(curr->right);
	                    if (curr->left) cands.push_front(curr->left);
	                }
	                if (order) cands.pop_front();
	                else cands.pop_back();
	            }
	            result.push_back(level);
	            order = !order;
	        }
	        
	        return result;
	    }
	};
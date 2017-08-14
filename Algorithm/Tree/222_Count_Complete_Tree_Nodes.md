### Count Complete Tree Nodes
Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

[leetcode](https://leetcode.com/problems/count-complete-tree-nodes/description/)

### Answer 
we can save traversal if we get a full complete tree with left side = right side length. 

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
	    int countNodes(TreeNode* root) {
	        return recur(root, -1, -1);
	    }
	    
	    int recur(TreeNode* iter, int ls, int rs)
	    {
	        if (iter == NULL) return 0;
	        
	        TreeNode *tmp = iter;
	        if (ls == -1)
	        {
	            ls = 0;
	            while (tmp)
	            {
	                tmp = tmp->left;
	                ++ls;
	            }
	        }
	        
	        tmp = iter;
	        if (rs == -1)
	        {
	            rs = 0;
	            while (tmp)
	            {
	                tmp = tmp->right;
	                ++rs;
	            }
	        }
	        
	        if (ls == rs) return pow(2, ls) - 1;
	        return recur(iter->left, ls - 1, -1) +  
	               recur(iter->right, -1, rs - 1) + 1;
	    }
	};
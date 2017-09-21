### Binary Tree Longest Consecutive Sequence
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    / 
   2    
  / 
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.

[leetcode](https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description/)

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
	    int longestConsecutive(TreeNode* root) {
	        int result = 0;
	        recur(root, result);
	        return result;
	    }
	    
	    int recur(TreeNode*iter, int &result)
	    {
	        if (iter == NULL) return 0;
	        
	        int path = 1; // including itself
	        if (iter->left != NULL)
	        {
	            int l = recur(iter->left, result);
	            if (iter->left->val - 1 == iter->val)
	                path = 1 + l;
	        }
	        if (iter->right != NULL)
	        {
	            int r = recur(iter->right, result);
	            if (iter->right->val - 1 == iter->val)
	                path = max(path, 1 + r);
	        }
	        result = max(result, path);
	        return path;
	    }
	};
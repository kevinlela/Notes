### Find Leaves of Binary Tree
Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

Example:
Given binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Returns [4, 5, 3], [2], [1].

Explanation:
1. Removing the leaves [4, 5, 3] would result in this tree:

          1
         / 
        2          
2. Now removing the leaf [2] would result in this tree:

          1          
3. Now removing the leaf [1] would result in the empty tree:

          []         
Returns [4, 5, 3], [2], [1].

[leetcode](https://leetcode.com/problems/find-leaves-of-binary-tree/description/)

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
	    vector<vector<int>> findLeaves(TreeNode* root) {
	        int dep = caldep(root);
	        vector<vector<int>> result(dep, vector<int>());
	        recur(root, result);
	        return result;
	    }
	    
	    int recur(TreeNode *iter, vector<vector<int>> &result)
	    {
	        if (iter == NULL) return -1;
	        int dL = recur(iter->left, result);
	        int dR = recur(iter->right, result);
	        int curr = max(dL, dR) + 1;
	        result[curr].push_back(iter->val);
	        return curr;
	    }
	    
	    int caldep(TreeNode *iter)
	    {
	        if (iter == NULL) return 0;
	        int dL = caldep(iter->left);
	        int dR = caldep(iter->right);
	        return max(dL, dR) + 1;
	    }
	};
### Unique Binary Search Trees II
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,
Given n = 3, your program should return all 5 unique BST's shown below.

	   1         3     3      2      1
	    \       /     /      / \      \
	     3     2     1      1   3      2
	    /     /       \                 \
	   2     1         2                 3

[leetcode](https://leetcode.com/problems/unique-binary-search-trees-ii/description/)

### Answer 
Think in a merge sort way. break all the element down and compose in all different way. 

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
	    vector<TreeNode*> generateTrees(int n) {
	        return n < 1 ? vector<TreeNode*>() : recur(1, n);
	    }
	    
	    vector<TreeNode*> recur(int st, int ed)
	    {
	        if (st > ed) return vector<TreeNode*> (1, NULL);
	        vector<TreeNode*> result;
	        
	        for (int i = st; i <= ed; ++i)
	        {
	            vector<TreeNode*> lefts = recur(st, i-1);
	            vector<TreeNode*> rights = recur(i+1, ed);
	            for (int n = 0; n < lefts.size(); ++n)
	            {
	                for (int m = 0; m < rights.size(); ++m)
	                {
	                    TreeNode* curr = new TreeNode (i);
	                    curr->left = lefts[n];
	                    curr->right = rights[m];
	                    result.push_back(curr);
	                }
	            }
	        }
	        
	        return result;
	    }
	};
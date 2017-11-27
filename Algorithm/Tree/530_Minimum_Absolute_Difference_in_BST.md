### Minimum Absolute Difference in BST
Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

	   1
	    \
	     3
	    /
	   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
Note: There are at least two nodes in this BST.

[leetcode](https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/)

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
	    int getMinimumDifference(TreeNode* root) {
	        int prev = 0, minDiff = INT_MAX;
	        bool first = true;
	        inOrder(root, prev, minDiff, first);
	        return minDiff;
	    }
	    
	    void inOrder(TreeNode* iter, int &prev, int &minDiff, bool &first)
	    {
	        if (iter == NULL) return;
	        inOrder(iter->left, prev, minDiff, first);
	        if (first)
	        {
	            prev = iter->val;
	            first = false;
	        }
	        else
	        {
	            minDiff = min(minDiff, iter->val - prev);
	            prev = iter->val;
	        }
	        inOrder(iter->right, prev, minDiff, first);
	    }
	};
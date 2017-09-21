### Closest Binary Search Tree Value
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
* Given target value is a floating point.
* You are guaranteed to have only one unique value in the BST that is closest to the target

[leetcode](https://leetcode.com/problems/closest-binary-search-tree-value/description/)

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
	    int closestValue(TreeNode* root, double target) {
	        TreeNode* iter = root;
	        double result = -1;
	        int res_element = 0;
	        while (iter)
	        {
	            if (iter->val == target) return iter->val;
	            else if (iter->val > target)
	            {
	                if (result == -1 || (double)iter->val - target < result)
	                {
	                    result = (double)iter->val - target;
	                    res_element = iter->val;
	                }
	                iter = iter->left;
	            }
	            else 
	            {
	                if (result == -1 || target - (double)iter->val < result)
	                {
	                    result = target - (double)iter->val;
	                    res_element = iter->val;
	                }
	                iter = iter->right;
	            }
	        }
	        return res_element;
	    }
	};
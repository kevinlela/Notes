### Convert Sorted Array to Binary Search Tree
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

[leetcode](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/)

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
	    TreeNode* sortedArrayToBST(vector<int>& nums) {
	        int len = nums.size();
	        return recur(nums, 0, len);
	    }
	    
	    TreeNode* recur(const vector<int> &nums, int st, int ed)
	    {
	        if (st >= ed) return NULL;
	        int mid = st + (ed - st)/2;
	        TreeNode *currNode = new TreeNode (nums[mid]);
	        currNode->left = recur(nums, st, mid);
	        currNode->right = recur(nums, mid + 1, ed);
	        return currNode;
	    }
	};
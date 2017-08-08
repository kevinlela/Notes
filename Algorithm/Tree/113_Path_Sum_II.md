### Path Sum II
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]

[leetcode](https://leetcode.com/problems/path-sum-ii/description/)

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
	    vector<vector<int>> pathSum(TreeNode* root, int sum) {
	        vector<vector<int>> result;
	        vector<int> comb;
	        recur(result, comb, root, sum, 0);
	        return result;
	    }
	    
	    void recur(vector<vector<int>> &result, vector<int> &comb, TreeNode* root, int sum, int prev)
	    {
	        if (root == NULL) return;
	        if (root->left == NULL && root->right == NULL)
	        {
	            if (prev + root->val == sum)
	            {
	                comb.push_back(root->val);
	                result.push_back(comb);
	                comb.pop_back();
	            }
	            return;
	        }
	        
	        comb.push_back(root->val);
	        recur(result, comb, root->left, sum, prev + root->val);
	        recur(result, comb, root->right, sum, prev + root->val);
	        comb.pop_back();
	    }
	};
### Find Largest Value in Each Tree Row
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]

[leetcode](https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/)

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
	    vector<int> largestValues(TreeNode* root) {
	        vector<int> result;
	        if (root == NULL) return result;
	        queue<TreeNode*> myQ;
	        myQ.push(root);
	        while (!myQ.empty())
	        {
	            int len = myQ.size();
	            int curr_max = 0;
	            for (int i = 0; i < len; ++i)
	            {
	                if (i == 0) curr_max = myQ.front()->val;
	                else curr_max = max(curr_max, myQ.front()->val);
	                if (myQ.front()->left) myQ.push(myQ.front()->left);
	                if (myQ.front()->right) myQ.push(myQ.front()->right);
	                myQ.pop();
	            }
	            result.push_back(curr_max);
	        }
	        return result;
	    }
	};
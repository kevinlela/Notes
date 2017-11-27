### Find Bottom Left Tree Value
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

	    2
	   / \
	  1   3

Output:
1
Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.

[leetcode](https://leetcode.com/problems/find-bottom-left-tree-value/description/)

### Answer
level order traversal, or dfs is also ok

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
	    int findBottomLeftValue(TreeNode* root) {
	        int result = 0;
	        queue<TreeNode*> myQ;
	        myQ.push(root);
	        while (!myQ.empty())
	        {
	            int len = myQ.size();
	            for (int i = 0; i < len; ++i)
	            {
	                if (i == 0) result = myQ.front()->val;
	                if (myQ.front()->left) myQ.push(myQ.front()->left);
	                if (myQ.front()->right) myQ.push(myQ.front()->right);
	                myQ.pop();
	            }
	        }
	        return result;
	    }
	};
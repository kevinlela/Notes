### Sum Root to Leaf Numbers
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.

[leetcode](https://leetcode.com/problems/sum-root-to-leaf-numbers/description/)

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
	    int sumNumbers(TreeNode* root) {
	        int sum = 0;
	        sumLeaves(root, 0, sum);
	        return sum;
	    }
	    
	    void sumLeaves(TreeNode* iter, int curr, int &sum)
	    {
	        if (iter == NULL) return;
	        if (iter->left == NULL && iter->right == NULL)
	        {
	            sum += curr*10 + iter->val;
	            return;
	        }
	        
	        curr = curr*10 + iter->val;
	        sumLeaves(iter->left, curr, sum);
	        sumLeaves(iter->right, curr, sum);
	    }
	};
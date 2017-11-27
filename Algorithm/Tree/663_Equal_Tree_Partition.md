### Equal Tree Partition
Given a binary tree with n nodes, your task is to check if it's possible to partition the tree to two trees which have the equal sum of values after removing exactly one edge on the original tree.

Example 1:
Input:  

	    5
	   / \
	  10 10
	    /  \
	   2   3

Output: True
Explanation: 

	    5
	   / 
	  10
      
Sum: 15

	   10
	  /  \
	 2    3

Sum: 15
Example 2:
Input:  
   
	    1
	   / \
	  2  10
	    /  \
	   2   20

Output: False
Explanation: You can't split the tree into two trees with equal sum after removing exactly one edge on the tree.
Note:
The range of tree node value is in the range of [-100000, 100000].
1 <= n <= 10000

[leetcode](https://leetcode.com/problems/equal-tree-partition/description/)

### Answer
corner case: do we cut edge connected to NULL node ?
in the corner case, NO
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
	    bool checkEqualTree(TreeNode* root) {
	        int sum = getSum(root);
	        if (sum % 2) return false;
	        d_target = sum / 2;
	        d_decision = false;
	        targetSum(root);
	        return d_decision;
	    }
	    
	    int targetSum(TreeNode *iter)
	    {
	        if (iter == NULL) return 0;
	        int left = targetSum(iter->left);
	        if (left == d_target && iter->left) d_decision = true;
	        int right = targetSum(iter->right);
	        if (right == d_target && iter->right) d_decision = true;
	        return left + right + iter->val;
	    }
	    
	    int getSum(TreeNode *iter)
	    {
	        if (iter == NULL) return 0;
	        return getSum(iter->left) + getSum(iter->right) + iter->val;
	    }
	private:
	    int d_target;
	    int d_decision;
	};
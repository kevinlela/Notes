### Symmetric Tree
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

[leetcode](https://leetcode.com/problems/symmetric-tree/description/)

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
	    bool isSymmetric(TreeNode* root) {
	        return recur(root, root);
	    }
	    
	    bool recur(TreeNode *iterL, TreeNode *iterR)
	    {
	        if (iterL == NULL && iterR == NULL) return true;
	        else if (iterL == NULL || iterR == NULL) return false;
	        if (iterL->val != iterR->val) return false;
	        
	        return recur(iterL->left, iterR->right) && recur(iterL->right, iterR->left);
	    }
	};
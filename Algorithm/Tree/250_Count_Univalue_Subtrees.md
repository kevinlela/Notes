### Count Univalue Subtrees
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

For example:
Given binary tree,
              5
             / \
            1   5
           / \   \
          5   5   5
return 4.

[leetcode](https://leetcode.com/problems/count-univalue-subtrees/description/)

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
	    int countUnivalSubtrees(TreeNode* root) {
	        int result = 0;
	        post(root, result);
	        return result;
	    }
	    
	    bool post(TreeNode *iter, int &result)
	    {
	        if (iter == NULL) return true;
	        bool leftUni = post(iter->left, result);
	        bool rightUni = post(iter->right, result);
	        if ( !leftUni || !rightUni ) return false;
	        if (iter->left && iter->left->val != iter->val) return false;
	        if (iter->right && iter->right->val != iter->val) return false;
	        result += 1;
	        
	        return true;
	    }
	};
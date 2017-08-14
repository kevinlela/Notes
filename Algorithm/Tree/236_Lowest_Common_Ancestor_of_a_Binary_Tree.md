### Lowest Common Ancestor of a Binary Tree
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes 5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

[leetcode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/)

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
	    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
	        TreeNode *result = NULL;
	        LCA(root, p, q, result);
	        return result;
	    }
	    
	    int LCA(TreeNode* iter, TreeNode* p, TreeNode*q, TreeNode *&result)
	    {
	        if (iter == NULL) return 0;
	        if (result) return 0;
	        
	        int curr = (iter == p || iter == q) ? 1 : 0;
	        int left = LCA(iter->left, p, q, result);
	        if (result) return 0;
	        int right = LCA(iter->right, p, q, result);
	        if (result) return 0;
	        
	        if (curr + left + right > 1) result = iter;
	        
	        return curr + left + right;
	    }
	};
### Find Mode in Binary Search Tree
Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

[leetcode](https://leetcode.com/problems/find-mode-in-binary-search-tree/description/)

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
	    vector<int> findMode(TreeNode* root) {
	        int count = 0, maxCount = 0;
	        vector<int> result;
	        TreeNode *prev = NULL;
	        inorder(root, prev, count, maxCount, result);
	        return result;
	    }
	    
	    void inorder(TreeNode* iter, TreeNode* &prev, int &count, int &maxCount, vector<int> &result)
	    {
	        if (iter == NULL) return;
	        
	        inorder(iter->left, prev, count, maxCount, result);
	        
	        if (prev == NULL)
	        {
	            result.push_back(iter->val);
	            count = 1;
	            maxCount = count;
	        }
	        else
	        {
	            if (prev->val == iter->val) ++count;
	            else count = 1;
	            if (count == maxCount)
	            {
	                result.push_back(iter->val);
	            }
	            else if (count > maxCount)
	            {
	                result.clear();
	                result.push_back(iter->val);
	            }
	            maxCount = max(maxCount, count);
	        }
	        prev = iter;
	        inorder(iter->right, prev, count, maxCount, result);
	    }
	};

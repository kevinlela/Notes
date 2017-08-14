### Kth Smallest Element in a BST
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ? k ? BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

[leetcode](https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/)

### Answer 
Inorder traversal 

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
	    int kthSmallest(TreeNode* root, int k) {
	        stack<TreeNode*> myStk;
	        TreeNode* iter = root;
	        
	        while (iter || !myStk.empty())
	        {
	            if (iter)
	            {
	                myStk.push(iter);
	                iter = iter->left;
	            }
	            else
	            {
	                k--;
	                if (k == 0) return myStk.top()->val;
	                TreeNode *top = myStk.top();
	                myStk.pop();
	                iter = top->right;
	            }
	        }
	        
	        return -1;
	    }
	};
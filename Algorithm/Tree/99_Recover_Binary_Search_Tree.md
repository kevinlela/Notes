### Recover Binary Search Tree
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

[leetcode](https://leetcode.com/problems/recover-binary-search-tree/description/)

### Answer 
BST can be converted into sorted sequence by inorder traversal. There are only two case of swaping

* swap ajacent 123546789
* swap non-ajacent 123856749

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
	    void recoverTree(TreeNode* root) {
	        // change two nodes cause inorder travesal incorrect
	        TreeNode *tA = NULL, *tB = NULL, *prev = NULL;
	        int curr = 0;
	        inOrder(tA, tB, root, prev, curr);
	        if (tA && tB)
	        {
	            int tmp = tA->val;
	            tA->val = tB->val;
	            tB->val = tmp;
	        }
	    }
	    
	    void inOrder(TreeNode* &tA, TreeNode* &tB, TreeNode* iter, TreeNode* &prev, int &curr)
	    {
	        if (iter == NULL) return;
	        
	        inOrder(tA, tB, iter->left, prev, curr);
	        if (prev != NULL && prev->val > iter->val)
	        {
	            if (curr == 0) tA = prev;
	            tB = iter;
	            ++curr;
	            if (curr == 2) return;
	        }
	        prev = iter;
	        inOrder(tA, tB, iter->right, prev, curr);
	    }
	};
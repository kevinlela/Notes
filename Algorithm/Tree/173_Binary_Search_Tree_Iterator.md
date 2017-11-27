### Binary Search Tree Iterator
implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

[leetcode](https://leetcode.com/problems/binary-search-tree-iterator/submissions/1)

### Answer 
This is similar to [94](94_Binary_Tree_Inorder_Traversal.md)

	/**
	 * Definition for binary tree
	 * struct TreeNode {
	 *     int val;
	 *     TreeNode *left;
	 *     TreeNode *right;
	 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
	 * };
	 */
	class BSTIterator {
	public:
	    BSTIterator(TreeNode *root) : d_iter(root) {
	    }
	    
	    /** @return whether we have a next smallest number */
	    bool hasNext() {
	        while (d_iter)
	        {
	            d_stk.push(d_iter);
	            d_iter = d_iter->left;
	        }
	        
	        return !d_stk.empty();
	    }
	    
	    /** @return the next smallest number */
	    int next() {
	        TreeNode *result = d_stk.top();
	        d_stk.pop();
	        d_iter = result->right;
	        
	        return result->val;
	    }
	    
	private:
	    TreeNode* d_iter;
	    stack<TreeNode*> d_stk;
	};

	/**
	 * Your BSTIterator will be called like this:
	 * BSTIterator i = BSTIterator(root);
	 * while (i.hasNext()) cout << i.next();
	 */
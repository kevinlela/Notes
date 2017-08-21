### Delete Node in a BST
Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7

[leetcode](https://leetcode.com/problems/delete-node-in-a-bst/description/)

### Answer
The deletion happens among three nodes parent N1, left child N2 and right child N3
1) delete N1 
2) let N2 becomes new N1
3) append N3 to the right most node of N2

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
	    TreeNode* deleteNode(TreeNode* root, int key) {
	        TreeNode *iter = root, *prev = NULL;
	        while (iter)
	        {
	            if (iter->val == key) break;
	            else if (iter->val > key) 
	            {
	                prev = iter;
	                iter = iter->left;
	            }
	            else 
	            {
	                prev = iter;
	                iter = iter->right;
	            }
	        }

	        if (iter == NULL) return root;
	        
	        if (prev == NULL) return deleteTop(iter);
	        else if (prev->left == iter) prev->left = deleteTop(iter);
	        else prev->right = deleteTop(iter);
	        
	        return root;
	    }
	    
	    TreeNode * deleteTop(TreeNode* iter)
	    {
	        TreeNode *left = iter->left;
	        TreeNode *right = iter->right;
	        
	        if (left == NULL && right == NULL)
	        {
	            delete iter;
	            return NULL;
	        }
	        else if (left == NULL)
	        {
	            delete iter;
	            return right;
	        }
	        else 
	        {
	            TreeNode *lr = left;
	            while (lr && lr->right)
	            {
	                lr = lr->right;
	            }
	            lr->right = right;
	            
	            delete iter;
	            return left;
	        }
	        
	        return NULL;
	    }
	};



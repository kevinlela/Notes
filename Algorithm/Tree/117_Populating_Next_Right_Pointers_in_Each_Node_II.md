### Populating Next Right Pointers in Each Node II
Follow up for problem "Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL

[leetcode](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/)

### Answer 

	/**
	 * Definition for binary tree with next pointer.
	 * struct TreeLinkNode {
	 *  int val;
	 *  TreeLinkNode *left, *right, *next;
	 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
	 * };
	 */
	class Solution {
	public:
	    void connect(TreeLinkNode *root) {
	        TreeLinkNode *iter = root;
	        while (iter)
	        {
	            TreeLinkNode *nextBegin = NULL;
	            TreeLinkNode *prev = NULL;
	            while (iter)
	            {
	                if (iter->left)
	                {
	                    if (prev) prev->next = iter->left;
	                    else nextBegin = iter->left;
	                    iter->left->next = NULL;
	                    prev = iter->left;
	                }
	                if (iter->right)
	                {
	                    if (prev) prev->next = iter->right;
	                    else nextBegin = iter->right;
	                    iter->right->next = NULL;
	                    prev = iter->right;
	                }
	                iter = iter->next;
	            }
	            
	            iter = nextBegin;
	        }
	        
	    }
	};
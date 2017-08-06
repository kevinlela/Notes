### Construct Binary Tree from Preorder and Inorder Traversal
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

[leetcode](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/)

### Answer 
Why do we need preorder and inorder?

preorder gives the order, and inorder gives the split, say
12345, it can be 2345 on the left of 1 or on the right of 1 or some on the left and some on the right, this is why we need inorder to split the left and right. 

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
	    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
	        unordered_map<int, int> indexes;
	        for (int i = 0; i < inorder.size(); ++i) //store the index of every node, since no duplicate
	        {
	            indexes[inorder[i]] = i;
	        }
	        int curr = 0;
	        return recur(preorder, indexes, 0, inorder.size(), curr);
	    }
	    
	    TreeNode* recur(const vector<int> &preorder, unordered_map<int, int> &indexes, 
	                    int st, int ed, int &curr)
	    {
	        if (curr >= preorder.size()) return NULL;
	        if (st > ed) return NULL;
	        
	        int currVal = preorder[curr];
	        int currIdx = indexes[currVal];
	        if (currIdx < st || currIdx > ed) return NULL;
	        
	        TreeNode* currNode = new TreeNode (currVal);
	        ++curr;
	        currNode->left = recur(preorder, indexes, st, currIdx-1, curr);
	        currNode->right = recur(preorder, indexes, currIdx+1, ed, curr);
	        
	        return currNode;
	    }
	};
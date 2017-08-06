### Construct Binary Tree from Inorder and Postorder Traversal
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

[leetcode](https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/)

### Answer 
similar to [104](104_Maximum_Depth_of_Binary_Tree.md)

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
	    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
	        vector<int> preRightOrder(postorder);
	        reverse(preRightOrder.begin(), preRightOrder.end());
	        unordered_map<int, int> indexes;
	        for (int i = 0; i < inorder.size(); ++i)
	        {
	            indexes[inorder[i]] = i;
	        }
	        
	        int curr = 0, len = inorder.size();
	        return recur(preRightOrder, indexes, 0, len - 1, curr);
	    }
	    
	    TreeNode* recur(const vector<int> &preRightOrder, unordered_map<int, int> &indexes,
	                    int st, int ed, int &curr)
	    {
	        if (curr >= preRightOrder.size() || st > ed) return NULL;
	        
	        int currVal = preRightOrder[curr];
	        int currIdx = indexes[currVal];
	        if (currIdx < st || currIdx > ed) return NULL;
	        
	        TreeNode* currNode = new TreeNode (currVal);
	        ++curr;
	        currNode->right = recur(preRightOrder, indexes, currIdx + 1, ed, curr);
	        currNode->left = recur(preRightOrder, indexes, st, currIdx - 1, curr);
	        
	        return currNode;
	    }
	};
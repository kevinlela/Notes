### Binary Tree Upside Down
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

For example:
Given a binary tree {1,2,3,4,5},
    1
   / \
  2   3
 / \
4   5
return the root of the binary tree [4,5,2,#,#,3,1].
   4
  / \
 5   2
    / \
   3   1  
confused what "{1,#,2,3}" means? 

[leetcode](https://leetcode.com/problems/binary-tree-upside-down/description/)

### Answer
Use inorder to find the root and use post order to change the structure. 

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
        TreeNode* upsideDownBinaryTree(TreeNode* root) {
            TreeNode* result = NULL;
            post(root, result);
            return result;
        }
        
        TreeNode* post(TreeNode* iter, TreeNode* &root)
        {
            if (iter == NULL) return iter;
            TreeNode *left = post(iter->left, root);
            if (root == NULL) root = iter;
            TreeNode *right = post(iter->right, root);
            
            if (left) 
            {
                left->left = right;
                left->right = iter;
            }
            iter->left = NULL;
            iter->right = NULL;
         
            return iter;
        }
    };

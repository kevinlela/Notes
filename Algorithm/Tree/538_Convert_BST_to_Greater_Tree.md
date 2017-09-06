### Convert BST to Greater Tree
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13

[leetcode](https://leetcode.com/problems/convert-bst-to-greater-tree/description/)

### Answer
Inorder start from right. 
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
    TreeNode* convertBST(TreeNode* root) {
        int prev = 0;
        recur(root, prev);
        return root;
    }
    
    void recur(TreeNode* iter, int &prev)
    {
        if (iter == NULL) return;
        recur(iter->right, prev);
        iter->val += prev;
        prev = iter->val;
        recur(iter->left, prev);
    }
};
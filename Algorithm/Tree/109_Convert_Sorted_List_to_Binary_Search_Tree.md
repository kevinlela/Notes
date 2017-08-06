### Convert Sorted List to Binary Search Tree
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

[leetcode](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/)

### Answer
Unlike array [108_Convert_Sorted_Array_to_Binary_Search_Tree.md], no direct access. So, we need to keep the in ordered traverse to traverse the linkedlist

	/**
	 * Definition for singly-linked list.
	 * struct ListNode {
	 *     int val;
	 *     ListNode *next;
	 *     ListNode(int x) : val(x), next(NULL) {}
	 * };
	 */
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
	    TreeNode* sortedListToBST(ListNode* head) {
	        // notice, traverse a link list is equivilant to inorder traversal
	        int len = getListLen(head);
	        return recur(head, 0, len);
	    }
	    
	    TreeNode* recur(ListNode* &iter, int st, int ed)
	    {
	        if (st >= ed) return NULL;
	        int mid = st + (ed - st)/2;
	        
	        TreeNode* left = recur(iter, st, mid);
	        TreeNode* currNode = new TreeNode(iter->val);
	        iter = iter->next;
	        TreeNode* right = recur(iter, mid + 1, ed);
	        
	        currNode->left = left;
	        currNode->right = right;
	        return currNode;
	    }
	    
	    int getListLen(ListNode* head)
	    {
	        int len = 0;
	        while (head)
	        {
	            head = head->next;
	            ++len;
	        }
	        return len;
	    }
	};
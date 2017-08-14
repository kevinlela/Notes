### Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

[leetcode](https://leetcode.com/problems/remove-linked-list-elements/description/)

### Answer 
	/**
	 * Definition for singly-linked list.
	 * struct ListNode {
	 *     int val;
	 *     ListNode *next;
	 *     ListNode(int x) : val(x), next(NULL) {}
	 * };
	 */
	class Solution {
	public:
	    ListNode* removeElements(ListNode* head, int val) {
	        ListNode *dum = new ListNode (0);
	        dum->next = head;
	        ListNode *prev = dum;
	        ListNode *iter = head;
	        
	        while (iter)
	        {
	            ListNode *next = iter->next;
	            if (iter->val == val)
	            {
	                delete iter;
	                prev->next = next;
	            }
	            else prev = iter;
	            iter = next;
	        }
	        
	        ListNode *result = dum->next;
	        delete dum;
	        return result;
	    }
	};
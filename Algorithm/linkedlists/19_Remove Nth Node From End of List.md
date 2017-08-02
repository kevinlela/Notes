### Remove Nth Node From End of List

Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.

[leetcode](https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/)

### Answer:

The safest way is do it in two passes. However, the problem requires us to do it in one pass, so just use two pointers. Actually, it is the same as do it in two passes. 

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
	    ListNode* removeNthFromEnd(ListNode* head, int n) {
	        if (head == NULL || n < 0) return NULL;
	        if (n == 0) return head;
	        
	        ListNode *iter = head, *target = NULL, *prev = NULL;
	        while (iter)
	        {
	            if (n <= 0) 
	            {
	                prev = target;
	                target = target->next;
	            }
	            iter = iter->next;
	            --n;
	            if (n == 0) target = head;
	        }
	        
	        if (!target) return NULL;
	        if (!prev) // head value
	        {
	            ListNode* result = target->next;
	            delete target;
	            return result;
	        }
	        
	        prev->next = target->next;
	        delete target;
	        return head;
	    }
	};
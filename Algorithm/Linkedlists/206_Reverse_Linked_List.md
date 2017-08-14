### Reverse Linked List
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?

[leetcode](https://leetcode.com/problems/reverse-linked-list/description/)

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
	    ListNode* reverseList(ListNode* head) {
	        ListNode *prev = NULL;
	        
	        while (head)
	        {
	            ListNode *next = head->next;
	            head->next = prev;
	            prev = head;
	            if (next == NULL) return head;
	            head = next;
	        }
	        
	        return head;
	    }
	};
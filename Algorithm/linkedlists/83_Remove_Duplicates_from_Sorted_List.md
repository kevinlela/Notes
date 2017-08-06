### Remove Duplicates from Sorted List
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

[leetcode](https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/)

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
	    ListNode* deleteDuplicates(ListNode* head) {
	        if (head == NULL) return head;
	        ListNode *curr = head, *iter = head->next;
	        while (iter)
	        {
	            if (iter->val != curr->val)
	            {
	                curr = iter;
	                iter = iter->next;
	            }
	            else
	            {
	                curr->next = iter->next;
	                delete iter;
	                iter = curr->next;
	            }
	        }
	        return head;
	    }
	};
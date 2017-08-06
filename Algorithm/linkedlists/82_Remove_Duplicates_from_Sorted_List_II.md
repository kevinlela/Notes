### Remove Duplicates from Sorted List II
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

[leetcode](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/)

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
	        ListNode *prev = NULL, *st = head, *iter = st->next;
	        while (st)
	        {
	            iter = st->next;
	            while (iter)
	            {
	                if (iter->val != st->val) break;
	                iter = iter->next;
	            }
	            
	            if (iter == st->next) // not duplicate
	            {
	                prev = st;
	                st = iter;
	            }
	            else //duplicate
	            {
	                if (prev == NULL) head = iter;
	                else prev->next = iter;
	                while (st != iter)
	                {
	                    ListNode *next = st->next;
	                    delete st;
	                    st = next;
	                }
	                st = iter;
	            }
	        }
	        
	        return head;
	    }
	};
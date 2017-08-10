### Reorder List
Given a singly linked list L: L0?L1?…?Ln-1?Ln,
reorder it to: L0?Ln?L1?Ln-1?L2?Ln-2?…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

[leetcode](https://leetcode.com/problems/reorder-list/description/)

### Answer 
Find the mid point and break into two list, reverse the second one and interleave them

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
	    void reorderList(ListNode* head) {
	        if (head == NULL) return;
	        
	        ListNode *L1 = head, *L1Head = NULL;
	        ListNode *L2 = head, *L2Head = NULL;
	        
	        while (L2)
	        {
	            L2 = L2->next;
	            if (L2) L2 = L2->next;
	            else break;
	            if (L2 == NULL) break;
	            L1 = L1->next;
	        }
	        
	        L2Head = L1->next;
	        L1Head = head;
	        
	        if (L1) L1->next = NULL;
	    
	        ListNode *iter = L2Head, *prev = NULL;
	        while (iter)
	        {
	            ListNode *next = iter->next;
	            iter->next = prev;
	            if (next == NULL) break;
	            prev = iter;
	            iter = next;
	        }
	        L2Head = iter;
	        
	        head = NULL; iter = NULL;
	        ListNode *iter1 = L1Head, *iter2 = L2Head;
	        bool oe = true;
	        
	        while (iter1 || iter2)
	        {
	            ListNode *curr = NULL;
	            if (oe) 
	            {
	                if (iter1) 
	                {
	                    curr = iter1;
	                    iter1 = iter1->next;
	                }
	                else 
	                {
	                    curr = iter2;
	                    iter2 = iter2->next;
	                }
	            }
	            else
	            {
	                if (iter2) 
	                {
	                    curr = iter2;
	                    iter2 = iter2->next;
	                }
	                else 
	                {
	                    curr = iter1;
	                    iter1 = iter1->next;
	                }
	            }
	            
	            if (iter) iter->next = curr;
	            iter = curr;
	            iter->next = NULL;
	            
	            oe = !oe;
	        }
	    }
	};
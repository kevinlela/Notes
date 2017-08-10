### Insertion Sort List
Sort a linked list using insertion sort.

[leetcode](https://leetcode.com/problems/insertion-sort-list/description/)

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
	    ListNode* insertionSortList(ListNode* head) {
	        ListNode* iter = head;
	        head = NULL;
	        while (iter)
	        {
	            ListNode *curr = iter;
	            iter = iter->next;
	            head = insertNode(head, curr);
	        }
	        return head;
	    }
	    
	    ListNode* insertNode(ListNode* head, ListNode* target)
	    {
	        if (target == NULL) return head;
	        
	        target->next = NULL;
	        
	        if (head == NULL) return target;
	        
	        ListNode* pos = NULL, *iter = head;
	        
	        while (iter && iter->val < target->val)
	        {
	            pos = iter;
	            iter = iter->next;
	        }
	        
	        target->next = iter;
	        
	        if (pos == NULL) return target;
	        
	        pos->next = target;
	        
	        return head;
	    }
	};
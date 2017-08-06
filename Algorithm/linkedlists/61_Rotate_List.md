### Rotate List
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

[leetcode](https://leetcode.com/problems/rotate-list/description/)

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
	    ListNode* rotateRight(ListNode* head, int k) {
	        int len = getListLen(head);
	        if (len == 0 || len == 1) return head;
	        k %= len;
	        if (k == 0) return head;
	        
	        ListNode *iter = head;
	        while (k)
	        {
	            iter = iter->next;
	            --k;
	        }
	        
	        ListNode *breakPoint = head;
	        while (iter->next)
	        {
	            breakPoint = breakPoint->next;
	            iter = iter->next;
	        }
	        
	        iter->next = head;
	        head = breakPoint->next;
	        breakPoint->next = NULL;
	        return head;
	    }
	    
	    int getListLen(const ListNode* head)
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
### Reverse Linked List II
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ? m ? n ? length of list.

[leetcode](https://leetcode.com/problems/reverse-linked-list-ii/description/)

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
	    ListNode* reverseBetween(ListNode* head, int m, int n) {
	        ListNode* prev = NULL, *iter = head;
	        int len = n - m;
	        
	        while (m-- > 1 && iter)
	        {
	            prev = iter;
	            iter = iter->next;
	        }
	        
	        ListNode *before = prev;
	        ListNode *st = iter; 
	        prev = iter;
	        iter = iter ? iter->next : iter;
	        
	        while (len-- > 0 && iter)
	        {
	            ListNode* next = iter->next;
	            iter->next = prev;
	            prev = iter;
	            iter = next;
	        }
	        
	        if (before) before->next = prev;
	        else head = prev;
	        st->next = iter;
	        return head;
	    }
	};
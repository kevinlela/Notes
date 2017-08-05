### Swap Nodes in Pairs

Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

[leetcode](https://leetcode.com/problems/swap-nodes-in-pairs/description/)

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
	    ListNode* swapPairs(ListNode* head) {
	        ListNode* iter1 = head, *prev = NULL;
	        
	        while (iter1)
	        {
	            ListNode* iter2 = iter1->next;
	            if (iter2 == NULL) return head;
	            iter1->next = iter2->next;
	            iter2->next = iter1;
	            if (prev == NULL) head = iter2;
	            else prev->next = iter2;
	            
	            prev = iter1;
	            iter1 = iter1->next;
	        }
	        
	        return head;
	    }
	};
### Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

[leetcode](https://leetcode.com/problems/merge-two-sorted-lists/description/)

### Answer:

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
	    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
	        ListNode *result = NULL, *head = NULL;
	        while (l1 != NULL || l2 != NULL)
	        {
	            if (l1 == NULL) mergeAndForward(l2, result, head);
	            else if (l2 == NULL) mergeAndForward(l1, result, head);
	            else if (l1->val > l2->val) mergeAndForward(l2, result, head);
	            else mergeAndForward(l1, result, head);
	        }
	        return head;
	    }
	    
	    void mergeAndForward(ListNode* &current, ListNode* &result, ListNode* &head)
	    {
	        if (result == NULL) head = current;
	        else result->next = current;
	        result = current;
	        current = current->next;
	        result->next = NULL;
	    }
	};
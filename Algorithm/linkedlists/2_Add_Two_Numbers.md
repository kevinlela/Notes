### Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

### Answer:

It is a very simple linkedlist, notice, the word called carry. 

	class Solution {
	public:
	    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
	        ListNode *result = NULL, *head = NULL;
	        int curr = 0;
	        int adv = 0;
	        while (l1 != NULL || l2 != NULL)
	        {
	            if (l1 == NULL) 
	            {
	                curr = l2->val + adv;
	                l2 = l2->next;
	            }
	            else if (l2 == NULL)
	            {
	                curr = l1->val + adv;
	                l1 = l1->next;
	            }
	            else 
	            {
	                curr = l1->val + l2->val + adv;
	                l1 = l1->next;
	                l2 = l2->next;
	            }
	            
	            adv = curr/10;
	            curr %= 10;
	            if (result == NULL)
	            {
	                result = new ListNode(curr);
	                head = result;
	            }
	            else
	            {
	                result->next = new ListNode(curr);
	                result = result->next;
	            }
	        }
	        
	        if (adv != 0) result->next = new ListNode(adv);
	        return head;
	    }
	};
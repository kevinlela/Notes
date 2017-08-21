### Add Two Numbers II
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

[leetcode](https://leetcode.com/problems/add-two-numbers-ii/description/)

### Answer
Solve it recursively if the reverse is not allowed. 

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
	    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
	       return reverseList(add(reverseList(l1), reverseList(l2))); 
	    }
	    
	    ListNode* add(ListNode* l1, ListNode* l2) {
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
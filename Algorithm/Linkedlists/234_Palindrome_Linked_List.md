### Palindrome Linked List
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?

[leetcode](https://leetcode.com/problems/palindrome-linked-list/description/)

### Answer 
The cleanest way is to break it into two halves, reverse one and check. 

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
	    bool isPalindrome(ListNode* head) {
	        ListNode *slow = head, *fast = head;
	        while (fast)
	        {
	            fast = fast -> next;
	            if (!fast) break;
	            fast = fast -> next;
	            if (!fast) break;
	            slow = slow -> next;
	        }
	        
	        ListNode *half = NULL;
	        if (slow)
	        {
	            half = slow -> next;
	            slow->next = NULL;
	        }
	        
	        ListNode *iter2 = reverseList(half);
	        ListNode *iter1 = head;
	        
	        while (iter1 && iter2)
	        {
	            if (iter1->val != iter2->val) return false;
	            iter1 = iter1->next;
	            iter2 = iter2->next;
	        }
	        
	        return true;
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
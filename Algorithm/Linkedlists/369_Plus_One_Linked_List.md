### Plus One Linked List
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example:
Input:
1->2->3

Output:
1->2->4

[leetcode](https://leetcode.com/problems/plus-one-linked-list/description/)

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
	    ListNode* plusOne(ListNode* head) {
	        int carry = recur(head);
	        if (carry)
	        {
	            ListNode* newHead = new ListNode (carry);
	            newHead->next = head;
	            return newHead;
	        }
	        return head;
	    }
	    
	    int recur(ListNode* iter)
	    {
	        if (iter == NULL) return 1;
	        int n = recur(iter->next);
	        iter->val += n;
	        int carry = iter->val / 10;
	        iter->val %= 10;
	        return carry;
	    }
	};
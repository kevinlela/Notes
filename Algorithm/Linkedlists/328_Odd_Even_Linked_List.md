### Odd Even Linked List
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...

[leetcode](https://leetcode.com/problems/odd-even-linked-list/description/)

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
	    ListNode* oddEvenList(ListNode* head) {
	        ListNode* odd = NULL, *odd_head = NULL;
	        ListNode* even = NULL, *even_head = NULL;
	        ListNode* iter = head;
	        
	        int num = 1;
	        
	        while (iter)
	        {
	            if (num % 2 == 1)
	            {
	                if (odd_head == NULL) odd_head = iter;
	                else odd->next = iter;
	                odd = iter;
	                iter = iter->next;
	                odd->next = NULL;
	            }
	            else
	            {
	                if (even_head == NULL) even_head = iter;
	                else even->next = iter;
	                even = iter;
	                iter = iter->next;
	                even->next = NULL;
	            }
	            ++num;
	        }
	        
	        if (odd) odd->next = even_head;
	        return odd_head;
	    }
	};
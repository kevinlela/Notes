### Intersection of Two Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.

[leetcode](https://leetcode.com/problems/intersection-of-two-linked-lists/description/)

### Answer 
It is like cycle in list. BUT, it is not the same, this one has cleaner solution. Suppose the len before intersection is L_a, L_b, and after intersection is L_c. We use two iterator to traverse A then B and the other one B then A, they will meet at intersection problem. 

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
	    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
	        //if (headA == NULL || headB == NULL) return NULL;
	        ListNode *iterA = headA, *iterB = headB;
	        
	        while (iterA != iterB)
	        {
	            if (iterA == NULL) iterA = headB;
	            else iterA = iterA->next;
	            if (iterB == NULL) iterB = headA;
	            else iterB = iterB->next;
	        }
	        
	        return iterA;
	    }
	};
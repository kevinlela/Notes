### Linked List Cycle
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

[leetcode](https://leetcode.com/problems/linked-list-cycle/description/)

### Answer 
Classic problem, send a fast and a slow iterator simoutenously. 

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
    bool hasCycle(ListNode *head) {
        ListNode *slow = head, *fast = head;
        
        while(fast)
        {
            slow = slow->next;
            fast = fast->next;
            if (fast) fast = fast->next;
            else return false;
            if (slow == fast) return true;
        }
        
        return false;
    }
};
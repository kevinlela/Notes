### Copy List with Random Pointer
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

[leetcode](https://leetcode.com/problems/copy-list-with-random-pointer/description/)

### Answer 
This is very like [133](133_Clone_Graph.md)

	/**
	 * Definition for singly-linked list with a random pointer.
	 * struct RandomListNode {
	 *     int label;
	 *     RandomListNode *next, *random;
	 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
	 * };
	 */
	class Solution {
	public:
	    typedef RandomListNode RLNode;
	    unordered_map<RLNode*, RLNode*> created;
	    RandomListNode *copyRandomList(RandomListNode *head) {
	        if (head == NULL) return NULL;
	        if (created.find(head) != created.end()) return created[head];
	        RLNode* newNode = new RLNode(head->label);
	        created[head] = newNode;
	        newNode->next = copyRandomList(head->next);
	        newNode->random = copyRandomList(head->random);
	        return newNode;
	    }
	};
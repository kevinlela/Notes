### Clone Graph
Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

[leetcode](https://leetcode.com/problems/clone-graph/description/)

### Answer 
We need to mark the visited nodes, here we use an unordered map to store the old node and new created node. 

	/**
	 * Definition for undirected graph.
	 * struct UndirectedGraphNode {
	 *     int label;
	 *     vector<UndirectedGraphNode *> neighbors;
	 *     UndirectedGraphNode(int x) : label(x) {};
	 * };
	 */
	class Solution {
	public:
	    typedef UndirectedGraphNode UGNode;
	    unordered_map<UGNode*, UGNode*> created;
	    
	    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
	        return deepClone(node);
	    }
	    
	    UGNode* deepClone(UGNode *node)
	    {
	        if (node == NULL) return node;
	        if (created.find(node) != created.end()) return created[node]; 
	        UGNode *curr = new UGNode (node->label);
	        created[node] = curr;
	        
	        for (auto iter = node->neighbors.begin(); iter != node->neighbors.end(); ++iter)
	        {
	            curr->neighbors.push_back(deepClone(*iter));
	        }
	        
	        return curr;
	    }
	};
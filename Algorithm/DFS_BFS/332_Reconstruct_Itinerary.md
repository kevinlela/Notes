### Reconstruct Itinerary
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].
Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.

[leetcode](https://leetcode.com/problems/reconstruct-itinerary/description/)

### Answer 
It is a DFS problem. But instead of black out a node, we need to count the used tickets

	class Solution {
	public:
	    vector<string> findItinerary(vector<pair<string, string>> tickets) {
	        unordered_map<string, map<string, int>> from_to;
	        for (int i = 0; i < tickets.size(); ++i)
	        {
	            from_to[tickets[i].first][tickets[i].second]++;
	        }
	        int len = tickets.size();
	        vector<string> result(1, "JFK");
	        dfs(from_to, len, "JFK", result);
	        return result;
	    }
	    
	    bool dfs(unordered_map<string, map<string, int>> &from_to, int numTickets,              const string &curr, vector<string> &result)
	    {
	        if (numTickets == 0) return true;
	        if (from_to.find(curr) == from_to.end()) return false;
	        
	        map<string, int> &currTo = from_to[curr];
	        for (auto iter = currTo.begin(); iter != currTo.end(); ++iter)
	        {
	            if (iter->second == 0) continue;
	            result.push_back(iter->first);
	            --iter->second;
	            if (dfs(from_to, numTickets-1, iter->first, result)) return true;
	            result.pop_back();
	            ++iter->second;
	        }
	        
	        return false;
	    }
	};
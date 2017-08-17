### Evaluate Division
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0. 
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? . 
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries , where equations.size() == values.size(), and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
The input is always valid. You may assume that evaluating the queries will result in no division by zero and there is no contradiction.

[leetcode](https://leetcode.com/problems/evaluate-division/description/)

### Answer 

	class Solution {
	public:
	    vector<double> calcEquation(vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries) {
	        unordered_map<string, int> strId;
	        unordered_map<int, unordered_map<int, double>> eqMap;
	        int id = 0;
	        for (int i = 0; i < equations.size(); ++i)
	        {
	            if (strId.find(equations[i].first) == strId.end())
	            {
	                strId[equations[i].first] = id++;
	            }
	            if (strId.find(equations[i].second) == strId.end())
	            {
	                strId[equations[i].second] = id++;
	            }
	            int id1 = strId[equations[i].first], id2 = strId[equations[i].second];
	            eqMap[id1][id2] = values[i];
	            if (values[i] != 0) eqMap[id2][id1] = 1/values[i]; 
	        }
	        
	        vector<double> result;
	        for (int i = 0; i < queries.size(); ++i)
	        {
	            auto iter1 = strId.find(queries[i].first);
	            auto iter2 = strId.find(queries[i].second);
	            
	            if (iter1 == strId.end() || iter2 == strId.end()) result.push_back(-1);
	            else if (iter1->second == iter2->second) result.push_back(1);
	            else
	            {
	                int id1 = iter1->second, id2 = iter2->second;
	                double res = bfs(id1, id2, eqMap);
	                result.push_back(res);
	                if (res == -1) continue;
	                eqMap[id1][id2] = res;
	                if (res != 0) eqMap[id2][id1] = 1/res; 
	            }
	        }
	        
	        return result;
	    }
	    
	    double bfs(int id1, int id2, 
	               unordered_map<int, unordered_map<int, double>> &eqMap)
	    {
	        set<int> visited;
	        queue<pair<int, double>> myQ;
	        myQ.push({id1, 1});
	        visited.insert(id1);
	        while (myQ.size() != 0)
	        {
	            int len = myQ.size();
	            for (int i = 0; i < len; ++i)
	            {
	                int curr = myQ.front().first;
	                double curr_res = myQ.front().second;
	                if (eqMap.find(curr) == eqMap.end()) continue;
	                unordered_map<int, double> &nei = eqMap[curr];
	                auto shortCut = nei.find(id2);
	                if (shortCut != nei.end()) return curr_res * shortCut->second;
	                for (auto iter = nei.begin(); iter != nei.end(); ++iter)
	                {
	                    if (visited.find(iter->first) == visited.end())
	                    {
	                        myQ.push({iter->first, curr_res * iter->second});
	                        visited.insert(iter->first);
	                    }
	                }
	                myQ.pop();
	            }
	        }
	        return -1;
	    }
	};
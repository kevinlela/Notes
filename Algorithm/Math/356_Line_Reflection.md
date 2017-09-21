### Line Reflection
Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

Example 1:
Given points = [[1,1],[-1,1]], return true.

Example 2:
Given points = [[1,1],[-1,-1]], return false.

Follow up:
Could you do better than O(n2)?

[leetcode](https://leetcode.com/problems/line-reflection/description/)

### Answer
we do not need to consider odd and even number for reflection 

	class Solution {
	public:
	    bool isReflected(vector<pair<int, int>>& points) {
	        if (points.size() == 0) return true;
	        unordered_map<double, unordered_set<double>> p;
	        for (int i = 0; i < points.size(); ++i)
	            p[points[i].second].insert(points[i].first);
	        
	        double mid = cal_mid_based_first(p);
	        for (auto it = p.begin(); it != p.end(); ++it)
	        {
	            if (!is_ref(it->second, mid)) return false;
	        }
	        
	        return true;
	    }
	    
	    bool is_ref(unordered_set<double> &line, double mid)
	    {
	        unordered_set<double> pos;
	        unordered_set<double> neg;
	        for (auto it = line.cbegin(); it != line.cend(); ++it)
	        {
	            double diff = *it - mid;
	            if (diff > 0) pos.insert(diff);
	            else if (diff < 0) neg.insert(diff);
	        }
	        
	        if (pos.size() != neg.size()) return false;
	        
	        for (auto it = pos.begin(); it != pos.end(); ++it)
	        {
	            if (neg.find(-*it) == neg.end()) return false;
	        }
	        
	        return true;
	    }
	    
	    double cal_mid_based_first(const unordered_map<double, unordered_set<double>> &p)
	    {
	        // cacluate the y
	        double sum = 0;
	        int count = 0;
	        auto ps = p.cbegin();
	        for (auto it = ps->second.cbegin(); it != ps->second.cend(); ++it)
	        {
	            sum += *it;
	            ++count;
	        }
	        
	        return sum/count;
	    }
	};
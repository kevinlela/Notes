### Convex Polygon
Given a list of points that form a polygon when joined sequentially, find if this polygon is convex (Convex polygon definition).

Note:

There are at least 3 and at most 10,000 points.
Coordinates are in the range -10,000 to 10,000.
You may assume the polygon formed by given points is always a simple polygon (Simple polygon definition). In other words, we ensure that exactly two edges intersect at each vertex, and that edges otherwise don't intersect each other.

[leetcode](https://leetcode.com/problems/convex-polygon/description/)

### Answer
	class Solution {
	public:
	    bool isConvex(vector<vector<int>>& points) {
	        int len = points.size();
	        int sign = 0;
	        for (int i = 0; i < len; ++i)
	        {
	            int prev = i == 0 ? len - 1: (i-1), next = (i + 1) % len;
	            pair<int, int> p1 = {points[prev][0] - points[i][0], points[prev][1] - points[i][1]};
	            pair<int, int> p2 = {points[next][0] - points[i][0], points[next][1] - points[i][1]};
	            int det = p1.second*p2.first - p1.first*p2.second;
	            if (det == 0) continue;
	            if (sign == 0) sign = det;
	            else if (sign > 0 && det < 0) return false;
	            else if (sign < 0 && det > 0) return false;
	            else sign = det;
	        }
	        return true;
	    }
	};
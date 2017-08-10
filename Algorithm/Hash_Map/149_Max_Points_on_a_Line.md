### Max Points on a Line
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

[leetcode](https://leetcode.com/submissions/detail/104682549/)
Brutal force, fix two points and search the third on which is on this line O(N^3)
Hash map, fix one point and store gradient to each key of a hash map O(N^2)
GCD needs to remember b' = a%b, a = b, b = b';

### Answer 
	/**
	 * Definition for a point.
	 * struct Point {
	 *     int x;
	 *     int y;
	 *     Point() : x(0), y(0) {}
	 *     Point(int a, int b) : x(a), y(b) {}
	 * };
	 */
	class Solution {
	public:
	    int maxPoints(vector<Point>& points) {
	        int num = points.size();
	        int result = 0;
	        for (int k = 0; k < num; ++k)
	        {
	            unordered_map<int, unordered_map<int, int>> counts;
	            counts[0][0] = 1;
	            int maxHere = 0;
	            for (int j = k + 1; j < num; ++j)
	            {
	                int dx = points[k].x - points[j].x;
	                int dy = points[k].y - points[j].y;
	                mappingPt(dx, dy);
	                ++counts[dx][dy];
	                if (dx != 0 || dy != 0) maxHere = max(maxHere, counts[dx][dy]);
	            }
	            result = max(result, maxHere + counts[0][0]);
	        }
	        
	        return result;
	    }
	    
	    void mappingPt(int &dx, int &dy)
	    {
	        int gcdRec = gcd(abs(dx), abs(dy));
	        dx /= gcdRec;
	        dy /= gcdRec;
	        if (dx == 0) dy = abs(dy);
	        else if (dy == 0) dx = abs(dx);
	        else if (dx < 0 && dy < 0)
	        {
	            dx = -dx;
	            dy = -dy;
	        }
	        else if (dx < 0)
	        {
	            dx = -dx;
	            dy = -dy;
	        }
	    }
	    
	    int gcd(int a, int b)
	    {
	        if (a == 0 && b == 0) return 1;
	        if (a == 0) return b;
	        if (b == 0) return a;
	        
	        if (a < b) return gcd(b, a);
	        
	        while (b)
	        {
	            int tmp = b;
	            b = a % b;
	            a = tmp;
	        }
	        
	        return a;
	    }
	};
### Rectangle Area
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

[leetcode](https://leetcode.com/problems/rectangle-area/description/)

### Answer 

	class Solution {
	public:
	    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H)
	    {
	        int all = (C - A) * (D - B) + (G - E) * (H - F);
	        return all - getSide(A, C, E, G) * getSide(B, D, F, H);
	    }
	    
	    int getSide(int a_0, int b_0, int a_1, int b_1)
	    {
	        if (a_0 < a_1)
	        {
	            if (b_0 < a_1) return 0;
	            else if (b_0 <= b_1) return b_0 - a_1;
	            else return b_1 - a_1;
	        }
	        else if (a_0 <= b_1)
	        {
	            if (b_0 <= b_1) return b_0 - a_0;
	            else return b_1 - a_0;
	        }
	        
	        return 0;
	    }
	};
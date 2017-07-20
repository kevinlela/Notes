shuffle an array

int len = d_nums.size();  
for (int i = 0; i < len; ++i)  
{  
    swap(d_nums[i], d_nums[i + rand() % (len - i)]);  
}  

why?

1) The 1 element has 1/len prob to be chosen

2) the second element has 
    P = (not in the first)*(select as second)  
      = (len-1)/len * 1/(len-1)  
      = 1/len  
3) the third element has
    P = (not in the first two)*(select as third)
      = (len-2)/len * 1/(len-2)
      = 1/len

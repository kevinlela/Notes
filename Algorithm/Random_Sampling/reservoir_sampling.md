* Create an array reservoir[0..k-1] and copy first k items of stream[] to it.
* Now one by one consider all items from (k+1)th item to nth item.
  Generate a random number from 0 to i where i is index of current item in stream[]. Let the generated random number is j.
  If j is in range 0 to k-1, replace reservoir[j] with arr[i]

why?

Choose 1, 2, 3, ..., k first and put them into the reservoir.
* At K + 1. P(i is selected at k + 1) = P(i is selected at k)\*p(k+1 is not selected and replace i)

* p(i is selected at k) = 1
* p(k+1 is selected) = k / (k+1)
* p(k+1 replace i) = 1/k
* p(k+1 not selected or not replace i) = 1 - [k / (k+1)] * [1/k] = k / (k + 1)
* p(i is selected at k + 1)  =  1 * k / (k + 1) = k / (k + 1)

* At k + 2
* p(i is selected at k + 1) = k / (k + 1)
* p(k+2 is selected) = k / (k+2)
* p(k+2 replace i) = 1/k
* p(k+2 not selected or not replace i) = 1 - [k / (k+2)] * [1/k] = (k + 1) / (k + 2)
* p(i is selected at k + 2)  =  [k / (k + 1)] * [(k + 1) / (k + 2)] = k / (k + 2)

* so at n: p(i is selected at n) = k / n

Choose 3 numbers from [111, 222, 333, 444]. Make sure each number is selected with a probability of 3/4
First, choose [111, 222, 333] as the initial reservior
Then choose 444 with a probability of 3/4
For 111, it stays with a probability of
P(444 is not selected) + P(444 is selected but it replaces 222 or 333)
= 1/4 + 3/4\*2/3
= 3/4
The same case with 222 and 333
Now all the numbers have the probability of 3/4 to be picked
THIS PROBLEM <LINKED LIST RANDOM NODE>

This problem is the sp case where k=1

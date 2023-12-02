# 0x00. Pascal's Triangle


Pascal’s Triangle is a kind of number pattern. Pascal’s Triangle is the triangular arrangement of numbers that gives the coefficients in the expansion of any binomial expression. The numbers are so arranged that they reflect as a triangle. Firstly, 1 is placed at the top, and then we start putting the numbers in a triangular pattern. The numbers which we get in each step are the addition of the above two numbers.


## Task
0. Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer



## Pattern Consideration 
```
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
```
1. when the index of the row and column is not thesame consider this 
- when the col is at index 1 the result to be appended is 1
- append the result of the previous row and col using the arithmetic operation
```
array[row-1][col] + array[row-1][col-1]
```
2. when the index of the row and column are same the result to be appended is 1

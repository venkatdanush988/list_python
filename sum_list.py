***
Write a program to find the sum of the elements in the array. 
Input Format: 
Input consists of n+1 integers where n corresponds to the number of elements in the array.
The first integer corresponds to n and the next n integers correspond to the elements in the array.
Assume that the maximum number of elements in the array is 20. 
Output Format: 
Output consists of a double value which corresponds to the mean of the array.
Refer sample input and output for formatting specifications.
Sample Input: 
5
2
4
1
3
1
Sample Output:
11

***
# Input reading
n = int(input().strip())
elements = []

# Read the elements into the array
for _ in range(n):
    element = int(input().strip())
    elements.append(element)

# Calculate the sum of the elements
total_sum = sum(elements)

# Output the result
print(total_sum)

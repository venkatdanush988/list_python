***
Write a Python Program to find the largest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
6

***
# Input reading
size = int(input().strip())
elements = []

# Read the elements into the list
for _ in range(size):
    element = int(input().strip())
    elements.append(element)

# Find the largest number in the list
largest_number = max(elements)

# Output the largest number
print(largest_number)

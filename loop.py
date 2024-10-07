"""Nested loops allow for more complex iterations and data processing.

grid_list = [
[[0,0],[0,1],[0,2]],
[[1,0],[1,1],[1,2]],
[[2,0],[2,1],[2,2]]
]
_CHALLENGE_

- **Task 3.1:** Write a nested `for` loop that prints a 3x3 grid of numbers (i.e., rows and columns of numbers from 0 to 2).
  ^^ skip task 3.1
- **Task 3.2:** Using nested loops, write a program to print the multiplication table for numbers 1 through 5.
"""

nested_list = []

for i in range(3):
	ind_list = []
	for j in range(3):
		ind_list.append([i, j])
	nested_list.append(ind_list)

for i in nested_list:
	print(i)

	

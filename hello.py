print("Hello World!")



# "8 8 Bi fk8h B 8 BB8B B B  B888 c hl8 BhB fd" -> "88Bifk8hB8BB8BBBB888chl8BhBfd"

def no_space(x):
	return x.replace(" ", "")

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
def solution(number):
	sum = 0
	for i in range(0, number):
		if i % 3 == 0 or i % 5 == 0:
			sum += i
	return sum
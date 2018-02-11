# Define a procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

''' way 1 '''
def find_element_1(stack,key):
	pos = -1
	for index in range(0,len(stack)):
		if stack[index] == key:
			pos = index
			break
	return pos

''' way 2 '''
def find_element(stack,key):
	if key not in stack: return -1
	return stack.index(key)

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1
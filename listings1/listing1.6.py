# List of number
nums = [5,10,1,60,25,3]
# Showing contents of the list
print("List of numbers:", nums)
# Length of the list
print("Length of list: ", len(nums))
# First element
print("First element in list: ", nums[0])
# Last element
print("Last element in list: ", nums[-1])
# Maximum value
print("Maximum element in list: ", max(nums))
# Minimum value
print("Minimum element in list: ", min(nums))
# Sum
print("Sum", sum(nums))
# Reversed list
print("Reversed list", list(reversed(nums)))
# Sort by ascending values
print("Sort by ascending", sorted(nums))
# Sort by descending value
print("Sort by descending", sorted(nums, reverse=True))
# Original list
print("Original list", nums)
# Changing the value of a list item
nums[1]="text"
print("After the changes have been made", nums)
# Getting a cut
print("Getting a cut", nums[1: len(nums)-1])
# Replacing part of list elements
nums[1:-1]=["A", "B"]
print("After replacing the elements", nums)
# List of numbers from 5 to 10
nums=list(range(5,11))
print("List of numbers from 5 to 10", nums)
# Removing items from the list
nums[2:4]=[]
print("After removing two items from the list", nums)
# Removing the last element
del nums[len(nums)-1]
print("After removing the last item from the list", nums)
# Odd numbers
nums=[2*k+1 for k in range(10)]
print("Odd numbers", nums)
# List of symbols is created based on the text
symbs=list("Python")
# Showing contents of the list
print("List of symbols", symbs)
# The first two symbols
print("The first two symbols", symbs[:2])
# Others symbols
print("Others symbols", symbs[2:])
arr=[1,2,3,4,5]
print("List 5-10", list(range(3,5)))
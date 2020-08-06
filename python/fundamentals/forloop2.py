# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(arr):
    for i in range(len(arr)):
        if arr[i]>0:
            arr[i]='big'
    return arr
print(biggie_size([-5,-6,8,9,-6,-5]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def count_positives(number):
    Count = 0
    for i in number:
        if i > 0:
            Count += 1
    number[len(number)-1] = Count
    return number
print([-2,-2,3,4,2])
print(count_positives([-2,-2,3,4,2]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def sum_total(total):
    sum = 0
    for i in total:
        sum += i
    return sum
print(sum_total([1,2,3,5]))

# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

def average(avg):
    sum = 0 
    for i in avg:
        sum += i
    return (sum/len(avg))
print(average([2,4,6]))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

def length(numbers):
    return len(numbers)
print(length([1,1,1,1,1,4]))
print(length([1,1]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def minimum(numbers):
    if len(numbers)<0:
        return False
    minInt = numbers [0]
    for val in numbers:
        if val<minInt:
            minInt = val
    return minInt
print(minimum([2,3,4,-5]))

# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def minimum(numbers):
    if len(numbers)<0:
        return False
    minInt = numbers [0]
    for val in numbers:
        if val>minInt:
            minInt = val
    return minInt
print(minimum([2,3,4,-5]))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(numbers):
    my_dictionary = {'sumTotal': 0, 'average': 0, 'minimum': numbers[0], 'maximum': numbers[0], 'length': len(numbers)}
    for val in numbers:
        if my_dictionary['minimum']<val:
            my_dictionary['minimum'] = val
        if my_dictionary['maximum']>val:
            my_dictionary['maximum'] = val
        my_dictionary['sumTotal']+= val
        my_dictionary['average']=my_dictionary['sumTotal']/len(numbers)
    return my_dictionary
print(ultimate_analysis([5,2,3,4,6,7,8]))

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(numbers):
    for i in range(0, (len(numbers)-1)//2):
        temp = numbers[i]
        numbers[i] = numbers[len(numbers)-1-i]
        numbers[len(numbers)-1-i] = temp
    return numbers
print(reverse_list([5,4,3,2,1]))
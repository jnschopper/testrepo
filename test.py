x = range(3,10)
y = range(1,3)

list1 = [1,2,3,4]
list2 = [3,4,5,6,7]

list3 = list1 + list2

list3.append('hello') # adds pme thing to the list at the end
print(list3)

tuple1 = (1,2,3,4)
tuple2 = (3,4,5,6,7)

tuple3 = tuple1 + tuple2
tuple3 = tuple3 + tuple('hello')
print(tuple3)

my_numbers = [3,1,4,1,5,9]
def sum_of_list(numbers):
    '''sums the numbers in a list'''
    sum = 0
    for number in numbers:
        sum += number
    return sum

#product of a list
def product_of_list(numbers):
    '''finds the product of numbers in a list'''
    product = 1
    for number in numbers:
        product *= number
    return product


#determine if all values in a list are even
#build a list of perfect squares
#rotate some values
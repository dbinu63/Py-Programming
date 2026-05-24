list_a, elements = [], 0 # list size is not set at init, python allocates memory dynamically & automatically, can also be left empty

elements = int(input("How many elements would you like to sort: ")) # replace w/ enter exit conditional
print("Enter the elements you want to sort through: ")
for e in range(0, elements):
    list_a.append(int(input(f"{e + 1}: "))) # does not automatically end and store buffer when space char is encountered
    # Despite python's automatic dynamic memory management and the list's mutable nature, you cannot simply set list_a[e] to int(input(...)). 
    # print(len(list_a)) memory increases accordingly

print("Current list: ")
for e in range(0, elements):
    print(list_a[e])

for e in range(0, elements - 1):
    if (list_a[e] > list_a[e + 1]):
        list_a[e], list_a[e + 1] = list_a[e + 1], list_a[e] # called 'tuple unpacking', simplifies var. value swapping

'''
list_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(print(len(list_a)))

post = len(list_a)
print(list_a[post]) # returns IndexError & quits

# len counts the number of elements in the list
# print has None return type
'''
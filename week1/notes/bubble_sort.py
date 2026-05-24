list_a, elements = [], 0 # list size is not set at init, python allocates memory dynamically & automatically, can also be left empty

elements = int(input("How many elements would you like to sort: "))
print("Enter the elements you want to sort through: ")
for e in range(0, elements):
    list_a.append(int(input(f"{e + 1}: "))) # does not automatically end and store buffer when space char is encountered
    # Despite python's automatic dynamic memory management and the list's mutable nature, you cannot simply set list_a[e] to int(input(...)). 
    print(len(list_a)) # memory increases accordingly



'''
list_a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(print(len(list_a)))

# len counts the number of elements in the list
# print has None return type
'''
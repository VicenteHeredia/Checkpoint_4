# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
print()

list = ['bravo', 'alpha', 'delta', 'charlie', 'echo']
print(list)
print()

tuple = ('alpha', 'bravo', 'charlie', 'delta', 'echo')
print(tuple)
print()

float = 2.34
print(float)
print()

integer = 2
print(integer)
print()

decimal = 2.34567891
print(decimal)
print()

dict = {
    'alpha': ['a', 'l', 'p', 'h', 'a']
    }
print(dict)
print()

# Exercise 2: Round your float up.
import math
print(math.ceil(float))
print()

# Exercise 3: Get the square root of your float.
print(math.sqrt(float))
print()

# Exercise 4: Select the first element from your dictionary.
print(dict['alpha'][0])
print()

# Exercise 5: Select the second element from your tuple.
print(tuple[1])
print()

# Exercise 6: Add an element to the end of your list.
new_list = list+['foxtrot']
print(new_list)
print()

# Exercise 7: Replace the first element in your list.
list [0] = 'golf'
print(list)
print()

new_list [0] = 'golf'
print(new_list)
print()

# Exercise 8: Sort your list alphabetically.
list.sort()
print(list)
print()

new_list.sort()
print(new_list)
print()

# Exercise 9: Use reassignment to add an element to your tuple.
tuple = tuple+('hotel',)
print(tuple)
print()

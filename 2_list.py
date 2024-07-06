fruits=['apple', 'orange', 'banana']

# print(fruits)

'''
fruits=   0        1       2
        apple   orange  banana
'''

# print(fruits[1])

#### max, min of list
age_list=[45,37,23,55,25,50]
# print(max(age_list))
# print(min(age_list))

# fruits=['apple', 'orange', 'banana']

# fruits.append("Cherry")
# print(fruits)

# fruits.pop()
# print(fruits)

# fruits.remove("orange")
# print(fruits)



### slicing
fruits=["apple", "banana", "charry", "Mango", "Jackfruit","Litchi"]
'''
            0       1           2       3           4       5
fruits=["apple", "banana", "charry", "Mango", "Jackfruit","Litchi"]

'''

print(fruits[0:6])  # Slice from index 0 to 4   = "apple", "banana", "charry", "Mango", "Jackfruit","Litchi"
print(fruits[0:])   # slice from 0 to last      = "apple", "banana", "charry", "Mango", "Jackfruit","Litchi"

print(fruits[1:4])  #slice from index 1 to 3    = "banana", "charry", "Mango"

print(fruits[:4])   # slice from 0 to 3         = "apple", "banana", "charry", "Mango"
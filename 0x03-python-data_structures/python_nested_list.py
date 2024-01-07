my_list = [3.5, 10, "code", [1, 2, 3], 8]

# add element to the end of the list
# my_list.append(12)
# print('{}'.format(my_list))

# add element at a specific position in a list
# my_list.insert(0, "Hello")
# print("{}".format(my_list))

# remove the first occurrence of a specified element from a list
# my_list.remove("code")
# print("{}".format(my_list))

# remove element at a specified position in a list and return it
# element = my_list.pop(2)
# print("{}".format(element))
# print("{}".format(my_list))

# sort elements in a list in ascending order and returns it. (form highest to lowest)
# my_list = [0, 3, 5, 7, 0, 3, 5, 5]
# ascending_order = sorted(my_list) # this line sorts the list without modifying the original list
# print("{}".format(ascending_order))
# my_list.sort() # this line sorts the list by modifying the original list
# print("{}".format(my_list))

# reverse the order of a list
# print("{}: {}\n".format("Original list", my_list))
# my_list.reverse()
# print("{}: {}".format("Reversed list", my_list))

# count the number of times a specified element appears in a list
# my_list = [2, 4, 56, 56, 45, 32, 2]
# appearance = my_list.count(56)
# print("{} {} {}".format("the element appeared", appearance, "times"))

# return the index of the first occurrence of a specified element in a list
# first_occurrence = my_list.index("code")
# print("{}".format(first_occurrence))

# extend a list by appending a list from another iterable
# bacteriology_RAs = ["Basit", "Amanda", "Ishaq"]
# bacteriology_PIs = ["Prof. Dorothy", "Dr. Asante-Poku", "Dr. Asare"]
# bacteriology_RAs.append(bacteriology_PIs)
# print("{}".format(bacteriology_RAs))

# AND THAT WOULD BE ALL FOR NOW



# A LIST WITHIN A LIST
# Python nested lists

# example of a nested list
# my_list = [[22, 14, 16], ["Joe", "Sam", "Abel"], [True, False, True]]

# print("{}".format(my_list[0])) # prints a sublist
# print("{}".format(my_list[0][0])) # prints an element within a sub-list
# my_list[0][0] = 20 # modifies an element within a sub-list
# print("{}".format(my_list))


# How to initialise a nested list
# 1. Using python's range() function

# my_list = [[] for i in range(5)]
# print("{}".format(my_list)) # This line creates a nested with 5 nested lists all having different ids


# Using a for loop
# first create an empty list
# my_list = []

# for i in range(4):
#     my_list.append([])

# print("{}".format(my_list))
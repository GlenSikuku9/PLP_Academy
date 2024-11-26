
# 1)Create an empty list
my_list=[]

# 2)Append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)


# 3)Insert the value 15 at the second position (index 1)
my_list.insert(1,15)

# 4)Extend my_list with another list
my_list.extend([50,60,70,80])

# 5)Remove the last element from my_list
my_list.pop()

# 6)Sort my_list in ascending order
my_list.sort()

# 7)Find and print the index of the value 30
index_of_30=my_list.index(30)
print("The index of the value 30 is:",index_of_30)

# 8)Print the final list
print("Final list:", my_list)

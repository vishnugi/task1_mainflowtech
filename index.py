#Declaring dictionaries
my_dict = {"1": "apple", "2":"banana"}
print(my_dict)
#Adding a key-value pair to the dictionary
my_dict[3]="orange"
print(my_dict)
#Removing  a value with its corresponding key from the dictionary
my_dict.pop("1")
print(my_dict)
#To know the length of the dictionary
print(len(my_dict))


#-------------------------------------------------------------------------------------

#Creating a list 
my_list=["apple", "banana","cherry"]
print(my_list)
#Accessing elements in the list by index
print(my_list[1])
#Append  an element at the end of the list
my_list.append("orange")
print(my_list)
#Insert an element at any given position in the list
my_list.insert(0,"grape")
print(my_list)
#Remove an element from the list using its index
del my_list[2]
print(my_list)

#--------------------------------------------------------------------------------------------------
#Declaring set
my_set={"pen","book","pencil","book"}
print(my_set)
#Appending  an element to the set
my_set.add("eraser")
print(my_set)
#Removing  an element from the set
my_set.remove("pen")
print(my_set)
#To find the length of the set
print(len(my_set))



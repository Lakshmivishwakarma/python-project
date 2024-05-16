# # 1. Write a  Python script to concatenate the following dictionaries to create a new one.
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
# dic4 = {}
# for d in (dic1, dic2, dic3):
#     print(d)
#     dic4.update(d)
# print(dic4)

# # 2. Check whether a given key already exists in a dictionary
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#
#
# def is_key_present(x):
#     if x in d:
#         print('Key is present in the dictionary')
#     else:
#         print('Key is not present in the dictionary')
#
# # Call the 'is_key_present' function with the argument 5 to check if 5 is a key in the dictionary.
#
#
# is_key_present(5)

# # 3.Iterate over dictionaries using for loops
# d = {'x': 10, 'y': 20, 'z': 30}
# for dict_key, dict_value in d.items():
#     print(dict_key, "-",  dict_value)

# # 4.Generate and print a dictionary that contains a number in the form (x, x*x)
# n = int(input("enter a number"))
# new_dict = {}
# for i in range(1, n + 1):
#     new_dict[i] = i*i
# print(new_dict)

# # 5.Print a dictionary where the keys are numbers between 1 and 15 and the values are square of keys
# new_dict = {}
# for i in range(1, 16):
#     new_dict[i] = i * i
# print(new_dict)


# # 6.Merge two Python dictionaries
# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
# new_dict = d1.copy()
# new_dict.update(d2)
# print(new_dict)

# # 7.Sum all the items in a dictionary
# my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
# sum_value = sum(my_dict.values())
# print(sum_value)

# # 8.Multiply all the items in a dictionary
# my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
# result = 1
# for key_value in my_dict:
#     result = result * my_dict[key_value]
# print(result)

# # 9.Remove a key from a dictionary
# my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(my_dict)
# if 'a' in my_dict:
#     del my_dict['a']
#
# print(my_dict)


# # 10. Sort a dictionary by key
# d = {1: 10, 3: 20, 2: 30, 5: 40, 6: 50, 4: 60}
# for key in sorted(d):
#     print("%s: %s" % (key, d[key]))


# # 11.Drop empty Items from a given Dictionary
# dict1 = {'c1': 'Red', 'c2': 'Green', 'c3': None}
# dict2 = {key: value for (key, value) in dict1.items() if value is not None}
# print(dict2)
#
# # 12.Remove a specified dictionary from a given list
# colors = [
#     {"id": "#FF0000", "color": "Red"},
#     {"id": "#800000", "color": "Maroon"},
#     {"id": "#FFFF00", "color": "Yellow"},
#     {"id": "#808000", "color": "Olive"}
# ]
# new_list = []
# r_id = "#FF0000"
# for i in colors:
#     print(i)
#     if r_id != i.get("id"):
#         new_list.append(i)
#
# print(new_list)

# # 13.Update the list values within a given dictionary
# marks = {
#     'Math': [88, 89, 90],
#     'Physics': [92, 94, 89],
#     'Chemistry': [90, 87, 93]
# }
#
# for i in marks:
#     print(i)
#     if i == "Math":
#         marks[i] = [x + 1 for x in marks[i]]
#     if i == "Physics":
#         marks[i] = [x - 2 for x in marks[i]]
#
# print(marks)


# # 14.Filter even numbers from a given dictionary values
# students = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# new_dict = {}
# for i, j in students.items():
#     print(i, j)
#     new_list = []
#     for x in j:
#         print(x)
#         if x % 2 != 0:
#             new_list.append(x)
#     new_dict[i] = new_list
# print(new_dict)
#

# # 15.Create a flat list of all the values in a flat dictionary
# students = {
#     'Theodore': 19,
#     'Roxanne': 20,
#     'Mathew': 21,
#     'Betty': 20
# }
#
# my_list = []
# for i, j in students.items():
#     my_list.append(j)
# print(my_list)

# # 16.Create a flat list of all the keys in a flat dictionary
#
# students = {
#     'Theodore': 19,
#     'Roxanne': 20,
#     'Mathew': 21,
#     'Betty': 20
# }
#
# my_list = []
# for key, value in students.items():
#     my_list.append(key)
# print(my_list)
#

# # 17.Convert a given dictionary to a list of tuples
# d = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# tuple_list = list(d.items())
# print(tuple_list)

# # 18.Combine two lists into a dictionary, where the elements of the first one serve as the keys and the elements of the second one serve as the values
# list1 = ['a', 'b', 'c', 'd', 'e', 'f']
# list2 = [1, 2, 3, 4, 5]
# new_dict = dict(zip(list1, list2))
# print(new_dict)

# 19.Find all keys in the provided dictionary that have the given value
# students = {
#     'Theodore': 19,
#     'Roxanne': 20,
#     'Mathew': 21,
#     'Betty': 20
# }
# check_value = 20
# new_dict = {}
# for i, j in students.items():
#     print(i, j)
#     if j == check_value:
#         new_dict[i] = j
# print(new_dict)


# # 20. Filter a dictionary based on values
# marks = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# above_marks = 175
# new_dict = {}
# for i, j in marks.items():
#     print(i, j)
#     if j >= above_marks:
#         new_dict[i] = j
#
# print(new_dict)

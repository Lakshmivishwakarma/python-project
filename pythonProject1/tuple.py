# #1. Removing duplicates from tuple
# test_tup = (1, 3, 5, 2, 3, 5, 1, 1, 3)
# print(test_tup)
# result = tuple(set(test_tup))
# print(result)

# #2.Adding Tuple to List and vice – versa
# test_list = [5, 6, 7]
# test_tup = (9, 10)
# add_tuple = tuple(test_list + list(test_tup))
# print(add_tuple)

# #3 Python program to concatenate tuples to make a nested tuple
#
# tpl1 = (1, 2, 3)
# tpl2 = (20, 30, 10)
# result = (tpl1,) + (tpl2,)
# print(result)


# #4. Python program to sort the nested tuple using the sorted() function
# students = ((1, "Alex", 21), (3, "Bobby", 20), (2, "Christina", 19))
# print(sorted(students, reverse=True))

# #5. Python program to record similar tuple occurrence
# tupList = [(9, 5), (0, 2), (3, 3), (9, 5), (3, 3)]
# dict_data = {}
# for i in tupList:
#     print(i)
#     if i in dict_data:
#         dict_data[i] += 1
#     else:
#         dict_data[i] = 1
#
# print(dict_data)


# #6.Finding the maximum difference between tuple pairs
# tupList = [(5, 7), (6, 2), (1, 9), (1, 3)]
# diff_list = []
# for i in tupList:
#     # abs is using for convert negative no in positive no.
#     res = abs(i[0]-i[1])
#     diff_list.append(res)
#
# difference = sorted(diff_list, reverse=True)
# print("maximum difference between tuple pairs is :", difference[0])


# #7.Filtering tuples according to list element
#
# tup1 = [(2, 9), (5, 6), (1, 3), (4, 8)]
# filter_tuples = [2, 3]
# tup_list = []
# for i in tup1:
#     for j in filter_tuples:
#         if j in i:
#             tup_list.append(i)
#
# print(tup_list)

# #8.Check if Two Lists of tuples are identical or not
# tupList1 = [(2, 9), (6, 1)]
# tupList2 = [(2, 9), (5, 1)]
# tupList2 = [(2, 9), (5, 1)]
# tupList2 = [(2, 9), (5, 1)]
# isIdentical = tupList1 == tupList2
#
# if isIdentical:
#     print("Identical")
# else:
#     print("Not identical")

# #9.Flatten tuple list to string
#
# myTuple = (4, 1, 7, 8, 9, 5)
# adj_dict = {}
# for idx in range(0, len(myTuple), 2):
#     adj_dict[myTuple[idx]] = myTuple[idx + 1]
#
# print(adj_dict)

# # 10.Checking if the tuple has any None Value
# myTup = (4, 8, None, 2)
# hasNone = not all(myTup)
# if hasNone:
#     print("The tuple has None Value")
# else:
#     print("The tuple has not any None Value")

# # 11.Maximum value in record list as tuple attribute
# tupleList = [('scala', [7, 2, 9]), ('Java', [1, 5, 2]), ('Python', [9, 3, 1])]
# new_tuple = []
# for i, recordList in tupleList:
#     print(i, recordList)
#     a = (i, max(recordList))
#     new_tuple.append(a)
# print(new_tuple)

# #12. Checking if the element is present in tuple
#
# myTuple = (5, 2, 7, 9, 1, 4)
# ele = 9
# is_present = False
# for i in myTuple:
#     if i == ele:
#         is_present = True
#         break
#
# if is_present:
#     print("The element is present in tuple")
# else:
#     print("The element is not present in tuple")

# # 13.Index Minimum Values Record
# # find the minimum value using the min()
# tupList = [('python', 51), ('Scala', 98), ('C/C++', 23)]
# min_val = min(tupList)
# print(min_val)
# print("the minimum value is ", min_val[0])

# # 14.Extracting unique elements in nested tuple
# my_tuple = [(4, 6, 9), (1, 5, 7), (3, 6, 7, 9)]
# new_tuple = []
# for i in my_tuple:
#     print(i)
#     for j in i:
#         print(j)
#         if j not in new_tuple:
#             new_tuple.append(j)
#
# print(new_tuple)
#
# # 15. Updating Each element in Tuple List
# my_tuple = [(12, 8), (5, 2), (1, 3, 7, 8)]
# ele = 6
# new_list = []
# for i in my_tuple:
#     a = []
#     for j in i:
#         # print(j)
#         b = ele + j
#         a.append(b)
#     new_list.append(tuple(a))
#
# print(new_list)
#
# # 16. Filtering Range Length Tuples
# tupList = [(5, 7), (4, 1, 8), (5, 8, 0), (1, 2, 3, 4, 5, 7)]
# i, j = 2, 3
# new_tup = []
# for tup in tupList:
#     print(type(tup))
#     if i <= len(tup) <= j:
#         new_tup.append(tup)
#
# print(new_tup)

# # 17.Finding the sum of tuple elements
# myTuple = (7, 8, 9, 1, 10, 7)
# tuple_sum = 0
# for i in myTuple:
#     print(i)
#     tuple_sum = tuple_sum + i
# print(tuple_sum)
#
# # 18.Get an item of a tuple
# tuple_data = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
# print(tuple_data)
# item = tuple_data[3]
# print(item)
# item1 = tuple_data[-4]
# print(item1)

# # 19.Write a Python program to replace the last value of tuples in a list.
# tuple_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# new_list = []
# for i in tuple_list:
#     print(i)
#     a = i[:-1] + (100,)
#     new_list.append(a)
# print(new_list)

# # 20.Average value of the numbers in a given tuple of tuples
# nums = ((10, 10, 10, 13), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
# average_list = []
# for i in nums:
#     sum_value = 0
#     for j in i:
#         sum_value += j
#
#     average = sum_value/2
#     average_list.append(average)
# print(average_list)

# # 21.Unpack a tuple in several variables
# tuple_list = 4, 8, 3
# print(tuple_list)
# # Unpack the values from the tuple into the variables n1, n2, and n3
# n1, n2, n3 = tuple_list
# print(n1 + n2 + n3)

# # 22.Repeated items of a tuple
# tuple_item = 2, 4, 5, 6, 2, 3, 4, 4, 7
# count = tuple_item.count(2)
# print(count)

# # 23.Python program to slice a tuple.
# tuple_item = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)
# new_tuple = tuple_item[3:5]
# print(new_tuple)
# new_tuple2 = tuple_item[1:-3:2]
# print(new_tuple2)

# # 24.Write a Python program to find the index of an item in a tuple.
# tuple_item = (2, 4, 3, 5, 2, 6, 7, 8, 6, 1)
# ele_index = 2
# index = tuple_item.index(ele_index, 1)
# print(index)

# 25.program to unzip a list of tuples into individual lists.
tuple_list = [(1, 2, 5), (3, 4, 9), (8, 9, 8)]
new_tuple = list(zip(*tuple_list))
print(new_tuple)



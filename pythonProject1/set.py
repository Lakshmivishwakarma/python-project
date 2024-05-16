# # 1. set.add()
# number_of_country = int(input("enter a value"))
# country = set()
# for i in range(0, number_of_country):
#     n = input("enter country name")
#     country.add(n)
#
# print(len(country))

# #2.Add a list of elements to a set
# sample_set = {"Yellow", "Orange", "Black"}
# sample_list = ["Blue", "Green", "Red"]
# sample_set.update(sample_list)
# print(sample_set)

# # 3. Return a new set of identical items from two sets
# # intersection() or & using to get comman item in sets
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# new_set = set1.intersection(set2)
# print(new_set)

# # 4.Get Only unique items from two sets
# # union() or | using to get unique items from sets
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# union_set = set1.union(set2)
# print(union_set)

# # 5. Update the first set with items that don’t exist in the second set
# # difference_update() method is used to modify a set by removing elements that are also present in one or more specified sets.
# # This method modifies the set in place, rather than returning a new set
# set1 = {10, 20, 30}
# set2 = {20, 40, 50}
# set1.difference_update(set2)
# print(set1)

#
# # 6.Write a Python program to remove items 10, 20, 30 from the following set at once.
# set1 = {10, 20, 30, 40, 50}
# set1.difference_update({10, 20, 30})
# print(set1)

# #7.Return a set of elements present in Set A or B, but not both
# # the symmetric difference of two sets is the set of elements that are present in either of the sets, but not in both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# print(set1.symmetric_difference(set2))

# # 8.Check if two sets have any elements in common. If yes, display the common elements
# # isdisjoint() method is used to determine whether two sets have any elements in common.
# # It returns True if the sets are disjoint (i.e., they have no elements in common), and False otherwise.
# set1 = {10, 20, 30, 40, 50}
# set2 = {60, 20, 80, 90, 10}
#
# if set1.isdisjoint(set2):
#     print("Two sets have no items in common")
# else:
#     print("Two sets have items in common")
#     print(set1.intersection(set2))

# # 9.Program in Python to Print Maximum and Minimum Elements
# set1 = {15, 25, 2, 10, 11, 55}
# print("Original set elements:", set1)
# print("Maximum value of given set:", max(set1))
# print("Minimum value of given set:", min(set1))

# # 10.Python Program to Count Number of Vowels in a Given String Using Sets
# def count_vowels(str1):
#     vowels = set("aeiouAEIOU")
#     counter = 0
#     for i in str1:
#         if i in vowels:
#             counter += 1
#
#     print("Number of Vowels in Given String = ", counter)
#
#
# string1 = "hello world"
# count_vowels(string1)

# # 11.Program in Python to Find Common Elements of Three Given Lists Using Sets
# def find_common(list1, list2, list3):
#     set1 = set(list1)
#     set2 = set(list2)
#     set3 = set(list3)
#
#     res_set1 = set1.intersection(set2)
#     res_set2 = res_set1.intersection(set3)
#     end_list = list(res_set2)
#     print(end_list)
#
#
# first_list = [10, 45, 34, 20, 11]
# second_list = [11, 25, 45, 20]
# third_list = [20, 25, 11, 14, 45, 65]
#
# find_common(first_list, second_list, third_list)


# # 12.Python Program To Square the Elements of Set Using for Loop
# set1 = {0, 1, 2, 3, 4}
# res_set = set()
# for i in set1:
#     a = i*i
#     res_set.add(a)
#
# print(res_set)

# # 13.Python Program to Check if a Set Is Superset Itself or Another Given Set
# # issuperset() method is used to determine whether a set is a superset of another set.
# # A set is considered a superset of another set if it contains all the elements of the other set.
# set1 = {10, 45, 34, 20}
# set2 = {10, 45, 34, 20, 11}
# set3 = {20, 25, 11, 14, 45, 65}
#
# print("Is set1 superset of itself?:", set1.issuperset(set1))
# print("Is set2 superset of set1?:", set2.issuperset(set1))
# print("Is set3 superset of set1?:", set3.issuperset(set1))

# # 14.Python Program To Check If a Given Value is Present in Set or Not
# set1 = {10, 45, 34, 20}
# check_value = 45
# if check_value in set1:
#     print(check_value, "is present in set1")
# else:
#     print(check_value, "is not present in set1")


# # 15. remove given element from set
# set1 = {10, 45, 34, 20}
# remove_ele = 10
# set1.remove(remove_ele)
# print(set1)



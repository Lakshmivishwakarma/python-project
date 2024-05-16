# # 1. Python program to interchange first and last elements in a list
# list_elements = [12, 35, 9, 56, 24]
# size = len(list_elements)
# print(size)
# temp = list_elements[0]
# print(temp)
# list_elements[0] = list_elements[size-1]
# print(list_elements[0])
# list_elements[size-1] = temp
# print(list_elements[size-1])
# print(list_elements)


# # 2. Check if element exists in list in Python
# list_element = [1, 6, 3, 5, 3, 4]
# check_element = 60
# if check_element in list_element:
#     print("elements exists in list")
# else:
#     print("element is not exists in list")


# #3. Reversing a List in Python
# list_element = [1, 6, 3, 5, 3, 4]
# new_list = []
# for i in list_element:
#     new_list.insert(0, i)
# print(new_list)

# # 4.Python Program to Find Largest Number in a List
# list_element = [1, 6, 3, 5, 3, 14]
# list_element.sort()
# size = len(list_element)
# largest_number = list_element[size-1]
# print(largest_number)
#
# # 5.Python Program to Print Largest Even and Largest Odd Number in a List
# list_element = [1, 6, 3, 5, 3, 14]
# list_element.sort()
# odd_list = []
# even_list = []
# for i in list_element:
#     print(i)
#     if i % 2 == 0:
#         odd_list.append(i)
#     else:
#         even_list.append(i)
#
# print(odd_list, even_list)
# odd_largest = odd_list[len(odd_list)-1]
# print(odd_largest)
# even_largest = even_list[len(even_list)-1]
# print(even_largest)

# #6. Python Program to Print Sum of Negative Numbers, Positive Even Numbers and Positive Odd numbers in a List
# n = int(input("Enter the number of elements to be in the list:"))
# b = []
# for i in range(0, n):
#     a = int(input("Element: "))
#     b.append(a)
# print(b)
# sum1 = 0
# sum2 = 0
# sum3 = 0
# for j in b:
#     if j > 0:
#         if j % 2 == 0:
#             sum1 = sum1 + j
#         else:
#             sum2 = sum2 + j
#     else:
#         sum3 = sum3 + j
# print("Sum of all positive even numbers:", sum1)
# print("Sum of all positive odd numbers:", sum2)
# print("Sum of all negative numbers:", sum3)


# #7. Python Program to Count Occurrences of Element in List
# list_element = [1, 6, 3, 5, 3, 14, 3, 3]
# elements_for_count = 3
# count = 0
# for i in list_element:
#     if i == elements_for_count:
#         count = count+1
#
# print("Number of times", elements_for_count, "appears is", count)


# # 8. Python Program to Find the Sum of Elements in a List using Recursion
#
# list_element = [1, 6, 3, 5, 3, 14, 3, 3]
#
#
# def sum_list(element, size):
#     if size == 0:
#         return 0
#     else:
#         return element[size-1] + sum_list(element, size-1)
#
#
# print(sum_list(list_element, len(list_element)))


# #9. Python Program to Merge Two Lists and Sort it
#
# first_list = [1, 6, 3, 5, 3, 14, 3, 3]
# second_list = [3, 5, 6, 8, 6, 9, 7]
# merged_list = first_list + second_list
# print(merged_list)

# #10. Python Program to Remove Duplicates from a List
# n = int(input("enter the number of elements in list : "))
# list_elements = []
# for x in range(0, n):
#     print(x)
#     element = int(input("enter a number: "))
#     list_elements.append(element)
# print(list_elements)
# new_list = []
# for i in list_elements:
#     print(i)
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

#11.
# element_list = []
# element_list.insert(0, 5)
# element_list.insert(1, 10)
# element_list.insert(0, 6)
# print(element_list)
# element_list.remove(6)
# element_list.append(9)
# element_list.append(1)
# element_list.sort()
# print(element_list)
# element_list.pop()
# element_list.reverse()
# print(element_list)

# #12.Write a Python Program to Remove Multiple Empty Strings From a List of Strings
# list1 = [1, 'ABC', 2, 3, 'abc', "", 'XYZ', 4]
# while "" in list1:
#     list1.remove("")
# print(list1)

# #13.Write a Program in Python to Print Elements With Frequency Greater Than a Given Value k
#
# list1 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
# k = 2
#
# count = 0
# for i in list1:
#     if i > k:
#         count = count+1
# print(count)


# #14.
# list1 = [[1, 3], [3, 4], [5, 6]]
# list2 = [[3, 4], [5, 7], [1, 2]]
#
# print("The original list 1 : " + str(list1))
# print("The original list 2 : " + str(list2))
# res_list = []
# for i in list1:
#     if i not in list2:
#         res_list.append(i)
# for i in list2:
#     if i not in list1:
#         res_list.append(i)
#
# print("The uncommon of two lists is : " + str(res_list))

# #15. Reverse Row sort in Lists of List
# list_elements = [[8, 1, 5], [5, 8, 4], [8, 10, 8]]
#
# for ele in list_elements:
#     ele.sort(reverse=True)
#
# print("The reverse sorted Matrix is : " + str(list_elements))

#
# #16.Test if List contains elements in Range
# list_element = [4, 5, 6, 7, 3, 9]
# i, j = 3, 10
# res = True
# for ele in list_element:
#
#     if ele < i or ele >= j:
#         res = False
#         break
#
# print("Does list contain all elements in range : " + str(res))

# # 17.Find missing and additional values in two lists
# list1 = ['a', 'b', 'c', 'd', 'e', 'f']
# list2 = ['d', 'e', 'f', 'g', 'h']
# missing_value = []
# additional_value = []
# for i in list1:
#     if i not in list2:
#         missing_value.append(i)
#
# for j in list2:
#     if j not in list1:
#         additional_value.append(j)
#
# print(missing_value)
# print(additional_value)

# # 18.Insert an element before each element of a list
# color = ['Red', 'Green', 'Black']
# insert_ele = "c"
# new_list = []
# for i in color:
#     new_ele = insert_ele, i
#     print(new_ele)
#     new_list.extend(new_ele)
#
# print(new_list)

# # 19.Split a list every Nth element
# list_ele = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# new_list = []
# step = 3
# for i in range(step):
#     print(i)
#     new = list_ele[i::step]
#     print(new)
#     new_list.append(new)
# print(new_list)
#
# # 20.Write a Python program to find items starting with a specific character from a list.
# text = ["abcd", "abc", "bcd", "bkie", "cder", "cdsw", "sdfsd", "dagfa", "acjd"]
# start = "b"
#
#
# def test(item_list, char_start):
#     new_list = []
#     for i in item_list:
#         if i[0] == char_start:
#             new_list.append(i)
#     return new_list
#
#
# print(test(text, start))

# 21.Generate groups of five consecutive numbers in a list
new_list = []
for i in range(5):
    print(i)
    list_ele = []
    for j in range(1, 6):
        list_ele.append(j)
    new_list.append(list_ele)
    print(list_ele)
print(new_list)











# #1 Python program to check if a string is palindrome or not
# input_string = "malayalam"
# reverse_string = ""
# for i in input_string:
#     reverse_string = i + reverse_string
# print(reverse_string)
# if input_string == reverse_string:
#     print("this is palindrome")
# else:
#     print("This is not a palindrome")


# #2. Python program to check whether the string is Symmetrical or Palindrome
# def check_palindrome(input_string):
#     reverse_string = ""
#     for i in input_string:
#         reverse_string = i + reverse_string
#     print(reverse_string)
#     if input_string == reverse_string:
#         return "this is palindrome"
#     else:
#         return "This is not a palindrome"
#
#
# print(check_palindrome("amaama"))


# #3.Reverse words in a given String in Python
# input_string = "lakshmi"
# new_string = ""
# for i in input_string:
#     new_string = i+new_string
#
# print("new string is ", new_string)


# #4.Ways to remove i’th character from string in Python
# input_string = "malyalam"
# remove_character = 2
# new_string = ""
# for i in range(len(input_string)):
#     if i != 2:
#         new_string = new_string+input_string[i]
#
# print("new string after delete i'th character ", new_string)


# # 5. Check if a Substring is Present in a Given String
# input_string = "hello world, welcome to here"
# check_substring = "welcome"
# if check_substring in input_string:
#     print("substring is in string")
# else:
#     print("substring is not in string")

# #6. Python Program to Replace Every Blank Space with Hyphen in a String
# input_string = input("enter string")
# print(input_string)
# modified_string = input_string.replace(" ", "_")
# print(modified_string)

# # 7. Python Program to Determine How Many Times a Given Letter Occurs in a String Recursively
# input_string = input("enter a string")
# print(input_string)
# check_letter = "a"
# count = 0
# for i in input_string:
#     print(i)
#     if i == check_letter:
#         count = count+1
# print(count)


# #7.Python Program to Count the Occurrences of Each Word in a Given String sentence
# string = "hello world hello india"
# word = "hello"
# count = 0
# new_string = string.split(" ")
# print(new_string)
# for i in new_string:
#     if i == word:
#         count = count + 1
# print("count of", word, "is", count)

# #8. Python Program to Count the Number of Words and Characters in a String
# input_string = input("enter string")
# print(input_string)
# word = 1
# characters = 0
# for i in input_string:
#     characters = characters+1
#     print(i)
#     if i == " ":
#         word = word+1
# print(word)
# print(characters)
#
#
# #9. Python Program to Find Common Characters in Two Strings
#
# s1 = "This is a first string "
# s2 = "This is second string"
# new_s1 = s1.split(" ")
# new_s2 = s2.split(" ")
# print(new_s1)
# common_character = []
# for i in new_s1:
#     print(i)
#     for j in new_s2:
#         print(j)
#         if i == j:
#             common_character.append(i)
#
# print(common_character)

# 10. Python Program that Displays which Letters are in First String but not in Second
# s1 = "python"
# s2 = "library"
# letters = []
# for i in s1:
#     print(i)
#     if i not in s2:
#         letters.append(i)
# print(letters)


# #11. Converting the characters list into a string
# list1 = ['H', 'e', 'l', 'l', 'o']
# new_string = ""
# for i in list1:
#     new_string = new_string + i
#
# print(new_string)

# #12.
# string_data = "Python is a programming language"
# new_string = string_data.split(" ")
# print(new_string)
# words = []
# for i in new_string:
#     if len(i) % 2 == 0:
#         words.append(i)
# print(words)

# #13. Create multiple copies of a string by using multiplication operator
#
# string_data = "hello"
# n = 3
# new_string = string_data*n
# print(new_string)


# #14.Python program for slicing a string
# def slice_string(string, n):
#     print(len(string))
#     if len(string) < n:
#         n = len(string)
#         print(n)
#     new_string = string[:n]
#     print(new_string)
#
#
# slice_string("Chocolate", 10)


# #15. program to repeat M characters of a string N times
#
# string_data = "chocolate"
# m = 3
# n = 2
# new_string = string_data[:3]
# print(new_string)
# new_word = new_string*2
# print(new_word)


# # 16. program to remove a character from a specified index in a string
# word = "chocolate"
# idx = 1
# front = word[: idx]
# back = word[idx+1:]
# res = front+back
# print(res)

# # 17. Python program for adding given string with a fixed message
# def greeting(string):
#     if len(string) >= 5 and string[:5] == "hello":
#         return string
#     return "hello " + string
#
#
# print(greeting("hello"))

# # 18.Python program to find the matched characters in a given string
# word = str(input("Enter a string: "))
# lettersGuessed = ['a', 'e', 'i', 'k', 'p', 'r', 's', 'l']
# matched_count = 0
# for i in word:
#     if i in lettersGuessed:
#         matched_count += 1
# if matched_count == len(word):
#     print("completely In")
# else:
#     print("Not completely In")
#
# print(matched_count, "matches")

#
# # 19. program to input a string and find total number uppercase and lowercase letters
# word = "hello World"
# u_case_count, l_case_count = 0, 0
# for i in word:
#     print(i)
#     if "A" <= i <= "Z":
#         u_case_count += 1
#     if "a" <= i <= "z":
#         l_case_count += 1
#
# print("uppercase count = ", u_case_count)
# print("lowercase count = ", l_case_count)

#
# # 20. program to input a string and find total number of letters and digits
# str1 = input("enter a word")
# no_of_letters = 0
# no_of_digits = 0
# for c in str1:
#     if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
#         no_of_letters += 1
#     if '0' <= c <= '9':
#         no_of_digits += 1
#
# print("Input string is: ", str1)
# print("Total number of letters: ", no_of_letters)
# print("Total number of digits: ", no_of_digits)

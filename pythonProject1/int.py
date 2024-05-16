# # 1. Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# # also create a lambda function that multiplies argument x with argument y and prints the result.
# add = lambda a: a + 15
# print(add(2))
# multi = lambda a, b: a * b
# print(multi(6, 5))

# # 2.Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
# def multi(n):
#     return lambda a: a * n
#
#
# result = multi(2)
# print(result(3))

# # 3.
# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# subject_marks.sort(key=lambda x: x[1])
# print(subject_marks)
#
# # 4.
# models = [
#     {'make': 'Nokia', 'model': 216, 'color': 'Black'},
#     {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
#     {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
# ]
# models.sort(key=lambda x: x["color"])
# print(models)

# # 5.program to square every number in a given list of integers using Lambda.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# square = list(map(lambda x: x*2, nums))
# print(square)

# 6.
a = "AAABCADDE"
b = 3


def result(string_item, k):
    substrings = []
    for i in range(0, len(string_item), k):
        substring = string_item[i:i+k]
        new = ""
        for j in substring:
            # print(j)
            if j not in new:
                new = new+j
        # print(substring)
        substrings.append(new)
    print(substrings)
    return substrings


for item in result(a, b):
    print(item)

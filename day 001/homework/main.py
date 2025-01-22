# დავალება ნომერი 1
# def func1(a ,b ,c):
#     if a % c != 0 or (a % c == 0 and b% c == 0):
#         return ((b + a % c) - a) // c
#     else:
#         return((b + a % c) - a) // c + 1

# print(func1(20, 40, 2))


# def func1_1(a, b, c):
#     count = 0
#     if a > b:
#         while b < a:
#             if b % c == 0 :
#                 count += 1
#             b += 1
#     else:
#         while a < b:
#             if a % c == 0 :
#                 count += 1
#             a += 1
#     return count

# print(func1_1(60, 40, 11))



#დავალება ნომერი 2
# def func2():
#     number = 75
#     numb_Binary = []

#     while(number > 0):

#         Binary_0_1_numbers = number % 2

#         numb_Binary.append(str(Binary_0_1_numbers))

#         number = number // 2

#     return "".join(numb_Binary[::-1])


# def func2_1(binary):

#     decimal = 0
#     position = 0

#     for bit in binary[::-1]:

#         decimal += bit * (2 ** position)
#         position += 1 

#     return decimal

# print(func2_1([1, 0, 1, 0,]))


#დავალება ნომერი 3
# a = 5
# b = 14
# c = 132
# d = 144
# def func3():
#     if a > b:
#         if a > c:
#             if a > d:
#                 return a
#             else:
#                 return d
#         else:
#             if c > d:
#                 return c
#             else:
#                 return d
#     else:
#         if b > c:
#             if b > d:
#                 return b
#             else:
#                 return d
#         else:
#             if c > d:
#                 return c
#             else:
#                 return d


# def func3_1():

#     largest = a

#     if b > largest:
#         largest = b
        
#     if c > largest:
#         largest = c

#     if d > largest:
#         largest = d

#     return largest

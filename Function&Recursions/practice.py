# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#         return c
    
# a = 50
# b = 20
# c = 30

# print(greatest(a,b,c))

# def f_to_c(f):
#     return 5*(f-32)/9

# f = int(input("Enter temperature in F: "))
# print(f_to_c(f))


# print("a")
# print("b")
# print("c", end="")
# print("d", end="")


# def sum(n):
#     if(n==1):
#         return 1
#     return sum(n-1) + n

# print(sum(5))

# 4 + 5  9
# 3 + 9  12
# 2 + 12 14
# 1 + 14 15


# def pattern(n):
#     if(n==0):
#         return
#     print("*" * n)
#     pattern(n - 1)

# pattern(5)


# def inch_to_cms(inch):
#     return inch * 2.54

# n = int(input("Enter Value in inch: "))

# print(f"The Corresponding value in cms is {inch_to_cms(n)}")

# def rem(l, word):
#     n = []
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n

# l = ["Shahzad", "Aman", "Rehman"]
# print(rem(l, "an"))



# def multiply(n):
#     for i in range(1, 11):
#         print(f"{n} X {i} {n * i}")

# multiply(5)
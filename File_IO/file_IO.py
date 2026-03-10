# read Mode
# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()


# write Mode
# st = "Shahzad Kese ho"

# f = open("myfile.txt", "w")
# f.write(st)
# f.close()


# f = open("file.txt")

# lines = f.readlines()
# print(lines, type(lines))

# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3 == "")

# f.close()


# append mode

# st = "Shahzad Kese ho "

# f = open("myfile.txt", "a")
# f.write(st)
# f.close()

# the same can be written using with statement like this:

# with open("file.txt") as f:
#     print(f.read())

# you dont have to explicitly close the file

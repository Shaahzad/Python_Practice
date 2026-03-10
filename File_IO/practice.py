# f = open("poem.txt")
# content = f.read()
# if("twinkle" in content):
#     print("The word twinkle present in the content")
# else:
#     print("The word twinkle is not present in the content")

# f.close()


# import random 

# def game():
#     print("You are playing the game..")
#     score = random.randint(1, 62)

#     # fetch high score
#     with open("hiscore.txt") as f:
#         hiscore = f.read()
#         if(hiscore != ""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0
    
#     print(f"Your Score: {score}")
#     if(score>hiscore):
#         # write this hiscore to the file
#         with open("hiscore.txt", "w") as f:
#             f.write(str(score))

#     return score

# game()



# def generateTable(n):
#     table = ""
#     for i in range(1, 11):
#         table += f"{n} X {i} = {n * i}\n"

#     with open(f"tables/table_{n}.txt", "w") as f:
#         f.write(table)

# for i in range(2, 21):
#     generateTable(i)


# word = "Donkey"

# with open("file1.txt", "r") as f:
#     content = f.read()

# contentNew = content.replace(word, "####")

# with open("file1.txt", "w") as f:
#     f.write(contentNew)


# words = {"Donkey", "bad", "ganda"}

# with open("file1.txt", "r") as f:
#     content = f.read()

# for word in words:
#     content = content.replace(word, "#" * len(word))

# with open("file1.txt", "w") as f:
#     f.write(content)


# with open("log.txt") as f:
#     content = f.read()

# if("Python" in content):
#     print("Yes python is present")
# else:
#     print("No python is not present")


# with open("log.txt") as f:
#     lines = f.readlines()

# lineno = 1
# for line in lines:
#     if("python" in line):
#         print(f"yes python is present in line no: {lineno}")
#         break
#     lineno += 1

# else:
#     print("python is not present")


# with open("this.txt") as f:
#     content = f.read()

# with open("this_copy.txt", "w") as f:
#     f.write(content)

# with open("this.txt") as f:
#     content1 = f.read()

# with open("this_copy.txt") as f:
#     content2 = f.read()

# if(content1 == content2):
#     print("Yes content Same")
# else:
#     print("No Content Not Same")

# with open("this_copy.txt", "w") as f:
#     f.write("")



# with open("file.txt") as f:
#     content = f.read()

# with open("rename.txt", "w") as f:
#     f.write(content)

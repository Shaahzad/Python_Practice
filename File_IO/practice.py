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
a = int(input("Enter your age: "))

# if elif else ladder
if(a>=18):
    print("You are Above age")
    print("Good For You")

elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("You are entering 0 which is not valid age")

else:
    print("You are Below Age")   
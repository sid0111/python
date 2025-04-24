age = int(input("Enter your age : "))

if(age>18):
    print("Eligible for voting!")
elif(age==18):
    co = input("Do you have registered? {yes/no}")
    if(co == "yes"):
        print("You will get notification soon")
    else:
        print("Please register first!")
else:
    print("Sorry, Not Eligible!")
questions = [
    [
        "What is the capital of France?", "A. Berlin", "B. Madrid", "C. Paris", "D. Rome", "C"
    ],
    [
        "Who wrote the play 'Romeo and Juliet'?", "A. William Wordsworth", "B. William Shakespeare", "C. George Orwell", "D. Jane Austen","B"
    ], 
    [
        "Which planet is known as the Red Planet?", "A. Venus", "B. Mars", "C. Jupiter", "D. Saturn", "B"
    ],
    [
        "What is the largest mammal in the world?", "A. African Elephant", "B. Blue Whale", "C. Giraffe", "D. Orca", "B"
    ],
    [
        "In which year did World War II end?", "A. 1940", "B. 1942", "C. 1945", "D. 1950", "C"
    ],
    [
        "Which element has the chemical symbol 'O'?", "A. Gold", "B. Oxygen", "C. Osmium", "D. Iron", "B"
    ],
    [
        "Who is known as the Father of Computers?", "A. Alan Turing", "B. Charles Babbage", "C. Steve Jobs", "D. Bill Gates", "B"
    ],
    [
        "Which continent is the largest by land area?", "A. Africa", "B. Europe", "C. Asia", "D. Antarctica", "C"
    ],
    [
        "What is the boiling point of water at sea level in Celsius?", "A. 90°C", "B. 95°C", "C. 100°C", "D. 110°C", "C"
    ],
    [
        "Which language has the most native speakers in the world?", "A. English", "B. Spanish", "C. Mandarin Chinese", "D. Hindi", "C"
    ]
]

prize_money = [10, 20, 40, 80, 160 , 320, 640, 1250, 2500, 5000]
print("Welcome to the Millionaire Quiz Game!")
print("You will be asked 10 questions. Each question has 4 options.")
print("You have to select the correct option. If you answer correctly, you will win the prize money.")
print("If you answer incorrectly, you will lose the game.")
print("Let's start the game!")

i = 0
for ques in questions:
    print(f"1. {ques[0]}")
    print(f"a. {ques[1]}")
    print(f"b. {ques[2]}")  
    print(f"c. {ques[3]}")
    print(f"d. {ques[4]}")
    print("\nEnter your answer (A, B, C, D):")
    ans = input("Enter your choice : ")

    if(ques[5] == ans):
        print("Correct Answer")
    else:
        print("Better lck next time!")
        print(f"Correct answer is : {ques[5]}")
        break
    i += 1

    print(f"Your current prize money is : {prize_money[i]}")
    print("--------------------------------------------------")
    if i == 9:
        print("Congratulations! You have won the game.")
        print(f"Your total prize money is : {prize_money[i]}")
        break
    else:
        print("You can quit the game by typing 'quit'")
        print("Do you want to continue? (yes/no)")
        choice = input("Enter your choice : ")
        if choice.lower() == "no":
            print("Thank you for playing!")
            break
        elif choice.lower() == "quit":
            print("Thank you for playing!")
            break   
        else:
            print("Invalid choice. Please select a valid option.")
            print("--------------------------------------------------")
        continue    
    
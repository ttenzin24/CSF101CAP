################################
# Sangay Tenzin
# 1 Mechanical
# 02230271
################################
# REFERENCES
# https://www.geeksforgeeks.org/python-program-implement-rock-paper-scissor-game/
# https://youtu.be/Loc3_Lg7JJg?si=jfTkfNFji_q5d4qH
################################
# SOLUTION
# Your Solution Score:
# 50055
################################

# Reading the input.txt file:
def read_input():
    file = open('CSF101CAP/input_1_cap1.txt','r')
    return file

# Solution
def calculate_score(text):
# Given information:
    A = 1 #1 for Rock 
    B = 2 #2 for Paper
    C = 3 #3 for Scissor

    X = 0 #0 if you lose
    Y = 3 #3 if it is draw
    Z = 6 #6 if you win

# Scoring system (your_pick + outcome):
# Here the first column is what the opponent is playing and the second column says how the round needs to end.
# For A(Rock):
    loseA = A + X # 3 + 0 = 3 (Since opponent is playing rock and the outcome is to lose, you need to play scissor(3) and lose(0).)
    drawA = A + Y # 1 + 3 = 4 
    winA = A + Z # 2 + 6 = 8
# For B(Paper):
    loseB = B + X # 1 + 0 = 1
    drawB = B + Y # 2 + 3 = 5 
    winB = B + Z # 3 + 6 = 9
# For C(Scissor):
    loseC = C + X # 2 + 0 = 2
    drawC = C + Y # 3 + 3 = 6
    winC = C + Z # 1 + 6 = 7

# Creating dictionary(key : value):
    score_dict = {'A X': 3, 'A Y': 4, 'A Z': 8, 'B X': 1, 'B Y': 5, 'B Z': 9, 'C X': 2, 'C Y': 6, 'C Z': 7 }
   
    result = 0 #Initial score
    for line in text: #Using For loop
        val = line.strip() #Removing any trailing whitespaces

        if val in score_dict: #Conditional statement
           result += score_dict[val] #Calculating the total score in result
    print(f"The total score is: {result}")

 # Calling function
calculate_score(read_input()) 
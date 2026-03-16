player1 = int(input("Choose 0 for Snake, 1 for Water and 2 for Gun : "))
player2 = int(input("Choose 0 for Snake, 1 for Water and 2 for Gun : "))
#    S  W  G 
# S  0  1 -1 
# W -1  0  1
# G  1 -1  0
cases = [# 0      1      2 player2
         ["Tie","Win","Lose"],#0 player1
         ["Lose","Tie","Win"],#1 player1
         ["Win","Lose","Tie"] #2 player1
         ]
# print(cases[1][2])

res = cases[player2][player1]
print(f"Player 2  {res}")

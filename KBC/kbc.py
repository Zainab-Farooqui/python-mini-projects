ques = [
        [" What is the capital of India?","Delhi","Mumbai","Kolkata","Chennai",1],
        [" Who is the current president of India?","Delhi","Draupati Murmu","Kolkata","Chennai",2],
        [" Dogs are better than?","Man","Mumbai","Kolkata","Chennai",1],
        [" One Indian Rupee is equal to how many paise?","Delhi","Mumbai","100","Chennai",3],
        [" What is the main ingredient in a burger?","Delhi","Bread","Kolkata","Chennai",2],
        [" What is my current relationship status?","Delhi","Mumbai","Kolkata","Single",4],
        [" What is the capital of India?","Delhi","Mumbai","Kolkata","Chennai",1],
        [" What is the capital of Afghanistan?","Delhi","Mumbai","Kabul","Chennai",3],
        [" What is the national animal of India?","Delhi","Mumbai","Kolkata","Tiger",4],
        [" What is the capital of Pakistan?","Delhi","Karachi","Kolkata","Chennai",2],
        ]
money  = 0
levels = [1000,5000,10000,20000,40000,80000,160000,320000,640000,1250000]
for i in range(0, len(ques)):
    question = ques[i]
    print("--------------------------------------------------------------------------------------------")
    print("Your question for Rs. ",levels[i])
    print("Q",i,question[0])
    print("Your options are:\n1.",question[1],"\t2.",question[2],"\t3.",question[3],"\t4.",question[4])
    ans = int(input("Enter your answer (1-4): "))
    if ans == question[5]:
        money = levels[i]
        print("Correct answer! \n You have won Rs.",levels[i])
    else:
        if money >= 20000 and money < 160000: 
            money = 20000 
        elif money >= 160000 and money < 1250000:
            money = 160000

        print("Wrong answer!")
        break

print("Your Take home money is Rs.",money)
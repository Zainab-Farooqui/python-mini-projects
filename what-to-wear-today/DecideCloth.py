import random
user_satisfaction = 'n'
user_will = input("May I help you decide what to wear today? (y/n) : ").lower()
if user_will == 'y':
    while user_satisfaction != 'y':         
        list_of_clothes = ["Baggy jeans","T-shirt", "Jeans", "Formal", "Traditional", "Shorts", "Cropped Top", "Skirt"]
        rand = random.randint(0, len(list_of_clothes) - 1)
        print(f"You can try wearing '{list_of_clothes[rand]}' today :)")
        user_satisfaction = input("\n Are you satisfied with this choice? (y/n) : ").lower()

else:
    print("Okay, have a great day dear!")
        
            
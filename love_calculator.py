print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Retrieve user input and lowercase
name1 = name1.lower()
name2 = name2.lower()

names = name1 + name2

#calculate totals 
t = names.count("t")
r = names.count("r")
u = names.count("u")
e = names.count("e")
true = t + r + u + e

l = names.count("l")
o = names.count("o")
v = names.count("v")
e = names.count("e")
love = l + o + v + e

#string concat scores
score = str(true) + str(love)

#make string back into integer
true_score = int(score)

if true_score < 10 or true_score > 90:
    print(f"Your score is {true_score}, you go together like coke and mentos.")
elif true_score >= 40 and true_score <=50:
    print(f"Your score is {true_score}, you are alright together.")
else:
    print(f"Your score is {true_score}.")

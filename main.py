print("Hello assalamualekum,welcome to my first python project alhamdulillah")
inp1=input("Would you like to play my game? Type yes/no ")

a = "yes"
b = "no"
score = 10

if inp1 == a :
  print("ok then answer my questions")
  inp2 = input("what's your age?")
  inp23con=int(inp2)
  if inp23con >= 18 :  
    print("YaY.... You are eligible to play my game...")
    print(" ")
    print("Lets play")
    print("Now let's start the game")
    print(" ")
    print("The rules are simple.You have health points of 10.") 
    print("For every correct answer you get 1 health point.")
    print("For every wrong answer you loose 2 health points.")
    print("To win the game,you require atleast total of 12 health points at the end of the game") 
    print(" ")  
    print("Now you have to answer my questions.")
    print("If your answer is correct, you score 1 point.") 
    print("If your answer is wrong, you loose 2 health points.")
    print(" ")
    print("NOTE:You must type everything in small letters!")
    print(" ")

    ans1= "charles babbage"
    input1 = input("Who found computer?")
    if input1==ans1:
      print("yay...Correct")
      score=score+2
      print("health:",score)
    else:
      print("oh no! its wrong")
      score=score-4
      print("health:",score)
    print(" ")  

    ans2 = "africa"
    input2 = input("Which continent is the origin place of humans?")
    if input2 == ans2:
      print("yay...Correct")
      score=score+2
      print("health:",score) 
    else:
      print("oh no! its wrong")  
      score=score-4
      print("health:",score)
    print(" ")  

    ans3 = "automated teller machine"
    input3 = input("What is the full form of ATM?(write the answer in small letters)")
    if input3 == ans3:
      print("yay...Correct") 
      score=score+2
      print("health:",score)
    else:
      print("oh no, its wrong")
      score=score-4 
      print("health:",score) 
    print(" ")

    ans4 = "chinese"
    input4 = input("What is the most spoken language around the world after english?")
    if input4 == ans4:
      print("yay...Correct") 
      score=score+2
      print("health:",score)
    else:
      print("oh no, its wrong")
      score=score-4 
      print("health:",score)
    print(" ")
        
    ans5 = "yellow"
    input5 = input("Which color is the most irritant color to eye?")
    if input5 == ans5:
      print("yay...Correct") 
      score=score+2
      print("health:",score)
    else:
      print("oh no, its wrong")
      score=score-4 
      print("health:",score)
    print(" ")
    print("total health:",score) 

  

    if score >= 10:
      print("You have won the game")   
    else:
      print("Oh no! Looks like you have lost the game")
      print(" ")
      print("Try your best next time...")
      print(" ")
      
    print("the correct answers are") 
    print("answer1:charles babbage") 
    print("answer2:africa") 
    print("answer3:automated teller machine") 
    print("answer4:chinese") 
    print("answer5:yellow")  

  else:
    print("you are not eligible for this game")
elif inp1 == b :
  print("ok your wish")
 
print("Thank you, jazakallahukhair")

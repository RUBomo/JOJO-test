print("Title of program: True JoJo fan test( Simple ) ")
print()

counter = 0
score = 0
total_num_of_qn = 3


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Who was the antagonist for Part IV")
  print("   a) Boki")
  print("   b) Killer Queen")
  print("   c) Kira")
  print("   d) Mona Lisa")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. That is what happen when Kira saw Mona Lisa's hand."
    score -=1
  elif answer == "b":
    output = "Wrong. The stand, not the antagonist."
    score -=1
  elif answer == "c":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "d":
    output = "Wrong. Are you dumb?."
    score -=1
  else:
    output = "Please choose a, b, c or d only."
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is the name of Joseph Joestar's best friend?")
  print("   a) Caesar Anthonio Zeppeli")
  print("   b) Gyro Caesar Zeppeli")
  print("   c) Caesar Bethonio Zeppeli")
  print("   d) Mario Anthonio Zeppeli")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  elif answer == "b":
    output = "Wrong. Confused Part II with Part VII?"
    score -=1
  elif answer == "c":
    output = "Wrong. Zeppelis all have A in their name."
    score -=1
    
  elif answer == "d":
    output = "Wrong. That would be his father"
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What is Joseph Joestar's mantra?")
  print("   a) Son of a Bitch!")
  print("   b) O MY GOD!")
  print("   c) You next sentence is...")
  print("   d) All of above")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. You are correct, but there are better choices."
    score -=1
  elif answer == "b":
    output = "Wrong. You are correct, but there are better choices."
    score -=1
  elif answer == "c":
    output = "Wrong. You are correct, but you haven't watch Part III have you?"
    score -=1
    
  elif answer == "d":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  
  
  counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "What are the names of the stands of Pucci")
  print("   a) Black snake, A Moon, Destroyed in Hell")
  print("   b) White snake, B Moon, Made in Hell")
  print("   c) Black snake, C Moon, Made in Heaven")
  print("   d) White snake, C Moon, Made in Heaven")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Read carefully."
    score -=1
  elif answer == "b":
    output = "Wrong. Read carefully."
    score -=1
  elif answer == "c":
    output = "Wrong. Read carefully."
    score -=1
    
  elif answer == "d":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  
  
  
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Who said the following phrase Hmm it is the same type of stand as mine")
  print("   a) Holly Joestar")
  print("   b) Kujo Jolyne")
  print("   c) Kujo Jotaro")
  print("   d) Jhonny Joestar")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. She can't even control her stand."
    score -=1
  elif answer == "b":
    output = "Wrong. Read carefully."
    score -=1
  elif answer == "c":
    output = "Correct!."
    tracker =1
    score +=1
    
  elif answer == "d":
    output = "No!"
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
print("End of quiz!")
  

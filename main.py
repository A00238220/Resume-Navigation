import json
import random
from clear_screen import clear
from stranger import get_advice
import time 

def intro():
  clear()  
  print("Welcome to my site! Thank you for stopping by\n\nThis is a great place to explore some of my code and creativity.")    
  
  print("Main Menu\n\n[1] Interactive Professional Resume\n[2] Play an adventure game\n[3] idea coming soon...\n") 
     
  
  try:
    
    choice = input("Please make a selection: ")
    if choice == "1":
      clear()
      print("[1] Competencies\n[2] Education\n[3] Certifications\n[4] Experience\n[5] Contact\n")    
      choice1 = input("Please make a selection: ")
      if choice1 == "1":
        clear()
        print("SQL\nPython\nR\nPower BI\nARCGIS\nPandas\nAnalytical and problem-solving skills\nMicrosoft Office proficiency\nExcellent communication skills\nCritical thinking skills\n")
        print()
        time.sleep(3)
        inputt = input("continue (y/n): ")
        if inputt == 'y':
          clear()
          print('wise choice :)')
          time.sleep(2)
          clear()
          intro()          
        elif inputt == 'n':
          clear()
          print("Glad you stopped by, feel free to explore the interesting projects I've worked on")
          time.sleep(2)
          
      elif choice1 == "2":
        clear()
        print("2011 – 2016 Pure and Applied Mathematics - Federal University of Technology Minna\n\nSeptember 2021 – to date Business Analytics - Cambrian College\n")
        print()
        time.sleep(3)
        inputt = input("continue (y/n): ")
        if inputt == 'y':
          clear()
          print('wise choice :)')
          time.sleep(2)
          clear()
          intro()          
        elif inputt == 'n':
          clear()
          print("Glad you stopped by, feel free to explore the interesting projects I've worked on")
          time.sleep(2)
          
      elif choice1 == "3":
        clear()
        print(["https://www.datacamp.com/statement-of-accomplishment/course/be40f66ed9298b63a86c247ce4c50550a9b6c412", "https://www.datacamp.com/statement-of-accomplishment/course/76e0738211a29ea986a8f8db3996f6a644dfe3c6"])
        print()
        time.sleep(3)
        inputt = input("continue (y/n): ")
        if inputt == 'y':
          clear()
          print('wise choice :)')
          time.sleep(2)
          clear()
          intro()          
        elif inputt == 'n':
          clear()
          print("Glad you stopped by, feel free to explore the interesting projects I've worked on")
          time.sleep(2)
        else:
          print("Please select a valid option")

          
      elif choice1 == "4":
        clear()
        print("2018 – 2021 Data Analyst - Keystone Bank Limited\n\n2017 – 2018 Tax Analyst - Federal Inland Revenue Services\n\n2015 (6months) Intern - Fin Insurance Company Limited")
        print()
        time.sleep(3)
        inputt = input("continue (y/n): ")
        if inputt == 'y':
          clear()
          print('wise choice :)')
          time.sleep(2)
          clear()
          intro()          
        elif inputt == 'n':
          clear()
          print("Glad you stopped by, feel free to explore the interesting projects I've worked on")
          time.sleep(2) 
          
      elif choice1 == "5":
        clear()
        print("sharonbandele@gmail.com")
        print()
        time.sleep(3)
        inputt = input("continue (y/n): ")
        if inputt == 'y':
          clear()
          print('wise choice :)')
          time.sleep(2)
          clear()
          intro()          
        elif inputt == 'n':
          clear()
          print("Glad you stopped by, feel free to explore the interesting projects I've worked on")
          time.sleep(2) 
        
    elif choice == "2":
      # read file
      with open('data.json', 'r') as myfile:
        data=myfile.read()
        # parse file
        data = json.loads(data)
      
      room = 0      
      while True:
        clear()
      
        chance = random.randint(1,2)
        if chance == 1:
          if data[room]["luck"] == 1:
            print("You are very lucky!")
            #something happens?
        if chance == 2:
          if data[room]["stranger"] == 1:
            print("A stranger walks by and starts talking to you")
            get_advice()
        
          #print(data[room])
          time.sleep(1)
          print(data[room]["story"])
          
          if data[room]["win"] == 1:
            print("You win the game!")
            #reset 
            break
          
          if data[room]["die"] == 1:
            print("You lose the game!")
            #reset 
            break

          time.sleep(1)
          print()
          print(data[room]["nav"])
          
          choice = input("\nPlease make a selection ")
          try:
            if choice == '1':
              room = data[room]["c1"] - 1
            elif choice == '2':
              room = data[room]["c2"] - 1
            elif choice == '3':
              room = data[room]["c3"] - 1
            else:
              print("Please select a valid option")
          except:
            continue 
    elif choice == "3":
      print('idea coming sooon...')
      time.sleep(3)
      clear()
      intro()
    else:
      print("Please select a valid option")
      time.sleep(3)
      clear()
      intro()
      
  except:
    print("Please select a valid option")
  
intro()
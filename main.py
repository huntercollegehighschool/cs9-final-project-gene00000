"""
Name(s):
Name of Project:
"""

#Write the main part of your program here. Use of the other pages is optional.

"""
Name(s): Sylvia Merrill, Genevieve Oudens
Name of Project: Choose Your Own Adventure
"""

def start(): 
  print("You wake up and struggle out of bed. do you want feed the cat or do you want to make yourself breakfast?")
  choice = input("\nEnter A or feed your cat or B for make breakfast. ").upper()
  if choice == ("A"):
    feedcat()
  elif choice == ("B"):
    breakfast()
  while choice != "A" and choice != "B":
    print("You must choose either A or B.")
    start()
  
def feedcat():
  print("Do you want to feed your cat cat food or marshmallows?")
  choice = input("\nEnter A for cat food, or B for marshmallows. ").upper()
  if choice == ("A"):
    catfood()
  elif choice == ("B"):
    marshmallows()
  while choice != "A" and choice != "B":
    print("You must choose either A or B.")
    start()

def catfood():
  print ("Do you want to sautee it or serve it cold?")
  choice = input ("\nEnter A for sautee, or B for serve cold. ").upper()
  if choice == ("A"):
    sautee()
  elif choice == ("B"):
    cold()
  while choice != "A" and choice != "B":
    print("You must choose either A or B.")
    start()

def sautee():
  print("You offer your cat sauteed cat food, but she is a picky eater and isn't interested. Better try something else!")

def cold():
  print("Your cat gives an affectionate purr before shoving past you to eat. Time to go prepare your own breakfast!")

def marshmallows(): 
  print ("Marshmallows?? Okay, then! Do you want to roast them or serve them with chocolate sauce?")
  choice = input("\nEnter A to roast them or B for chocolate sauce. ").upper()
  if choice == ("A"):
    roast()
  elif choice == ("B"):
    chocolate()
  while choice != "A" and choice != "B":
    print("You must choose either A or B.")
    start()

def roast():
  print ("Your cat is not you. Why did you think she would like this??")

def chocolate():
  print("Oops! Cats aren't supposed to have chocolate...better call the vet! Quick!")

def breakfast():
  print("Do you want toast or live calamari with worcestershire sauce?")
  choice = input("\nEnter A for toast, or B for calamari with worcestershire sauce. ").upper()
  if choice == ("A"): 
    toast()
  elif choice == ("B"): 
    calamari()
  while choice != "A" and choice != "B":
    print("You must choose either A or B.")
    start()

def toast():
  print("Do you want to stick to your routine or are you feeling adventurous?")
  choice = input("\nEnter A to stick to your routine or B to try something new. ")
  if choice ==("A"):
    routine()
  elif choice == ("B"):
    new()
  while choice != "A" and choice != "B":
    print("You must choose either A or B.")
    start()

def routine():
  print("You make yourself toast with butter and jam. Enjoy!")

def new():
  print("You make yourself toast with nutella and coleslaw. Too each their own, ... I guess.")

def calamari():
  print("Do you want to make it yourself or pick some up from the gas station down the block?")
  choice = input("\nEnter A to make it yourself or B to get it from the gas station. ")
  if choice ==("A"):
    make()
  elif choice == ("B"):
    gas()
  while choice != "A" and choice != "B":
    print("You must choose either A or B.")
    start()

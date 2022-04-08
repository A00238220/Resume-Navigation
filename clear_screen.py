from os import system, name
# define our clear function
def clear():
  if name == 'nt': #windows
    _ = system('cls')
  else:
    _ = system('clear') #mac or linux
   
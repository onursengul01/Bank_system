#Stil Working on it...



import os, sys, random
import os.path

def crl_screen():
  os.system("clear")

class Bank:
  def __init__(self):
    crl_screen()
    print("""
    
{1}--Log in

{2}--Sign up

{e}--Exit
        
    """)

    self.options = input("Choose: ")

    if self.options == "1":
      login()

    if self.options == "2":
      signup()

    if self.options == "3":
      quit()

    if self.options == "":
      Bank()
     
    

    else:
      Bank()
     
class login:
  pass

class signup:
  def __init__(self):
    self.name = input("Enter your name: ")
    self.last_name = input(f"{self.name} enter your last name: ")

    self.email = input(f"{self.name} {self.last_name} enter your email: ")
    self.number = input(f"{self.name} {self.last_name}")

    if os.path.exists('database.txt'):
      with open('dataase.txt', 'wb') as t:
        t.write("name: " + self.name)

        t.close()

    else:
      print("File does not exist")
if __name__ == "__main__":
  try:
    Bank()
  except KeyboardInterrupt:
    sys.exit()

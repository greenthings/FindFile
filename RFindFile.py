from pathlib import Path

# -------------------------------------------------------

Name=""
Drive=""
Adress=""
BigAdress=""

# --------------------------------------------------------

print("please, Tell me. where do you wanna go?")
print("D or C?")
Drive = input()
print("please, let me know where it is.")
Adress = input()
print("what do you wanna find out?")
Name = input()

# you can create own adress. so, you can fastly find what you want.
# A sample code is shown below.

# BigAdress = Drive+':/Users/Username/'+Adress+'/'+Name

print(BigAdress)

# --------------------------------------------------------

file = Path(BigAdress) 

if file.is_file():
  print("Yes, there is a file") 
else :
  print("there is Nothing")  

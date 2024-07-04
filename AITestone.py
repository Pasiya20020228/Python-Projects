#Data Enter Programme

def  getname():
  name = str(input("Enter Your Name: "))


def getage():
    age = int(input("Enter Your Age: "))



print("Welcome to this Programme , Enjoy yourself..")
star = "#"
for i in range(10):
  print(star)
  star = star + "#"


print("My name is Alex, How are you?")
if input("Answer: ") == "I'm fine":
    getname()
    print("Whats's your age?")
    getage()
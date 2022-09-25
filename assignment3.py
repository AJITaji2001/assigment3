# Read Mode
# """"The read mode in Python opens an existing file for reading, positioning the pointer at the file's start it only allow as to read the file which we have created .""""
   
myfile=open("read.txt","r")
print(myfile.read())


# Write Mode
# """""Write mode creates a file for writing content and places the pointer at the start. If the file exists, write truncates (clears) any existing information.""""

myfile=open("write.txt","w")
print(myfile.write())

# Append Mode
# """""Append mode adds information to an existing file, placing the pointer at the end. If a file does not exist, append mode creates the file.""""

mylines=["hi" ,"hello","hai "]
with open ("read.txt","a") as file1:
  file1.writelines(mylines)
  
# calculator
 
 
# define functions

# To print sum(+)

def add(x, y):
   """This function adds two numbers"""

   return x + y
   
# To print sub(-)

def subtract(x, y):
   """This function subtracts two numbers"""

   return x - y

# To print mul(*)

def multiply(x, y):
   """This function multiplies two numbers"""

   return x * y
    
# To print div(/)

def divide(x, y):
   """This function divides two numbers"""

   return x / y

# take input from the user

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")

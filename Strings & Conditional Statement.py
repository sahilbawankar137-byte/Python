#1.WAP to input user's first name & print its length.
first = input("enter your name")
print("lenth of your name is:",len(first))

#2.WAP to find the occurence of '$' in a string.
str = "hi, i am a $ the $ symbol $ 99.99"
print(str.count("$"))


#WAP to check if a number evtered by the user is odd or even.
  num = int(input("enter the number:"))
  rum = num/2

if(rem == 0):
  print("even")
else:
  print("odd")

#WAP to check if a number is a multiple of 7 or not.
num = int(input("enter number"))
rem = num/7
if(rem == 0):
  print("your number is multiple of 7)
        else:
          print("your number is not multiple of 7")

#WAP to find the greatest of 3 numvers entered by the user.
a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("entere third number))

if(a > b and b > c):
  print("The greatest value is a")
  elif(b > a and a > c):
        print("The greatest value is b")
              else:
              print("The greatest value is c")

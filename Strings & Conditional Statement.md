# Strings
-string is data type that stores a sequence of characters.

Basic Operations
-concatenation
  "hello" + "world" ----> "helloworld"

-length of str
    len(str)

# Indexing
S a h i l b a w a n  k  a  r

0 1 2 3 4 5 6 7 8 9 10 11 12

# Slicing
-Accessing parts of a string

  str[ starting_idx : ending_idx]#ending idx is  not included
  str = "sahilbawankar" 
  str[1 : 4] is "ahi"
  str[1 : 4] is same as str[0 : 4]
  str[1 : ] is same as str[1 : len(str)]

# Slicing
-Nagative Index
 A  p  p  l  e
-5 -4 -3 -2 -1

str = "Apple"
str[-3 : -1] is "pl"

# string Function
-str = "I am a coder."
-s tr.endsWith("er.") #return true if string ends with substr
str.capitalize() #capitalizes 1st char
str.replace(old,new) #replaces all occurrencese of ald with new
str.find(word) #returns 1st indes of 1st occurrences
str.count("am") #count the occurrence of substr in string

# Let's Practice
1.WAP to input user's first name & print its length.

first = input("enter your name")

print("lenth of your name is:",len(first))

2.WAP to find the occurence of '$' in a string.

str = "hi, i am a $ the $ symbol $ 99.99"

print(str.count("$")

# Condiational Statements 
-if-elif-else(Statement1)

if(condirion):
  Statement1
elif(condition):
  Statement2
else:
  StatementN

# Conditional Statements
-Grade students based on marks

  marks >= 90, grade = "A"
  90 > marks >= 80, grade = "B"
  80 > marks >= 70, grade = "c"
  70 > marks, grade = "D"

  -code
  marks = int(input("enter your marks:"))
  if(marks >= 90):
     print("your grade is:A")
  elif(90 > marks >= 80):
     print("your grade is:B")
  elif(80 > marks >= 80)
     print("your grade is:c")
  else:
     print("your grade is:D")


  

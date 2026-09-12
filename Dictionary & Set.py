#!Let's Prctice
# 1.Store following word meanings in a python dictionary:

dict = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": "a small animal"
}

print(dict)

# 2.You are fiven a list of subjects for students. Assume one classroom is required for 1 subject. HOw many classroom are needed by all students.
#"python", "java", "c++, "python, "javascript", "java", "pthon", "java", "c++", "c"

Subjects = {
"python", "java", "C++", "python", "javascript", "java", "python", "C++", "C"
}
print(len(Subjects))

# 3.WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary add one by one . Use subject name as key & marks as value.

mark ={}

math = float(input("enter your math marks:"))
physics = float(input("enter your physics marks:"))
chemistry = float(input("enter your chemistry marks:"))

mark.update({"math": math, "physics": physics, "chemistry": chemistry})
print(mark)

# 4.Figure out way to store 9 and 9.0 as separate values in the set. ( you can rake help of built-in data types)

values ={9, 9.0}
print(values)

values = {9, "9.0"}
print(values)

values = {
    ("float", 9.0),
    ("int", 9)
}
print(values)

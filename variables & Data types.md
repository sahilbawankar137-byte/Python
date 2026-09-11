# PROGRAMING!

```text
Machine <------------------ Translator <------------------ Python
(ex. Laptop, PC)              (ex. Compiler/Interpreter)    (code)
```

# What is Python??

- Python is simple & easy
- Free & open source
- High level language
- Developed by Guido Van Rossum
- Portable

---

# Our First Code

```python
print("hello world")
```

```text
print       ----> Function

hello world ----> Output
```

---

# Python Character Set

- **Letters** — A–Z, a–z
- **Digits** — 0–9
- **Special Symbols** — `-`, `+`, `/`, etc.
- **Whitespaces** — Blank Space, tab, carriage return, newline, formfeed
- **Other characters** — Python can process all ASCII and Unicode characters as part of data or literals

---

# Variables

- A variable is a name given to a memory location in a program.

```python
name = "sahil"

age = 23

price = 35.99
```

---

# Rules for Identifiers

1. Identifiers can be a combination of uppercase and lowercase letters, digits or an underscore (`_`).

   So **myVariable**, **variable_1**, **variable_for_print** all are valid Python identifiers.

2. An identifier cannot start with a digit.

   So while **variable1** is valid, **1variable** is not valid.

3. We can't use special symbols like **#**, **@**, **%**, **$**, etc. in our identifier.

4. Identifier can be of any length.

---

# Data Types

- Integers
- String
- Float
- Boolean
- None

```python
print(type(age))          # <class 'int'>

print(type(pi))           # <class 'float'>

print(type(complex_num))  # <class 'bool'>

print(type(A))            # <class 'complex'>

print(type(name))         # <class 'str'>
```

---

# Keywords

- Keywords are reserved words in Python.

> **False** should be uppercase.

![Python Keywords](https://github.com/user-attachments/assets/adf0e892-62f5-4210-ad5d-a2d1a2e86b49)

---

# Print Sum

```python
a = 2

b = 5

sum = a + b

print(sum)
```

---

# Comments in Python

### Single Line Comment

- Represented by `#`

```python
# Single Line comment
```

### Multi Line Comment

```python
"""
Multi Line

Comment
"""
```

---

# Types of Operators

An operator is a symbol that performs a certain operation between operands.

### 1. Arithmetic Operators

```text
+  -  *  /  %  **
```

### 2. Relational / Comparison Operators

```text
==  !=  <  >  <=  >=
```

### 3. Assignment Operators

```text
=  +=  -=  /=  %=  **=
```

### 4. Logical Operators

```text
not  and  or
```

---

# Type Conversion

```python
a, b = 1, 2.0

sum = a + b
```

### Error

```python
a, b = 1, "2"

sum = a + b
```

---

# Type Casting

```python
a, b = 1, "2"

c = int(b)

sum = a + c
```

![Type Casting](https://github.com/user-attachments/assets/9a5e8326-da65-46cd-8774-417549efd897)

---

# Input in Python

- `input()` statement is used to accept values using the keyboard from the user.

```python
input()
```

- Result for `input()` is always a `str`.

```python
input()       # str

int(input())  # int

float(input()) # float
```

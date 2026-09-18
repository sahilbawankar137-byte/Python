# 🐍 PROGRAMMING!

```text
Machine <------------------ Translator <------------------ Python
(ex. Laptop, PC)              (ex. Compiler/Interpreter)    (code)
```

---

# 🐍 What is Python?

* Python is simple & easy to learn.
* Free & open source.
* High-level programming language.
* Developed by **Guido van Rossum**.
* Portable — Python programs can run on different platforms.

---

# 🚀 Our First Code

```python
print("hello world")
```

```text
print       ----> Function

hello world ----> Output
```

---

# 🔤 Python Character Set

* **Letters** — `A–Z`, `a–z`
* **Digits** — `0–9`
* **Special Symbols** — `+`, `-`, `*`, `/`, etc.
* **Whitespaces** — Blank space, tab, carriage return, newline, formfeed
* **Other characters** — Python can process ASCII and Unicode characters as part of data or literals.

---

# 📦 Variables

* A variable is a name given to a memory location in a program.

```python
name = "sahil"

age = 23

price = 35.99
```

---

# 🏷️ Rules for Identifiers

### 1️⃣ Letters, digits & underscore

Identifiers can be a combination of uppercase and lowercase letters, digits, or an underscore (`_`).

```python
myVariable = 10
variable_1 = 20
variable_for_print = 30
```

All of the above are valid Python identifiers.

---

### 2️⃣ Cannot start with a digit

An identifier cannot start with a digit.

```python
variable1 = 10    # ✅ Valid

1variable = 10    # ❌ Invalid
```

---

### 3️⃣ Special symbols are not allowed

We can't use special symbols like `#`, `@`, `%`, `$`, etc. in identifiers.

```python
my_name = "sahil"    # ✅ Valid

my-name = "sahil"    # ❌ Invalid
```

---

### 4️⃣ Identifier length

An identifier can be of any length.

---

# 📊 Data Types

Python has several built-in data types:

* **Integer** — `int`
* **String** — `str`
* **Float** — `float`
* **Boolean** — `bool`
* **Complex** — `complex`
* **None** — `NoneType`

### 🔢 Integer

```python
age = 23

print(type(age))
# <class 'int'>
```

### 🔤 String

```python
name = "sahil"

print(type(name))
# <class 'str'>
```

### 🔢 Float

```python
price = 35.99

print(type(price))
# <class 'float'>
```

### ✅ Boolean

```python
is_adult = True

print(type(is_adult))
# <class 'bool'>
```

### 🧮 Complex

```python
complex_num = 2 + 3j

print(type(complex_num))
# <class 'complex'>
```

### 🚫 None

```python
A = None

print(type(A))
# <class 'NoneType'>
```

---

# 🔑 Keywords

* Keywords are **reserved words** in Python.
* They have a special meaning and cannot be used as variable names.

> ⚠️ `False` should be written with an uppercase `F`.

![Python Keywords](https://github.com/user-attachments/assets/adf0e892-62f5-4210-ad5d-a2d1a2e86b49)

---

# ➕ Print Sum

```python
a = 2
b = 5

sum = a + b

print(sum)
```

---

# 💬 Comments in Python

Comments are used to add notes or explanations in code. They are ignored by Python during execution.

### 📝 Single-Line Comment

* Represented by `#`.

```python
# Single Line comment
```

### 📄 Multi-Line Comment

```python
"""
Multi Line

Comment
"""
```

---

# ⚙️ Types of Operators

An operator is a symbol that performs a certain operation between operands.

### 1️⃣ Arithmetic Operators

```text
+   -   *   /   %   **
```

### 2️⃣ Relational / Comparison Operators

```text
==   !=   <   >   <=   >=
```

### 3️⃣ Assignment Operators

```text
=   +=   -=   *=   /=   %=   **=
```

### 4️⃣ Logical Operators

```text
not   and   or
```

---

# 🔄 Type Conversion

Type conversion happens when Python **automatically converts** one data type into another compatible type.

```python
a, b = 1, 2.0

sum = a + b

print(sum)
print(type(sum))
```

Here, Python converts the integer `1` into a float before performing the addition.

---

### ❌ Error

Different incompatible data types cannot always be operated on directly.

```python
a, b = 1, "2"

sum = a + b
```

This gives a **TypeError** because an `int` and a `str` cannot be added directly.

---

# 🎭 Type Casting

Type casting means **manually converting** one data type into another.

```python
a, b = 1, "2"

c = int(b)

sum = a + c

print(sum)
```

![Type Casting](https://github.com/user-attachments/assets/9a5e8326-da65-46cd-8774-417549efd897)

---

# ⌨️ Input in Python

* The `input()` function is used to accept values from the user through the keyboard.

```python
input()
```

### 📌 Input Data Types

The result returned by `input()` is always a `str`.

```python
input()          # str

int(input())     # int

float(input())   # float
```

### Example

```python
name = input("Enter your name: ")

print(name)
```

```python
age = int(input("Enter your age: "
```

# 📝 Let's Practice — Variables

---

## 1️⃣ Input 2 Numbers & Print Their Sum

**Question:**
Write a program to input 2 numbers and print their sum.

```python
a = float(input("Enter first value: "))
b = float(input("Enter second value: "))

print("Sum:", a + b)
```

### 🔹 Example Output

```text
Enter first value: 10
Enter second value: 20
Sum: 30.0
```

---

## 2️⃣ Area of a Square

**Question:**
Write a program to input the side of a square and print its area.

📐 **Formula:** `Area = side × side`

```python
side = float(input("Enter side: "))

print("Area:", side * side)
```

### 🔹 Example Output

```text
Enter side: 5
Area: 25.0
```

---

## 3️⃣ Average of 2 Floating-Point Numbers

**Question:**
Write a program to input 2 floating-point numbers and print their average.

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Average:", (a + b) / 2)
```

### 🔹 Example Output

```text
Enter first number: 10
Enter second number: 20
Average: 15.0
```

> ⚠️ **Important:**
> `(a + b) / 2` is required.
> `a + b / 2` gives a different result because of **operator precedence**.

---

## 4️⃣ Compare Two Numbers

**Question:**
Write a program to input 2 integer numbers `a` and `b`.
Print `True` if `a` is **greater than or equal to** `b`. Otherwise, print `False`.

```python
a = int(input("Enter first: "))
b = int(input("Enter second: "))

print(a >= b)
```

### 🔹 Example Output

```text
Enter first: 10
Enter second: 5
True
```

```text
Enter first: 3
Enter second: 8
False
```

---

## 🧠 Quick Revision

| Task                  | Code             |
| --------------------- | ---------------- |
| Take decimal input    | `float(input())` |
| Take integer input    | `int(input())`   |
| Addition              | `a + b`          |
| Square area           | `side * side`    |
| Average               | `(a + b) / 2`    |
| Greater than or equal | `a >= b`         |
| Print result          | `print()`        |

---

### 🚀 Remember

* `input()` always takes input as a **string**.
* Use `int()` for integer values.
* Use `float()` for decimal values.
* Use parentheses when needed to control the order of operations.
* Comparison operators return **`True` or `False`**.

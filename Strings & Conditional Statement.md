# 🔤 Strings in Python

* String is a data type that stores a sequence of characters.

---

# ⚙️ Basic Operations

### 🔗 Concatenation

Concatenation means joining two or more strings.

```python
"hello" + "world"  # "helloworld"
```

### 📏 Length of String

The `len()` function returns the number of characters in a string.

```python
len(str)
```

---

# 🔢 Indexing

Each character in a string has an index number.

```text
S  a  h  i  l  b  a  w  a  n  k  a  r
0  1  2  3  4  5  6  7  8  9  10 11 12
```

---

# ✂️ Slicing

* Slicing is used to access parts of a string.

```text
str[starting_idx : ending_idx]
```

> 💡 Ending index is **not included**.

```python
str = "sahilbawankar"

str[1:4]  # "ahi"

str[0:4]  # "sahi"

str[1:]   # same as str[1:len(str)]
```

---

# 🔢 Slicing — Negative Index

Negative indexing starts from the end of the string.

```text
 A  p  p  l  e
-5 -4 -3 -2 -1
```

```python
str = "Apple"

str[-3:-1]  # "pl"
```

---

# 🛠️ String Functions

```python
str = "I am a coder."
```

### 🔚 `endswith()`

```python
str.endswith("er.")
```

* Returns `True` if the string ends with the given substring.

---

### 🔠 `capitalize()`

```python
str.capitalize()
```

* Capitalizes the first character of the string.

---

### 🔄 `replace()`

```python
str.replace(old, new)
```

* Replaces all occurrences of `old` with `new`.

---

### 🔍 `find()`

```python
str.find(word)
```

* Returns the first index of the first occurrence of the given word.

---

### 🔢 `count()`

```python
str.count("am")
```

* Counts the occurrences of the given substring in the string.

---

# 📝 Let's Practice

### 1️⃣ WAP to input user's first name & print its length

```python
first = input("Enter your name: ")

print("Length of your name is:", len(first))
```

---

### 2️⃣ WAP to find the occurrence of `$` in a string

```python
str = "hi, i am a $ the $ symbol $ 99.99"

print(str.count("$"))
```

---

# 🔀 Conditional Statements

Conditional statements are used to execute different blocks of code based on conditions.

### `if-elif-else`

```python
if condition:
    Statement1

elif condition:
    Statement2

else:
    StatementN
```

---

# 🎓 Grade Students Based on Marks

```text
marks >= 90       → grade = "A"

90 > marks >= 80  → grade = "B"

80 > marks >= 70  → grade = "C"

70 > marks       → grade = "D"
```

### 💻 Code

```python
if marks >= 90:
    grade = "A"

elif 90 > marks >= 80:
    grade = "B"

elif 80 > marks >= 70:
    grade = "C"

else:
    grade = "D"
```

> 💡 Python supports **chained comparisons** like `90 > marks >= 80`.

# 📝 Let's Practice — Strings & Conditional Statements

---

## 🔤 Strings — Practice

### 1️⃣ Find the Length of User's Name

**Question:**
Write a program to input the user's first name and print its length.

```python
first = input("Enter your name: ")

print("Length of your name is:", len(first))
```

### 🔹 Example Output

```text
Enter your name: Sahil
Length of your name is: 5
```

---

### 2️⃣ Count the Occurrence of `$`

**Question:**
Write a program to find the number of occurrences of `$` in a string.

```python
text = "hi, i am a $ the $ symbol $ 99.99"

print(text.count("$"))
```

### 🔹 Output

```text
3
```

> 💡 `count()` returns the number of times a particular character or substring occurs in a string.

---

# 🔀 Conditional Statements — Practice

### 3️⃣ Check Odd or Even

**Question:**
Write a program to check if a number entered by the user is **odd or even**.

```python
num = int(input("Enter the number: "))

rem = num % 2

if rem == 0:
    print("Even")
else:
    print("Odd")
```

### 🔹 Example Output

```text
Enter the number: 8
Even
```

```text
Enter the number: 7
Odd
```

> ⚠️ **Important:** Use `%` (modulus) to find the remainder.
> `/` gives division result, while `%` gives remainder.

---

### 4️⃣ Check Multiple of 7

**Question:**
Write a program to check if a number is a **multiple of 7** or not.

```python
num = int(input("Enter number: "))

rem = num % 7

if rem == 0:
    print("Your number is a multiple of 7")
else:
    print("Your number is not a multiple of 7")
```

### 🔹 Example Output

```text
Enter number: 21
Your number is a multiple of 7
```

```text
Enter number: 20
Your number is not a multiple of 7
```

---

### 5️⃣ Find the Greatest of 3 Numbers

**Question:**
Write a program to find the **greatest of 3 numbers** entered by the user.

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("The greatest value is:", a)
elif b >= a and b >= c:
    print("The greatest value is:", b)
else:
    print("The greatest value is:", c)
```

### 🔹 Example Output

```text
Enter first number: 25
Enter second number: 18
Enter third number: 12

The greatest value is: 25
```

> 💡 `and` is used because the selected number must be greater than or equal to **both** other numbers.

---

## 🧠 Quick Revision

| Problem       | Main Concept                |
| ------------- | --------------------------- |
| Name length   | `len()`                     |
| Count `$`     | `count()`                   |
| Odd / Even    | `% 2`                       |
| Multiple of 7 | `% 7`                       |
| Greatest of 3 | `if`, `elif`, `else`, `and` |

---

### 🚀 Key Takeaways

* `len()` → finds the length of a string.
* `count()` → counts occurrences of a character/string.
* `%` → gives the remainder.
* `if` → checks a condition.
* `elif` → checks another condition.
* `else` → runs when all previous conditions are false.
* `and` → both conditions must be `True`.

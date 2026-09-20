# 🐍 Functions & Recursion in Python

---

# 🔧 Functions in Python

A **function** is a block of statements that performs a specific task.

## 📌 Syntax

```python
def func_name(param1, param2):
    # some work
    return

func_name(arg1, arg2)
```

* `def` → used to define a function
* `param` → parameter
* `arg` → argument
* `return` → sends a value back from the function
* Function call → executes the function

---

# 🤔 Why Functions?

Functions help us:

* ♻️ Avoid repeating the same code
* 🧹 Keep code clean and organized
* 🔄 Reuse code multiple times
* 📖 Make programs easier to understand

### Without Function

```python
a = 5
b = 10

sum = a + b
print(sum)

# More lines of code...

a = 12
b = 17

sum = a + b
print(sum)
```

We are doing the **same work repeatedly**.

### With Function

```python
def calc_sum(a, b):
    sum = a + b
    print(sum)
    return sum

calc_sum(5, 10)
calc_sum(12, 17)
```

---

# 🔹 Function with Parameters & Return

```python
def calc_sum(a, b):
    return a + b

sum = calc_sum(5, 76)

print(sum)
```

Here:

* `a` and `b` → **parameters**
* `5` and `76` → **arguments**
* `calc_sum(5, 76)` → **function call**
* `return a + b` → returns the result

---

# 👋 Simple Function

```python
def print_hello():
    print("hello")

print_hello()
print_hello()
```

### 🔹 Output

```text
hello
hello
```

### `None` with `return`

If a function doesn't return anything, Python returns `None`.

```python
def print_hello():
    print("hello")

print(print_hello())
```

### 🔹 Output

```text
hello
None
```

---

# 📊 Average of 3 Numbers

```python
def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum / 3

    print(avg)
    return avg

calc_avg(1, 2, 3)
```

### 🔹 Output

```text
2.0
```

---

# 🧩 Types of Functions in Python

## 1️⃣ Built-in Functions

Functions that are already provided by Python.

Examples:

```python
print()
len()
type()
range()
```

### `sep` and `end`

```python
print("ankita", "sahil", sep=" ")
print("bawankar")
```

* `sep` → separates multiple values
* `end` → decides what is printed at the end

By default:

```python
sep = " "
end = "\n"
```

---

## 2️⃣ User-Defined Functions

Functions created by the programmer using `def`.

Example:

```python
def calc_prod(a, b):
    print(a * b)
    return a * b

calc_prod(2, 3)
```

---

# 🎯 Default Parameters

A parameter can have a default value.

### Without Arguments

```python
def calc_prod(a=2, b=2):
    print(a * b)
    return a * b

calc_prod()
```

### 🔹 Output

```text
4
```

---

### One Default Parameter

```python
def calc_prod(a, b=2):
    print(a * b)
    return a * b

calc_prod(1)
```

### 🔹 Output

```text
2
```

Here `b` automatically takes the value `2`.

---

### ❌ Invalid Default Parameter Order

```python
def calc_prod(a=2, b):
    print(a * b)
    return a * b
```

This gives an error.

> ⚠️ **Rule:** A non-default parameter cannot come after a default parameter.

✅ Correct:

```python
def calc_prod(a, b=2):
    pass
```

❌ Incorrect:

```python
def calc_prod(a=2, b):
    pass
```

---

# 📝 Let's Practice

## 1️⃣ Print Length of a List

**Question:**
Write a function to print the length of a list.
`list` is the parameter.

```python
cities = ["delhi", "nagpur", "mumbai"]
heroes = ["iron man", "spider man", "hulk"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)
```

### 🔹 Output

```text
3
3
```

---

## 2️⃣ Print List Elements in a Single Line

**Question:**
Write a function to print all elements of a list in a single line.

```python
heroes = ["iron man", "spider man", "hulk"]

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heroes)
```

### 🔹 Output

```text
iron man spider man hulk
```

---

## 3️⃣ Find Factorial of `n`

**Question:**
Write a function to find the factorial of `n`.

### Without Function

```python
n = 5
fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)
```

### Using Function

```python
def calc_fact(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    print(fact)

calc_fact(5)
```

### 🔹 Output

```text
120
```

---

## 4️⃣ Convert USD to INR

**Question:**
Write a function to convert USD to INR.

```python
def converter(usd_val):
    inr_val = usd_val * 95
    print(usd_val, "USD =", inr_val, "INR")

n = int(input("Enter value to convert into INR: "))

converter(n)
```

> 💡 Here `95` is the conversion rate used in this example.

---

## 5️⃣ Check Odd or Even

**Question:**
Write a function to check whether the given number is odd or even.

```python
def odd_even(n):
    remainder = n % 2

    if remainder == 0:
        print("Even")
    else:
        print("Odd")

x = int(input("Enter number to check odd or even: "))

odd_even(x)
```

### 🔹 Example Output

```text
Enter number to check odd or even: 7
Odd
```

---

# ♻️ Recursion

**Recursion** is when a function calls **itself** repeatedly until a base condition is reached.

A recursive function generally has:

1. 🛑 **Base Case** → stops the recursion
2. 🔁 **Recursive Case** → function calls itself

---

# 🔢 Print `n` to `1` Backwards

```python
def show(n):
    if n == 0:
        return

    print(n)
    show(n - 1)

showx = int(input("Enter your value: "))

show(showx)
```

### 🔹 Example

```text
Enter your value: 5

5
4
3
2
1
```

Here:

```python
if n == 0:
    return
```

is the **base case**.

---

# 🧮 Factorial Using Recursion

```python
def fact(n):
    if n == 0 or n == 1:
        return 1

    return n * fact(n - 1)

x = int(input("Enter your number to calculate factorial: "))

print(fact(x))
```

### 🔹 Example

For `5`:

```text
5 × 4 × 3 × 2 × 1 = 120
```

Output:

```text
120
```

---

# 📝 Recursion — Let's Practice

## 1️⃣ Sum of First `n` Natural Numbers

**Question:**
Write a recursive function to calculate the sum of the first `n` natural numbers.

```python
def calc_sum(n):
    if n == 0:
        return 0

    return calc_sum(n - 1) + n

a = int(input("Enter number to calculate sum: "))

sum = calc_sum(a)

print(sum)
```

### 🔹 Example

For `5`:

```text
1 + 2 + 3 + 4 + 5 = 15
```

Output:

```text
15
```

---

## 2️⃣ Print All Elements of a List Using Recursion

**Question:**
Write a recursive function to print all elements in a list.

💡 **Hint:** Use `list` and `index` as parameters.

```python
def print_list(list, idx):
    if idx == len(list):
        return

    print(list[idx])
    print_list(list, idx + 1)

items = input("Enter list elements separated by space: ").split()

idx = int(input("Enter index to start from: "))

print_list(items, idx)
```

### 🔹 Example Output

```text
Enter list elements separated by space: delhi nagpur mumbai
Enter index to start from: 0

delhi
nagpur
mumbai
```

---

# 🧠 Quick Revision

| Concept               | Meaning                           |
| --------------------- | --------------------------------- |
| `def`                 | Defines a function                |
| Parameter             | Variable in function definition   |
| Argument              | Value passed during function call |
| `return`              | Returns a value                   |
| Built-in Function     | Already available in Python       |
| User-Defined Function | Created by programmer             |
| Default Parameter     | Parameter with a default value    |
| Recursion             | Function calling itself           |
| Base Case             | Condition that stops recursion    |
| Recursive Case        | Function calling itself           |

---

## 🚀 Remember

```text
Function
   ↓
Define → Call → Execute → Return
```

```text
Recursion
   ↓
Function calls itself
   ↓
Base Case
   ↓
Stops
```

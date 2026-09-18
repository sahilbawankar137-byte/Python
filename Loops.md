# 🐍 Loops in Python

* Loops are used to repeat instructions.
* They help us execute the same block of code multiple times.

---

# 🔄 While Loops

```python
while condition:
    # some work
```

### 👋 Print `"hello"` 5 times

```python
count = 1

while count <= 5:
    print("hello")
    count += 1
```

![Output](https://github.com/user-attachments/assets/1fb90db4-1362-4a12-b1c0-ce0db5ec487c)

---

### 🔢 Print numbers from 5 to 1

```python
i = 5

while i >= 1:
    print(i)
    i -= 1
```

![Output](https://github.com/user-attachments/assets/465e28e2-0a25-4a31-89a8-76dbc8f55412)

---

### ♾️ Infinite Loop

```python
i = 5

while i >= 1:
    print(i)
    i += 1
```

⚠️ Here, `i` keeps increasing while the condition `i >= 1` remains `True`, so the loop never ends.

---

# 📝 Let's Practice

### 1️⃣ Print numbers from 1 to 100

```python
i = 1

while i <= 100:
    print(i)
    i += 1
```

---

### 2️⃣ Print numbers from 100 to 1

```python
i = 100

while i >= 1:
    print(i)
    i -= 1
```

---

### 3️⃣ Print the multiplication table of a number `n`

```python
n = int(input("Enter a number to print its multiplication table: "))

i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1
```

![Output](https://github.com/user-attachments/assets/af3f08ff-9b9d-4819-b275-26d9cbd2cbee)

---

### 4️⃣ Print the elements of the following list using `while` Loop

```text
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

```python
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0

while idx < len(nums):
    print(nums[idx])
    idx += 1
```

![Output](https://github.com/user-attachments/assets/8e2e9053-4b5e-4619-afe8-2f365030c638)

---

### 5️⃣ Search for a number `X` in this list using a loop

```python
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = int(input("Enter the number to search for: "))

idx = 0

while idx < len(nums):
    if nums[idx] == x:
        print("Number found at index:", idx)
    idx += 1
```

![Output](https://github.com/user-attachments/assets/013a135f-1788-440a-862c-a8277d8f6397)

---

# 🛑 Break & Continue

## 🛑 Break

* Used to terminate the loop when encountered.

```python
i = 1

while i <= 5:
    print(i)

    if i == 3:
        break

    i += 1

print("Loop ended because of break statement")
```

![Output](https://github.com/user-attachments/assets/bca2760f-6f25-453f-bd9d-7d0de8c3005c)

---

## ⏭️ Continue

* Used to skip the current iteration of the loop and move on to the next iteration.

### Print odd numbers

```python
i = 1

while i <= 10:
    if i % 2 == 0:
        i += 1
        continue

    print(i)
    i += 1
```

![Output](https://github.com/user-attachments/assets/6045b445-f938-4887-966e-42d89ed446d2)

---

### Print even numbers

```python
i = 1

while i <= 10:
    if i % 2 != 0:
        i += 1
        continue

    print(i)
    i += 1
```

![Output](https://github.com/user-attachments/assets/5da55b7c-c6ed-4d82-86cf-618d43a40377)

---

# 🔁 For Loops

* `for` loops are used for sequential traversal.
* They can be used to traverse lists, strings, tuples, etc.

```python
for el in list:
    # some work
```

---

## 📋 List

```python
list = [1, 2, 3]

for el in list:
    print(el)
```

![Output](https://github.com/user-attachments/assets/7c23d361-c10f-4274-a19e-ad48b12a3a27)

---

## 👥 String List

```python
list = ["sahil", "ankita", "varsh", "bhajan"]

for el in list:
    print(el)
```

![Output](https://github.com/user-attachments/assets/de560631-79ce-426e-a10e-a6d13814cb70)

---

## 📦 Tuple

```python
tup = (1, 2, 3, 4, 2, 8, 9)

for num in tup:
    print(num)
```

![Output](https://github.com/user-attachments/assets/7334b289-e1ce-4858-ac8b-44f2cddad497)

---

## 🔤 String

```python
str = "Ankitasahil"

for char in str:
    print(char)
```

![Output](https://github.com/user-attachments/assets/2d42e807-be0a-480e-901a-915f734439bf)

---

# 🔚 For Loop with `else`

```python
for el in list:
    # some work

else:
    # work when loop ends
```

The `else` block runs when the `for` loop completes normally, without encountering a `break`.

### Example

```python
str = "ankita"

for char in str:
    print(char)

else:
    print("End")
```

---

### 🛑 Example with `break`

```python
str = "ankita"

for char in str:
    if char == "k":
        print("k found")
        break

    print(char)

else:
    print("End")
```

❌ The `else` block does **not** execute because the loop was terminated using `break`.

---

### ⏭️ Example with `continue`

```python
str = "ankita"

for char in str:
    if char == "k":
        print("k found")
        continue

    print(char)

else:
    print("End")
```

✅ The `else` block executes because `continue` only skips the current iteration; it does not terminate the loop.

---

# 📝 Let's Practice

### 1️⃣ Print the elements of the following list using a loop

```text
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

```python
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for num in nums:
    print(num)
```

---

### 2️⃣ Search for a number `X` in this tuple using a loop

```text
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

```python
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = int(input("Enter your number: "))

idx = 0

for el in nums:
    if el == x:
        print("Your number is found at index:", idx)

    idx += 1
```

---

# 📏 Range()

The `range()` function returns a sequence of numbers.

* Starts from `0` by default.
* Increases by `1` by default.
* Stops **before** the specified `stop` value.

```python
range(start, stop, step)
```

### 🔹 `range(stop)`

```python
for i in range(10):
    print(i)
```

---

### 🔹 `range(start, stop)`

```python
for i in range(5, 10):
    print(i)
```

---

### 🔹 `range(start, stop, step)`

```python
for i in range(5, 10, 2):
    print(i)
```

Here, `2` is the step value, so the numbers increase by `2`.

---

### 🔢 Another Example

```python
seq = range(5)

for i in seq:
    print(i)
```

Or simply:

```python
for i in range(5):
    print(i)
```

---

### 🟢 Print Even Numbers using `range()`

```python
for i in range(2, 11, 2):
    print(i)
```

---

# 📝 Let's Practice — Using `for` & `range()`

### 1️⃣ Print numbers from 1 to 100

```python
for nums in range(1, 101):
    print(nums)
```

---

### 2️⃣ Print numbers from 100 to 1

```python
for nums in range(100, 0, -1):
    print(nums)
```

---

### 3️⃣ Print the multiplication table of a number `n`

```python
n = int(input("Enter the number for multiplication table: "))

for nums in range(1, 11):
    print(n * nums)
```

---

# ⏸️ Pass Statement

`pass` is a null statement that does nothing.

It is used as a **placeholder for future code**.

```python
for i in range(5):
    pass
```

```python
if 1 > 4:
    pass

print("some useful work")
```

---

# 🧠 Let's Practice

### 1️⃣ WAP to find the sum of first `n` natural numbers using `while`

```python
n = int(input("Enter n: "))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print("Sum =", sum)
```

### Using `for` loop

```python
n = int(input("Enter n: "))

sum = 0

for i in range(1, n + 1):
    sum += i

print(sum)
```

---

### 2️⃣ WAP to find the factorial of `n` using `for`

```python
n = int(input("Enter n: "))

fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)
```

---

# 🎯 Quick Revision

| Concept    | Use                                     |
| ---------- | --------------------------------------- |
| `while`    | Repeat while a condition is `True`      |
| `for`      | Traverse a sequence                     |
| `break`    | Stop the loop                           |
| `continue` | Skip current iteration                  |
| `else`     | Runs when loop finishes without `break` |
| `range()`  | Generate a sequence of numbers          |
| `pass`     | Placeholder that does nothing           |

---

## 🚀 Keep Coding!

> **Practice → Make mistakes → Debug → Learn → Repeat.** 🐍💻

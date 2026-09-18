# 📋 Lists in Python

* A built-in data type that stores a collection of values.
* A list can store elements of different types such as integers, floats, strings, etc.
* Lists are **mutable**, which means their elements can be changed.

```python id="z8x0qv"
marks = [87, 64, 33, 85, 76]

# marks[0], marks[1], ...
```

### 📦 Different Data Types in a List

```python id="xj3q3c"
students = ["Karan", 85, "Delhi"]

# students[0], students[1], ...
```

### ✏️ Changing List Elements

```python id="m8k5ps"
student = ["Karan", 85, "Delhi"]

student[0] = "Arjun"  # Allowed in Python
```

### 📏 Length of a List

```python id="j5f8qv"
len(student)  # Returns the length of the list
```

---

# ✂️ List Slicing

* List slicing is similar to **String Slicing**.

```python id="b0x3ta"
list_name[starting_idx : ending_idx]
```

> 💡 Ending index is **not included**.

```python id="v3o7xk"
marks = [87, 64, 33, 95, 76]
```

### 🔹 Basic Slicing

```python id="9c9qv8"
marks[1:4]  # [64, 33, 95]
```

### 🔹 From Beginning

```python id="m6z6gc"
marks[:4]  # Same as marks[0:4]
```

### 🔹 Till the End

```python id="5k1e6v"
marks[1:]  # Same as marks[1:len(marks)]
```

### 🔹 Negative Index Slicing

```python id="2k6m3w"
marks[-3:-1]  # [33, 95]
```

---

# 🛠️ List Methods

```python id="r8k1z7"
list = [2, 1, 3]
```

### ➕ `append()`

Adds one element at the end of the list.

```python id="8c6v8u"
list.append(4)

# [2, 1, 3, 4]
```

### 🔼 `sort()`

Sorts the list in ascending order.

```python id="q5x9az"
list.sort()

# [1, 2, 3]
```

### 🔽 `sort(reverse=True)`

Sorts the list in descending order.

```python id="w7d3rs"
list.sort(reverse=True)

# [3, 2, 1]
```

### 📍 `insert()`

Inserts an element at a specific index.

```python id="3c1r8p"
list.insert(idx, el)
```

### ❌ `remove()`

Removes the first occurrence of the given element.

```python id="0v4y4h"
list.remove(1)
```

### 🗑️ `pop()`

Removes the element at the given index.

```python id="t1y6ku"
list.pop(idx)
```

---

# 📦 Tuples in Python

* A tuple is a built-in data type that stores an **ordered, immutable sequence** of values.
* Tuples are **immutable**, which means their elements cannot be changed after creation.

```python id="6z8v0n"
tup = (87, 64, 33, 95, 76)
```

### 🚫 Tuples are Immutable

```python id="9y7p4q"
tup[0] = 43  # Not allowed in Python
```

---

# 1️⃣ Single-Element Tuple

> 💡 A comma is required to create a single-element tuple.

```python id="h7q
```

# 📚 Lists & Tuples — Let's Practice

---

## 📝 Practice Questions

### 1️⃣ Store 3 Favorite Movies

**Question:**
Write a program to ask the user to enter the names of their **3 favorite movies** and store them in a list.

```python
movies = []

mov1 = input("Enter first movie: ")
mov2 = input("Enter second movie: ")
mov3 = input("Enter third movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)
```

---

### 2️⃣ Check for Palindrome

**Question:**
Write a program to check if a list contains a **palindrome** of elements.

💡 **Hint:** Use the `copy()` method.

```python
list1 = [1, 2, 3, 2, 1]
list2 = [1, "abc", "abc", 1]

copy_list1 = list1.copy()
copy_list1.reverse()

copy_list2 = list2.copy()
copy_list2.reverse()

if copy_list1 == list1:
    print("Palindrome")
else:
    print("NOT palindrome")

if copy_list2 == list2:
    print("Palindrome")
else:
    print("NOT palindrome")
```

### 💡 How it works

```text
Original List       Reversed Copy
[1, 2, 3, 2, 1]  →  [1, 2, 3, 2, 1]  ✅ Palindrome

[1, "abc", "abc", 1] → [1, "abc", "abc", 1] ✅ Palindrome
```

---

### 3️⃣ Count Students with Grade "A"

**Question:**
Write a program to count the number of students with the **"A" grade** in the following tuple.

```python
tup1 = ("C", "D", "A", "A", "B", "B", "A")

count = 0

for grade in tup1:
    if grade == "A":
        count += 1

print(count)
```

### 🔹 Output

```text
3
```

### ⚡ Easy Way — Using `count()`

Since tuples have a built-in `count()` method, we can do the same thing in one line:

```python
grade = ("C", "D", "A", "A", "B", "B", "A")

print(grade.count("A"))
```

### 🔹 Output

```text
3
```

> ⭐ **Remember:** `count()` returns how many times a particular value appears in a list or tuple.

---

## 🧠 Quick Revision

| Concept        | Example                   |
| -------------- | ------------------------- |
| Create List    | `movies = []`             |
| Add Element    | `movies.append("Dangal")` |
| Copy List      | `list2 = list1.copy()`    |
| Reverse List   | `list1.reverse()`         |
| Create Tuple   | `tup = (1, 2, 3)`         |
| Count in Tuple | `tup.count("A")`          |
| Check Equality | `list1 == list2`          |

---

### 🚀 Key Takeaways

* `append()` → adds an element to a list.
* `copy()` → creates a copy of a list.
* `reverse()` → reverses a list.
* `count()` → counts how many times a value occurs.
* Lists are **mutable** → can be changed.
* Tuples are **immutable** → cannot be changed.

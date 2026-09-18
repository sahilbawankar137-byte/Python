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

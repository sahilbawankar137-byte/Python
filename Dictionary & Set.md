# 📖 Dictionary in Python

* Dictionaries are used to store data values in **key:value pairs**.
* They are **mutable (changeable)**.
* Keys must be **unique**.
* Dictionaries preserve insertion order in modern Python.

```python
info = {
    "key": "value",
    "subjects": ["python", "c"],
    "topics": ("dict", "set"),
    "is_adult": 25,
}
```

### 🔍 Accessing Dictionary Values

```python
print(info["key"])

print(info["subjects"])

print(info["topics"])

print(info["is_adult"])
```

<img width="145" height="90" alt="image" src="https://github.com/user-attachments/assets/f68b9fd5-e148-4b3b-a559-30ee34ab1b29" />

---

### ❌ Accessing a Non-Existing Key

```python
print(info["surname"])  # ERROR
```

This gives a `KeyError` because `"surname"` does not exist in the dictionary.

---

### ✏️ Updating a Value

```python
info["key"] = "sahil"

print(info)
```

---

### 🆕 Creating an Empty Dictionary

```python
null_dict = {}

null_dict["name"] = "sahilbawankar"

print(null_dict)
```

---

# 🪆 Nested Dictionaries

A dictionary can contain another dictionary as a value.

```python
student = {
    "name": "ankita sakharwade",

    "subjects": {
        "phy": 97,
        "chem": 98,
        "math": 95
    }
}
```

### 🔍 Accessing Nested Values

```python
print(student["subjects"]["chem"])
```

<img width="26" height="15" alt="image" src="https://github.com/user-attachments/assets/c57e5c6e-83bb-4022-813a-1ae888b33e97" />

---

# 🛠️ Methods of Dictionary

1. `myDict.keys()` → Returns all keys.
2. `myDict.values()` → Returns all values.
3. `myDict.items()` → Returns all `(key, value)` pairs as tuples.
4. `myDict.get("key")` → Returns the value associated with the key.
5. `myDict.update(newDict)` → Inserts or updates the specified items in the dictionary.

---

# 💻 Dictionary Methods — Code

```python
student = {
    "name": "ankita sakharwade",

    "subject
```

# 📝 Let's Practice — Dictionaries & Sets

---

## 📖 Dictionaries — Practice

### 1️⃣ Store Word Meanings in a Dictionary

**Question:**
Store the following word meanings in a Python dictionary:

* `table` → a piece of furniture / list of facts & figures
* `cat` → a small animal

```python
word_meanings = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": "a small animal"
}

print(word_meanings)
```

### 🔹 Output

```text
{
    'table': ['a piece of furniture', 'list of facts & figures'],
    'cat': 'a small animal'
}
```

> 💡 A dictionary value can also be a **list**.

---

### 2️⃣ Find Number of Required Classrooms

**Question:**
You are given a list of subjects for students. Assume **one classroom is required for each subject**.

Find the total number of classrooms required.

```python
subjects = {
    "python",
    "java",
    "C++",
    "python",
    "javascript",
    "java",
    "python",
    "C++",
    "C"
}

print(len(subjects))
```

### 🔹 Output

```text
5
```

> 💡 A **set automatically removes duplicate values**, so only unique subjects are counted.

```text
python
java
C++
javascript
C
```

---

## 📊 Dictionaries — Storing Marks

### 3️⃣ Store Marks of 3 Subjects

**Question:**
Write a program to enter marks of **3 subjects** from the user and store them in a dictionary.

Start with an empty dictionary and add values one by one.
Use the **subject name as key** and **marks as value**.

```python
marks = {}

math = float(input("Enter your math marks: "))
physics = float(input("Enter your physics marks: "))
chemistry = float(input("Enter your chemistry marks: "))

marks.update({
    "math": math,
    "physics": physics,
    "chemistry": chemistry
})

print(marks)
```

### 🔹 Example Output

```text
Enter your math marks: 90
Enter your physics marks: 85
Enter your chemistry marks: 88

{'math': 90.0, 'physics': 85.0, 'chemistry': 88.0}
```

---

# 🧩 Sets — Practice

### 4️⃣ Store `9` and `9.0` as Separate Values

**Question:**
Find a way to store `9` and `9.0` as separate values in a set.

### ❌ This does NOT work

```python
values = {9, 9.0}

print(values)
```

Because Python considers:

```python
9 == 9.0
```

as `True`, so the set keeps only one value.

---

### ✅ Method 1 — Use Different Data Types

```python
values = {9, "9.0"}

print(values)
```

Here `9` is an integer and `"9.0"` is a string, so they are treated as different values.

---

### ✅ Method 2 — Store Type Along With Value

```python
values = {
    ("float", 9.0),
    ("int", 9)
}

print(values)
```

### 🔹 Output

```text
{('float', 9.0), ('int', 9)}
```

> 💡 By storing the **type information along with the value**, both values can exist separately.

---

## 🧠 Quick Revision

| Problem                | Main Concept             |
| ---------------------- | ------------------------ |
| Word meanings          | Dictionary + List        |
| Unique subjects        | Set                      |
| Count classrooms       | `len()`                  |
| Store marks            | Dictionary               |
| Add dictionary values  | `update()`               |
| `9` vs `9.0`           | Same numeric value       |
| Separate values in set | Different representation |

---

### 🚀 Key Takeaways

* Dictionaries store data in **key-value pairs**.
* A dictionary value can be a **list**.
* Sets automatically remove **duplicate**

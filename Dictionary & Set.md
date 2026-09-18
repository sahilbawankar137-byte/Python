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

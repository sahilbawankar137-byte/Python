# Dictionary in Python

---

- Dictionaries are used to store data values in key:value pairs
- They are unordered, mutable (changeable) & don't allow duplicate keys

---

```python
info = {
    "key": "value",

    "subjects": ["python", "c"],

    "topics": ("dict", "set"),

    "is_adult": 25,
}
```

```python
print(info["key"])

print(info["subjects"])

print(info["topics"])

print(info["is_adult"])
```

---

```python
print(info["surname"]) # ERROR
```

---

```python
info["key"] = "sahil"

print(info)
```

---

```python
null_dict = {}

null_dict["name"] = "sahilbawankar"

print(null_dict)
```

---

# Nested Dictionaries

```python
student = {
    "name": " ankita sakharwade",

    "subjects": {

        "phy": 97,

        "chem": 98,

        "math": 95
    }
}
```

```python
print(student["subjects"]["chem"])
```

---

# Method of dictionary

1. `myDict.keys()` # returns all keys

2. `myDict.values()` # returns all values

3. `myDict.items()` # returns all (key,val) pairs as tuples

4. `myDict.get("key")` # returns all key according to value

5. `myDict.update(newDict)` # inserts the specified items to the dictionary

---

# CODE

```python
student = {
    "name": " ankita sakharwade",

    "subjects": {

        "phy": 97,

        "chem": 98,

        "math": 95
    }
}
```

### 1.

```python
print(list(student.keys()))

print(len(student))

print(len(list(student.keys())))
```

---

### 2.

```python
print(student.values())

print(list(student.values()))

print(len(list(student.values())))
```

---

### 3.

```python
print(student.items())

pairs = list(student.items())

print(pairs[1][1]["phy"])

print(list(student.items()))

print(len(list(student.items())))
```

---

### 4.

```python
print(student.get("name")) # Same

print(student["name"]) # Same
```

- Then why myDict.items()...because

```python
print(student.get("name2")) # no error -> None

print(student["name2"]) # error
```

---

### 5.

```python
student.update(list(new_dict.items()))

new_dict = {
    "city": "Nagpur",
    "state": "Maharashtra"
}

print(student)
```

---

```python
new_dict = {
    "name": "andkita",
    "age": 17
}

print(student)
```

---

# SET IN PYTHON

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
<img width="145" height="90" alt="image" src="https://github.com/user-attachments/assets/f68b9fd5-e148-4b3b-a559-30ee34ab1b29" />

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

<img width="26" height="15" alt="image" src="https://github.com/user-attachments/assets/c57e5c6e-83bb-4022-813a-1ae888b33e97" />

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

### 1.myDict.keys()

```python
print(list(student.keys()))

print(len(student))

print(len(list(student.keys())))
```

<img width="197" height="67" alt="image" src="https://github.com/user-attachments/assets/168cdddd-efa0-4b63-a487-1606c4da77cc" />

---

### 2.myDict.values()

```python
print(student.values())

print(list(student.values()))

print(len(list(student.values())))
```

<img width="682" height="72" alt="image" src="https://github.com/user-attachments/assets/fb26f846-cc17-4e8d-ac98-0b2fc3c69190" />

---

### 3.myDict.items()

```python
print(student.items())

pairs = list(student.items())

print(pairs[1][1]["phy"])

print(list(student.items()))

print(len(list(student.items())))
```

<img width="857" height="92" alt="image" src="https://github.com/user-attachments/assets/c8321cd1-b372-4c24-a1ca-ba2b6a54f0f3" />

---

### 4.myDict.get("key")

```python
print(student.get("name")) # Same

print(student["name"]) # Same
```

<img width="171" height="45" alt="image" src="https://github.com/user-attachments/assets/080a8a81-1ba5-452d-8818-a23956865a74" />

- Then why myDict.get()...because

```python
print(student.get("name2")) # no error -> None

print(student["name2"]) # error
```

---

### 5.myDict.update(newDict)

```python
new_dict = {"city" : "Nagpur", "state" : "Maharashtra"}
student.update(list(new_dict.items()))

print(student)
```

<img width="1093" height="30" alt="image" src="https://github.com/user-attachments/assets/c3b9c782-9e34-4df7-a3f6-e788273fd50f" />

---

```python
new_dict = {
    "name": "ankita",
    "age": 17
}

print(student)
```

<img width="727" height="22" alt="image" src="https://github.com/user-attachments/assets/897e6439-95ac-4adb-86dd-180c381437c7" />

---

# SET IN PYTHON

- Set is the collection of the unordered items.
- Each element in the set must be unique & immutable.

```python
collection = {1, 3, 4, 5, "hello", "world", "world"}

print(collection)
print(type(collection))
```

<img width="272" height="40" alt="image" src="https://github.com/user-attachments/assets/0481f6e1-f972-4b48-9f88-72129fb67937" />

```python
collection = {1, 2, 2, 2, "hello", "world", "world"}

print(collection)
print(type(collection))
print(len(collection))  # total number of items
```

<img width="228" height="67" alt="image" src="https://github.com/user-attachments/assets/ba896b96-309f-45e1-b89b-bd38816bae0f" />

```python
collection = {}  # empty dictionary

print(type(collection))
```

<img width="142" height="23" alt="image" src="https://github.com/user-attachments/assets/aa437468-3c28-4a66-9d3e-92a5f7a68701" />

```python
collection = set()  # empty set syntax

print(type(collection))
```

<img width="128" height="20" alt="image" src="https://github.com/user-attachments/assets/557b4982-c702-4fe3-998e-61bd61f54e71" />

---

# Set Methods

## 1. `set.add(el)`

- Adds an element to the set.

```python
collection = set()

collection.add(2009)
collection.add(7)
collection.add(13)
collection.add("sahil")

print(collection)
```

<img width="201" height="23" alt="image" src="https://github.com/user-attachments/assets/35b85c71-2802-4143-afbb-c33351c5acea" />

---

## 2. `set.remove(el)`

- Removes an element from the set.

```python
collection.remove(2009)

print(collection)
```

<img width="147" height="25" alt="image" src="https://github.com/user-attachments/assets/ad84f43e-568e-4c1c-b184-44e07426f16b" />

---

## 3. `set.clear()`

- Empties the set.

```python
collection = {1, 3, 4, 5, "hello", "world", "world"}

print(len(collection))

collection.clear()

print(len(collection))
```

<img width="25" height="45" alt="image" src="https://github.com/user-attachments/assets/f01388f1-f585-4b20-852f-b188f71acf83" />

---

## 4. `set.pop()`

- Removes a random value.

```python
collection = {1, 3, 4, 5, "hello", "world", "world"}

print(collection.pop())
```

<img width="45" height="18" alt="image" src="https://github.com/user-attachments/assets/bddedea4-34f6-409c-98e1-5a20bd21d510" />

<img width="28" height="18" alt="image" src="https://github.com/user-attachments/assets/6a6dd4ef-fbda-41b0-b9fd-15046b1ab2c4" />

---

## 5. `set.union(set2)`

- Combines both set values & returns a new set.

```python
set1 = {1, 2, 3}

set2 = {2, 3, 4}

print(set1.union(set2))
```

---

## 6. `set.intersection(set2)`

- Combines common values.

```python
set1 = {1, 2}

set2 = {2, 3, 4}

print(set1.intersection(set2))
```

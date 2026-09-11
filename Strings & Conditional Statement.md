# Strings

- String is a data type that stores a sequence of characters.

---

# Basic Operations

### Concatenation

```python
"hello" + "world"  # "helloworld"
```

### Length of String

```python
len(str)
```

---

# Indexing

```text
S  a  h  i  l  b  a  w  a  n  k  a  r
0  1  2  3  4  5  6  7  8  9  10 11 12
```

---

# Slicing

- Accessing parts of a string.

```text
str[starting_idx : ending_idx]
```

> Ending index is not included.

```python
str = "sahilbawankar"

str[1:4]  # "ahi"

str[0:4]  # same as str[1:4]

str[1:]   # same as str[1:len(str)]
```

---

# Slicing — Negative Index

```text
 A  p  p  l  e
-5 -4 -3 -2 -1
```

```python
str = "Apple"

str[-3:-1]  # "pl"
```

---

# String Function

```python
str = "I am a coder."
```

### `endswith()`

```python
str.endswith("er.")
```

- Returns `True` if the string ends with the given substring.

### `capitalize()`

```python
str.capitalize()
```

- Capitalizes the first character.

### `replace()`

```python
str.replace(old, new)
```

- Replaces all occurrences of `old` with `new`.

### `find()`

```python
str.find(word)
```

- Returns the first index of the first occurrence.

### `count()`

```python
str.count("am")
```

- Counts the occurrence of the substring in the string.

---

# Let's Practice

## 1. WAP to input user's first name & print its length.

```python
first = input("enter your name")

print("length of your name is:", len(first))
```

---

## 2. WAP to find the occurrence of `$` in a string.

```python
str = "hi, i am a $ the $ symbol $ 99.99"

print(str.count("$"))
```

---

# Conditional Statements

- `if-elif-else` statements

```python
if(condition):
    Statement1

elif(condition):
    Statement2

else:
    StatementN
```

---

# Conditional Statements

## Grade Students Based on Marks

```text
marks >= 90       → grade = "A"

90 > marks >= 80  → grade = "B"

80 > marks >= 70  → grade = "C"

70 > marks       → grade = "D"
```

### Code

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

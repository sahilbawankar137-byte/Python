# List in python

- A built-in type that store set of values
- It can store elements of different types(integers,float,string,etc.)

```python
mark = [87,64,33,85,76] # marks[0],marks[1]...
```

```python
students = ["Karan",85,"Delhi"] # student[0],student[1]...
```

```python
student[0] = "arjun" # = allowed in python
```

```python
len(student) # return length
```

---

# List Slicing

- Similar to String Slicing

```python
list_name[starting_idx:ending_idx] # ending idx is not included
```

```python
marks = [87,64,33,95,76]
```

```python
marks[1:4] # is [64,33,95]
```

```python
marks[:4] # is same as marks[0:4]
```

```python
marks[1:] # is same as marks[1:len(marks)]
```

```python
marks[-3:-1] # is [33,95]
```

---

# List Methods

```python
list = [2,1,3]
```

```python
list.append(4)    # adds one element at the end [2,1,3,4]
```

```python
list.sort()    # sorts in ascending order [1,2,3]
```

```python
list.sort(reverse=True)    # sort in descending order [3,2,1]
```

```python
list.insert(idx,el)    # insert element at index
```

```python
list.remove(1)    # removes first occurrence of element [2,3,1]
```

```python
list.pop(idx)   # remove element at idx
```

---

# Tuples in Python

- A built-in data type that create immutable sequences of values.

```python
tup = (87,64,33,95,76)
```

```python
tup[0] = 43 # Not allowed in Python
```

```python
tup = [1,]
```

```python
tup2 = (1,)
```

```python
tup3 = (1,2,3)
```

# Loops in Python

- Loops are used to repeat instructions.

---

# While Loops

```python
while condition:
    # some work
```

### Print "hello" 5 times

```python
count = 1

while count <= 5:
    print("hello")
    count += 1
```

![Output](https://github.com/user-attachments/assets/1fb90db4-1362-4a12-b1c0-ce0db5ec487c)

---

### Print numbers from 1 to 5

```python
i = 5

while i >= 1:
    print(i)
    i -= 1
```

![Output](https://github.com/user-attachments/assets/465e28e2-0a25-4a31-89a8-76dbc8f55412)

---

### Infinite Iterator

```python
i = 5

while i >= 1:
    print(i)
    i += 1
```

---

# Let's Practice

### Print numbers from 1 to 100

```python
i = 1

while i <= 100:
    print(i)
    i += 1
```

---

### Print numbers from 100 to 1

```python
i = 100

while i >= 1:
    print(i)
    i -= 1
```

---

### Print the multiplication table of a number `n`

```python
n = int(input("Enter a number to print its multiplication table: "))

i = 1

while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1
```

![Output](https://github.com/user-attachments/assets/af3f08ff-9b9d-4819-b275-26d9cbd2cbee)

---

### Print the elements of the following list using while Loop

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

### Search for a number `X` in this tuple using Loop

```python
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

x = int(input("Enter the number to search for: "))

idx = 0

while idx < len(nums):
    if nums[idx] == x:
        print("Number found at index:", idx)
    idx += 1
else:
    print("Number not found")
```

![Output](https://github.com/user-attachments/assets/013a135f-1788-440a-862c-a8277d8f6397)

---

# Break & Continue

### Break

- Used to terminate the loop when encountered.

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

### Continue

- Used to skip the current iteration of the loop and move on to the next iteration.

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

```python
i = 1

while i <= 100:
    if i % 2 != 0:
        i += 1
        continue

    print(i)
    i += 1
```

![Output](https://github.com/user-attachments/assets/bfe17098-666e-4b09-9b8f-b5667cd9c985)

---

# For Loops

- Loops are used for sequential traversal.
- For traversing list, string, tuples etc.

```python
for el in list:
    # same work
```

---

### List

```python
list = [1, 2, 3]

for el in list:
    print(el)
```

![Output](https://github.com/user-attachments/assets/7c23d361-c10f-4274-a19e-ad48b12a3a27)

---

### String List

```python
list = ["sahil", "ankita", "varsh", "bhajan"]

for el in list:
    print(el)
```

![Output](https://github.com/user-attachments/assets/de560631-79ce-426e-a10e-a6d13814cb70)

---

### Tuple

```python
tup = (1, 2, 3, 4, 2, 8, 9)

for num in tup:
    print(num)
```

![Output](https://github.com/user-attachments/assets/7334b289-e1ce-4858-ac8b-44f2cddad497)

---

### String

```python
str = "Ankitasahil"

for char in str:
    print(char)
```

![Output](https://github.com/user-attachments/assets/2d42e807-be0a-480e-901a-915f734439bf)

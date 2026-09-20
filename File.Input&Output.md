# 📁 File I/O in Python

Python can be used to perform operations on files, such as **reading and writing data**.

---

# 📂 Types of Files

There are mainly two types of files:

### 1️⃣ Text Files

Examples:

```text
.txt
.docx
.log
```

### 2️⃣ Binary Files

Examples:

```text
.mp4
.mov
.png
.jpeg
```

---

# 🔓 Open, Read & Close a File

We have to **open a file** before reading or writing.

### Syntax

```python
f = open("file_name", "mode")
```

* `file_name` → Name/path of the file
* `mode` → Specifies what operation we want to perform

Example:

```python
f = open(r"C:\Users\sahil\OneDrive\Apps\Clipchamp Classic\demo.txt","r")

data = f.read()

print(data)
print(type(data))

f.close()
```

---

# ⚙️ File Modes

| Mode | Meaning                                     |
| ---- | ------------------------------------------- |
| `r`  | Read mode (default)                         |
| `w`  | Write mode — truncates/overwrites the file  |
| `x`  | Creates a new file and opens it for writing |
| `a`  | Append mode — adds data to the end          |
| `b`  | Binary mode                                 |
| `t`  | Text mode (default)                         |
| `+`  | Opens file for both reading and writing     |

### 💡 Examples

```python
"rb"   # Read binary
"wb"   # Write binary
"r+"   # Read + Write
"w+"   # Write + Read
"a+"   # Append + Read
```

> ⚠️ **Important:** `a` means **append**, not binary.
> `b` is used for **binary mode**.

---

# 📖 Reading a File

## `read()`

`read()` reads the **entire file**.

```python
f = open(r"C:\Users\sahil\OneDrive\Apps\Clipchamp Classic\demo.txt","r")

data = f.read()

print(data)

f.close()
```

---

## `readline()`

`readline()` reads **one line at a time**.

```python
f = open(r"C:\Users\sahil\OneDrive\Apps\Clipchamp Classic\demo.txt","r")

line1 = f.readline()

print(line1)

f.close()
```

---

# ✍️ Writing to a File

## `w` — Write Mode

`w` writes data to a file and **overwrites the existing content**.

```python
f = open(r"C:\Users\sahil\OneDrive\Apps\Clipchamp Classic\demo.txt","w")

f.write("This is a new line")

f.close()
```

> ⚠️ If the file already contains data, `w` will erase the old content.

---

# ➕ Append Mode

`a` adds new data to the **end of the file** without deleting existing content.

```python
f = open("demo.txt", "a")

f.write("This is a new line")

f.close()
```

---

## 📝 Writing Multiple Lines

```python
f = open(r"C:\Users\sahil\OneDrive\Apps\Clipchamp Classic\demo.txt","w")

f.write("I want to learn mathematics tomorrow")
f.write("\nI love programming")

f.close()
```

---

# 🆕 Creating a File

We can create a new file using `a` or `x`.

```python
f = open("sahil.txt", "a")
f.close()
```

Or:

```python
f = open("sahil.txt", "x")
f.close()
```

> 💡 `x` gives an error if the file already exists.

---

# 🔄 `r+` Mode

`r+` allows us to **read and write**.

```python
f = open(r"C:\Users\sahil\OneDrive\Apps\Clipchamp Classic\demo.txt","r+")

print(f.read())

f.close()
```

### We can also write:

```python
f = open(r"C:\Users\sahil\OneDrive\Apps\Clipchamp Classic\demo.txt","r+")

f.write("abc")

print(f.read())

f.close()
```

> 💡 `r+` does **not** erase the existing file content.

---

# 🔄 `w+` Mode

`w+` allows **writing and reading**, but it first **truncates the file**.

```python
f = open(r"C:\Users\sahil\OneDrive\Apps\Clipchamp Classic\demo.txt","w+")

print(f.read())

f.close()
```

Because `w+` truncates the file, the existing content is removed.

---

# ➕ `a+` Mode

`a+` allows **appending and reading**.

```python
f = open(r"C:\Users\sahil\OneDrive\Apps\Clipchamp Classic\demo.txt","a+")

f.write("abc")

f.seek(0)

print(f.read())

f.close()
```

> 💡 In `a+`, writing happens at the **end of the file**.
> `seek(0)` moves the file pointer back to the beginning so we can read the content.

---

# 🧠 File Pointer

Whenever we read or write a file, Python keeps track of the current position using a **file pointer**.

We can move it using:

```python
f.seek(0)
```

`seek(0)` → moves the pointer to the beginning of the file.

---

# 🧹 `with` Syntax

Python provides an easier way to work with files using `with`.

```python
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)
```

We **do not need to call ****`f.close()`** when using `with`.

Python automatically closes the file after the `with` block ends.

### Writing with `with`

```python
with open("demo.txt", "w") as f:
    f.write("New data")
```

### Reading & Writing

```python
with open(r"C:\Users\sahil\OneDrive\Apps\Clipchamp Classic\demo.txt","r+") as f:
    data = f.read()
    print(data)
```

---

# 🗑️ Deleting a File

We can delete a file using the **`os`**** module**.

### 📦 What is a Module?

A module is a Python file/library containing code and functions that we can use in our programs.

### Syntax

```python
import os

os.remove("filename")
```

### Example

```python
import os

os.remove("sahil.txt")
```

---

# 📝 Let's Practice

## 1️⃣ Create `practice.txt`

**Question:**
Create a new file `practice.txt` using Python and add the following data:

```text
Hi everyone
we are learning File I/O
using Java
I like programming in Java
```

### Solution

```python
with open("practice.txt", "w") as f:
    f.write("Hi everyone\n")
    f.write("we are learning File I/O\n")
    f.write("using Java.\n")
    f.write("I like programming in Java.")
```

---

## 2️⃣ Replace `Java` with `Python`

**Question:**
Write a function to replace all occurrences of `"Java"` with `"Python"` in the above file.

```python
with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")

with open("practice.txt", "w") as f:
    f.write(new_data)

print(new_data)
```

### 🔹 Output

```text
Hi everyone
we are learning File I/O
using Python.
I like programming in Python.
```

---

## 3️⃣ Search for a Word

**Question:**
Search if the word `"learning"` exists in the file or not.

```python
def check_for_word():
    word = input("Enter word to find: ")

    with open("practice.txt", "r") as f:
        data = f.read()

        if data.find(word) != -1:
            print("Found")
        else:
            print("Not found")

check_for_word()
```

### 🔹 Example

```text
Enter word to find: learning
Found
```

> 💡 `find()` returns the index of the word if found.
> If the word is not found, it returns `-1`.

---

## 4️⃣ Find the First Line Containing a Word

**Question:**
Write a function to find the line number where the word `"learning"` occurs first.

If the word is not found, print `-1`.

```python
def check_for_line():
    word = input("Enter word to find: ")

    line_no = 1

    with open("practice.txt", "r") as f:
        while True:
            data = f.readline()

            if not data:
                break

            if word in data:
                print(line_no)
                return

            line_no += 1

    print(-1)

check_for_line()
```

### 🔹 Example

```text
Enter word to find: learning
2
```

---

# 🔢 5️⃣ Count Even Numbers

**Question:**
A file contains numbers separated by commas.
Read the file and print the **count of even numbers**.

### Example File

```text
1,2,3,4,5,6,7,8
```

### Solution

```python
with open("practice.txt", "r") as f:
    data = f.read()

nums = data.split(",")

count = 0

for val in nums:
    if int(val) % 2 == 0:
        count += 1

print(count)
```

### 🔹 Output

```text
4
```

### 💡 How it works

```text
"1,2,3,4,5,6,7,8"
          ↓
       split(",")
          ↓
[1, 2, 3, 4, 5, 6, 7, 8]
          ↓
    Check % 2 == 0
          ↓
     2, 4, 6, 8
          ↓
         4
```

---

# 🧠 Quick Revision

| Operation           | Mode / Method |
| ------------------- | ------------- |
| Read file           | `r`           |
| Write file          | `w`           |
| Append data         | `a`           |
| Create new file     | `x`           |
| Binary mode         | `b`           |
| Text mode           | `t`           |
| Read + Write        | `r+`          |
| Write + Read        | `w+`          |
| Append + Read       | `a+`          |
| Read entire file    | `read()`      |
| Read one line       | `readline()`  |
| Write data          | `write()`     |
| Move file pointer   | `seek()`      |
| Delete file         | `os.remove()` |
| Automatically close | `with`        |

---

# 🚀 Key Takeaways

* `r` → read
* `w` → overwrite/write
* `a` → append
* `x` → create
* `b` → binary
* `+` → read + write
* `read()` → reads entire file
* `readline()` → reads one line
* `write()` → writes data
* `with open()` → automatically closes the file
* `os.remove()` → deletes a file
* `%` → useful for checking even/odd numbers

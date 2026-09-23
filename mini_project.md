# 🐍 Python Mini Projects

A collection of beginner-friendly Python mini projects created while learning Python.

---

# 🎯 1. Guess the Number Game

A simple guessing game where Python randomly selects a number between **1 and 100**, and the user has to guess it.

The program gives hints after every wrong guess:

* 📉 Guess is too small → Try a bigger number
* 📈 Guess is too big → Try a smaller number
* 🎯 Correct guess → Game ends
* ❌ `Q` / `q` → Quit the game

---

## 💻 Code

```python
import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target or Quit(Q): ")

    if userChoice.lower() == "q":
        break

    userChoice = int(userChoice)

    if userChoice == target:
        print("Success: Correct Guess!!")
        break

    elif userChoice < target:
        print("Your number was too small. Take a bigger guess.")

    else:
        print("Your number was too big. Take a smaller guess.")

print("-------- GAME OVER --------")
```

---

## 🧠 Concepts Used

* `random` module
* `random.randint()`
* `while` loop
* `if / elif / else`
* `input()`
* Type casting using `int()`
* `break`
* String methods → `.lower()`

---

## 🎮 How It Works

```text
Python generates a random number
           ↓
     User enters guess
           ↓
     Is it "Q" / "q"?
       ↙           ↘
     Yes            No
      ↓              ↓
     Quit       Convert to int
                     ↓
             Compare with target
               ↙    ↓     ↘
            Small  Correct  Big
              ↓      ↓       ↓
           Bigger   Win    Smaller
            guess          guess
```

---

# 🔐 2. Random Password Generator

A simple password generator that creates a random password based on the length entered by the user.

The password can contain:

* 🔤 Uppercase & lowercase letters
* 🔢 Numbers
* 🔣 Special characters

---

## 💻 Code

```python
import random
import string

pass_len = int(
    input("Enter the length of password which you want to generate: ")
)

charValues = string.ascii_letters + string.digits + string.punctuation

# password = ""

# for i in range(pass_len):
#     password += random.choice(charValues)

# List comprehension / generator expression
res = "".join(
    random.choice(charValues)
    for i in range(pass_len)
)

print("Your generated password is:", res)
```

---

## 🧠 Concepts Used

* `random` module
* `string` module
* `string.ascii_letters`
* `string.digits`
* `string.punctuation`
* `random.choice()`
* `input()`
* Type casting using `int()`
* `range()`
* `join()`
* Generator expression

---

## 🔍 Important Parts

### `string.ascii_letters`

Contains:

```text
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

### `string.digits`

Contains:

```text
0123456789
```

### `string.punctuation`

Contains special characters such as:

```text
! @ # $ % ^ & * ( ) ...
```

### Combining Them

```python
charValues = string.ascii_letters + string.digits + string.punctuation
```

Now `charValues` contains letters, numbers, and special characters.

---

## 🎲 `random.choice()`

`random.choice()` selects one random character from a sequence.

```python
random.choice(charValues)
```

---

## 🔗 `join()`

This:

```python
"".join(...)
```

combines all generated characters into one string.

Example:

```python
"".join(["a", "7", "@", "K"])
```

Output:

```text
a7@K
```

---

# 📚 Mini Projects — Quick Revision

| Project               | Main Concepts                                       |
| --------------------- | --------------------------------------------------- |
| 🎯 Guess the Number   | `random`, `while`, conditions, `break`, `input()`   |
| 🔐 Password Generator | `random`, `string`, `choice()`, `join()`, `range()` |

---

# 🚀 What I Learned

Through these mini projects, I practiced:

* Taking user input
* Using Python modules
* Generating random values
* Working with loops
* Using conditional statements
* Using `break`
* Type casting
* Working with strings
* Using `random.choice()`
* Using `join()`
* Creating small real-world Python programs

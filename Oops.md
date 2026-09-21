# 🐍 OOP in Python

**OOP = Object-Oriented Programming**

To map real-world scenarios into code, we use **objects**.

This approach is called **Object-Oriented Programming (OOP)**.

---

# 🧱 Class & Object in Python

### What is a Class?

A **class** is a blueprint/template for creating objects.

### Creating a Class

```python
class Student:
    name = "sahil"
```

### Creating an Object (Instance)

```python
s1 = Student()

print(s1.name)
```

### Multiple Objects

```python
class Student:
    name = "sahil bawankar"

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)
```

Both `s1` and `s2` are objects of the `Student` class.

---

### Example: Car

```python
class Car:
    color = "blue"       # Class Attribute
    brand = "Mercedes"   # Class Attribute

car1 = Car()             # Object

print(car1.color)
print(car1.brand)
```

**Output:**

```text
blue
Mercedes
```

---

# ⚙️ `__init__()` Function

`__init__()` is a special method that is automatically executed when an object is created.

It is commonly called a **constructor**.

### Creating a Class

```python
class Student:
    def __init__(self, fullname):
        self.name = fullname
```

### Creating an Object

```python
s1 = Student("karan")

print(s1.name)
```

**Output:**

```text
karan
```

---

### Example

```python
class Student:
    def __init__(self, fullname):
        print("Adding new student in Database.")

s1 = Student("sahil")
```

**Output:**

```text
Adding new student in Database.
```

---

### Using Multiple Parameters

```python
class Student:
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks

        print("Adding new student in Database..")


s1 = Student("sahil", 99)

print(s1.name, s1.marks)

s2 = Student("arjun", 97)

print(s2.name, s2.marks)
```

**Output:**

```text
Adding new student in Database..
sahil 99
Adding new student in Database..
arjun 97
```

---

## 🧍 What is `self`?

The `self` parameter is a reference to the **current object (instance)** of the class.

It is used to access variables and methods belonging to that object.

Example:

```python
class Student:
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
```

Here:

* `self.name` → name of the current object
* `self.marks` → marks of the current object

---

# 🔹 Types of Constructors

## 1. Default Constructor

A constructor that does not take additional parameters.

```python
class Student:
    def __init__(self):
        pass
```

---

## 2. Parameterized Constructor

A constructor that accepts parameters.

```python
class Student:
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks
```

---

# 📌 Class & Instance Attributes

There are two common types of attributes:

### Class Attribute

A **class attribute** belongs to the class and is shared by all objects of that class.

```python
class Student:
    college_name = "ABC College"
```

Access using:

```python
Student.college_name
```

or

```python
s1.college_name
```

---

### Instance Attribute

An **instance attribute** belongs to a particular object.

It is usually created using `self`.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
```

Access using:

```python
s1.name
s1.marks
```

### Example

```python
class Student:
    college_name = "ABC College"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


s1 = Student("sahil", 99)

print(s1.name)
print(s1.marks)
print(s1.college_name)
```

### Quick Difference

| Type               | Belongs To | Example                |
| ------------------ | ---------- | ---------------------- |
| Class Attribute    | Class      | `Student.college_name` |
| Instance Attribute | Object     | `s1.name`              |

> **Instance attributes generally take priority over class attributes when both have the same name.**

---

# 🔧 Methods

**Methods are functions that belong to a class/object.**

### Example

```python
class Student:
    def __init__(self, fullname):
        self.name = fullname

    def hello(self):
        print("Hello", self.name)


s1 = Student("karan")

s1.hello()
```

**Output:**

```text
Hello karan
```

---

### Example with Multiple Methods

```python
class Student:
    college_name = "ABC"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome student,", self.name)

    def get_marks(self):
        return self.marks


s1 = Student("sahil", 99)

s1.welcome()

print("Your mark is:", s1.get_marks())
```

**Output:**

```text
Welcome student, sahil
Your mark is: 99
```

---

# 📝 Let's Practice

### Question

Create a `Student` class that takes **name** and **marks of 3 subjects** as arguments in the constructor.

Then create a method to print the **average marks**.

### Solution

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        total = 0

        for val in self.marks:
            total += val

        print("Hi", self.name, "your avg score is:", total / 3)


s1 = Student("Tony Stark", [99, 98, 97])

s1.get_avg()
```

**Output:**

```text
Hi Tony Stark your avg score is: 98.0
```

### Changing Instance Attribute

```python
s1.name = "Ironman"

s1.get_avg()
```

Now the output becomes:

```text
Hi Ironman your avg score is: 98.0
```

---

# ⚡ Static Methods

A **static method** is a method that does not use the `self` parameter.

It is created using the `@staticmethod` decorator.

```python
class Student:

    @staticmethod
    def hello():
        print("Hello")


s1 = Student()

s1.hello()
```

**Output:**

```text
Hello
```

---

## 🎀 Decorators

**Decorators** allow us to extend the behavior of a function without permanently modifying the original function.

Example:

```python
@staticmethod
```

Here, `@staticmethod` is a decorator.

---

# 🚗 Important OOP Concepts

## 1. Abstraction

**Abstraction** means hiding the implementation details and showing only the essential features to the user.

### Example

```python
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True

        print("Car started..")


car1 = Car()

car1.start()
```

The user only needs to call:

```python
car1.start()
```

The internal implementation is hidden.

---

# 🔒 2. Encapsulation

**Encapsulation** means wrapping data and functions together into a single unit (object).

Example:

```python
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount

        print("Rs.", amount, "was debited.")
        print("Total balance =", self.get_balance())

    def credit(self, amount):
        self.balance += amount

        print("Rs.", amount, "was credited.")
        print("Total balance =", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(100000, 12345)

acc1.debit(1000)
acc1.credit(500)
acc1.credit(1000000)
acc1.debit(100000)
acc1.credit(499)
```

Here, **data** (`balance`, `account_no`) and **methods** (`debit`, `credit`, `get_balance`) are wrapped together inside the `Account` class.

---

# 🧠 OOP Quick Revision

| Concept                | Meaning                                    |
| ---------------------- | ------------------------------------------ |
| **Class**              | Blueprint for creating objects             |
| **Object**             | Instance of a class                        |
| `__init__()`           | Constructor, runs when object is created   |
| `self`                 | Reference to the current object            |
| **Class Attribute**    | Attribute shared by the class/objects      |
| **Instance Attribute** | Attribute belonging to a particular object |
| **Method**             | Function inside a class                    |
| `@staticmethod`        | Creates a method that doesn't use `self`   |
| **Decorator**          | Extends/modifies function behavior         |
| **Abstraction**        | Hides implementation details               |
| **Encapsulation**      | Combines data and methods into one unit    |

---

## 🔥 Key Takeaways

* **Class** → Blueprint
* **Object** → Real instance created from the blueprint
* `__init__()` → Automatically runs when an object is created
* `self` → Refers to the current object
* **Class Attribute** → Shared at class level
* **Instance Attribute** → Specific to an object
* **Method** → Function inside a class
* `@staticmethod` → Method without `self`
* **Abstraction** → Hide unnecessary implementation details
* **Encapsulation** → Bundle data + methods together

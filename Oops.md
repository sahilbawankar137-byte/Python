# 🐍 OOP in Python

To map real-world scenarios into code, we started using **objects**.

This is called **Object-Oriented Programming (OOP)**.

---

# 🧱 Class & Object in Python

### Class

A **class** is a blueprint for creating objects.

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

### Example

```python
class Student:
    name = "sahil bawankar"

s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)
```

---

### 🚗 Example: Car

```python
class Car:
    color = "blue"       # Class Attribute
    brand = "Mercedes"   # Class Attribute


car1 = Car()             # Object

print(car1.color)
print(car1.brand)
```

---

# ⚙️ `__init__()` Function

## Constructor

`__init__()` is a special function that is automatically executed when an object is created.

### Example

```python
class Student:
    def __init__(self, fullname):
        self.name = fullname


s1 = Student("karan")

print(s1.name)
```

**Output:**

```text
karan
```

---

### Example with Multiple Parameters

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

---

## 🧍 `self` Parameter

The `self` parameter is a reference to the **current instance/object** of the class.

It is used to access variables and methods that belong to the object.

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

## Class Attribute

A **class attribute** belongs to the class and is shared by its objects.

```python
class Student:
    college_name = "ABC College"
```

Access:

```python
Student.college_name
```

or:

```python
s1.college_name
```

---

## Instance Attribute

An **instance attribute** belongs to a particular object.

It is usually created using `self`.

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
```

Access:

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

| Attribute          | Belongs To | Example                |
| ------------------ | ---------- | ---------------------- |
| Class Attribute    | Class      | `Student.college_name` |
| Instance Attribute | Object     | `s1.name`              |

> If a class attribute and instance attribute have the same name, the **instance attribute gets priority** when accessed through the object.

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

---

# 📝 Let's Practice

### Question

Create a `Student` class that takes **name** and marks of 3 subjects as arguments in the constructor.

Then create a method to print the average.

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

### Changing an Instance Attribute

```python
s1.name = "Ironman"

s1.get_avg()
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

---

## 🎀 Decorators

Decorators allow us to extend the behavior of a function without permanently modifying the original function.

Example:

```python
@staticmethod
```

Here, `@staticmethod` is a decorator.

---

# 🧠 Important OOP Concepts

## 1. Abstraction

**Abstraction** means hiding the implementation details of a class and showing only the essential features to the user.

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

**Encapsulation** means wrapping data and functions into a single unit (object).

### Example

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

---

# 🗑️ `del` Keyword

The `del` keyword is used to delete **object properties** or an **object itself**.

### Example

```python
class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("sahil")

del s1.name

print(s1.name)   # Error
```

After `del s1.name`, the `name` attribute no longer exists.

---

# 🔐 Private Attributes & Methods

Python does not have strict private members like some other languages, but we can use `__` to indicate that an attribute or method is intended for internal use.

## Normal Code

```python
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass


acc1 = Account("12345", "abcde")

print(acc1.acc_no)
print(acc1.acc_pass)
```

---

## Private-like Attribute

```python
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def reset_pass(self):
        print(self.__acc_pass)


acc1 = Account("12345", "abcde")

print(acc1.acc_no)

# print(acc1.__acc_pass)  # Error

acc1.reset_pass()
```

`__acc_pass` cannot be accessed directly from outside the class using its normal name.

---

### Private Method Example

```python
class Person:
    __name = "anonymous"

    def __hello(self):
        print("Hello person!")

    def welcome(self):
        self.__hello()


p1 = Person()

p1.welcome()
```

Here, `__hello()` is a private-like method and is called internally through `welcome()`.

---

# 🧬 Inheritance

**Inheritance** is when one class (child/derived class) derives properties and methods from another class (parent/base class).

### Basic Syntax

```python
class Car:
    pass


class ToyotaCar(Car):
    pass
```

---

### Example

```python
class Car:
    color = "black"

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped.")


class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name


car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

print("Your car name is:", car1.name)
print("Your car color is:", car1.color)

car1.start()
car1.stop()
```

`ToyotaCar` inherits `color`, `start()` and `stop()` from `Car`.

---

# 🔗 Types of Inheritance

* **Single Inheritance**
* **Multilevel Inheritance**
* **Multiple Inheritance**

---

## 1. Multilevel Inheritance

```python
class Car:
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped.")


class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name


class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type


car1 = Fortuner("Diesel")

car1.start()
```

Here:

```text
Car
 ↓
ToyotaCar
 ↓
Fortuner
```

---

## 2. Multiple Inheritance

A class can inherit from more than one parent class.

```python
class A:
    varA = "Welcome to class A"


class B:
    varB = "Welcome to class B"


class C(A, B):
    varC = "Welcome to class C"


c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)
```

---

# 🦸 `super()` Method

The `super()` method is used to access methods and the constructor of the parent class.

```python
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped.")


class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name

        super().__init__(type)
        super().start()


car1 = ToyotaCar("Prius", "Electric")

print(car1.type)
```

---

# 🏫 Class Method

A **class method** is bound to the class and receives the class as its first argument, usually named `cls`.

It is created using the `@classmethod` decorator.

```python
class Student:

    @classmethod
    def college(cls):
        print("ABC College")
```

### Three Different Types of Methods

| Method          | First Parameter | Used For          |
| --------------- | --------------- | ----------------- |
| Static Method   | None            | Utility functions |
| Class Method    | `cls`           | Class-level data  |
| Instance Method | `self`          | Object-level data |

---

# 👤 Class Method Example

### Instance Method

```python
class Person:
    name = "anonymous"

    def changeName(self, name):
        self.name = name


p1 = Person()

p1.changeName("Sahil")

print(p1.name)
print(Person.name)
```

Output:

```text
Sahil
anonymous
```

Here, `self.name` creates/changes the **instance attribute**, not the class attribute.

---

### Changing Class Attribute

```python
class Person:
    name = "anonymous"

    def changeName(self, name):
        Person.name = name


p1 = Person()

p1.changeName("Sahil")

print(p1.name)
print(Person.name)
```

Now the class attribute is changed.

---

### Using `self.__class__`

```python
class Person:
    name = "anonymous"

    def changeName(self, name):
        self.__class__.name = name


p1 = Person()

p1.changeName("Sahil")

print(p1.name)
print(Person.name)
```

---

### Using `@classmethod`

```python
class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls, name):
        cls.name = name


p1 = Person()

p1.changeName("Sahil")

print(p1.name)
print(Person.name)
```

This is the cleaner way to modify class-level data.

---

# 🏷️ Property

We use the `@property` decorator to make a method behave like an attribute.

### Example

```python
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"


stu1 = Student(89, 90, 99)

print(stu1.percentage)
```

If marks are changed:

```python
stu1.phy = 86

print(stu1.percentage)
```

The percentage is automatically recalculated.

---

# 🔄 Polymorphism

**Polymorphism** means the same operator/function can have different meanings depending on the context.

## Operator Overloading

Python uses **dunder methods** to implement operator overloading.

### Operators & Dunder Functions

| Operator | Dunder Function    |
| -------- | ------------------ |
| `a + b`  | `a.__add__(b)`     |
| `a - b`  | `a.__sub__(b)`     |
| `a * b`  | `a.__mul__(b)`     |
| `a / b`  | `a.__truediv__(b)` |
| `a % b`  | `a.__mod__(b)`     |

### Examples

```python
print(1 + 2)                  # 3

print("sahil" + "bawankar")   # sahilbawankar

print([1, 2, 3] + [4, 5, 6])  # [1, 2, 3, 4, 5, 6]
```

The `+` operator behaves differently depending on the data type.

---

# 🔢 Operator Overloading with Custom Classes

```python
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img

        return Complex(newReal, newImg)

    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img

        return Complex(newReal, newImg)

    def __mul__(self, num2):
        newReal = self.real * num2.real
        newImg = self.img * num2.img

        return Complex(newReal, newImg)


num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()
```

---

# 📝 Let's Practice

## 1. Circle Class

Define a `Circle` class to create a circle with radius `r` using the constructor.

Define:

* `area()` method to calculate the area.
* `perimeter()` method to calculate the perimeter.

### Solution

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (22 / 7) * self.radius ** 2

    def perimeter(self):
        return 2 * (22 / 7) * self.radius


c1 = Circle(21)

print(c1.area())
print(c1.perimeter())
```

---

## 2. Employee & Engineer

Create an `Employee` class with attributes:

* `role`
* `department`
* `salary`

The class should also have a `showDetails()` method.

Create an `Engineer` class that inherits from `Employee` and has additional attributes:

* `name`
* `age`

### Solution

```python
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Role =", self.role)
        print("Department =", self.dept)
        print("Salary =", self.salary)


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age

        super().__init__("Engineer", "IT", 75000)


engg1 = Engineer("Sahil", 18)

engg1.showDetails()
```

---

## 3. Order & `__gt__()`

Create a class called `Order` which stores an item and its price.

Use the dunder function `__gt__()` to compare two orders.

`order1 > order2` should return `True` if the price of `order1` is greater than the price of `order2`.

### Solution

```python
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price


order1 = Order("Chips", 20)
order2 = Order("Tea", 15)

print(order1 > order2)
```

**Output:**

```text
True
```

---

# 🧠 OOP Quick Revision

| Concept                | Meaning                                  |
| ---------------------- | ---------------------------------------- |
| **Class**              | Blueprint for creating objects           |
| **Object**             | Instance of a class                      |
| `__init__()`           | Constructor                              |
| `self`                 | Reference to current object              |
| **Class Attribute**    | Shared class-level attribute             |
| **Instance Attribute** | Object-specific attribute                |
| **Method**             | Function inside a class                  |
| `@staticmethod`        | Method without `self`                    |
| `@classmethod`         | Method that receives `cls`               |
| `@property`            | Makes a method behave like an attribute  |
| **Abstraction**        | Hides implementation details             |
| **Encapsulation**      | Combines data and methods                |
| **Inheritance**        | Child class gets features of parent      |
| `super()`              | Access parent class functionality        |
| **Polymorphism**       | Same operation with different behavior   |
| **Dunder Method**      | Special methods like `__add__`, `__gt__` |

---

# 🔥 Key Takeaways

* **Class** → Blueprint
* **Object** → Instance of a class
* `__init__()` → Automatically runs when an object is created
* `self` → Refers to the current object
* **Class Attribute** → Shared at class level
* **Instance Attribute** → Specific to an object
* **Method** → Function inside a class
* `@staticmethod` → Method without `self`
* `@classmethod` → Method with `cls`
* `@property` → Method accessed like an attribute
* **Abstraction** → Hide unnecessary implementation details
* **Encapsulation** → Bundle data + methods
* **Inheritance** → Reuse parent class properties/methods
* `super()` → Access parent class
* **Polymorphism** → Same operator, different behavior
* **Dunder Methods** → Special methods used by Python operators

# Loops in python
- loops are used to repeat insructions.

# while loops

   #while condition:
     #some work

!print hello 5 times

 count = 1 
 while count <= 5 
    print ("hello")
    count += 1

<img width="368" height="115" alt="image" src="https://github.com/user-attachments/assets/1fb90db4-1362-4a12-b1c0-ce0db5ec487c" />


!print number from 1 to 5

i = 5
while i >= 1:
  print(i)
  i -= 1

  <img width="232" height="107" alt="image" src="https://github.com/user-attachments/assets/465e28e2-0a25-4a31-89a8-76dbc8f55412" />

!Infinite, iterator

i = 5
while i >= 1:
    print(i)
    i += 1

# Let's Practice

- print numbers from 1 to 100

while i <= 100:
    print(i)
    i += 1

- print numbers from 100 to 1
  
  = 100
while i >= 1:
    print(i)
   
- print the multiplication table of a number n.
  
n = int(input("Enter a number to print its multiplication table:"))

i = 1
while i <= 10:
    print(n, "x", i, "=", n*i)
    i += 1

<img width="581" height="293" alt="image" src="https://github.com/user-attachments/assets/af3f08ff-9b9d-4819-b275-26d9cbd2cbee" />


- Print the elements of the following list using while Loop
- [1, 4, 9,16, 25, 36, 49, 64, 81, 100]

  ums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

   <img width="372" height="252" alt="image" src="https://github.com/user-attachments/assets/8e2e9053-4b5e-4619-afe8-2f365030c638" />


- Search for a number X in this tuple using Loop:

  ms = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
x = int(input("Enter the number to search for: "))
idx = 0
while idx < len(nums):
    if nums[idx] == x:
        print("Number found at index:", idx)
    idx += 1
else:
    print("Number not found")

<img width="415" height="52" alt="image" src="https://github.com/user-attachments/assets/013a135f-1788-440a-862c-a8277d8f6397" />

# Break & Continue

Break: used to terminate the loop when encountered.


i = 1 
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1

print("Loop ended because of break statement")

<img width="267" height="77" alt="image" src="https://github.com/user-attachments/assets/bca2760f-6f25-453f-bd9d-7d0de8c3005c" />

# continue : used to skip the current iteration of the loop and move on to the next iteration
eg.
i = 1 
while i <=10:
    if i%2 == 0:
        i += 1
        continue
    print(i)
    i += 1

<img width="275" height="132" alt="image" src="https://github.com/user-attachments/assets/6045b445-f938-4887-966e-42d89ed446d2" />


i = 1 
while i <=100:
    if i%2 != 0:
        i += 1
        continue
    print(i)
    i += 1

<img width="412" height="255" alt="image" src="https://github.com/user-attachments/assets/bfe17098-666e-4b09-9b8f-b5667cd9c985" />

- Loops are used for sequential traversal. For traversing list,string,tuples etc.

  # For Loops
  for el in list:
  #same work

- list = [ 1, 2, 3]

for el in list :
print(el)

<img width="163" height="80" alt="image" src="https://github.com/user-attachments/assets/7c23d361-c10f-4274-a19e-ad48b12a3a27" />


- list = ["sahil, "ankita","varsh","bhajan"]

for el in list:
  print(el)

<img width="242" height="102" alt="image" src="https://github.com/user-attachments/assets/de560631-79ce-426e-a10e-a6d13814cb70" />

tup = (1, 2, 3, 4, 2, 8, 9)

for num in tup:
    print(num

<img width="402" height="173" alt="image" src="https://github.com/user-attachments/assets/7334b289-e1ce-4858-ac8b-44f2cddad497" />


str = "Ankitasahil"

for char in str:
    print(char)

<img width="285" height="280" alt="image" src="https://github.com/user-attachments/assets/2d42e807-be0a-480e-901a-915f734439bf" />

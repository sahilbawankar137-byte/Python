# LET'S PRACTICE


# 1. WAP to ask the user to enter names of their 3 favorite movies
#    & store them in a list.

movies = []

mov1 = input("enter first movie:")
mov2 = input("enter second movie:")
mov3 = input("enter third movie:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)


# 2. WAP to check if a list contains a palindrome of elements.
#    Hint: use copy() method.

list1 = [1, 2, 3, 2, 1]
list2 = [1, "abc", "abc", 1]

copy_list1 = list1.copy()
copy_list1.reverse()

copy_list2 = list2.copy()
copy_list2.reverse()

if copy_list1 == list1:
    print("palindrome")
else:
    print("NOT palindrome")

if copy_list2 == list2:
    print("palindrome")
else:
    print("NOT palindrome")


# 3. WAP to count a number of students with the "A" grade
#    in the following tuple.

tup1 = ["C", "D", "A", "A", "B", "B", "A"]

count = 0

for grade in tup1:
    if grade == "A":
        count += 1

print(count)


# OR

grade = ("C", "D", "A", "A", "B", "B", "A")

print(grade.count("A"))

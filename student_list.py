# Initial list of students
#TODO: Create a List of Students names. Add 10 names. Name this list as 'student'
student = ["Celeste", "Facundo", "Lautaro", "Franco", "Martina", "Sam", "Julieta", "Agustin", "Lucas", "Isaak"]
def display_students():
    print(f"_____________________________________")
    print(f"Current students:\n")
    for i in student:
        print(i) 

# Add a new student to the list
def add_student():
    new_name = input("Type the name of the new student: ")
    student.append(new_name)
    display_students()


# Remove a student from the list by name
def remove_student():
    remove = input("What is the name you want to remove: ")
    if remove in student:
        student.remove(remove)
    else:
        print("Name not found")
    display_students()


# remove a student from the end of the list
def pop_student():
    last = student.pop()
    print(f"{last} was removed from the end of the list")
    if not student:
        print("There are no elements left")
    display_students()

# Update a student's name in the list
def update_student():
    #TODO HINT: ask for the current name of the student
    name = input("Write the student name: ")
    if name in student:
        new = input("Write the name you want to update it from: ")
    find = student.index(name)
    student[find] = new
    if not new:
        print("This name does not exist")
    else:
        print("This name exist")
    display_students()


# Menu to manage student operations
def menu():
    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. Remove a student")
        print("3. Pop a student")
        print("4. Update a student's name")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        if choice == "2":
            remove_student()
        if choice == "3":
            pop_student()
        if choice == "4":
            update_student()
        if choice == "5":
            break
        else:
            "Not valid"

menu()
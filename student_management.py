import os

FILE_NAME = "students.txt"
students = []

# Load students from file
def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 4:
                    student = {
                        "id": data[0],
                        "name": data[1],
                        "age": data[2],
                        "course": data[3]
                    }
                    students.append(student)

# Save students to file
def save_students():
    with open(FILE_NAME, "w") as file:
        for s in students:
            file.write(f"{s['id']},{s['name']},{s['age']},{s['course']}\n")

# Add student
def add_student():
    sid = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    students.append({
        "id": sid,
        "name": name,
        "age": age,
        "course": course
    })

    save_students()
    print("✅ Student Added Successfully!\n")

# View students
def view_students():
    if not students:
        print("⚠ No students available.\n")
        return

    print("\n--- Student List ---")
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']} | Course: {s['course']}")
    print()

# Search student
def search_student():
    sid = input("Enter Student ID: ")
    for s in students:
        if s["id"] == sid:
            print("\n🎯 Student Found:")
            print(s)
            print()
            return
    print("❌ Student Not Found!\n")

# Delete student
def delete_student():
    sid = input("Enter Student ID: ")
    for s in students:
        if s["id"] == sid:
            students.remove(s)
            save_students()
            print("🗑 Student Deleted Successfully!\n")
            return
    print("❌ Student Not Found!\n")

# Update student
def update_student():
    sid = input("Enter Student ID: ")
    for s in students:
        if s["id"] == sid:
            print("Leave blank to keep old value")
            name = input(f"New Name ({s['name']}): ") or s["name"]
            age = input(f"New Age ({s['age']}): ") or s["age"]
            course = input(f"New Course ({s['course']}): ") or s["course"]

            s["name"] = name
            s["age"] = age
            s["course"] = course

            save_students()
            print("✏ Student Updated Successfully!\n")
            return
    print("❌ Student Not Found!\n")

# Main Menu
def main_menu():
    while True:
        print("====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("👋 Thank you! Program Closed.")
            break
        else:
            print("⚠ Invalid choice! Try again.\n")

# Program start
load_students()
main_menu()

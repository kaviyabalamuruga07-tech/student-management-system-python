from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os

FILE_NAME = "students.txt"
students = []

# ---------------- File Handling ----------------

def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 4:
                    students.append({
                        "id": data[0],
                        "name": data[1],
                        "age": data[2],
                        "course": data[3]
                    })

def save_students():
    with open(FILE_NAME, "w") as file:
        for s in students:
            file.write(f"{s['id']},{s['name']},{s['age']},{s['course']}\n")

# ---------------- Functions ----------------

def add_student():
    sid = entry_id.get()
    name = entry_name.get()
    age = entry_age.get()
    course = entry_course.get()

    if sid == "" or name == "" or age == "" or course == "":
        messagebox.showwarning("Warning", "All fields required")
        return

    students.append({"id": sid, "name": name, "age": age, "course": course})
    save_students()
    view_students()
    clear_fields()
    messagebox.showinfo("Success", "Student Added Successfully")

def view_students():
    for row in table.get_children():
        table.delete(row)

    for s in students:
        table.insert("", END, values=(s["id"], s["name"], s["age"], s["course"]))

def delete_student():
    selected = table.focus()
    if not selected:
        messagebox.showwarning("Warning", "Select a student")
        return

    values = table.item(selected, "values")
    for s in students:
        if s["id"] == values[0]:
            students.remove(s)
            break

    save_students()
    view_students()
    messagebox.showinfo("Deleted", "Student Deleted")

def update_student():
    selected = table.focus()
    if not selected:
        messagebox.showwarning("Warning", "Select a student")
        return

    values = table.item(selected, "values")

    for s in students:
        if s["id"] == values[0]:
            s["name"] = entry_name.get()
            s["age"] = entry_age.get()
            s["course"] = entry_course.get()
            break

    save_students()
    view_students()
    clear_fields()
    messagebox.showinfo("Updated", "Student Updated")

def select_student(event):
    selected = table.focus()
    values = table.item(selected, "values")
    if values:
        entry_id.set(values[0])
        entry_name.set(values[1])
        entry_age.set(values[2])
        entry_course.set(values[3])

def clear_fields():
    entry_id.set("")
    entry_name.set("")
    entry_age.set("")
    entry_course.set("")

# ---------------- GUI Design ----------------

root = Tk()
root.title("Student Management System")
root.geometry("750x500")
root.resizable(False, False)

title = Label(root, text="Student Management System", font=("Arial", 18, "bold"))
title.pack(pady=10)

# Input Frame
frame = Frame(root)
frame.pack()

Label(frame, text="ID").grid(row=0, column=0, padx=5, pady=5)
Label(frame, text="Name").grid(row=0, column=2, padx=5, pady=5)
Label(frame, text="Age").grid(row=1, column=0, padx=5, pady=5)
Label(frame, text="Course").grid(row=1, column=2, padx=5, pady=5)

entry_id = StringVar()
entry_name = StringVar()
entry_age = StringVar()
entry_course = StringVar()

Entry(frame, textvariable=entry_id).grid(row=0, column=1)
Entry(frame, textvariable=entry_name).grid(row=0, column=3)
Entry(frame, textvariable=entry_age).grid(row=1, column=1)
Entry(frame, textvariable=entry_course).grid(row=1, column=3)

# Buttons
btn_frame = Frame(root)
btn_frame.pack(pady=10)

Button(btn_frame, text="Add", width=12, command=add_student).grid(row=0, column=0, padx=5)
Button(btn_frame, text="Update", width=12, command=update_student).grid(row=0, column=1, padx=5)
Button(btn_frame, text="Delete", width=12, command=delete_student).grid(row=0, column=2, padx=5)
Button(btn_frame, text="Clear", width=12, command=clear_fields).grid(row=0, column=3, padx=5)

# Table
table_frame = Frame(root)
table_frame.pack()

table = ttk.Treeview(table_frame, columns=("ID", "Name", "Age", "Course"), show="headings", height=10)
table.heading("ID", text="ID")
table.heading("Name", text="Name")
table.heading("Age", text="Age")
table.heading("Course", text="Course")

table.column("ID", width=100)
table.column("Name", width=200)
table.column("Age", width=100)
table.column("Course", width=200)

table.pack()
table.bind("<ButtonRelease-1>", select_student)

# Load old data
load_students()
view_students()

root.mainloop()

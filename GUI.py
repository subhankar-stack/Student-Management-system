import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os

FILE_NAME = "Student_Details.txt"

# ---------------- FILE FUNCTIONS ----------------
def read_students():
    students = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                if line.startswith("|"):
                    parts = line.strip().split("|")

                    if len(parts) >= 8:
                        students.append([
                            parts[1].strip(),
                            parts[2].strip(),
                            parts[3].strip(),
                            parts[4].strip(),
                            parts[5].strip(),
                            parts[6].strip(),
                            parts[7].strip()
                        ])

    return students


def save_students(students):
    BORDER = "+---+--------------------+---+---------+---------+--------------------------+---------------------+\n"

    with open(FILE_NAME, "w") as file:
        for student in students:
            file.write(
                f"|{student[0]:<3}"
                f"|{student[1]:<20}"
                f"|{student[2]:<3}"
                f"|{student[3]:<9}"
                f"|{student[4]:<9}"
                f"|{student[5]:<26}"
                f"|{student[6]:<20}|\n"
            )
            file.write(BORDER)


# ---------------- MAIN FUNCTIONS ----------------
def refresh_table():
    for row in tree.get_children():
        tree.delete(row)

    students = read_students()

    for student in students:
        tree.insert("", tk.END, values=student)


def add_student():
    students = read_students()

    slno = str(len(students) + 1)
    name = entry_name.get()
    age = entry_age.get()
    month = entry_month.get()
    date = entry_date.get()
    college = entry_college.get()
    school = entry_school.get()

    if name == "" or age == "":
        messagebox.showerror("Error", "Name and Age are required")
        return

    students.append([
        slno,
        name,
        age,
        month,
        date,
        college,
        school
    ])

    save_students(students)
    refresh_table()
    clear_entries()

    messagebox.showinfo("Success", "Student Added Successfully")


def delete_student():
    selected = tree.selection()

    if not selected:
        messagebox.showerror("Error", "Select a student")
        return

    item = tree.item(selected)
    slno = item['values'][0]

    students = read_students()

    new_students = []
    count = 1

    for student in students:
        if student[0] != str(slno):
            student[0] = str(count)
            new_students.append(student)
            count += 1

    save_students(new_students)
    refresh_table()

    messagebox.showinfo("Success", "Student Deleted")


def update_student():
    selected = tree.selection()

    if not selected:
        messagebox.showerror("Error", "Select a student")
        return

    item = tree.item(selected)
    old_slno = str(item['values'][0])

    students = read_students()

    for student in students:
        if student[0] == old_slno:
            student[1] = entry_name.get()
            student[2] = entry_age.get()
            student[3] = entry_month.get()
            student[4] = entry_date.get()
            student[5] = entry_college.get()
            student[6] = entry_school.get()
            break

    save_students(students)
    refresh_table()

    messagebox.showinfo("Success", "Student Updated")


def select_student(event):
    selected = tree.selection()

    if selected:
        item = tree.item(selected)
        values = item['values']

        clear_entries()

        entry_name.insert(0, values[1])
        entry_age.insert(0, values[2])
        entry_month.insert(0, values[3])
        entry_date.insert(0, values[4])
        entry_college.insert(0, values[5])
        entry_school.insert(0, values[6])


def clear_entries():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_month.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    entry_college.delete(0, tk.END)
    entry_school.delete(0, tk.END)


# ---------------- GUI ----------------
root = tk.Tk()
root.title("Student Management System")
root.geometry("1100x600")
root.configure(bg="#1e1e1e")

# ---------------- TITLE ----------------
heading = tk.Label(
    root,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="cyan"
)
heading.pack(pady=10)

# ---------------- FORM FRAME ----------------
form_frame = tk.Frame(root, bg="#1e1e1e")
form_frame.pack(pady=10)

# Labels and Entries
labels = [
    "Name",
    "Age",
    "Admission Month",
    "Admission Date",
    "College",
    "School"
]

entries = []

for i, text in enumerate(labels):
    lbl = tk.Label(
        form_frame,
        text=text,
        font=("Arial", 12),
        bg="#1e1e1e",
        fg="white"
    )
    lbl.grid(row=i, column=0, padx=10, pady=5, sticky="w")

    ent = tk.Entry(form_frame, width=40, font=("Arial", 11))
    ent.grid(row=i, column=1, padx=10, pady=5)

    entries.append(ent)

entry_name = entries[0]
entry_age = entries[1]
entry_month = entries[2]
entry_date = entries[3]
entry_college = entries[4]
entry_school = entries[5]

# ---------------- SEARCH ----------------
def search_student():
    keyword = search_entry.get().lower()

    for row in tree.get_children():
        tree.delete(row)

    students = read_students()
    found = False

    for student in students:
        if (
            keyword in student[1].lower() or
            keyword in student[2].lower() or
            keyword in student[3].lower() or
            keyword in student[4].lower() or
            keyword in student[5].lower() or
            keyword in student[6].lower()
        ):
            tree.insert("", tk.END, values=student)
            found = True

    if not found:
        messagebox.showinfo("Search", "No student found")


def show_all_students():
    search_entry.delete(0, tk.END)
    refresh_table()


# ---------------- SEARCH BAR ----------------
search_frame = tk.Frame(root, bg="#1e1e1e")
search_frame.pack(pady=10)

search_label = tk.Label(
    search_frame,
    text="Search:",
    font=("Arial", 12, "bold"),
    bg="#1e1e1e",
    fg="white"
)
search_label.grid(row=0, column=0, padx=5)

search_entry = tk.Entry(search_frame, width=40, font=("Arial", 11))
search_entry.grid(row=0, column=1, padx=10)

search_btn = tk.Button(
    search_frame,
    text="Search",
    font=("Arial", 10, "bold"),
    bg="purple",
    fg="white",
    width=12,
    command=search_student
)
search_btn.grid(row=0, column=2, padx=5)

show_btn = tk.Button(
    search_frame,
    text="Show All",
    font=("Arial", 10, "bold"),
    bg="cyan",
    fg="black",
    width=12,
    command=show_all_students
)
show_btn.grid(row=0, column=3, padx=5)


# ---------------- BUTTONS ----------------
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=10)

btn_add = tk.Button(
    button_frame,
    text="Add Student",
    font=("Arial", 11, "bold"),
    bg="green",
    fg="white",
    width=15,
    command=add_student
)
btn_add.grid(row=0, column=0, padx=10)

btn_update = tk.Button(
    button_frame,
    text="Update Student",
    font=("Arial", 11, "bold"),
    bg="blue",
    fg="white",
    width=15,
    command=update_student
)
btn_update.grid(row=0, column=1, padx=10)

btn_delete = tk.Button(
    button_frame,
    text="Delete Student",
    font=("Arial", 11, "bold"),
    bg="red",
    fg="white",
    width=15,
    command=delete_student
)
btn_delete.grid(row=0, column=2, padx=10)

btn_clear = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 11, "bold"),
    bg="orange",
    fg="black",
    width=15,
    command=clear_entries
)
btn_clear.grid(row=0, column=3, padx=10)

# ---------------- TABLE ----------------
columns = (
    "SL No",
    "Name",
    "Age",
    "Month",
    "Date",
    "College",
    "School"
)

style = ttk.Style()
style.theme_use("default")

style.configure(
    "Treeview",
    background="#2b2b2b",
    foreground="white",
    rowheight=25,
    fieldbackground="#2b2b2b",
    font=("Arial", 10)
)

style.configure(
    "Treeview.Heading",
    font=("Arial", 11, "bold")
)

tree = ttk.Treeview(root, columns=columns, show="headings", height=12)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)

tree.pack(fill="both", expand=True, padx=20, pady=10)

# Select Event
tree.bind("<<TreeviewSelect>>", select_student)

# Load Data
refresh_table()

# ---------------- RUN ----------------
root.mainloop()
 

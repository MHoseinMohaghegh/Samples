import tkinter as tk
import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkinter import *
import form2
# Connect to the data base
conn = sqlite3.connect("data_base.db")

cur = conn.cursor()

# Create a table to store contacts
cur.execute("""CREATE TABLE IF NOT EXISTS students (
    first_name varchar(20) ,
    last_name varchar(20),
    title varchar(10),
    age int(100),
    nationality varchar(20),
    completed_courses int(100),
    semesters int(100)
)""")

x = False
window = tk.Tk()
window.title("Data Entry Form")
frame = tkinter.Frame(window)
frame.pack()
# Enter data function


def enter_data():
    # Create a cursor
    cur = conn.cursor()
    accepted = accept_var.get()
    if accepted == "Accepted":
        # User info
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()

        if first_name and last_name:
            title = title_combobox.get()
            try:
                age = int(age_spinbox.get())
            except ValueError:
                print("Invalid input: age must be an integer")
                return
            nationality = nationality_combobox.get()
            # Course info
            try:
                completed_courses = int(numcourses_spinbox.get())
            except ValueError:
                print("Invalid input: courses number must be an integer")
                return
            try:
                semesters = int(numsemesters_spinbox.get())
            except ValueError:
                print("Invalid input: courses number must be an integer")
                return
            # Create a SQL query to insert the data into the table
            sql = """INSERT INTO students (first_name,last_name,title,age,nationality,
            completed_courses, semesters) VALUES (?, ?, ?, ?, ?, ?, ?)"""
            # Execute the query with the user input as parameters
            cur.execute(sql, (first_name, last_name, title, age, nationality,
                              completed_courses, semesters))
            # Commit the changes to the database
            conn.commit()
            # Close the cursor
            cur.close()

        else:
            tkinter.messagebox.showwarning(
                title="Error", message="First name and last name are required.")
    else:
        tkinter.messagebox.showwarning(
            title="Error", message="You have not accepted the terms")


def open_list_window():
    new_window = Toplevel(window)
    new_window.title("Users information")
    new_window.geometry("280x420")
    form2.open_list_window(new_window)


# Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=[
                              "", "Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa",
                                                             "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
courses_frame = tkinter.LabelFrame(frame)
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Registration Status")
reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not registered")

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text="# Completed Courses")
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Semesters")
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Buttons
buttons_frame = tkinter.LabelFrame(frame, text="Buttons")
buttons_frame.grid(row=3, column=0, padx=20, pady=10)
button_enter = tkinter.Button(buttons_frame, text="Enter data", font=(
    'Arial', 20, 'bold'), command=enter_data)
button_enter.grid(row=0, column=0, columnspan=3, sticky="EW", padx=20, pady=10)
button_list = tkinter.Button(buttons_frame, text="List", font=(
    'Arial', 20, 'bold'), command=open_list_window)
button_list.grid(row=0, column=3, columnspan=3, sticky="EW", padx=20, pady=10)

window.mainloop()

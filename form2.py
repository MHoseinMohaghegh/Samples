import tkinter as tk
import tkinter
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from tkinter import *

def open_list_window(x):
    def get_names():
        # Connect to the database
        # Create a cursor object
        cur1 = conn.cursor()
        # Define the SQL query to select the first and last names
        sql_query = "SELECT first_name, last_name FROM students"
        # Execute the query
        cur1.execute(sql_query)
        # Fetch the results
        results = cur1.fetchall()
        # Close the connection
        conn.commit()
        # Create an empty list to store the concatenated names
        names = []
        # Loop through the results
        for row in results:
            # Concatenate the first and last names with a space
            name = row[0] + row[1]
            # Append the name to the list
            names.append(name)
        # Return the list of names
        return names

    def update_combobox():
        # Get the list of names from the database
        names = get_names()
        # Configure the combobox with the names
        names_combobox.configure(values=names)

    def clear():
        first_name_entry.delete(0, END)
        last_name_entry.delete(0, END)
        title_entry.delete(0, END)
        age_entry.delete(0, END)
        nationality_entry.delete(0, END)
        completed_courses_entry.delete(0, END)
        semesters_entry.delete(0, END)

    def delete_user():
        # Create a cursor object
        cur2 = conn.cursor()
        # Define the SQL query to delete one row
        cur2.execute(
            "DELETE FROM students WHERE first_name || last_name = ?", (names_combobox.get(),))
        # Commit the changes
        conn.commit()
        update_combobox()
        clear()
        names_combobox.set(first_name_entry.get() + last_name_entry.get())

    def write():
        clear()
        x = names_combobox.get()
        cur3 = conn.cursor()
        cur3.execute(
            "SELECT * FROM students WHERE first_name || last_name = ?", (x,))
        # Fetch the data as a tuple
        data = []
        data = cur3.fetchone()
        if data:
            # Assign the data to variables
            first_name = data[0]
            last_name = data[1]
            title = data[2]
            age = data[3]
            nationality = data[4]
            completed_courses = data[5]
            semesters = data[6]
            # Insert the data into the entries
            first_name_entry.insert(0, first_name)
            last_name_entry.insert(0, last_name)
            title_entry.insert(0, title)
            age_entry.insert(0, age)
            nationality_entry.insert(0, nationality)
            completed_courses_entry.insert(0, completed_courses)
            semesters_entry.insert(0, semesters)
        else:
            # Display a message if the data is empty
            print("No data found for this ID")

    def edit():
        x = names_combobox.get()
        cur4 = conn.cursor()
        sql_query = """
        UPDATE students
        SET first_name = ?, last_name = ?, title = ?, age = ?,
        nationality = ?, completed_courses = ?, semesters = ?
        WHERE first_name || last_name = '{}' """.format(x)
        values = (first_name_entry.get(), last_name_entry.get(), title_entry.get(),
                  age_entry.get(), nationality_entry.get(),
                  completed_courses_entry.get(), semesters_entry.get())
        cur4.execute(sql_query, values)
        conn.commit()
        update_combobox()
        names_combobox.set(first_name_entry.get() + last_name_entry.get())

    # create a Toplevel(window)
    # new_window = Toplevel(main.window)
    # new_window.title("Users information")
    # new_window.geometry("280x420")
    # create a Frame widget inside the new window
    frame = Frame(x)
    frame.pack(fill=BOTH, expand=1)
    # create 3 LabelFrame widgets and place them on the Frame
    labelframe1 = LabelFrame(frame, text="Choose the name:")
    labelframe1.grid(row=0, column=0, padx=10, pady=10, sticky=NSEW)
    labelframe2 = LabelFrame(frame, text="Information:")
    labelframe2.grid(row=1, column=0, padx=10, pady=10, sticky=NSEW)
    labelframe3 = LabelFrame(frame, text="Buttons:")
    labelframe3.grid(row=2, column=0, padx=10, pady=10, sticky=NSEW)
    # configure the row and column weight of the Frame
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)
    frame.columnconfigure(0, weight=1)
    # creating name label
    name_label = tkinter.Label(labelframe1, text="Names:")
    name_label.grid(row=0, column=0, padx=20, pady=10)
    conn = sqlite3.connect("data_base.db")
    cur5 = conn.cursor()

    # Execute a query to get the values of first_name and last_name columns
    cur5.execute("SELECT first_name || last_name AS name FROM students ")

    # Fetch the data as a list of tuples
    data = cur5.fetchall()
    names = [row[0] for row in data]

    # Close the cursor and the connection
    names_combobox = ttk.Combobox(labelframe1, values=names)
    names_combobox.grid(row=1, column=0)
    # creating enter button
    enter_button = tkinter.Button(labelframe1, text="Enter", command=write, font=(
        'Arial', 14, 'bold'))
    # creating label_frame2 objects
    enter_button.grid(row=1, column=1, rowspan=2)

    first_name_label = tkinter.Label(labelframe2, text="First Name:")
    last_name_label = tkinter.Label(labelframe2, text="Last Name:")
    title_label = tkinter.Label(labelframe2, text="Title:")
    age_label = tkinter.Label(labelframe2, text="Age:")
    nationality_label = tkinter.Label(labelframe2, text="Nationality:")
    completed_courses_label = tkinter.Label(
        labelframe2, text="Completed Courses:")
    semesters_label = tkinter.Label(labelframe2, text="Semesters:")

    first_name_label.grid(row=0, column=0)
    last_name_label.grid(row=1, column=0)
    title_label.grid(row=2, column=0)
    age_label.grid(row=3, column=0)
    nationality_label.grid(row=4, column=0)
    completed_courses_label.grid(row=5, column=0)
    semesters_label.grid(row=6, column=0)

    first_name_entry = tk.Entry(labelframe2, text="First Name:")
    last_name_entry = tk.Entry(labelframe2, text="Last Name:")
    title_entry = tk.Entry(labelframe2, text="Title:")
    age_entry = tk.Entry(labelframe2, text="Age:")
    nationality_entry = tk.Entry(labelframe2, text="Nationality:")
    completed_courses_entry = tk.Entry(
        labelframe2, text="Completed Courses:")
    semesters_entry = tk.Entry(labelframe2, text="Semesters:")

    first_name_entry.grid(row=0, column=1)
    last_name_entry.grid(row=1, column=1)
    title_entry.grid(row=2, column=1)
    age_entry.grid(row=3, column=1)
    nationality_entry.grid(row=4, column=1)
    completed_courses_entry.grid(row=5, column=1)
    semesters_entry.grid(row=6, column=1)

    # creating label_frame3 objects
    edit_button = tkinter.Button(labelframe3, text="Edit", font=(
        'Arial', 14, 'bold'), command=edit)
    remove_button = tkinter.Button(labelframe3, text="Remove", font=(
        'Arial', 14, 'bold'), command=delete_user)
    edit_button.grid(row=0, column=0, padx=20, pady=10)
    remove_button.grid(row=0, column=1, padx=20, pady=10)

    clear()
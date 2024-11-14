import tkinter as tk
from tkinter import ttk
import datetime
import sqlite3


currentDateTime = datetime.datetime.now()
formated_currentDate = currentDateTime.strftime("%Y-%m-%d")
formated_currentTime = currentDateTime.strftime("%H:%M")


def save_result():
    conn = sqlite3.connect("push_ups.db")
    cursor = conn.cursor()

    insert_query = "INSERT INTO daily_result (date, result) VALUES (?, ?)"
    # insert_query = "INSERT INTO daily_result (date, result, average) VALUES (?, ?, ?)"
    update_query = "UPDATE daily_result SET result = ? WHERE date = ?"

    cursor.execute(insert_query, (formated_currentDate, e1.get()))
    conn.commit()
    lbl.config(text=e1.get())


def daily_result():
    conn = sqlite3.connect("push_ups.db")
    cursor = conn.cursor()

    current_day_result_query = "SELECT result FROM daily_result WHERE date = ?;"

    no_reps = cursor.execute(
        current_day_result_query, (formated_currentDate,)
    ).fetchone()
    lbl_result.config(text=no_reps[0])


def show_id():
    conn = sqlite3.connect("push_ups.db")
    cursor = conn.cursor()
    select_id_query = "SELECT id FROM daily_result WHERE date = ?;"

    searched_id = cursor.execute(select_id_query, (formated_currentDate,)).fetchone()
    lbl_searched_id.config(text=searched_id[0])


def delete_record():
    conn = sqlite3.connect("push_ups.db")
    cursor = conn.cursor()
    delete_query = "DELETE FROM daily_result WHERE id = ?"


def select_all_records():
    conn = sqlite3.connect("push_ups.db")
    cursor = conn.cursor()
    select_all_query = "SELECT * FROM daily_result;"

    all_results = cursor.execute(select_all_query).fetchall()
    print_records = ""
    for result in all_results:
        print_records += str(result) + "\n"

    all_records_lbl = tk.Label(root, text=print_records)
    all_records_lbl.grid(row=8, column=0, columnspan=2)


root = tk.Tk()
root.title("Daily push-ups counter")

greeting_lbl = tk.Label(root, text=f"{formated_currentDate} {formated_currentTime}")
greeting_lbl.grid(row=0, column=0)

label = tk.Label(root, text="How many push-ups did you just do?")
label.grid(row=1, column=0)

e1 = tk.Entry(root)
e1.grid(row=1, column=1)

lbl = tk.Label(root, text="How many push-ups did you just do?")
lbl.grid(row=2, column=0)

btn = tk.Button(root, text="Submit", command=save_result)
btn.grid(row=2, column=1)

lbl_result = tk.Label(root, text="")
lbl_result.grid(row=3, column=0)

btn_result = tk.Button(root, text="Daily Result", command=daily_result)
btn_result.grid(row=3, column=1)

label_id = tk.Label(root, text="Which record?")
label_id.grid(row=4, column=0)

id_entry = tk.Entry(root)
id_entry.grid(row=4, column=1)

lbl_searched_id = tk.Label(root, text="")
lbl_searched_id.grid(row=5, column=0)

btn_ID = tk.Button(root, text="Search ID", command=show_id)
btn_ID.grid(row=5, column=1)

delete_entry = tk.Entry(root)
delete_entry.grid(row=6, column=0)

btn_delete = tk.Button(root, text="Delete", command=show_id)
btn_delete.grid(row=6, column=1)

all_records_btn = tk.Button(root, text="All Records", command=select_all_records)
all_records_btn.grid(row=7, column=0, columnspan=2)

root.mainloop()

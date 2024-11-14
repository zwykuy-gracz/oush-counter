# 5 5, 5 5, 5 5, 10, 5 5, 5 5, 5 5, 5 20241023
# 6 6, 6 6, 6 6, 6 6, 6 6, 6 6 20241024
# 7 7, 7

# cursor.execute(
#     "CREATE TABLE daily_result (id INTEGER PRIMARY KEY, date TIMESTAMP, result INTEGER, average INTEGER)"
# )
# select_query = "SELECT COUNT(*) FROM daily_result WHERE date = ?;"

import datetime
import sqlite3


currentDateTime = datetime.datetime.now()
formated_currentDateTime = currentDateTime.strftime("%Y-%m-%d")

conn = sqlite3.connect("push_ups.db")
cursor = conn.cursor()

insert_query = "INSERT INTO daily_result (date, result, average) VALUES (?, ?, ?)"
update_query = "UPDATE daily_result SET result = ? WHERE date = ?"
current_day_result_query = "SELECT result FROM daily_result WHERE date = ?;"
update_or_insert_query = (
    "INSERT OR REPLACE INTO daily_result (date, result, average) VALUES (?, ?, ?);"
)
delete_query = "DELETE FROM daily_result WHERE id = ?"


def current_day_no_reps(current_day_result_query, formated_currentDateTime):
    no_reps = cursor.execute(
        current_day_result_query, (formated_currentDateTime,)
    ).fetchone()
    if no_reps:
        return no_reps[0]
    else:
        return 0


already_done_reps = current_day_no_reps(
    current_day_result_query, formated_currentDateTime
)


def main(update_query, formated_currentDateTime, already_done_reps):
    no_reps = input("How many push ups did you do? ")
    daily_total = already_done_reps + int(no_reps)
    if already_done_reps:
        cursor.execute(update_query, (daily_total, formated_currentDateTime))
        conn.commit()
    else:
        cursor.execute(insert_query, (formated_currentDateTime, daily_total, no_reps))
        conn.commit()
    print(f"Today you did {daily_total} push ups so far")


main(update_query, formated_currentDateTime, already_done_reps)
# if __name__ == "__main__":

# def deleting_records(record_id):
#     record_to_delete = cursor.execute(delete_query, (record_id,))
#     conn.commit()
# deleting_records(5)

# def update_func(update_query, formated_currentDateTime, already_done_reps, no_reps):
#     cursor.execute(update_query, (formated_currentDateTime, daily_total, no_reps))
#     conn.commit()

# insert_or_update = update_func()

# def insert_func():
#     cursor.execute(insert_query, (formated_currentDateTime, daily_total, single_rep))
#     conn.commit()

# def select_func(select_query, formated_currentDateTime):
#     row = cursor.execute(select_query, (formated_currentDateTime,)).fetchall()
#     # cursor.execute(select_query, (formated_currentDateTime,))
#     return row[0][0]


# current_day_exists = select_func(select_query, formated_currentDateTime)

import tkinter as tk
import sqlite3
root = tk.Tk()
root.title("Student Management Record")
connection = sqlite3.connect('test_Student DB') # creating a file
print("Database opened successfully")
TABLE_NAME = "student_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"
connection.execute("create table if not exists " + TABLE_NAME + " ( " + STUDENT_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, "
                   + STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " + STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER) ;")
print("table created successfully")
label = tk.Label(root, text="Enter your name :", pady=(10))
label.pack()
student_name = tk.Entry(root)
student_name.pack()
label = tk.Label(root, text="Enter your college name :", pady=(10))
label.pack()
college_name = tk.Entry(root)
college_name.pack()
label = tk.Label(root, text="Enter your address :", pady=(10))
label.pack()
address = tk.Entry(root)
address.pack()
label = tk.Label(root, text="Enter your phoneno  :", pady=(10))
label.pack()
phone_number = tk.Entry(root)
phone_number.pack()
printing = tk.Label(root, text="Printing the Details : ")
printing.pack()
def takevalueinput():
    name = student_name.get()
    phone = phone_number.get()
    add = address.get()
    college = college_name.get()
    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " + STUDENT_COLLEGE + ", " + STUDENT_ADDRESS +
                        ", " + STUDENT_PHONE + ") VALUES ('"+name+"', '"+college+"', " + "'"+add+"', "+phone+" ); ")
    connection.commit()
def display():
    cursor = connection.execute("select * from " + TABLE_NAME + " ;")

    for row in cursor:
        print("Student id is : ", row[0])
        print("Student_name is : ", row[1])
        print("College_name  is : ", row[2])
        print("Address  is :", row[3])
        print("Phone_number is :", row[4])

save_button = tk.Button(root, text='Save Record',
                        command = lambda : takevalueinput())
save_button.pack()

display_button = tk.Button(root, text='Display Record', command=lambda: display())
display_button.pack()
root.mainloop()





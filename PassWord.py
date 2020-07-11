# PassWord - The Safe Password Generator App!

#  importing the tkinter module for GUI
from tkinter import *

# importing the message box widget from tkinter
from tkinter import messagebox

# importing sqlite3 for database
import sqlite3

# importing random for password generation
import random

# creating fonts
font = ('Fixedsys', 10)
font2 = ('Comic Sans MS', 9)
font3 = ('System', 9)
font4 = ('Two Cen MT', 9)

# creating a database and establishing a connection
conn = sqlite3.connect('password.db')

# creating a cursor to navigate through database
c = conn.cursor()

# creating the table
'''
c.execute("""CREATE TABLE passwords (
    password text
)""")
'''

# defining the root variable
root = Tk()

# Naming the app
root.title('PassWord')

# creating a label frame to organize content
label_frame = LabelFrame(root, padx=10, pady=10, text='Password Generator', font=font)

# printing the label frame onto the screen or window
label_frame.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky=E + W)

# creating a separate label frame to perform delete functions
delete_labelframe = LabelFrame(root, text='Delete Password', padx=10, pady=10, font=font4)

# printing delete labelframe onto the screen
delete_labelframe.grid(row=5, column=0, columnspan=1, padx=10, pady=10, sticky=E + W)

# making the text box where password is going to be displayed
e = Entry(label_frame, fg='black', bg='white')

# printing the text box to the screen
e.grid(row=0, column=0, padx=10, pady=10, columnspan=1)

# (for the delete function) to give information on input for delete function
# (for the delete function) to give information on input for delete function
info = Label(delete_labelframe, text='Password ID', fg='black', font=font2)

# printing the label onto the screen
info.grid(row=6, column=0, pady=10)

# making the entry for user to input which password
e2 = Entry(delete_labelframe, fg='black', bg='white')

# printing the entry onto the screen
e2.grid(row=6, column=1, pady=10)


# making the password generate function
def generate():
    # creating lists
    lowercase_letters = ['a', 'b', 'c', 'd', 'e' 'f' 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't',
                         'u' 'v', 'w', 'x', 'y', 'z']
    # creating lists
    uppercase_letters = ['A', 'B', 'C', 'D', 'E' 'F' 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                         'T', 'U' 'V', 'W', 'X', 'Y', 'Z']
    # creating lists
    symbols_list = ['-', '@', '!' '$', '%' '&' '?', '#', '^']
    # creating lists
    numbers_list = ['1', '2', '3', '4', '5', '6', '7' '8', '9' '0']

    # generating a random value from the lists
    lowercase_letter = random.choice(lowercase_letters)

    # generating a random value from the lists
    lowercase_letter2 = random.choice(lowercase_letters)

    # generating a random value from the lists
    uppercase_letter = random.choice(uppercase_letters)

    # generating a random value from the lists
    uppercase2_letter = random.choice(uppercase_letters)

    # generating a random value from the lists
    symbol = random.choice(symbols_list)

    # generating a random value from the lists
    symbol2 = random.choice(symbols_list)

    # generating a random value from the lists
    number = random.choice(numbers_list)

    # generating a random value from the lists
    number2 = random.choice(numbers_list)

    # creating a password list made of random values from previous lists
    password = [lowercase_letter, uppercase_letter, uppercase2_letter, lowercase_letter2, symbol, symbol2, number,
                number2]

    # shuffling password list
    password1 = random.sample(password, 8)

    # concatenating and making final list
    final_password = password1[0] + password1[1] + password1[2] + password1[3] + password1[4] + password1[5] + \
                     password1[6] + password1[7]

    # deleting previous item from entry
    e.delete(0, END)

    # inserting the final password
    e.insert(0, final_password)


# making a function to save the password into the database
def save_password():
    conn = sqlite3.connect('password.db')
    c = conn.cursor()
    c.execute("INSERT INTO passwords VALUES (?)", (e.get(),))
    e.delete(0, END)
    conn.commit()
    conn.close()


# making a function to show all the saved passwords
def show_password():
    global passcode_label
    conn = sqlite3.connect('password.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM passwords")
    passcodes = c.fetchall()
    print_code = ''
    for passcode in passcodes:
        print_code += str(passcode[0]) + '.' + '  ' + str(passcode[1]) + '\n'
    passcode_label = Text(label_frame, height=15, width=25)
    passcode_label.configure(state='normal')
    passcode_label.insert(1.0, print_code)
    passcode_label.grid(row=5, column=0, padx=10, pady=10)
    passcode_label.configure(state='disabled')
    conn.commit()
    conn.close()


# making a function to hide the saved passwords
def hide_password():
    passcode_label.destroy()


# making a function to delete passwords from database
def delete():
    conn = sqlite3.connect('password.db')
    c = conn.cursor()

    c.execute("DELETE from passwords WHERE oid = (?)", (e2.get(),))
    e2.delete(0, END)

    passcode_label.destroy()

    conn.commit()
    conn.close()


# making a function to delete all the passwords in the database
def delete_all():
    global number_of_passwords
    conn = sqlite3.connect('password.db')
    c = conn.cursor()
    c.execute("SELECT rowid FROM passwords")
    number_of_passwords = c.fetchall()
    num_of_passwords = len(number_of_passwords)
    confirmation = messagebox.askyesno('Delete All Passwords?',
                                       'You have chosen to delete ' + str(
                                           num_of_passwords) + ' passwords. This action cannot be reversed. Do you wish to proceed?')
    if confirmation == 1:
        c.execute("DELETE FROM passwords")

    conn.commit()
    conn.close()


# button for generating password
generate_password = Button(label_frame, text='Generate Strong Password', command=generate, font=font2)

# printing the button onto the screen
generate_password.grid(row=1, padx=10, pady=10, column=0)

# button to save password
save = Button(label_frame, text='Save Password', command=save_password, font=font2)

# printing the button onto the screen
save.grid(row=2, padx=10, pady=10, column=0)

# making a button to show all the passwords
show = Button(label_frame, text='Show Passwords', command=show_password, font=font2)

# printing the button onto the screen
show.grid(row=4, padx=10, pady=10, column=0)

# making a button to hide the shown passwords
hide = Button(label_frame, text='Hide Passwords', command=hide_password, font=font2)

# printing the button onto the screen
hide.grid(row=6, column=0, padx=10, pady=10)

# making a button to delete a password
delete = Button(delete_labelframe, text='Delete Password', command=delete, font=font2)

# printing the button onto the screen
delete.grid(row=8, padx=10, pady=10, column=1)

# making a button to delete all the passwords
delete_all = Button(delete_labelframe, text='Delete All', command=delete_all, fg='dark red', width=20, anchor=CENTER,
                    font=font3)

# printing the button onto the screen
delete_all.grid(row=9, column=1, padx=10, pady=10, ipadx=15)

# committing the changes to the database
conn.commit()

# closing the connection with database
conn.close()

# making the final loop
root.mainloop()

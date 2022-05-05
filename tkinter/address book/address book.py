import tkinter
from tkinter import filedialog
import sqlite3

root = tkinter.Tk()
root.title('zaglavie')
root.iconbitmap('alabala.ico')
root.geometry('400x400')

conn = sqlite3.connect('address_book.db')
c = conn.cursor()

# c.execute('''CREATE TABLE addresses (
#    first_name text,
#    last_name text,
#    address text,
#    city text,
#    state text,
#    zipcode integer
#    )''')

def save():



    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute('''UPDATE addresses SET
    first_name = :first,
    last_name = :last,
    address = :address,
    city = :city,
    state = :state,
    zipcode = :zipcode
    
    WHERE oid = :oid''',
              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'address': address_editor.get(),
                  'city': city_editor.get(),
                  'state': state_editor.get(),
                  'zipcode': zipcode_editor.get(),
                  'oid': record_id
              })


    conn.commit()
    conn.close()

    editor.destroy()



def edit():
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    global record_id
    global editor

    editor = tkinter.Tk()
    editor.title('update record')
    editor.iconbitmap('alabala.ico')
    editor.geometry('400x400')

    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute('SELECT * FROM  addresses WHERE oid=' + record_id)
    records = c.fetchall()


    f_name_editor = tkinter.Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = tkinter.Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = tkinter.Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = tkinter.Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = tkinter.Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = tkinter.Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    f_name_label = tkinter.Label(editor, text='First name')
    f_name_label.grid(row=0, column=0)
    l_name_label = tkinter.Label(editor, text='Last name')
    l_name_label.grid(row=1, column=0)
    address_label = tkinter.Label(editor, text='address')
    address_label.grid(row=2, column=0)
    city_label = tkinter.Label(editor, text='city')
    city_label.grid(row=3, column=0)
    state_label = tkinter.Label(editor, text='state')
    state_label.grid(row=4, column=0)
    zipcode_label = tkinter.Label(editor, text='zipcode')
    zipcode_label.grid(row=5, column=0)

    save_btn = tkinter.Button(editor, text='save record', command=save)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)


def delete():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute('DELETE from addresses WHERE oid=' + delete_box.get())




    conn.commit()
    conn.close()


def submit():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute('INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)',
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    conn.commit()

    conn.close()

    f_name.delete(0, tkinter.END)
    l_name.delete(0, tkinter.END)
    address.delete(0, tkinter.END)
    city.delete(0, tkinter.END)
    state.delete(0, tkinter.END)
    zipcode.delete(0, tkinter.END)

def query():
    conn = sqlite3.connect('address_book.db')
    c = conn.cursor()

    c.execute('SELECT *, oid FROM  addresses')
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + '\n'

    query_label = tkinter.Label(root, text=print_records)
    query_label.grid(row=12, column=0, columnspan=2)


    conn.commit()

    conn.close()





f_name = tkinter.Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = tkinter.Entry(root, width=30)
l_name.grid(row=1, column=1)
address = tkinter.Entry(root, width=30)
address.grid(row=2, column=1)
city = tkinter.Entry(root, width=30)
city.grid(row=3, column=1)
state = tkinter.Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = tkinter.Entry(root, width=30)
zipcode.grid(row=5, column=1)
delete_box = tkinter.Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

f_name_label = tkinter.Label(root, text='First name')
f_name_label.grid(row=0, column=0)
l_name_label = tkinter.Label(root, text='Last name')
l_name_label.grid(row=1, column=0)
address_label = tkinter.Label(root, text='address')
address_label.grid(row=2, column=0)
city_label = tkinter.Label(root, text='city')
city_label.grid(row=3, column=0)
state_label = tkinter.Label(root, text='state')
state_label.grid(row=4, column=0)
zipcode_label = tkinter.Label(root, text='zipcode')
zipcode_label.grid(row=5, column=0)
delete_box_label = tkinter.Label(root, text='Select ID number')
delete_box_label.grid(row=9, column=0, pady=5)

submit_btn = tkinter.Button(root, text='Add record to database', command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = tkinter.Button(root, text='show records', command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

delete_btn = tkinter.Button(root, text='delete record', command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

edit_btn = tkinter.Button(root, text='edit record', command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

conn.commit()

conn.close()

root.mainloop()

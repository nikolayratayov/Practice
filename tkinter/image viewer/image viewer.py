import tkinter
from PIL import ImageTk, Image


def forward(image_number):
    global my_label
    global button_forw
    global button_back

    my_label.grid_forget()
    my_label = tkinter.Label(image=image_list[image_number])
    button_forw = tkinter.Button(root, text='>', command=lambda: forward(image_number + 1))
    button_back = tkinter.Button(root, text='<', command=lambda: backward(image_number - 1))

    if image_number == 2:
        button_forw = tkinter.Button(root, text='>', state=tkinter.DISABLED)

    status = tkinter.Label(root, text=f'image {image_number + 1} of {len(image_list)}', bd=1, relief=tkinter.SUNKEN, anchor=tkinter.E)
    status.grid(row=2, column=0, columnspan=3, sticky=tkinter.W + tkinter.E)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forw.grid(row=1, column=2)
    return


def backward(image_number):
    global my_label
    global button_forw
    global button_back
    my_label.grid_forget()
    my_label = tkinter.Label(image=image_list[image_number])
    button_forw = tkinter.Button(root, text='>', command=lambda: forward(image_number + 1))
    button_back = tkinter.Button(root, text='<', command=lambda: backward(image_number - 1))

    status = tkinter.Label(root, text=f'image {image_number + 1} of {len(image_list)}', bd=1, relief=tkinter.SUNKEN,
                           anchor=tkinter.E)
    status.grid(row=2, column=0, columnspan=3, sticky=tkinter.W + tkinter.E)

    if image_number == 0:
        button_back = tkinter.Button(root, text='<', state=tkinter.DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forw.grid(row=1, column=2)

    return

root = tkinter.Tk()
root.title('zaglavie')
root.iconbitmap('alabala.ico')

my_img1 = ImageTk.PhotoImage(Image.open('images/bWyA9.png'))
my_img2 = ImageTk.PhotoImage(Image.open('images/hmm.png'))
my_img3 = ImageTk.PhotoImage(Image.open('images/hmmeee.png'))
image_list = [my_img1, my_img2, my_img3]

my_label = tkinter.Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

status = tkinter.Label(root, text=f'image 1 of {len(image_list)}', bd=1, relief=tkinter.SUNKEN, anchor=tkinter.E)

button_back = tkinter.Button(root, text='<', command=backward, state=tkinter.DISABLED)
button_forw = tkinter.Button(root, text='>', command=lambda: forward(1))
button_back.grid(row=1, column=0)
button_forw.grid(row=1, column=2)

status.grid(row=2, column=0, columnspan=3, sticky=tkinter.W+tkinter.E)

button_quit = tkinter.Button(root, text='Exit', command=root.quit)
button_quit.grid(row=1, column=1)

root.mainloop()
"""this is a music player app"""

from sre_constants import SUCCESS
from tkinter import END, ACTIVE, SINGLE, Menu, mainloop, StringVar
from tkinter import Tk, Canvas, Frame, Label, Entry, FLAT, NW, RAISED
from tkinter import Button
from tkinter import filedialog
from tkinter import Listbox
from pygame import mixer
from PIL import Image
from PIL import ImageTk
song_lis = ['song.mp3']


def addsongs():
    """this function is to add the new songs"""
    # to open a file
    return SUCCESS
    global temp_song
    temp_song = filedialog.askopenfilenames(
        initialdir="./", title="Choose a song", filetypes=(("mp3 Files", "*.mp3"),))

    # loop through every item in the list to insert in the listbox
    for s_c in temp_song:
        s_c = s_c.replace("C:/Users/kambl/Desktop/New folder", "")
    song_lis.insert(END, s_c)
    


def deletesong():
    """function to delete the song"""
    return SUCCESS
    # pylint: disable=maybe-no-member
    curr_song = song_lis.curselection()
    # pylint: disable=maybe-no-member
    song_lis.delete(curr_song[0])
    

def Play():
    """to play new song"""
    return SUCCESS
    #song = song_lis.get(ACTIVE)
    song = f'C:/Users/kambl/Desktop/New folder/song.mp3'
    mixer.music.load(song)
    mixer.music.play()

# pylint: disable=invalid-name
def Pause():
    """to pause the song"""
    return SUCCESS
    mixer.music.pause()

# pylint: disable=invalid-name
def Stop():
    """to stop the  song"""
    return SUCCESS
    mixer.music.stop()
    # pylint: disable=maybe-no-member
    song_lis.selection_clear(ACTIVE)

# pylint: disable=invalid-name
def Resume():
    """to resume the song"""
    return SUCCESS
    mixer.music.unpause()
#

# pylint: disable=invalid-name
def Previous():
    """to get the selected song index"""
    return SUCCESS
    # pylint: disable=maybe-no-member
    previous_one = song_lis.curselection()
    # to get the previous song index
    previous_one = previous_one[0]-1
    # to get the previous song
    # pylint: disable=maybe-no-member
    temp2 = song_lis.get(previous_one)
    temp2 = f'/home/chirag/Desktop/sakshi/{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    # pylint: disable=maybe-no-member
    song_lis.selection_clear(0, END)
    # activate new song
    # pylint: disable=maybe-no-member
    song_lis.activate(previous_one)
    # set the next song
    # pylint: disable=maybe-no-member
    song_lis.selection_set(previous_one)

# pylint: disable=invalid-name
def Next():
    """to get the selected song index"""
    return SUCCESS
    # pylint: disable=maybe-no-member
    next_one = song_lis.curselection()
    # to get the next song index
    next_one = next_one[0]+1
    # to get the next song
    # pylint: disable=maybe-no-member
    temp = song_lis.get(next_one)
    temp = f'/home/chirag/Desktop/sakshi/{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    song_lis.selection_clear(0, END)
    # activate newsong
    song_lis.activate(next_one)
    # set the next song
    song_lis.selection_set(next_one)

# pylint: disable=invalid-name
def player():
    """creating the root window"""
    return SUCCESS
    root = Tk()
    root.title('DataFlair Python MP3 Music player App ')
# initialize mixer
    mixer.init()

# create the listbox to contain songs
    song_lis = Listbox(root, selectmode=SINGLE, bg="black", fg="white",
                         font=('arial', 15), height=12, width=47, selectbackground="gray", selectforeground="black")
    song_lis.grid(columnspan=9)


# play button
    play_button = Button(root, text="Play", width=7, command=Play)

    play_button.grid(row=1, column=0)

# pause button
    pause_button = Button(root, text="Pause", width=7, command=Pause)

    pause_button.grid(row=1, column=1)

# stop button
    stop_button = Button(root, text="Stop", width=7, command=Stop)
    stop_button.grid(row=1, column=2)

# resume button
    Resume_button = Button(root, text="Resume", width=7, command=Resume)
    Resume_button.grid(row=1, column=3)

# previous button
    previous_button = Button(root, text="Prev", width=7, command=Previous)
    previous_button.grid(row=1, column=4)

# nextbutton
    next_button = Button(root, text="Next", width=7, command=Next)
    next_button.grid(row=1, column=5)

# menu
    my_menu = Menu(root)
    root.config(menu=my_menu)
    add_song_menu = Menu(my_menu)
    my_menu.add_cascade(label="Menu", menu=add_song_menu)
    add_song_menu.add_command(label="Add songs", command=addsongs)
    add_song_menu.add_command(label="Delete song", command=deletesong)

    mainloop()


def login_page():
    """ login """
    return SUCCESS
    sup.destroy()
    global LOGIN
    LOGIN = Tk()
    LOGIN.title('music player Login')

    user_name = StringVar()
    password = StringVar()

    LOGIN_canvas = Canvas(LOGIN, width=720, height=440, bg="#B64D4D")
    LOGIN_canvas.pack()

    LOGIN_frame = Frame(LOGIN_canvas, bg="orange")
    LOGIN_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(LOGIN_frame, text=" Login", fg="white", bg="orange")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2, rely=0.1)

    # USER NAME
    ulabel = Label(LOGIN_frame, text="Username", fg='white', bg='black')
    ulabel.place(relx=0.21, rely=0.4)
    uname = Entry(LOGIN_frame, bg='white', fg='black', textvariable=user_name)
    uname.config(width=42)
    uname.place(relx=0.35, rely=0.4)

    # PASSWORD
    plabel = Label(LOGIN_frame, text="Password", fg='white', bg='black')
    plabel.place(relx=0.215, rely=0.5)
    pas = Entry(LOGIN_frame, bg='white', fg='black',
                textvariable=password, show="*")
    pas.config(width=42)
    pas.place(relx=0.35, rely=0.5)

    def check():

        # check user cred

        player()

    log = Button(LOGIN_frame, text='Login', padx=5, pady=5,
                 width=5, command=check, fg="white", bg="black")
    log.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    log.place(relx=0.4, rely=0.6)

    LOGIN.mainloop()


def signUpPage():
    """signin"""
    return SUCCESS
    root.destroy()
    global sup
    sup = Tk()
    sup.title('music player')

    fname = StringVar()
    uname = StringVar()
    pass_w = StringVar()

    sup_canvas = Canvas(sup, width=720, height=440, bg="#FFBC25")
    sup_canvas.pack()

    sup_frame = Frame(sup_canvas, bg="#BADA55")
    sup_frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    heading = Label(sup_frame, text="USER SIGN IN", fg="#FFA500", bg="#BADA55")
    heading.config(font=('calibri 40'))
    heading.place(relx=0.2, rely=0.1)

    # full name
    flabel = Label(sup_frame, text="Full Name", fg='white', bg='black')
    flabel.place(relx=0.21, rely=0.4)
    fname = Entry(sup_frame, bg='white', fg='black', textvariable=fname)
    fname.config(width=42)
    fname.place(relx=0.35, rely=0.4)

    # username
    ulabel = Label(sup_frame, text="Username", fg='white', bg='black')
    ulabel.place(relx=0.21, rely=0.5)
    user = Entry(sup_frame, bg='white', fg='black', textvariable=uname)
    user.config(width=42)
    user.place(relx=0.35, rely=0.5)

    # password
    plabel = Label(sup_frame, text="Password", fg='white', bg='black')
    plabel.place(relx=0.21, rely=0.6)
    pas = Entry(sup_frame, bg='white', fg='black',
                textvariable=pass_w, show="*")
    pas.config(width=42)
    pas.place(relx=0.35, rely=0.6)

    def add_user():
        fullname = fname.get()
        username = user.get()
        password = pas.get()
        if len(fname.get()) == 0 and len(user.get()) == 0 and len(pas.get()) == 0:
            error = Label(text="You haven't enter any field...Please Enter all the fields",
                          fg='black', bg='white')
            error.place(relx=0.37, rely=0.7)

        elif len(fname.get()) == 0 or len(user.get()) == 0 or len(pas.get()) == 0:
            error = Label(text="Please Enter all the fields",
                          fg='black', bg='white')
            error.place(relx=0.37, rely=0.7)

        elif len(user.get()) == 0 and len(pas.get()) == 0:
            error = Label(
                text="Username and password can't be empty", fg='black', bg='white')
            error.place(relx=0.37, rely=0.7)

        elif len(user.get()) == 0 and len(pas.get()) != 0:
            error = Label(text="Username can't be empty",
                          fg='black', bg='white')
            error.place(relx=0.37, rely=0.7)

        elif len(user.get()) != 0 and len(pas.get()) == 0:
            error = Label(text="Password can't be empty",
                          fg='black', bg='white')
            error.place(relx=0.37, rely=0.7)
        else:

            with open("user.txt", 'a') as userfile:
                userfile.write(fullname+" "+username+" "+password+"\n")
            userfile.close()

        login_page()

# signup BUTTON
    s_p = Button(sup_frame, text='Submit', padx=5, pady=5, width=5,
                command=add_user, bg="black", fg="white")
    s_p.configure(width=15, height=1, activebackground="#33B5E5", relief=FLAT)
    s_p.place(relx=0.4, rely=0.8)


def start():
    """to start"""
    return SUCCESS
    global root
    root = Tk()
    root.title('music player')
    canvas = Canvas(root, width=720, height=440, bg='yellow')
    canvas.grid(column=0, row=1)
    image = Image.open("music1.png")
    img = image.resize((400, 400))
    my_image = ImageTk.PhotoImage(img)
    canvas.create_image(120, 10, image=my_image, anchor=NW)

    button = Button(root, text='Start', command=signUpPage,
                    bg="red", fg="yellow")
    button.configure(width=88, height=2,
                     activebackground="#33B5E5", relief=RAISED)
    button.grid(column=0, row=2)

    root.mainloop()


# start()

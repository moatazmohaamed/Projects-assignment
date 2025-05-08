import tkinter as tkinter
from tkinter import *
import datetime
# ay lon most5dm gebna el drga bta3to bzbt 3shan yb2a shbh el app bgd bdl ma n7ot green w white w keda
window = tkinter.Tk()
window.title("Whatsapp")
window.configure(bg="#ece5dd")
window.geometry("480x900")

# header section
header = tkinter.Frame(window, bg="#128c7e", width=400, height=100)
header.pack(side="top", fill="x")

label = Label(header, text="Whatsapp", font=("Arial", 20), bg="#128c7e", fg="white")
label.pack(side="left")

three_dots_icon = PhotoImage(file="./assets/3dots.png")
three_dots_icon = three_dots_icon.subsample(1, 1)

threedotsbtn = Button(header, image=three_dots_icon, bg="#128c7e", fg="white", bd=0)
threedotsbtn.pack(side="right", padx=20, pady=20)

search_icon = PhotoImage(file="./assets/search-icon.png")
search_icon = search_icon.subsample(1, 1)

searchbtn = Button(header, image=search_icon, bg="#128c7e", fg="white", bd=0)
searchbtn.pack(side="right", padx=20, pady=20)

# widgets section
widget = tkinter.Frame(window, bg="#128c7e", height=40)
widget.pack(side="top", fill="x")

camera = PhotoImage(file="./assets/camera.png")
camera = camera.subsample(2, 2)

camera_icon = Button(widget, image=camera, bg="#128c7e", fg="white", bd=0, font=("Arial", 12))
camera_icon.pack(side="left", padx=20, pady=20)

chats = Button(widget, text="Chats", bg="#128c7e", fg="white", bd=0, font=("Arial", 12))
chats.pack(side="left", padx=20, pady=20)

chatCount = PhotoImage(file="./assets/6.png")
chatCount = chatCount.subsample(2, 2)

chatCountbtn = Label(widget, image=chatCount, bg="#128c7e", fg="white", bd=0, font=("Arial", 12))
chatCountbtn.pack(side="left", pady=20)

status = Button(widget, text="Status", bg="#128c7e", fg="white", bd=0, font=("Arial", 12))
status.pack(side="left", expand=True, padx=20, pady=20)

calls = Button(widget, text="Calls", bg="#128c7e", fg="white", bd=0, font=("Arial", 12))
calls.pack(side="left", expand=True, padx=20, pady=20)

# chat section
chats = [
    {
        'name': "Moataz Mohamed",
        'message': "Hello, how are you?",
        'time': "12:00 PM",
        'profile': "./assets/profile.png",
    },
    {
        'name': "Mostafa Mourad",
        'message': "dr.engy el top ybny",
        'time': "11:00 am",
        'profile': "./assets/prof3.png",
    },
    {
        'name': "Mostafa Ahmed",
        'message': "Ehhh kalam?",
        'time': "8:00 am",
        'profile': "./assets/profile2.png",
    },
    {
        'name': "Malak Ashraf",
        'message': "tb klmo",
        'time': "2:36 am",
        'profile': "./assets/prof4.png",
    },
    {
        'name': "Mostafa Khaled",
        'message': "Khlst el meeting?",
        'time': "10:30 am",
        'profile': "./assets/prof5.png",
    },
]

chats_container = tkinter.Frame(window, bg="#fff")
chats_container.pack(side="top", fill="both", expand=True)

def showChat(name_text):
    for widget in header.winfo_children():
        widget.destroy()

    contact_label = Label(header, text=name_text, font=("Arial", 20), bg="#128c7e", fg="white")
    contact_label.pack(side="left", padx=20, pady=20)

    back_button = Button(header, text="Back", bg="#128c7e", fg="white", bd=0, font=("Arial", 12), command=showContactList)
    back_button.pack(side="right", padx=20, pady=20)

    for widget in chats_container.winfo_children():
        widget.destroy()

    for chat in chats:
        if chat['name'] == name_text:
            received_container = Frame(chats_container, bg="#000")
            received_container.pack(padx=10, pady=5, anchor="w")

            received_message = Label(received_container, text=chat['message'], font=("Arial", 12), bg="#f0f0f0", fg="black")
            received_message.pack(padx=1, pady=1)
            break

    messages_frame = Frame(chats_container, bg="#fff")
    messages_frame.pack(side="top", fill="both", expand=True)

    input_frame = Frame(chats_container, bg="#ece5dd")
    input_frame.pack(side="bottom", fill="x")

    message_entry = Entry(input_frame, font=("Arial", 12), bg="#fff", fg="black", bd=1)
    message_entry.pack(side="left", fill="x", expand=True, padx=10, pady=10)

    def send_message():
        message = message_entry.get()
        now = datetime.datetime.now()
        current_time = f"{now.hour:02}:{now.minute:02}"

        message_container = Frame(messages_frame, bg="#fff")
        message_container.pack(padx=10, pady=5, fill="x")

        bubble = Frame(message_container, bg="#dcf8c6", padx=10, pady=5)
        bubble.pack(side="right", padx=10)

        sent_message = Label(bubble, text=message, font=("Arial", 12), bg="#dcf8c6", fg="black", wraplength=250, justify="left")
        sent_message.pack(side="top")

        time_label = Label(bubble, text=current_time, font=("Arial", 8), bg="#dcf8c6", fg="gray")
        time_label.pack(side="top")

        message_entry.delete(0, END)

    send_button = Button(input_frame, text="Send", font=("Arial", 12), bg="#128c7e", fg="white", bd=0, command=send_message)
    send_button.pack(side="right", padx=10, pady=10)

def showContactList():
    for widget in header.winfo_children():
        widget.destroy()
        
    for widget in chats_container.winfo_children():
        widget.destroy()

    label = Label(header, text="Whatsapp", font=("Arial", 20), bg="#128c7e", fg="white")
    label.pack(side="left", padx=20, pady=20)

    threedotsbtn = Button(header, image=three_dots_icon, bg="#128c7e", fg="white", bd=0)
    threedotsbtn.pack(side="right", padx=20, pady=20)

    searchBtn = Button(header, image=search_icon, bg="#128c7e", fg="white", bd=0)
    searchBtn.pack(side="right", padx=20, pady=20)

    for chat in chats:
        chatSection(
            chats_container,
            chat['name'],
            chat['message'],
            chat['time'],
            chat['profile']
        )

def chatSection(parent, name_text, message_text, time_text, profile_path):
    profilePhoto = PhotoImage(file=profile_path)
    profilePhoto = profilePhoto.subsample(3, 3)
    chat_section = Button(parent, bg="#fff", bd=0, command=lambda: showChat(name_text))
    chat_section.pack(side="top", fill="x", pady=5)

    profile = Label(chat_section, image=profilePhoto, bg="#fff", fg="white", bd=0, font=("Arial", 12))
    profile.image = profilePhoto
    profile.grid(row=0, column=0, padx=20, pady=10)

    text_section = tkinter.Frame(chat_section, bg="#fff")
    text_section.grid(row=0, column=1)

    name = Label(text_section, text=name_text, bg="#fff", fg="black", bd=0, font=("Arial", 12))
    name.pack()

    message = Label(text_section, text=message_text, bg="#fff", fg="gray", bd=0, font=("Arial", 10))
    message.pack()

    chat_section.grid_columnconfigure(2, weight=1)

    time = Label(chat_section, text=time_text, bg="#fff", fg="gray", bd=0, font=("Arial", 10))
    time.grid(row=0, column=3, padx=10)

for chat in chats:
    chatSection(
        chats_container,
        chat['name'],
        chat['message'],
        chat['time'],
        chat['profile']
    )

window.mainloop()

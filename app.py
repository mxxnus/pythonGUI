import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


# Define functions for button


def addApp():

    # removes previous apps in the frame so there are not duplicates
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir='/', title='Select File',
                                          filetypes=(("executables", "*.exe"), ("all files", "*.*")))
    # append exe's to apps list
    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)


# large frame
canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack()

# smaller frame
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.5, relx=0.1, rely=0.1)

# opens the apps in the display as a list
openFile = tk.Button(root, text="Open File", padx=10,
                     pady=5, fg='white', bg='#263D42', command=addApp)

openFile.pack()


# runs the apps in the list
runApps = tk.Button(root, text="Run Apps", padx=10,
                    pady=5, fg='white', bg='#263D42', command=runApps)


runApps.pack()
root.mainloop()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

# whever app is closed, apps are saved and added to the apps array
with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')

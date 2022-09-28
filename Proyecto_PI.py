import PySimpleGUI as sg
import os.path

## Simple program: Window text
#sg.Window(title = "Hello World", layout = [[]], margins = (100, 50)).read()


## layout with a button

#layout = [
#    [sg.Text("Hello")],
#    [sg.Button("EXIT")]
#]
# create the window
#window = sg.Window("Demo", layout)

#while True:
#    event, values = window.read()
    # End the program if user closes the window
    # or presses the EXIT button
#    if event == "EXIT" or event == sg.WIN_CLOSED:
#        break

#window.close()


## Image viewer

file_list_column = [# This represents the users interface
    [
        sg.Text("Image Folder"),
        sg.In(size = (25, 1), enable_events = True, key = "-FOLDER-"), # Identity of folder, acces the content of an element
        sg.FolderBrowse(), # Opens the os folder selector
    ],
    [
        sg.Listbox( # A list of paths to choose from to display an image
            values = [], enable_events = True, size = (40, 20),
            key = "-FILE LIST-" # These key elements are very important, like tags
        )
    ]
]

# Show the name od the chosen file
image_viewer_column = [
    [sg.Text("Choose an image from the list on the left:")],
    [sg.Text(size = (40, 1), key = "-TOUT-")],
    [sg.Image(key = "-IMAGE-")],
]

# layout
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(), # Vertical separator
        sg.Column(image_viewer_column),
        sg.Button("EXIT"),
    ]
]

window = sg.Window("Image Viewer", layout)

# loop
while True:
    event, values = window.read()
    if event == "EXIT" or event == sg.WIN_CLOSED:
        break
    # folder name was filled in, we have to make a list of files
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png", ".gif"))
        ]
        window["-FILE LIST-"].update(fnames)
    elif event == "-FILE LIST-": # A file was chosen
        try:
            filename = os.path.join(
                values["-FOLDER-"], values["-FILE LIST-"][0]
            )
            window["-TOUT-"].update(filename)
            window["-IMAGE-"].update(filename = filename)
        except:
            pass
window.close()



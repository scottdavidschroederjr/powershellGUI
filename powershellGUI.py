import tkinter
import subprocess

# Sets up tkinter to be used to create the GUI
root = tkinter.Tk()

# Defines PowerShell command execution
def run(cmd):
    completed = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)
    print(completed.stdout)  # Print the output from the command
    print(completed.stderr)   # Print any error messages
    return completed

# Software selection button
softwareOptions = ["Snagit", "Sketch"]
selectedSoftware = tkinter.StringVar(value=softwareOptions[0])  # Set default value

dropdown_software = tkinter.OptionMenu(root, selectedSoftware, *softwareOptions)
dropdown_software.pack(padx=20, pady=20)

# Platform selection button
platformOptions = ["PC", "MAC"]
selectedPlatform = tkinter.StringVar(value=platformOptions[0])  # Set default value

dropdown_platform = tkinter.OptionMenu(root, selectedPlatform, *platformOptions)
dropdown_platform.pack(padx=20, pady=20)

# Create an Entry widget for user input
userEntry = tkinter.Entry(root)
userEntry.pack(pady=10)

def adRequestBuilder():
    # Retrieve current values from the selected options and entry
    selected_platform = selectedPlatform.get()
    selected_software = selectedSoftware.get()
    user_input = userEntry.get()

    software = ""

    # Construct the appropriate software string based on selections
    if selected_platform == "PC":
        if selected_software == "Snagit":
            software = "GSG-APP-W-Snagit "
    else:
        if selected_software == "Snagit":
            software = "GSG-APP-M-Snagit "
        elif selected_software == "Sketch":
            software = "GSG-APP-M-Sketch "

    # Build the AD request command
    adRequest = f"ADD-ADGroupMember -Identity {software} -Members {user_input}"

    print(adRequest)

    # Execute the command
    run(adRequest)

# Creating a button to add user to AD
button = tkinter.Button(root, text="Add user to software group", command=adRequestBuilder)
button.pack(padx=20, pady=20)

root.mainloop()
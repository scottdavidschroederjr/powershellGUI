Use Tkinter and PyInstaller to create an executable GUI that runs PowerShell commands to speed up the process of adding users to AD software groups.

**How to Use**
![Image of the GUI]([url_of_image](https://i.imgur.com/S0OTwdE.jpeg))
Using the application is quite straightforward. Once opening the app, you choose the piece of software and platform then type in the username of the person who you want added to the software group in AD and the powershell command runs with those paramiters. 

There are two ways to open the GUI. First is by running the powershellGUI.py file which will open the window up. Second is by using the EXE which is located [INSERT PATH HERE].

**Scope**
The scope of this project is very minimal for a twofold reason. Firstly, the access we're given to AD is quite minimal so there's not much further that can be done with an application like this to help automate. Secondly, the project was more meant to get a basic understanding of the tools used within namely Powershell, Tkinter to make GUIs and PyInstaller to convert py files into exes. So there's obviously a lot that could be cleaned up here (namely more robust error handling) but I have been an enormous victim of scope creep in the past so it's nice to not get stuck in the mud yet again.

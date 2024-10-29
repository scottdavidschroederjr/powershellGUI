Use Tkinter and PyInstaller to create an executable GUI that runs PowerShell commands to speed up the process of adding users to AD software groups.

**How to Use**
<img src="https://i.imgur.com/S0OTwdE.jpeg" align="center"/>

Using the application is quite straightforward. Once opening the app, you choose the piece of software and platform then type in the username of the person who you want added to the software group in AD and the powershell command runs with those paramiters. 

To open the GUI run the powershellGUI.py file which will open the window up.

**Scope**
The scope of this project is very minimal for a twofold reason. Firstly, the access we're given to AD is quite minimal so there's not much further that can be done with an application like this to help automate. Secondly, the project was more meant to get a basic understanding of the tools used within namely Powershell, Tkinter to make GUIs and PyInstaller to convert py files into EXEs.

So there's obviously a lot that could be cleaned up here (namely more robust error handling) but I have been an enormous victim of scope creep in the past so it's nice to not get stuck in the mud yet again.

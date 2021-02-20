# OpenCore Updater

Python script which can update kexts, EFI files and OpenCore. there is still alot i have to do, so i don't recommend using this script as of right now.

***

# What can the updater do, and what do i want to include:

- [x] Can update most Kexts
- [x] Can update OpenCore, and some efi's (warning, you need to update your config.plist)
- [ ] Can merge old config.plist with newest version, this is currently in the works
- [x] Can automatically grab the newest version of everything so you don't have to redownload the script, yes it can now! worked on that the whole day :))
- [ ] Lets the user choose what they want to upgrade, im currently busy with making this.
- [ ] Has a compiler (so you don't have to run it from the command line)
- [ ] Is cross platform; i am also working on this, windows and macos will be supported and tested by myself.

***

# We are going over the following topics:

- [Download/Installation](#installation)
- [Usage](#Usage)
- [What do i want to inprove](#improvements)
    

***

## Installation

### With Git Clone

Run the following one line at a time in Terminal:

    git clone https://github.com/Tiemon-hoi/OpenCore-Updater.git
    cd OpenCore-Updater
    chmod +x script.py
    
Run this in the directory: python3 script.py

### Releases:

Get the latest release from [here](https://github.com/Tiemon-hoi/OpenCore-Updater/releases). then run with python3 script.py (in the directory)

***

## Usage
- At the moment this script is only for testing purposes
- only use it when you know what you are doing
- if you have anything that you want me to include, feel free to contact me
- if there are any bugs etc, contact me (Tijmen#9962 on Discord.)

## Improvements

Currently i have alot of things i still want to include, im currently working on *all* of them. A couple of these are:
- merging the old config.plist with the newer config.plist (this will be excluded for now, since i want the fundamentals first)
- Automatically grab newest versions, so you don't have to redownload the script
- Cross Platform (Windows and MacOS)
- Automatic EFI Mounting
- Letting people choose what they want to update (eg: only kexts, or only opencore, or even only certain kexts)
- A compiler, like a .bat or a .command, or even a .app and .exe
- Both Python 2 and 3 (didnt test both versions)



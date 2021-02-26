# OpenCore Updater

Python script which can update kexts, EFI files and OpenCore. there is still alot i have to do, so i don't recommend using this script as of right now.

***

# What can the updater do, and what do i want to include:

- [x] Can update most Kexts
- [x] Can update OpenCore, and some efi's (warning, you need to update your config.plist)
- [x] Can automatically grab the newest version of everything so you don't have to redownload the script, yes it can now! worked on that the whole day :))
- [x] Lets the user choose what they want to upgrade, it has now!
- [ ] Has a compiler (so you don't have to run it from the command line).
- [ ] Is cross-platform, this will come around 28/29-2-2021!

***

# We are going over the following topics:

- [Download/Installation](#Installation)
- [Supported Files](#Supported-Files)
- [Usage](#Usage)
    

***

## Installation

### Prerequirements

- Python 3, I tested both MacOS standard version, and the [Official](https://www.python.org/downloads/release/) release.

### With Git Clone

Run the following one line at a time in Terminal:

    git clone https://github.com/Tiemon-hoi/OpenCore-Updater.git
    cd OpenCore-Updater
    chmod +x script.py
    
Run this in the directory (from terminal): python3 script.py

### Releases:

Get the latest release from [here](https://github.com/Tiemon-hoi/OpenCore-Updater/releases). then run with python3 script.py, like this:

    cd Downloads/OpenCore-Updater
    chmod +x script.py
    python3 script.py

***

## Supported-Files

### Kexts
At the moment the script supports all kexts referred in [kexts.md](https://github.com/acidanthera/OpenCorePkg/blob/master/Docs/Kexts.md)
- AMDRyzenCPUPowermanagement is also supported
- SMCAMDProcessor is also supported, but doesn't get updates (AFAIK) 
### Drivers
At the moment the script can update the files mentioned in the [guide](https://dortania.github.io/OpenCore-Install-Guide/ktext.html#must-haves):
- OpenCore.efi
- BOOTx64.efi
- BOOTIA32.efi
- OpenRuntime.efi
- OpenCanopy.efi
- OpenUsbKbDxe.efi
- HfsPlusLegacy.efi
- HfsPlus32.efi
- OpenPartitionDxe.efi
### Full list
For a Full list of supported files, refer [here](https://github.com/Tiemon-hoi/OpenCore-Updater/blob/main/fulllist.md)

***

## Usage
- only use it when you know what you are doing
- if you have anything that you want me to include, feel free to contact me
- if there are any bugs etc, contact me (Tijmen#9962 on Discord.)




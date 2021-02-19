print("Hello! Welcome to my OC Updater script! this script is still in beta and if there is a bug dm me on Discord, or make an issue on GitHub.")
print("To use this script you need to do the following prerequiresites:")
print("You need to have your EFI mounted, you can do this with CorpNewt's script as of this moment i haven't implemented this")
print("Make sure you don't have two EFI's mounted at the same time") 
print("The script will now check if you have an EFI mounted...")
import time
time.sleep(10) 
import os
if os.path.exists('/Volumes/EFI'):
    print ("You mounted your EFI! the script will continue.")
else: 
    print ("You didn't mount your EFI, the script will go to sleep....")
    exit()
import os, sys, stat
os.chmod("/Volumes/EFI/EFI/OC", stat.S_IRWXO)
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VirtualSMC.kext"):
    import urllib.request
    url = 'https://github.com/acidanthera/VirtualSMC/releases/download/1.2.0/VirtualSMC-1.2.0-RELEASE.zip'
    urllib.request.urlretrieve(url, 'VirtualSMC-1.2.0-RELEASE.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VirtualSMC-1.2.0-RELEASE.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VirtualSMC.kext")
    shutil.copytree("Kexts/VirtualSMC.kext", "/Volumes/EFI/EFI/OC/Kexts/VirtualSMC.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCBatteryManager.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCBatteryManager.kext")
    shutil.copytree("Kexts/SMCBatteryManager.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCBatteryManager.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCDellSensors.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCDellSensors.kext")
    shutil.copytree("Kexts/SMCDellSensors.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCDellSensors.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCLightSensor.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCLightSensor.kext")
    shutil.copytree("Kexts/SMCLightsensor.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCLightSensor.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCProcessor.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCProcessor.kext")
    shutil.copytree("Kexts/SMCProcessor.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCProcessor.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCSuperIO.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCSuperIO.kext")
    shutil.copytree("Kexts/SMCSuperIO.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCSuperIO.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/Lilu.kext"):
    import urllib.request
    url = 'https://github.com/acidanthera/Lilu/releases/download/1.5.1/Lilu-1.5.1-RELEASE.zip'
    urllib.request.urlretrieve(url, 'Lilu.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('Lilu.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/Lilu.kext")
    shutil.copytree("Lilu.kext", "/Volumes/EFI/EFI/OC/Kexts/Lilu.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/Whatevergreen.kext"):
    import urllib.request
    url = 'https://github.com/acidanthera/WhateverGreen/releases/download/1.4.7/WhateverGreen-1.4.7-RELEASE.zip'
    urllib.request.urlretrieve(url, 'Whatevergreen.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('Whatevergreen.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/Whatevergreen.kext")
    shutil.copytree("Whatevergreen.kext", "/Volumes/EFI/EFI/OC/Kexts/Whatevergreen.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AppleALC.kext"):
    import urllib.request
    url = 'https://github.com/acidanthera/AppleALC/releases/download/1.5.7/AppleALC-1.5.7-RELEASE.zip'
    urllib.request.urlretrieve(url, 'AppleALC.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AppleALC.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AppleALC.kext")
    shutil.copytree("AppleALC.kext", "/Volumes/EFI/EFI/OC/Kexts/AppleALC.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AppleALC.kext"):
    import urllib.request
    url = 'https://github.com/acidanthera/AppleALC/releases/download/1.5.7/AppleALC-1.5.7-RELEASE.zip'
    urllib.request.urlretrieve(url, 'AppleALC.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AppleALC.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AppleALC.kext")
    shutil.copytree("AppleALC.kext", "/Volumes/EFI/EFI/OC/Kexts/AppleALC.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/IntelMausi.kext"):
    import urllib.request
    url = 'https://github.com/acidanthera/IntelMausi/releases/download/1.0.5/IntelMausi-1.0.5-RELEASE.zip'
    urllib.request.urlretrieve(url, 'IntelMausi.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('IntelMausi.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/IntelMausi.kext")
    shutil.copytree("IntelMausi.kext", "/Volumes/EFI/EFI/OC/Kexts/IntelMausi.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SmallTreeIntel82576.kext"):
    import urllib.request
    url = 'https://github.com/khronokernel/SmallTree-I211-AT-patch/releases/download/1.3.0/SmallTreeIntel82576.kext.zip'
    urllib.request.urlretrieve(url, 'SmallTreeIntel82576.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('SmallTreeIntel82576.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SmallTreeIntel82576.kext")
    shutil.copytree("SmallTreeIntel82576.kext", "/Volumes/EFI/EFI/OC/Kexts/SmallTreeIntel82576.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AtherosE2200Ethernet.kext"):
    import urllib.request
    url = 'https://github.com/Mieze/AtherosE2200Ethernet/releases/download/2.2.2/AtherosE2200Ethernet-V2.2.2.zip'
    urllib.request.urlretrieve(url, 'AtherosE2200Ethernet.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AtherosE2200Ethernet.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AtherosE2200Ethernet.kext")
    shutil.copytree("Release/AtherosE2200Ethernet.kext", "/Volumes/EFI/EFI/OC/Kexts/AtherosE2200Ethernet.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8111.kext"):
    import urllib.request
    url = 'https://github.com/Mieze/RTL8111_driver_for_OS_X/releases/download/V2.4.0/RealtekRTL8111-V2.4.0.zip'
    urllib.request.urlretrieve(url, 'RealtekRTL8111.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('RealtekRTL8111.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8111.kext")
    shutil.copytree("Release/RealtekRTL8111.kext", "/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8111.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/LucyRTL8125Ethernet.kext"):
    import urllib.request
    url = 'https://www.insanelymac.com/forum/files/file/1004-lucyrtl8125ethernet/?do=download&csrfKey=9da7156f1e6ce2d23fee67731e9fc70b'
    urllib.request.urlretrieve(url, 'LucyRTL8125Ethernet.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('LucyRTL8125Ethernet.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/LucyRTL8125Ethernet.kext")
    shutil.copytree("Release/LucyRTL8125Ethernet.kext", "/Volumes/EFI/EFI/OC/Kexts/LucyRTL8125Ethernet.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AppleIntelE1000e.kext"):
    import urllib.request
    url = 'https://github.com/chris1111/AppleIntelE1000e/files/5112385/Release.V-3.3.7.10.6.to.Big.Sur.11.zip'
    urllib.request.urlretrieve(url, 'AppleIntelE1000e.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AppleIntelE1000e.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AppleIntelE1000e.kext")
    shutil.copytree("AppleIntelE1000e.kext", "/Volumes/EFI/EFI/OC/Kexts/AppleIntelE1000e.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8100.kext"):
    import urllib.request
    url = 'https://www.insanelymac.com/forum/files/file/259-realtekrtl8100-binary/?do=download&csrfKey=9da7156f1e6ce2d23fee67731e9fc70b'
    urllib.request.urlretrieve(url, 'RealtekRTL8100.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('RealtekRTL8100.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8100.kext")
    shutil.copytree("Release/RealtekRTL8100.kext", "/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8100.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BCM5722D.kext"):
    import urllib.request
    url = 'https://github.com/chris1111/BCM5722D/files/1942667/BCM5722D.kext.zip'
    urllib.request.urlretrieve(url, 'BCM5722D.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('BCM5722D.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BCM5722D.kext")
    shutil.copytree("BCM5722D.kext", "/Volumes/EFI/EFI/OC/Kexts/BCM5722D.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/USBInjectAll.kext"):
    import urllib.request
    url = 'https://bitbucket.org/RehabMan/os-x-usb-inject-all/downloads/RehabMan-USBInjectAll-2018-1108.zip'
    urllib.request.urlretrieve(url, 'USBInjectAll.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('USBInjectAll.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/USBInjectAll.kext")
    shutil.copytree("Release/USBInjectAll.kext", "/Volumes/EFI/EFI/OC/Kexts/USBInjectAll.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/XHCI-unsupported.kext"):
    import urllib.request
    url = 'https://github.com/RehabMan/OS-X-USB-Inject-All/archive/master.zip'
    urllib.request.urlretrieve(url, 'XHCI-unsupported.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('XHCI-unsupported.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/XHCI-unsupported.kext")
    shutil.copytree("XHCI-unsupported.kext", "/Volumes/EFI/EFI/OC/Kexts/XHCI-unsupported.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/itlwm.kext"):
    import urllib.request
    url = 'https://github.com/OpenIntelWireless/itlwm/releases/download/v1.2.0/itlwm_v1.2.0_stable.kext.zip'
    urllib.request.urlretrieve(url, 'itlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('itlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/itlwm.kext")
    shutil.copytree("itlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/itlwm.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothFirmware.kext"):
    import urllib.request
    url = 'https://github.com/OpenIntelWireless/IntelBluetoothFirmware/releases/download/1.1.2/IntelBluetooth.zip'
    urllib.request.urlretrieve(url, 'IntelBluetoothFirmware.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('IntelBluetoothFirmware.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothFirmware.kext")
    shutil.copytree("IntelBluetoothFirmware.kext", "/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothFirmware.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothInjector.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothInjector.kext")
    shutil.copytree("IntelBluetoothInjector.kext", "/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothInjector.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AirportBrcmFixup.kext"):
    import urllib.request
    url = 'https://github.com/acidanthera/AirportBrcmFixup/releases/download/2.1.2/AirportBrcmFixup-2.1.2-RELEASE.zip'
    urllib.request.urlretrieve(url, 'AirportBrcmFixup.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportBrcmFixup.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportBrcmFixup.kext")
    shutil.copytree("AirportBrcmFixup.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportBrcmFixup.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjector.kext"):
    import urllib.request
    url = 'https://github.com/acidanthera/BrcmPatchRAM/releases/download/2.5.6/BrcmPatchRAM-2.5.6-RELEASE.zip'
    urllib.request.urlretrieve(url, 'BrcmBluetoothInjector.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('BrcmBluetoothInjector.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjector.kext")
    shutil.copytree("BrcmBluetoothInjector.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjector.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjector.kext"):
    import urllib.request
    url = 'https://github.com/acidanthera/BrcmPatchRAM/releases/download/2.5.6/BrcmPatchRAM-2.5.6-RELEASE.zip'
    urllib.request.urlretrieve(url, 'BrcmBluetoothInjectorLegacy.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('BrcmBluetoothInjectorLegacy.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjectorLegacy.kext")
    shutil.copytree("BrcmBluetoothInjectorLegacy.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjectorLegacy.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareData.kext"):
    import urllib.request
    url = 'https://github.com/acidanthera/BrcmPatchRAM/releases/download/2.5.6/BrcmPatchRAM-2.5.6-RELEASE.zip'
    urllib.request.urlretrieve(url, 'BrcmFirmwareData.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('BrcmFirmwareData.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareData.kext")
    shutil.copytree("BrcmFirmwareData.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareData.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareRepo.kext"):
    import urllib.request
    url = 'https://github.com/acidanthera/BrcmPatchRAM/releases/download/2.5.6/BrcmPatchRAM-2.5.6-RELEASE.zip'
    urllib.request.urlretrieve(url, 'BrcmFirmwareRepo.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('BrcmFirmwareRepo.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareRepo.kext")
    shutil.copytree("BrcmFirmwareRepo.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareRepo.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM.kext"):
    import urllib.request
    url = 'https://github.com/acidanthera/BrcmPatchRAM/releases/download/2.5.6/BrcmPatchRAM-2.5.6-RELEASE.zip'
    urllib.request.urlretrieve(url, 'BrcmNonPatchRAM.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('BrcmNonPatchRAM.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM.kext")
    shutil.copytree("BrcmNonPatchRAM.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM2.kext"):
    import urllib.request
    url = 'https://github.com/acidanthera/BrcmPatchRAM/releases/download/2.5.6/BrcmPatchRAM-2.5.6-RELEASE.zip'
    urllib.request.urlretrieve(url, 'BrcmNonPatchRAM2.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('BrcmNonPatchRAM2.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM2.kext")
    shutil.copytree("BrcmNonPatchRAM2.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM2.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM2.kext"):
    import urllib.request
    url = 'https://github.com/acidanthera/BrcmPatchRAM/releases/download/2.5.6/BrcmPatchRAM-2.5.6-RELEASE.zip'
    urllib.request.urlretrieve(url, 'BrcmPatchRAM2.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('BrcmPatchRAM2.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM2.kext")
    shutil.copytree("BrcmPatchRAM2.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM2.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM3.kext"):
    import urllib.request
    url = 'https://github.com/acidanthera/BrcmPatchRAM/releases/download/2.5.6/BrcmPatchRAM-2.5.6-RELEASE.zip'
    urllib.request.urlretrieve(url, 'BrcmPatchRAM3.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('BrcmPatchRAM3.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM3.kext")
    shutil.copytree("BrcmPatchRAM3.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM3.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/XLNCUSBFix.kext"):
    import urllib.request
    url = 'https://cdn.discordapp.com/attachments/566705665616117760/566728101292408877/XLNCUSBFix.kext.zip'
    urllib.request.urlretrieve(url, 'XLNCUSBFix.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('XLNCUSBFix.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/XLNCUSBFix.kext")
    shutil.copytree("XLNCUSBFix.kext", "/Volumes/EFI/EFI/OC/Kexts/XLNCUSBFix.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooHDA.kext"):
    import urllib.request
    url = 'https://sourceforge.net/projects/voodoohda/files/latest/download'
    urllib.request.urlretrieve(url, 'VoodooHDA.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooHDA.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooHDA.kext")
    shutil.copytree("VoodooHDA.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooHDA.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AppleMCEReporterDisabler.kext"):
    import urllib.request
    url = 'https://github.com/acidanthera/bugtracker/files/3703498/AppleMCEReporterDisabler.kext.zip'
    urllib.request.urlretrieve(url, 'AppleMCEReporterDisabler.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AppleMCEReporterDisabler.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AppleMCEReporterDisabler.kext")
    shutil.copytree("AppleMCEReporterDisabler.kext", "/Volumes/EFI/EFI/OC/Kexts/AppleMCEReporterDisabler.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/CpuTscSync.kext"):
    import urllib.request
    url = 'https://github.com/acidanthera/CpuTscSync/releases/download/1.0.3/CpuTscSync-1.0.3-RELEASE.zip'
    urllib.request.urlretrieve(url, 'CpuTscSync.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('CpuTscSync.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/CpuTscSync.kext")
    shutil.copytree("CpuTscSync.kext", "/Volumes/EFI/EFI/OC/Kexts/CpuTscSync.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/NVMeFix.kext"):
    import urllib.request
    url = 'https://github.com/acidanthera/NVMeFix/releases/download/1.0.5/NVMeFix-1.0.5-RELEASE.zip'
    urllib.request.urlretrieve(url, 'NVMeFix.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('NVMeFix.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/NVMeFix.kext")
    shutil.copytree("NVMeFix.kext", "/Volumes/EFI/EFI/OC/Kexts/NVMeFix.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SATA-unsupported.kext"):
    import urllib.request
    url = 'https://github.com/khronokernel/Legacy-Kexts/blob/master/Injectors/Zip/SATA-unsupported.kext.zip?raw=true'
    urllib.request.urlretrieve(url, 'SATA-unsupported.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('SATA-unsupported.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SATA-unsupported.kext")
    shutil.copytree("SATA-unsupported.kext", "/Volumes/EFI/EFI/OC/Kexts/SATA-unsupported.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AHCIPortInjector.kext"):
    import urllib.request
    url = 'https://github.com/khronokernel/Legacy-Kexts/blob/master/Injectors/Zip/AHCIPortInjector.kext.zip?raw=true'
    urllib.request.urlretrieve(url, 'AHCIPortInjector.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AHCIPortInjector.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AHCIPortInjector.kext")
    shutil.copytree("AHCIPortInjector.kext", "/Volumes/EFI/EFI/OC/Kexts/AHCIPortInjector.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/ATAPortInjector.kext"):
    import urllib.request
    url = 'https://github.com/khronokernel/Legacy-Kexts/blob/master/Injectors/Zip/ATAPortInjector.kext.zip?raw=true'
    urllib.request.urlretrieve(url, 'ATAPortInjector.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('ATAPortInjector.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/ATAPortInjector.kext")
    shutil.copytree("ATAPortInjector.kext", "/Volumes/EFI/EFI/OC/Kexts/ATAPortInjector.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext"):
    import urllib.request
    url = 'https://github.com/acidanthera/VoodooPS2/releases/download/2.2.1/VoodooPS2Controller-2.2.1-RELEASE.zip'
    urllib.request.urlretrieve(url, 'VoodooPS2Controller.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooPS2Controller.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext")
    shutil.copytree("VoodooPS2Controller.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooRMI.kext"):
    import urllib.request
    url = 'https://github.com/VoodooSMBus/VoodooRMI/releases/download/1.3.1/VoodooRMI-1.3.1-Release.zip'
    urllib.request.urlretrieve(url, 'VoodooRMI.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooRMI.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooRMI.kext")
    shutil.copytree("VoodooRMI.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooRMI.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooRMI.kext"):
    import urllib.request
    url = 'https://github.com/VoodooSMBus/VoodooSMBus/releases/download/v2.2/VoodooSMBus-v2.2.zip'
    urllib.request.urlretrieve(url, 'VoodooSMBus.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooSMBus.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooSMBus.kext")
    shutil.copytree("kext/VoodooSMBus.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooSMBus.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2C.kext"):
    import urllib.request
    url = 'https://github.com/VoodooI2C/VoodooI2C/releases/download/2.6.4/VoodooI2C-2.6.4.zip'
    urllib.request.urlretrieve(url, 'VoodooI2C.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooI2C.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2C.kext")
    shutil.copytree("VoodooI2C.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2C.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CAtmelMXT.kext"):
    import urllib.request
    url = 'https://github.com/VoodooI2C/VoodooI2C/releases/download/2.6.4/VoodooI2C-2.6.4.zip'
    urllib.request.urlretrieve(url, 'VoodooI2CAtmelMXT.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooI2CAtmelMXT.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CAtmelMXT.kext")
    shutil.copytree("VoodooI2CAtmelMXT.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2CAtmelMXT.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CELAN.kext"):
    import urllib.request
    url = 'https://github.com/VoodooI2C/VoodooI2C/releases/download/2.6.4/VoodooI2C-2.6.4.zip'
    urllib.request.urlretrieve(url, 'VoodooI2CELAN.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooI2CELAN.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CELAN.kext")
    shutil.copytree("VoodooI2CELAN.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2CELAN.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CFTE.kext"):
    import urllib.request
    url = 'https://github.com/VoodooI2C/VoodooI2C/releases/download/2.6.4/VoodooI2C-2.6.4.zip'
    urllib.request.urlretrieve(url, 'VoodooI2CFTE.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooI2CFTE.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CFTE.kext")
    shutil.copytree("VoodooI2CFTE.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2CFTE.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CHID.kext"):
    import urllib.request
    url = 'https://github.com/VoodooI2C/VoodooI2C/releases/download/2.6.4/VoodooI2C-2.6.4.zip'
    urllib.request.urlretrieve(url, 'VoodooI2CHID.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooI2CHID.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CHID.kext")
    shutil.copytree("VoodooI2CHID.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2CHID.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CSynaptics.kext"):
    import urllib.request
    url = 'https://github.com/VoodooI2C/VoodooI2C/releases/download/2.6.4/VoodooI2C-2.6.4.zip'
    urllib.request.urlretrieve(url, 'VoodooI2CSynaptics.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooI2CSynaptics.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CSynaptics.kext")
    shutil.copytree("VoodooI2CSynaptics.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2CSynaptics.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AtherosL1cEthernet.kext"):
    import urllib.request
    url = 'https://www.insanelymac.com/applications/core/interface/file/attachment.php?id=115905'
    urllib.request.urlretrieve(url, 'AtherosL1cEthernet.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AtherosL1cEthernet.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AtherosL1cEthernet.kext")
    shutil.copytree("AtherosL1cEthernet.kext", "/Volumes/EFI/EFI/OC/Kexts/AtherosL1cEthernet.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AirPortAtheros40.kext"):
    import urllib.request
    url = 'https://i.applelife.ru/2018/12/442854_AirPortAtheros40.kext.zip'
    urllib.request.urlretrieve(url, 'AirPortAtheros40.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirPortAtheros40.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirPortAtheros40.kext")
    shutil.copytree("AirPortAtheros40.kext", "/Volumes/EFI/EFI/OC/Kexts/AirPortAtheros40.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/ATH9KFixup.kext"):
    import urllib.request
    url = 'https://github.com/chunnann/ATH9KFixup/archive/master.zip'
    urllib.request.urlretrieve(url, 'ATH9KFixup.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('ATH9KFixup.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/ATH9KFixup.kext")
    shutil.copytree("ATH9KFixup.kext", "/Volumes/EFI/EFI/OC/Kexts/ATH9KFixup.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext"):
    import urllib.request
    url = 'https://github.com/acidanthera/VoodooPS2/releases/download/2.2.1/VoodooPS2Controller-2.2.1-RELEASE.zip'
    urllib.request.urlretrieve(url, 'VoodooPS2Controller.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooPS2Controller.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext")
    shutil.copytree("VoodooPS2Controller.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AMDRyzenCPUPowerManagement.kext"):
    import urllib.request
    url = 'https://github.com/trulyspinach/SMCAMDProcessor/releases/download/0.6.6/AMDRyzenCPUPowerManagement.kext.zip'
    urllib.request.urlretrieve(url, 'AMDRyzenCPUPowerManagement.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AMDRyzenCPUPowerManagement.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AMDRyzenCPUPowerManagement.kext")
    shutil.copytree("AMDRyzenCPUPowerManagement.kext", "/Volumes/EFI/EFI/OC/Kexts/AMDRyzenCPUPowerManagement.kext")

import time, os
print("The script has been completed, if there are any bugs feel free to contact me.")
print("The script will now SELF DESTRUCT BYE BYE")
file_path = '~/Downloads/OpenCore-updater/'
os.remove(file_path)

print("BYE BYE")

time.sleep(1)
exit()




































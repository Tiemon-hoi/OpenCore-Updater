#!/usr/bin/python3
print("Hello! Welcome to my OC Updater script!If there is a bug dm me on Discord (Tijmen#9962), or make an issue on GitHub.")
print("The script will now check for newer updates...")
import urllib.request
import time, os, urllib, sys, stat, json, zipfile, shutil, platform, subprocess, re
import urllib.request
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
pathdownload = "downloadtemp"
if os.path.exists(pathdownload):
    shutil.rmtree(pathdownload)
    os.mkdir(pathdownload)
    os.chdir("downloadtemp")
else:
    os.mkdir(pathdownload)
    os.chdir("downloadtemp")
version=0.8
version = str(version)
time.sleep(3)
page = urllib.request.urlopen('https://raw.githubusercontent.com/Tiemon-hoi/OpenCore-Updater/main/script.py').read().decode('utf-8')
xyzpersion = re.findall(r'version=\s*([\d.]+)', page)
xyzpersion = str(xyzpersion[0])
path = os.path.realpath(__file__)
if version < xyzpersion:
    print("newer version " + xyzpersion + " available... updating ...")
    time.sleep(2)
    with urllib.request.urlopen("https://github.com/Tiemon-hoi/OpenCore-Updater/raw/main/script.py") as upd:
     with open(path, "wb+") as f:
        f.write(upd.read())
    import subprocess
    subprocess.call(["chmod" ,"+x", __file__])
    os.execv(__file__, sys.argv)
else: 
    print("the script has the newest version " + xyzpersion)
time.sleep(7)

def efimounting():
    if os.path.exists('/Volumes/EFI'):
        print ("You mounted your EFI! Going back to main menu....")
        time.sleep(3)
        mainMenu()
    else: 
        print ("You didn't mount your EFI, the script will now automatically mount your EFI....")
        time.sleep(3)
        try:
            print("Mounting EFI....")
            subprocess.call(r"sudo diskutil mount $(nvram 4D1FDA02-38C7-4A6A-9CC6-4BCCA8B30102:boot-path | sed 's/.*GPT,\([^,]*\),.*/\1/')", shell=True)
            if os.path.exists("/Volumes/EFI"):
                print("well done! your EFI is mounted.")
                time.sleep(3)
                mainMenu()
        except Exception:
            print("The script couldn't  mount your EFI, falling back to mountEFI")
            time.sleep(3)
            url2 = 'https://github.com/corpnewt/MountEFI/archive/update.zip'
            urllib.request.urlretrieve(url2, 'MountEFI.zip')
            with zipfile.ZipFile('MountEFI.zip', 'r') as zip_ref:
                zip_ref.extractall()
            print("opening MountEFI, the awesome tool from CorpNewt....")
            b = 'MountEFI-update/MountEFI.command'
            subprocess.call(["chmod" ,"+x", b])
            subprocess.Popen(['open', '-a', 'Terminal.app', b])
            time.sleep(15)
            subprocess.call("kill $(ps aux | grep '[M]ountEFI' | awk '{print $2}')", shell=True)
            if os.path.exists("/Volumes/EFI"):
                print("well done! your EFI is mounted, continuing...")
            else: 
                print("Mount your EFI and come back.....")
                time.sleep(3)
                mainMenu()
def everything():
    if os.path.exists(pathdownload):
        shutil.rmtree(pathdownload)
        os.mkdir(pathdownload)
        os.chdir("downloadtemp")
    else:
        os.mkdir(pathdownload)
        os.chdir("downloadtemp")
    if os.path.exists('/Volumes/EFI'):
        print ("You mounted your EFI! the script will continue.")
    else: 
        print ("You didn't mount your EFI, the script will now automatically mount your EFI....")
        time.sleep(3)
        try:
            print("Mounting EFI....")
            subprocess.call(r"sudo diskutil mount $(nvram 4D1FDA02-38C7-4A6A-9CC6-4BCCA8B30102:boot-path | sed 's/.*GPT,\([^,]*\),.*/\1/')", shell=True)
            if os.path.exists("/Volumes/EFI"):
                print("well done! your EFI is mounted, continuing...")
        except:
            print("The script couldn't  mount your EFI, falling back to mountEFI")
            time.sleep(3)
            url2 = 'https://github.com/corpnewt/MountEFI/archive/update.zip'
            urllib.request.urlretrieve(url2, 'MountEFI.zip')
            with zipfile.ZipFile('MountEFI.zip', 'r') as zip_ref:
                zip_ref.extractall()
            print("opening MountEFI, the awesome tool from CorpNewt....")
            b = 'MountEFI-update/MountEFI.command'
            subprocess.call(["chmod" ,"+x", b])
            subprocess.Popen(['open', '-a', 'Terminal.app', b])
            time.sleep(15)
            subprocess.call("kill $(ps aux | grep '[M]ountEFI' | awk '{print $2}')", shell=True)
            if os.path.exists("/Volumes/EFI"):
                print("well done! your EFI is mounted, continuing...")
            else: 
                print("Mount your EFI and come back.....")
                time.sleep(3)
                mainMenu()
    os.chmod("/Volumes/EFI/EFI/OC", stat.S_IRWXO)
    os.chmod("/Volumes/EFI/EFI", stat.S_IRWXO)
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VirtualSMC.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/VirtualSMC/releases/latest").read()
        json_data = json.loads(url_data)
        versionvirtualsmc = json_data["tag_name"]
        print("updating VirtualSMC to " + versionvirtualsmc +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'Virtualsmc.zip')
        with zipfile.ZipFile('Virtualsmc.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VirtualSMC.kext", ignore_errors=True)
        shutil.copytree("Kexts/VirtualSMC.kext", "/Volumes/EFI/EFI/OC/Kexts/VirtualSMC.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCBatteryManager.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCBatteryManager.kext", ignore_errors=True)
        shutil.copytree("Kexts/SMCBatteryManager.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCBatteryManager.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCDellSensors.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCDellSensors.kext", ignore_errors=True)
        shutil.copytree("Kexts/SMCDellSensors.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCDellSensors.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCLightSensor.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCLightSensor.kext", ignore_errors=True)
        shutil.copytree("Kexts/SMCLightsensor.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCLightSensor.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCProcessor.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCProcessor.kext", ignore_errors=True)
        shutil.copytree("Kexts/SMCProcessor.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCProcessor.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCSuperIO.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCSuperIO.kext", ignore_errors=True)
        shutil.copytree("Kexts/SMCSuperIO.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCSuperIO.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/Lilu.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/Lilu/releases/latest").read()
        json_data = json.loads(url_data)
        versionlilu = json_data["tag_name"]
        print("updating Lilu to " + versionlilu +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'Lilu.zip')
        with zipfile.ZipFile('Lilu.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/Lilu.kext", ignore_errors=True)
        shutil.copytree("Lilu.kext", "/Volumes/EFI/EFI/OC/Kexts/Lilu.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/CPUFriend.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/CPUFriend/releases/latest").read()
        json_data = json.loads(url_data)
        versioncpufriend = json_data["tag_name"]
        print("updating CPUFriend to " + versioncpufriend +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        urlcpufriend = asset["browser_download_url"]
        urllib.request.urlretrieve(urlcpufriend, 'CPUFriend.zip')
        with zipfile.ZipFile('CPUFriend.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/CPUFriend.kext", ignore_errors=True)
        shutil.copytree("CPUFriend.kext", "/Volumes/EFI/EFI/OC/Kexts/CPUFriend.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/WhateverGreen.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/Whatevergreen/releases/latest").read()
        json_data = json.loads(url_data)
        versionwhatever = json_data["tag_name"]
        print("updating WhateverGreen to " + versionwhatever +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'WhateverGreen.zip')
        with zipfile.ZipFile('WhateverGreen.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/WhateverGreen.kext", ignore_errors=True)
        shutil.copytree("WhateverGreen.kext", "/Volumes/EFI/EFI/OC/Kexts/WhateverGreen.kext")  
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/Polaris22Fixup.kext"):
        url_data = urlopen("https://api.github.com/repos/osy/Polaris22Fixup/releases/latest").read()
        json_data = json.loads(url_data)
        versionpolaris22 = json_data["tag_name"]
        print("updating Polaris22Fixup to " + versionpolaris22 +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'Polaris22Fixup.zip')
        with zipfile.ZipFile('Polaris22Fixup.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/Polaris22Fixup.kext", ignore_errors=True)
        shutil.copytree("Polaris22Fixup.kext", "/Volumes/EFI/EFI/OC/Kexts/Polaris22Fixup.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AppleALC.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/AppleALC/releases/latest").read()
        json_data = json.loads(url_data)
        versionapplealc = json_data["tag_name"]
        print("updating AppleALC to " + versionapplealc +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'AppleALC.zip')
        with zipfile.ZipFile('AppleALC.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AppleALC.kext", ignore_errors=True)
        shutil.copytree("AppleALC.kext", "/Volumes/EFI/EFI/OC/Kexts/AppleALC.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/IntelMausi.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/IntelMausi/releases/latest").read()
        json_data = json.loads(url_data)
        versionintelmausi = json_data["tag_name"]
        print("updating IntelMausi to " + versionintelmausi +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'IntelMausi.zip')
        with zipfile.ZipFile('IntelMausi.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/IntelMausi.kext", ignore_errors=True)
        shutil.copytree("IntelMausi.kext", "/Volumes/EFI/EFI/OC/Kexts/IntelMausi.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SmallTreeIntel82576.kext"):
        url_data = urlopen("https://api.github.com/repos/khronokernel/SmallTree-I211-AT-patch/releases/latest").read()
        json_data = json.loads(url_data)
        versionsmalltreei211 = json_data["tag_name"]
        print("updating SmallTreeIntel to " + versionsmalltreei211 +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'SmallTreeIntel82576.zip')
        with zipfile.ZipFile('SmallTreeIntel82576.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SmallTreeIntel82576.kext", ignore_errors=True)
        shutil.copytree("SmallTreeIntel82576.kext", "/Volumes/EFI/EFI/OC/Kexts/SmallTreeIntel82576.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AtherosE2200Ethernet.kext"):
        url_data = urlopen("https://api.github.com/repos/Mieze/AtherosE2200Ethernet/releases/latest").read()
        json_data = json.loads(url_data)
        versionatherose2200 = json_data["tag_name"]
        print("updating AtherosE2200Ethernet to " + versionatherose2200 +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'AtherosE2200Ethernet.zip')
        with zipfile.ZipFile('AtherosE2200Ethernet.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AtherosE2200Ethernet.kext", ignore_errors=True)
        shutil.copytree("AtherosE2200Ethernet-V2.2.2/Release/AtherosE2200Ethernet.kext", "/Volumes/EFI/EFI/OC/Kexts/AtherosE2200Ethernet.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8111.kext"):
        url_data = urlopen("https://api.github.com/repos/Mieze/RTL8111_driver_for_OS_X/releases/latest").read()
        json_data = json.loads(url_data)
        versionrtl8111 = json_data["tag_name"]
        print("updating RealtekRTL8111 to " + versionrtl8111 +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'RealtekRTL8111.zip')
        with zipfile.ZipFile('RealtekRTL8111.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8111.kext", ignore_errors=True)
        shutil.copytree("RealtekRTL8111-V2.4.0/Release/RealtekRTL8111.kext", "/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8111.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/LucyRTL8125Ethernet.kext"):
        url = 'https://www.insanelymac.com/forum/files/file/1004-lucyrtl8125ethernet/?do=download&csrfKey=9da7156f1e6ce2d23fee67731e9fc70b'
        urllib.request.urlretrieve(url, 'LucyRTL8125Ethernet.zip')
        print("Updating LucyRTL8125Ethernet to the newest version.....")
        with zipfile.ZipFile('LucyRTL8125Ethernet.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/LucyRTL8125Ethernet.kext", ignore_errors=True)
        shutil.copytree("Release/LucyRTL8125Ethernet.kext", "/Volumes/EFI/EFI/OC/Kexts/LucyRTL8125Ethernet.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8100.kext"):
        url = 'https://www.insanelymac.com/forum/files/file/259-realtekrtl8100-binary/?do=download&csrfKey=9da7156f1e6ce2d23fee67731e9fc70b'
        urllib.request.urlretrieve(url, 'RealtekRTL8100.zip')
        print("Updating RealtekRTL8100 to the newest version.....")
        with zipfile.ZipFile('RealtekRTL8100.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8100.kext", ignore_errors=True)
        shutil.copytree("Release/RealtekRTL8100.kext", "/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8100.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/itlwm.kext"):
        url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
        json_data = json.loads(url_data)
        versionitlwm = json_data["tag_name"]
        print("updating Itlwm to " + versionitlwm +".....")
        for asset in json_data["assets"]:
            if "itlwm" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'itlwm.zip')
        with zipfile.ZipFile('itlwm.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/itlwm.kext", ignore_errors=True)
        shutil.copytree("itlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/itlwm.kext")
    v, _, _ = platform.mac_ver()
    v = float('.'.join(v.split('.')[:2]))
    if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 11.2)):
        url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
        json_data = json.loads(url_data)
        versionitlwm = json_data["tag_name"]
        print("updating AirportItlwm to " + versionitlwm +".....")
        for asset in json_data["assets"]:
            if "BigSur" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'AirportItlwm.zip')
        with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
        shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
    if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 11.1)):
        url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
        json_data = json.loads(url_data)
        versionitlwm = json_data["tag_name"]
        print("updating AirportItlwm to " + versionitlwm +".....")
        for asset in json_data["assets"]:
            if "BigSur" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'AirportItlwm.zip')
        with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
        shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
    if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 11.0)):
        url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
        json_data = json.loads(url_data)
        versionitlwm = json_data["tag_name"]
        print("updating AirportItlwm to " + versionitlwm +".....")
        for asset in json_data["assets"]:
            if "BigSur" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'AirportItlwm.zip')
        with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
        shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
    if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.16)):
        url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
        json_data = json.loads(url_data)
        versionitlwm = json_data["tag_name"]
        print("updating AirportItlwm to " + versionitlwm +".....")
        for asset in json_data["assets"]:
            if "BigSur" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'AirportItlwm.zip')
        with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
        shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
    if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.15)):
        url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
        json_data = json.loads(url_data)
        versionitlwm = json_data["tag_name"]
        print("updating AirportItlwm to " + versionitlwm +".....")
        for asset in json_data["assets"]:
            if "Catalina" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'AirportItlwm.zip')
        with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
        shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
    if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.14)):
        url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
        json_data = json.loads(url_data)
        versionitlwm = json_data["tag_name"]
        print("updating AirportItlwm to " + versionitlwm +".....")
        for asset in json_data["assets"]:
            if "Mojave" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'AirportItlwm.zip')
        with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
        shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
    if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.13)):
        url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
        json_data = json.loads(url_data)
        versionitlwm = json_data["tag_name"]
        print("updating AirportItlwm to " + versionitlwm +".....")
        for asset in json_data["assets"]:
            if "HighSierra" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'AirportItlwm.zip')
        with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
        shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothFirmware.kext"):
        url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/intelbluetoothfirmware/releases/latest").read()
        json_data = json.loads(url_data)
        versionintelbluetoothfirmware = json_data["tag_name"]
        print("updating AirportItlwm to " + versionintelbluetoothfirmware +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'IntelBluetoothFirmware.zip')
        with zipfile.ZipFile('IntelBluetoothFirmware.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothFirmware.kext", ignore_errors=True)
        shutil.copytree("IntelBluetoothFirmware.kext", "/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothFirmware.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothInjector.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothInjector.kext", ignore_errors=True)
        shutil.copytree("IntelBluetoothInjector.kext", "/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothInjector.kext")
        print("updated IntelBluetoothInjector to version " + versionintelbluetoothfirmware +"......")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AirportBrcmFixup.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/AirportBrcmFixup/releases/latest").read()
        json_data = json.loads(url_data)
        versionairportbrcmfixup = json_data["tag_name"]
        print("updating AirportBrcmFixup to " + versionairportbrcmfixup +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'AirportBrcmFixup.zip')
        with zipfile.ZipFile('AirportBrcmFixup.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportBrcmFixup.kext", ignore_errors=True)
        shutil.copytree("AirportBrcmFixup.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportBrcmFixup.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjector.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
        json_data = json.loads(url_data)
        versionbrcmpatchram = json_data["tag_name"]
        print("updating BrcmPatchRAM to " + versionbrcmpatchram +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'BrcmBluetoothInjector.zip')
        with zipfile.ZipFile('BrcmBluetoothInjector.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjector.kext", ignore_errors=True)
        shutil.copytree("BrcmBluetoothInjector.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjector.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjectorLegacy.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
        json_data = json.loads(url_data)
        versionbrcmpatchram = json_data["tag_name"]
        print("updating BrcmBluetoothInjectorlegacy to " + versionbrcmpatchram +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'BrcmBluetoothInjectorlegacy.zip')
        with zipfile.ZipFile('BrcmBluetoothInjectorLegacy.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjectorLegacy.kext", ignore_errors=True)
        shutil.copytree("BrcmBluetoothInjectorLegacy.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjectorLegacy.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareData.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
        json_data = json.loads(url_data)
        versionbrcmpatchram = json_data["tag_name"]
        print("updating BrcmFirmwareData to " + versionbrcmpatchram +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'BrcmFirmwareData.zip')
        with zipfile.ZipFile('BrcmFirmwareData.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareData.kext", ignore_errors=True)
        shutil.copytree("BrcmFirmwareData.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareData.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareRepo.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
        json_data = json.loads(url_data)
        versionbrcmpatchram = json_data["tag_name"]
        print("updating BrcmFirmwareRepo to " + versionbrcmpatchram +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'BrcmFirmwareRepo.zip')
        with zipfile.ZipFile('BrcmFirmwareRepo.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareRepo.kext", ignore_errors=True)
        shutil.copytree("BrcmFirmwareRepo.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareRepo.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
        json_data = json.loads(url_data)
        versionbrcmpatchram = json_data["tag_name"]
        print("updating BrcmNonPatchRAM to " + versionbrcmpatchram +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'BrcmNonPatchRAM.zip')
        with zipfile.ZipFile('BrcmNonPatchRAM.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM.kext", ignore_errors=True)
        shutil.copytree("BrcmNonPatchRAM.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM2.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
        json_data = json.loads(url_data)
        versionbrcmpatchram = json_data["tag_name"]
        print("updating BrcmNonPatchRAM2 to " + versionbrcmpatchram +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'BrcmNonPatchRAM2.zip')
        with zipfile.ZipFile('BrcmNonPatchRAM2.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM2.kext", ignore_errors=True)
        shutil.copytree("BrcmNonPatchRAM2.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM2.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM2.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
        json_data = json.loads(url_data)
        versionbrcmpatchram = json_data["tag_name"]
        print("updating BrcmPatchRAM2 to " + versionbrcmpatchram +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'BrcmPatchRAM2.zip')
        with zipfile.ZipFile('BrcmPatchRAM2.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM2.kext", ignore_errors=True)
        shutil.copytree("BrcmPatchRAM2.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM2.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM3.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
        json_data = json.loads(url_data)
        versionbrcmpatchram = json_data["tag_name"]
        print("updating BrcmPatchRAM3 to " + versionbrcmpatchram +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'BrcmPatchRAM3.zip')
        with zipfile.ZipFile('BrcmPatchRAM3.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM3.kext", ignore_errors=True)
        shutil.copytree("BrcmPatchRAM3.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM3.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/XLNCUSBFix.kext"):
        url = 'https://cdn.discordapp.com/attachments/566705665616117760/566728101292408877/XLNCUSBFix.kext.zip'
        urllib.request.urlretrieve(url, 'XLNCUSBFix.zip')
        print("Updating XLNCUSBFix to the newest version.....")
        with zipfile.ZipFile('XLNCUSBFix.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/XLNCUSBFix.kext", ignore_errors=True)
        shutil.copytree("XLNCUSBFix.kext", "/Volumes/EFI/EFI/OC/Kexts/XLNCUSBFix.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooHDA.kext"):
        url = 'https://sourceforge.net/projects/voodoohda/files/VoodooHDA.kext-296.zip/download'
        urllib.request.urlretrieve(url, 'VoodooHDA.zip')
        time.sleep(6)
        with zipfile.ZipFile('VoodooHDA.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooHDA.kext", ignore_errors=True)
        shutil.copytree("VoodooHDA.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooHDA.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/CpuTscSync.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/CpuTscSync/releases/latest").read()
        json_data = json.loads(url_data)
        versioncputscsync = json_data["tag_name"]
        print("updating CpuTscSync to " + versioncputscsync +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'CpuTscSync.zip')
        with zipfile.ZipFile('CpuTscSync.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/CpuTscSync.kext", ignore_errors=True)
        shutil.copytree("CpuTscSync.kext", "/Volumes/EFI/EFI/OC/Kexts/CpuTscSync.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/NVMeFix.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/NVMeFix/releases/latest").read()
        json_data = json.loads(url_data)
        versionnvmefix = json_data["tag_name"]
        print("updating NVMeFix to " + versionnvmefix +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'NVMeFix.zip')
        with zipfile.ZipFile('NVMeFix.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/NVMeFix.kext", ignore_errors=True)
        shutil.copytree("NVMeFix.kext", "/Volumes/EFI/EFI/OC/Kexts/NVMeFix.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/HibernationFixup.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/HibernationFixup/releases/latest").read()
        json_data = json.loads(url_data)
        versiohibernation = json_data["tag_name"]
        print("updating HibernationFixup to " + versiohibernation +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'HibernationFixup.zip')
        with zipfile.ZipFile('HibernationFixup.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/HibernationFixup.kext", ignore_errors=True)
        shutil.copytree("HibernationFixup.kext", "/Volumes/EFI/EFI/OC/Kexts/HibernationFixup.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/NightShiftEnabler.kext"):
        url_data = urlopen("https://api.github.com/repos/cdf/NightShiftEnabler/releases/latest").read()
        json_data = json.loads(url_data)
        versionnightshift = json_data["tag_name"]
        print("updating NVMeFix to " + versionnightshift +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'NightShiftEnabler.zip')
        with zipfile.ZipFile('NightShiftEnabler.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/NightShiftEnabler.kext", ignore_errors=True)
        shutil.copytree("NightShiftEnabler.kext", "/Volumes/EFI/EFI/OC/Kexts/NightShiftEnabler.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/Innie.kext"):
        url_data = urlopen("https://api.github.com/repos/cdf/Innie/releases/latest").read()
        json_data = json.loads(url_data)
        versioninnie = json_data["tag_name"]
        print("updating Innie to " + versioninnie +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'Innie.zip')
        with zipfile.ZipFile('Innie.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/Innie.kext", ignore_errors=True)
        shutil.copytree("Innie.kext", "/Volumes/EFI/EFI/OC/Kexts/Innie.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SATA-unsupported.kext"):
        url = 'https://github.com/khronokernel/Legacy-Kexts/blob/master/Injectors/Zip/SATA-unsupported.kext.zip?raw=true'
        urllib.request.urlretrieve(url, 'SATA-unsupported.zip')
        print("Updating SATA-Unsupported.......")
        with zipfile.ZipFile('SATA-unsupported.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SATA-unsupported.kext", ignore_errors=True)
        shutil.copytree("SATA-unsupported.kext", "/Volumes/EFI/EFI/OC/Kexts/SATA-unsupported.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AHCIPortInjector.kext"):
        url = 'https://github.com/khronokernel/Legacy-Kexts/blob/master/Injectors/Zip/AHCIPortInjector.kext.zip?raw=true'
        urllib.request.urlretrieve(url, 'AHCIPortInjector.zip')
        print("Updating AHCIPortInjector.....")
        with zipfile.ZipFile('AHCIPortInjector.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AHCIPortInjector.kext", ignore_errors=True)
        shutil.copytree("AHCIPortInjector.kext", "/Volumes/EFI/EFI/OC/Kexts/AHCIPortInjector.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/ATAPortInjector.kext"):
        url = 'https://github.com/khronokernel/Legacy-Kexts/blob/master/Injectors/Zip/ATAPortInjector.kext.zip?raw=true'
        urllib.request.urlretrieve(url, 'ATAPortInjector.zip')
        print("Updating ATAPortInjector to newest version....")
        with zipfile.ZipFile('ATAPortInjector.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/ATAPortInjector.kext", ignore_errors=True)
        shutil.copytree("ATAPortInjector.kext", "/Volumes/EFI/EFI/OC/Kexts/ATAPortInjector.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/VoodooPS2/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodoops2 = json_data["tag_name"]
        print("updating VoodooPS2Controller to " + versionvoodoops2 +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'VoodooPS2Controller.zip')
        with zipfile.ZipFile('VoodooPS2Controller.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext", ignore_errors=True)
        shutil.copytree("VoodooPS2Controller.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooInput.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/Voodooinput/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodooinput = json_data["tag_name"]
        print("updating VoodooInput to " + versionvoodooinput +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'VoodooInput.zip')
        with zipfile.ZipFile('VoodooInput.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooInput.kext", ignore_errors=True)
        shutil.copytree("VoodooInput.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooInput.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooRMI.kext"):
        url_data = urlopen("https://api.github.com/repos/VoodooSmbus/VoodooRMI/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodoormi = json_data["tag_name"]
        print("updating VoodooRMI to " + versionvoodoormi +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'VoodooRMI.zip')
        with zipfile.ZipFile('VoodooRMI.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooRMI.kext", ignore_errors=True)
        shutil.copytree("VoodooRMI.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooRMI.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AMDRyzenCPUPowerManagement.kext"):
        url_data = urlopen("https://api.github.com/repos/trulyspinach/SMCAMDProcessor/releases/latest").read()
        json_data = json.loads(url_data)
        versionAMDRyzenCPUPowerManagement = json_data["tag_name"]
        print("updating AMDRyzenCPUPowerManagement to " + versionAMDRyzenCPUPowerManagement +".....")
        for asset in json_data["assets"]:
            if ".kext" not in asset["browser_download_url"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'AMDRyzenCPUPowerManagement.zip')
        with zipfile.ZipFile('AMDRyzenCPUPowerManagement.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AMDRyzenCPUPowerManagement.kext", ignore_errors=True)
        shutil.copytree("AMDRyzenCPUPowerManagement.kext", "/Volumes/EFI/EFI/OC/Kexts/AMDRyzenCPUPowerManagement.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AlpsT4USB.kext"):
        url = 'https://github.com/blankmac/AlpsT4USB/files/5933051/AlpsT4USB.zip'
        urllib.request.urlretrieve(url, 'AlpsT4USB.zip')
        print("Updating AlpsT4USB to the newest version....")
        with zipfile.ZipFile('AlpsT4USB.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AlpsT4USB.kext", ignore_errors=True)
        shutil.copytree("Release/AlpsT4USB.kext", "/Volumes/EFI/EFI/OC/Kexts/AlpsT4USB.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooSMBus.kext"):
        url_data = urlopen("https://api.github.com/repos/VoodooSmbus/VoodooSMBus/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodoosmbus = json_data["tag_name"]
        print("updating VoodooSMBus to " + versionvoodoosmbus +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'VoodooSMBus.zip')
        with zipfile.ZipFile('VoodooSMBus.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooSMBus.kext", ignore_errors=True)
        shutil.copytree("VoodooSMBus-v2.2/kext/VoodooSMBus.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooSMBus.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2C.kext"):
        url_data = urlopen("https://api.github.com/repos/VoodooI2C/VoodooI2C/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodooi2c = json_data["tag_name"]
        print("updating VoodooI2C to " + versionvoodooi2c +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'VoodooI2C.zip')
        with zipfile.ZipFile('VoodooI2C.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2C.kext", ignore_errors=True)
        shutil.copytree("VoodooI2C.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2C.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CAtmelMXT.kext"):
        url_data = urlopen("https://api.github.com/repos/VoodooI2C/VoodooI2C/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodooinput = json_data["tag_name"]
        print("updating VoodooI2CAtmelMXT to " + versionvoodooinput +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'VoodooI2CAtmelMXT.zip')
        with zipfile.ZipFile('VoodooI2CAtmelMXT.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CAtmelMXT.kext", ignore_errors=True)
        shutil.copytree("VoodooI2CAtmelMXT.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2CAtmelMXT.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CELAN.kext"):
        url_data = urlopen("https://api.github.com/repos/VoodooI2C/VoodooI2C/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodooinput = json_data["tag_name"]
        print("updating VoodooI2CELAN to " + versionvoodooinput +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'VoodooI2CELAN.zip')
        with zipfile.ZipFile('VoodooI2CELAN.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CELAN.kext", ignore_errors=True)
        shutil.copytree("VoodooI2CELAN.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2CELAN.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CFTE.kext"):
        url_data = urlopen("https://api.github.com/repos/VoodooI2C/VoodooI2C/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodooinput = json_data["tag_name"]
        print("updating VoodooI2CFTE to " + versionvoodooinput +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'VoodooI2CFTE.zip')
        with zipfile.ZipFile('VoodooI2CFTE.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CFTE.kext", ignore_errors=True)
        shutil.copytree("VoodooI2CFTE.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2CFTE.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CHID.kext"):
        url_data = urlopen("https://api.github.com/repos/VoodooI2C/VoodooI2C/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodooinput = json_data["tag_name"]
        print("updating VoodooI2CHID to " + versionvoodooinput +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'VoodooI2CHID.zip')
        with zipfile.ZipFile('VoodooI2CHID.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CHID.kext", ignore_errors=True)
        shutil.copytree("VoodooI2CHID.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2CHID.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CSynaptics.kext"):
        url_data = urlopen("https://api.github.com/repos/VoodooI2C/VoodooI2C/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodooinput = json_data["tag_name"]
        print("updating VoodooI2CSynaptics to " + versionvoodooinput +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'VoodooI2CSynaptics.zip')
        with zipfile.ZipFile('VoodooI2CSynaptics.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CSynaptics.kext", ignore_errors=True)
        shutil.copytree("VoodooI2CSynaptics.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2CSynaptics.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCAMDProcessor.kext"):
        url = 'https://github.com/trulyspinach/SMCAMDProcessor/releases/download/0.6.4/SMCAMDProcessor.kext.zip'
        urllib.request.urlretrieve(url, 'SMCAMDProcessor.zip')
        print("Updating SMCAMDProcessor to the newest version....")
        with zipfile.ZipFile('SMCAMDProcessor.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCAMDProcessor.kext", ignore_errors=True)
        shutil.copytree("SMCAMDProcessor.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCAMDProcessor.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/FakeSMC.kext"):
        url_data = urlopen("https://api.github.com/repos/CloverHackyColor/FakeSMC3_with_plugins/releases/latest").read()
        json_data = json.loads(url_data)
        versionfakesmc = json_data["tag_name"]
        print("updating FakeSMC to release " + versionfakesmc +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'FakeSMC.zip')
        with zipfile.ZipFile('FakeSMC.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/FakeSMC.kext", ignore_errors=True)
        shutil.copytree("FakeSMC.kext", "/Volumes/EFI/EFI/OC/Kexts/FakeSMC.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/ACPIMonitor.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/ACPIMonitor.kext", ignore_errors=True)
        shutil.copytree("ACPIMonitor.kext", "/Volumes/EFI/EFI/OC/Kexts/ACPIMonitor.kext")
        print("Updating FakeSMC Plugin ACPIMonitor....")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AmdCPUMonitor.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AmdCPUMonitor.kext", ignore_errors=True)
        shutil.copytree("AmdCPUMonitor.kext", "/Volumes/EFI/EFI/OC/Kexts/AmdCPUMonitor.kext")
        print("Updating FakeSMC Plugin AMDCPUMonitor....")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/F718x.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/F718x.kext", ignore_errors=True)
        shutil.copytree("F718x.kext", "/Volumes/EFI/EFI/OC/Kexts/F718x.kext")
        print("Updating FakeSMC Plugin F718x .....")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/GeforceSensor.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/GeforceSensor.kext", ignore_errors=True)
        shutil.copytree("GeforceSensor.kext", "/Volumes/EFI/EFI/OC/Kexts/GeforceSensor.kext")
        print("Updating FakeSMC Plugin GeforceSensor....")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/IntelCPUMonitor.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/IntelCPUMonitor.kext", ignore_errors=True)
        shutil.copytree("IntelCPUMonitor.kext", "/Volumes/EFI/EFI/OC/Kexts/IntelCPUMonitor.kext")
        print("Updating FakeSMC Plugin IntelCPUMonitor.....")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/IntelMCHMonitor.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/IntelMCHMonitor.kext", ignore_errors=True)
        shutil.copytree("IntelMCHMonitor.kext", "/Volumes/EFI/EFI/OC/Kexts/IntelMCHMonitor.kext")
        print("Updating FakeSMC Plugin IntelMCHMonitor.....")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/ITEIT87x.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/ITEIT87x.kext", ignore_errors=True)
        shutil.copytree("ITEIT87x.kext", "/Volumes/EFI/EFI/OC/Kexts/ITEIT87x.kext")
        print("Updating other FakeSMC plugins.....")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/NVClockX.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/NVClockX.kext", ignore_errors=True)
        shutil.copytree("NVClockX.kext", "/Volumes/EFI/EFI/OC/Kexts/NVClockX.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/RadeonMonitor.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/RadeonMonitor.kext", ignore_errors=True)
        shutil.copytree("RadeonMonitor.kext", "/Volumes/EFI/EFI/OC/Kexts/RadeonMonitor.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMIMonitor.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMIMonitor.kext", ignore_errors=True)
        shutil.copytree("SMIMonitor.kext", "/Volumes/EFI/EFI/OC/Kexts/SMIMonitor.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooBatterySMC.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooBatterySMC.kext", ignore_errors=True)
        shutil.copytree("VoodooBatterySMC.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooBatterySMC.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/W836x.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/W836x.kext", ignore_errors=True)
        shutil.copytree("W836x.kext", "/Volumes/EFI/EFI/OC/Kexts/W836x.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AtherosL1cEthernet.kext"):
        url = 'https://www.insanelymac.com/applications/core/interface/file/attachment.php?id=115905'
        urllib.request.urlretrieve(url, 'AtherosL1cEthernet.zip')
        print("Updating AtherosL1cEthernet.....")
        with zipfile.ZipFile('AtherosL1cEthernet.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AtherosL1cEthernet.kext", ignore_errors=True)
        shutil.copytree("AtherosL1cEthernet.kext", "/Volumes/EFI/EFI/OC/Kexts/AtherosL1cEthernet.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AirPortAtheros40.kext"):
        url = 'https://i.applelife.ru/2018/12/442854_AirPortAtheros40.kext.zip'
        urllib.request.urlretrieve(url, 'AirPortAtheros40.zip')
        print("Updating AirPortAtheros40......")
        with zipfile.ZipFile('AirPortAtheros40.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirPortAtheros40.kext", ignore_errors=True)
        shutil.copytree("AirPortAtheros40.kext", "/Volumes/EFI/EFI/OC/Kexts/AirPortAtheros40.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/VoodooPS2/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodoops2 = json_data["tag_name"]
        print("updating VoodooPS2Controller to " + versionvoodoops2 +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'VoodooPS2Controller.zip')
        with zipfile.ZipFile('VoodooPS2Controller.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext", ignore_errors=True)
        shutil.copytree("VoodooPS2Controller.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrightnessKeys.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/BrightnessKeys/releases/latest").read()
        json_data = json.loads(url_data)
        versionbrightnesskeys = json_data["tag_name"]
        print("updating BrightnessKeys to " + versionbrightnesskeys +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'BrightnessKeys.zip')
        with zipfile.ZipFile('BrightnessKeys.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrightnessKeys.kext", ignore_errors=True)
        shutil.copytree("BrightnessKeys.kext", "/Volumes/EFI/EFI/OC/Kexts/BrightnessKeys.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/OpenCore.efi"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest").read()
        json_data = json.loads(url_data)
        versionopencore = json_data["tag_name"]
        print("updating OpenCore.efi to " + versionopencore +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'OpenCoreefi.zip')
        with zipfile.ZipFile('OpenCoreefi.zip', 'r') as zip_ref:
            zip_ref.extractall()
        os.remove("/Volumes/EFI/EFI/OC/OpenCore.efi")
        shutil.copy2("X64/EFI/OC/OpenCore.efi", "/Volumes/EFI/EFI/OC/OpenCore.efi")
    if os.path.exists("/Volumes/EFI/EFI/BOOT/BOOTx64.efi"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest").read()
        json_data = json.loads(url_data)
        versionopencore = json_data["tag_name"]
        print("updating BOOTx64.efi to " + versionopencore +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'OpenCorebootx64.zip')
        with zipfile.ZipFile('OpenCorebootx64.zip', 'r') as zip_ref:
            zip_ref.extractall()
        os.remove("/Volumes/EFI/EFI/BOOT/BOOTx64.efi")
        shutil.copy2("X64/EFI/BOOT/BOOTx64.efi", "/Volumes/EFI/EFI/BOOT/BOOTx64.efi")
    if os.path.exists("/Volumes/EFI/EFI/BOOT/BOOTIA32.efi"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest").read()
        json_data = json.loads(url_data)
        versionopencore = json_data["tag_name"]
        print("updating BOOTIA32.efi to " + versionopencore +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'OpenCorebootia32.zip')
        with zipfile.ZipFile('OpenCorebootia32.zip', 'r') as zip_ref:
            zip_ref.extractall()
        os.remove("/Volumes/EFI/EFI/BOOT/BOOTIA32.efi")
        shutil.copy2("IA32/EFI/BOOT/BOOTIA32.efi", "/Volumes/EFI/EFI/BOOT/BOOTIA32.efi")
    if os.path.exists("/Volumes/EFI/EFI/OC/Drivers/OpenRuntime.efi"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest").read()
        json_data = json.loads(url_data)
        versionopencore = json_data["tag_name"]
        print("updating OpenRuntime.efi to " + versionopencore +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'OpenRuntime.zip')
        with zipfile.ZipFile('OpenRuntime.zip', 'r') as zip_ref:
            zip_ref.extractall()
        os.remove("/Volumes/EFI/EFI/OC/Drivers/OpenRuntime.efi")
        shutil.copy2("X64/EFI/OC/Drivers/OpenRuntime.efi", "/Volumes/EFI/EFI/OC/Drivers/OpenRuntime.efi")
    if os.path.exists("/Volumes/EFI/EFI/OC/Drivers/OpenCanopy.efi"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest").read()
        json_data = json.loads(url_data)
        versionopencore = json_data["tag_name"]
        print("updating OpenCanopy.efi to " + versionopencore +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'OpenCanopy.zip')
        with zipfile.ZipFile('OpenCanopy.zip', 'r') as zip_ref:
            zip_ref.extractall()
        os.remove("/Volumes/EFI/EFI/OC/Drivers/OpenCanopy.efi")
        shutil.copy2("X64/EFI/OC/Drivers/OpenCanopy.efi", "/Volumes/EFI/EFI/OC/Drivers/OpenCanopy.efi")
    if os.path.exists("/Volumes/EFI/EFI/OC/Drivers/OpenUsbKbDxe.efi"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest").read()
        json_data = json.loads(url_data)
        versionopencore = json_data["tag_name"]
        print("updating OpenUsbKbDxe.efi to " + versionopencore +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'OpenUsbKbDxe.zip')
        with zipfile.ZipFile('OpenUsbKbDxe.zip', 'r') as zip_ref:
            zip_ref.extractall()
        os.remove("/Volumes/EFI/EFI/OC/Drivers/OpenUsbKbDxe.efi")
        shutil.copy2("X64/EFI/OC/Drivers/OpenUsbKbDxe.efi", "/Volumes/EFI/EFI/OC/Drivers/OpenUsbKbDxe.efi")
    if os.path.exists("/Volumes/EFI/EFI/OC/Drivers/HfsPlusLegacy.efi"):
        url = 'https://github.com/acidanthera/OcBinaryData/raw/master/Drivers/HfsPlusLegacy.efi'
        urllib.request.urlretrieve(url, 'HfsPlusLegacy.efi')
        print("Updating HfsPlusLegacy.efi to version " + versionopencore)
        os.remove("/Volumes/EFI/EFI/OC/Drivers/HfsPlusLegacy.efi")
        shutil.copy2("HfsPlusLegacy.efi", "/Volumes/EFI/EFI/OC/Drivers/HfsPlusLegacy.efi")
    if os.path.exists("/Volumes/EFI/EFI/OC/Drivers/HfsPlus32.efi"):
        url = 'https://github.com/acidanthera/OcBinaryData/raw/master/Drivers/HfsPlus32.efi'
        urllib.request.urlretrieve(url, 'HfsPlus32.efi')
        print("Updating HfsPlus32.efi to version " + versionopencore)
        os.remove("/Volumes/EFI/EFI/OC/Drivers/HfsPlus32.efi")
        shutil.copy2("HfsPlus32.efi", "/Volumes/EFI/EFI/OC/Drivers/HfsPlus32.efi")
    if os.path.exists("/Volumes/EFI/EFI/OC/Drivers/HfsPlus.efi"):
        url = 'https://github.com/acidanthera/OcBinaryData/raw/master/Drivers/HfsPlus.efi'
        urllib.request.urlretrieve(url, 'HfsPlus.efi')
        print("Updating HfsPlus.efi to version " + versionopencore)
        os.remove("/Volumes/EFI/EFI/OC/Drivers/HfsPlus.efi")
        shutil.copy2("HfsPlus.efi", "/Volumes/EFI/EFI/OC/Drivers/HfsPlus.efi")
    if os.path.exists("/Volumes/EFI/EFI/OC/Drivers/OpenPartitionDxe.efi"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest").read()
        json_data = json.loads(url_data)
        versionopencore = json_data["tag_name"]
        print("updating OpenPartitionDxe.efi to " + versionopencore +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'OpenPartitionDxe.zip')
        with zipfile.ZipFile('OpenPartitionDxe.zip', 'r') as zip_ref:
            zip_ref.extractall()
        os.remove("/Volumes/EFI/EFI/OC/Drivers/OpenPartitionDxe.efi")
        shutil.copy2("X64/EFI/OC/Drivers/OpenPartitionDxe.efi", "/Volumes/EFI/EFI/OC/Drivers/OpenPartitionDxe.efi")
    if os.path.exists(pathdownload):
          shutil.rmtree(pathdownload)
          print("The downloads have been deleted... have a nice day!")
    else:
          print("The downloads have been deleted... have a nice day!")
    time.sleep(2)
    mainMenu()
def updatedrivers():
    if os.path.exists(pathdownload):
        shutil.rmtree(pathdownload)
        os.mkdir(pathdownload)
        os.chdir("downloadtemp")
    else:
        os.mkdir(pathdownload)
        os.chdir("downloadtemp")
    if os.path.exists('/Volumes/EFI'):
        print ("You mounted your EFI! the script will continue.")
    else: 
        print ("You didn't mount your EFI, the script will now automatically mount your EFI....")
        time.sleep(3)
        try:
            print("Mounting EFI....")
            subprocess.call(r"sudo diskutil mount $(nvram 4D1FDA02-38C7-4A6A-9CC6-4BCCA8B30102:boot-path | sed 's/.*GPT,\([^,]*\),.*/\1/')", shell=True)
            if os.path.exists("/Volumes/EFI"):
                print("well done! your EFI is mounted, continuing...")
        except:
            print("The script couldn't  mount your EFI, falling back to mountEFI")
            time.sleep(3)
            url2 = 'https://github.com/corpnewt/MountEFI/archive/update.zip'
            urllib.request.urlretrieve(url2, 'MountEFI.zip')
            with zipfile.ZipFile('MountEFI.zip', 'r') as zip_ref:
                zip_ref.extractall()
            print("opening MountEFI, the awesome tool from CorpNewt....")
            b = 'MountEFI-update/MountEFI.command'
            subprocess.call(["chmod" ,"+x", b])
            subprocess.Popen(['open', '-a', 'Terminal.app', b])
            time.sleep(15)
            subprocess.call("kill $(ps aux | grep '[M]ountEFI' | awk '{print $2}')", shell=True)
            if os.path.exists("/Volumes/EFI"):
                print("well done! your EFI is mounted, continuing...")
            else: 
                print("Mount your EFI and come back.....")
                time.sleep(3)
                mainMenu()
    os.chmod("/Volumes/EFI/EFI/OC", stat.S_IRWXO)
    os.chmod("/Volumes/EFI/EFI", stat.S_IRWXO)
    if os.path.exists("/Volumes/EFI/EFI/BOOT/BOOTx64.efi"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest").read()
        json_data = json.loads(url_data)
        versionopencore = json_data["tag_name"]
        print("updating BOOTx64.efi to " + versionopencore +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'OpenCorebootx64.zip')
        with zipfile.ZipFile('OpenCorebootx64.zip', 'r') as zip_ref:
            zip_ref.extractall()
        os.remove("/Volumes/EFI/EFI/BOOT/BOOTx64.efi")
        shutil.copy2("X64/EFI/BOOT/BOOTx64.efi", "/Volumes/EFI/EFI/BOOT/BOOTx64.efi")
    if os.path.exists("/Volumes/EFI/EFI/OC/OpenCore.efi"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest").read()
        json_data = json.loads(url_data)
        versionopencore = json_data["tag_name"]
        print("updating OpenCore.efi to " + versionopencore +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'OpenCoreefi.zip')
        with zipfile.ZipFile('OpenCoreefi.zip', 'r') as zip_ref:
            zip_ref.extractall()
        os.remove("/Volumes/EFI/EFI/OC/OpenCore.efi")
        shutil.copy2("X64/EFI/OC/OpenCore.efi", "/Volumes/EFI/EFI/OC/OpenCore.efi")
    if os.path.exists("/Volumes/EFI/EFI/BOOT/BOOTIA32.efi"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest").read()
        json_data = json.loads(url_data)
        versionopencore = json_data["tag_name"]
        print("updating BOOTIA32.efi to " + versionopencore +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'OpenCorebootia32.zip')
        with zipfile.ZipFile('OpenCorebootia32.zip', 'r') as zip_ref:
            zip_ref.extractall()
        os.remove("/Volumes/EFI/EFI/BOOT/BOOTIA32.efi")
        shutil.copy2("IA32/EFI/BOOT/BOOTIA32.efi", "/Volumes/EFI/EFI/BOOT/BOOTIA32.efi")
    if os.path.exists("/Volumes/EFI/EFI/OC/Drivers/OpenRuntime.efi"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest").read()
        json_data = json.loads(url_data)
        versionopencore = json_data["tag_name"]
        print("updating OpenRuntime.efi to " + versionopencore +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'OpenRuntime.zip')
        with zipfile.ZipFile('OpenRuntime.zip', 'r') as zip_ref:
            zip_ref.extractall()
        os.remove("/Volumes/EFI/EFI/OC/Drivers/OpenRuntime.efi")
        shutil.copy2("X64/EFI/OC/Drivers/OpenRuntime.efi", "/Volumes/EFI/EFI/OC/Drivers/OpenRuntime.efi")
    if os.path.exists("/Volumes/EFI/EFI/OC/Drivers/OpenCanopy.efi"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest").read()
        json_data = json.loads(url_data)
        versionopencore = json_data["tag_name"]
        print("updating OpenCanopy.efi to " + versionopencore +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'OpenCanopy.zip')
        with zipfile.ZipFile('OpenCanopy.zip', 'r') as zip_ref:
            zip_ref.extractall()
        os.remove("/Volumes/EFI/EFI/OC/Drivers/OpenCanopy.efi")
        shutil.copy2("X64/EFI/OC/Drivers/OpenCanopy.efi", "/Volumes/EFI/EFI/OC/Drivers/OpenCanopy.efi")
    if os.path.exists("/Volumes/EFI/EFI/OC/Drivers/OpenUsbKbDxe.efi"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest").read()
        json_data = json.loads(url_data)
        versionopencore = json_data["tag_name"]
        print("updating OpenUsbKbDxe.efi to " + versionopencore +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'OpenUsbKbDxe.zip')
        with zipfile.ZipFile('OpenUsbKbDxe.zip', 'r') as zip_ref:
            zip_ref.extractall()
        os.remove("/Volumes/EFI/EFI/OC/Drivers/OpenUsbKbDxe.efi")
        shutil.copy2("X64/EFI/OC/Drivers/OpenUsbKbDxe.efi", "/Volumes/EFI/EFI/OC/Drivers/OpenUsbKbDxe.efi")
    if os.path.exists("/Volumes/EFI/EFI/OC/Drivers/HfsPlusLegacy.efi"):
        url = 'https://github.com/acidanthera/OcBinaryData/raw/master/Drivers/HfsPlusLegacy.efi'
        urllib.request.urlretrieve(url, 'HfsPlusLegacy.efi')
        print("Updating HfsPlusLegacy to version " + versionopencore)
        os.remove("/Volumes/EFI/EFI/OC/Drivers/HfsPlusLegacy.efi")
        shutil.copy2("HfsPlusLegacy.efi", "/Volumes/EFI/EFI/OC/Drivers/HfsPlusLegacy.efi")
    if os.path.exists("/Volumes/EFI/EFI/OC/Drivers/HfsPlus32.efi"):
        url = 'https://github.com/acidanthera/OcBinaryData/raw/master/Drivers/HfsPlus32.efi'
        urllib.request.urlretrieve(url, 'HfsPlus32.efi')
        print("Updating HfsPlus32 to version " + versionopencore)
        os.remove("/Volumes/EFI/EFI/OC/Drivers/HfsPlus32.efi")
        shutil.copy2("HfsPlus32.efi", "/Volumes/EFI/EFI/OC/Drivers/HfsPlus32.efi")
    if os.path.exists("/Volumes/EFI/EFI/OC/Drivers/HfsPlus.efi"):
        url = 'https://github.com/acidanthera/OcBinaryData/raw/master/Drivers/HfsPlus.efi'
        urllib.request.urlretrieve(url, 'HfsPlus.efi')
        print("Updating HfsPlus.efi to version " + versionopencore)
        os.remove("/Volumes/EFI/EFI/OC/Drivers/HfsPlus.efi")
        shutil.copy2("HfsPlus.efi", "/Volumes/EFI/EFI/OC/Drivers/HfsPlus.efi")
    if os.path.exists("/Volumes/EFI/EFI/OC/Drivers/OpenPartitionDxe.efi"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest").read()
        json_data = json.loads(url_data)
        versionopencore = json_data["tag_name"]
        print("updating OpenPartitionDxe.efi to " + versionopencore +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'OpenPartitionDxe.zip')
        with zipfile.ZipFile('OpenPartitionDxe.zip', 'r') as zip_ref:
            zip_ref.extractall()
        os.remove("/Volumes/EFI/EFI/OC/Drivers/OpenPartitionDxe.efi")
        shutil.copy2("X64/EFI/OC/Drivers/OpenPartitionDxe.efi", "/Volumes/EFI/EFI/OC/Drivers/OpenPartitionDxe.efi")
    os.chdir("..")
    if os.path.exists("downloadtemp"):
          shutil.rmtree(pathdownload)
          print("The driver downloads have been deleted... have a nice day!")
    else:
          print("The driver downloads have been deleted... have a nice day!")
    time.sleep(2)
    mainMenu()
def kextsupdate():
    if os.path.exists(pathdownload):
        shutil.rmtree(pathdownload)
        os.mkdir(pathdownload)
        os.chdir("downloadtemp")
    else:
        os.mkdir(pathdownload)
        os.chdir("downloadtemp")
    if os.path.exists('/Volumes/EFI'):
        print ("You mounted your EFI! the script will continue.")
    else: 
        print ("You didn't mount your EFI, the script will now automatically mount your EFI....")
        time.sleep(3)
        try:
            print("Mounting EFI....")
            subprocess.call(r"sudo diskutil mount $(nvram 4D1FDA02-38C7-4A6A-9CC6-4BCCA8B30102:boot-path | sed 's/.*GPT,\([^,]*\),.*/\1/')", shell=True)
            if os.path.exists("/Volumes/EFI"):
                print("well done! your EFI is mounted, continuing...")
        except:
            print("The script couldn't  mount your EFI, falling back to mountEFI")
            time.sleep(3)
            url2 = 'https://github.com/corpnewt/MountEFI/archive/update.zip'
            urllib.request.urlretrieve(url2, 'MountEFI.zip')
            with zipfile.ZipFile('MountEFI.zip', 'r') as zip_ref:
                zip_ref.extractall()
            print("opening MountEFI, the awesome tool from CorpNewt....")
            b = 'MountEFI-update/MountEFI.command'
            subprocess.call(["chmod" ,"+x", b])
            subprocess.Popen(['open', '-a', 'Terminal.app', b])
            time.sleep(15)
            subprocess.call("kill $(ps aux | grep '[M]ountEFI' | awk '{print $2}')", shell=True)
            if os.path.exists("/Volumes/EFI"):
                print("well done! your EFI is mounted, continuing...")
            else: 
                print("Mount your EFI and come back.....")
                time.sleep(3)
                mainMenu()
    os.chmod("/Volumes/EFI/EFI/OC", stat.S_IRWXO)
    os.chmod("/Volumes/EFI/EFI", stat.S_IRWXO)
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VirtualSMC.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/VirtualSMC/releases/latest").read()
        json_data = json.loads(url_data)
        versionvirtualsmc = json_data["tag_name"]
        print("updating VirtualSMC to " + versionvirtualsmc +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'Virtualsmc.zip')
        with zipfile.ZipFile('Virtualsmc.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VirtualSMC.kext", ignore_errors=True)
        shutil.copytree("Kexts/VirtualSMC.kext", "/Volumes/EFI/EFI/OC/Kexts/VirtualSMC.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCBatteryManager.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCBatteryManager.kext", ignore_errors=True)
        shutil.copytree("Kexts/SMCBatteryManager.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCBatteryManager.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCDellSensors.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCDellSensors.kext", ignore_errors=True)
        shutil.copytree("Kexts/SMCDellSensors.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCDellSensors.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCLightSensor.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCLightSensor.kext", ignore_errors=True)
        shutil.copytree("Kexts/SMCLightsensor.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCLightSensor.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCProcessor.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCProcessor.kext", ignore_errors=True)
        shutil.copytree("Kexts/SMCProcessor.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCProcessor.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCSuperIO.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCSuperIO.kext", ignore_errors=True)
        shutil.copytree("Kexts/SMCSuperIO.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCSuperIO.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/Lilu.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/Lilu/releases/latest").read()
        json_data = json.loads(url_data)
        versionlilu = json_data["tag_name"]
        print("updating Lilu to " + versionlilu +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'Lilu.zip')
        with zipfile.ZipFile('Lilu.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/Lilu.kext", ignore_errors=True)
        shutil.copytree("Lilu.kext", "/Volumes/EFI/EFI/OC/Kexts/Lilu.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/CPUFriend.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/CPUFriend/releases/latest").read()
        json_data = json.loads(url_data)
        versioncpufriend = json_data["tag_name"]
        print("updating CPUFriend to " + versioncpufriend +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        urlcpufriend = asset["browser_download_url"]
        urllib.request.urlretrieve(urlcpufriend, 'CPUFriend.zip')
        with zipfile.ZipFile('CPUFriend.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/CPUFriend.kext", ignore_errors=True)
        shutil.copytree("CPUFriend.kext", "/Volumes/EFI/EFI/OC/Kexts/CPUFriend.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/WhateverGreen.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/Whatevergreen/releases/latest").read()
        json_data = json.loads(url_data)
        versionwhatever = json_data["tag_name"]
        print("updating WhateverGreen to " + versionwhatever +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'WhateverGreen.zip')
        with zipfile.ZipFile('WhateverGreen.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/WhateverGreen.kext", ignore_errors=True)
        shutil.copytree("WhateverGreen.kext", "/Volumes/EFI/EFI/OC/Kexts/WhateverGreen.kext")  
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/Polaris22Fixup.kext"):
        url_data = urlopen("https://api.github.com/repos/osy/Polaris22Fixup/releases/latest").read()
        json_data = json.loads(url_data)
        versionpolaris22 = json_data["tag_name"]
        print("updating Polaris22Fixup to " + versionpolaris22 +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'Polaris22Fixup.zip')
        with zipfile.ZipFile('Polaris22Fixup.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/Polaris22Fixup.kext", ignore_errors=True)
        shutil.copytree("Polaris22Fixup.kext", "/Volumes/EFI/EFI/OC/Kexts/Polaris22Fixup.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AppleALC.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/AppleALC/releases/latest").read()
        json_data = json.loads(url_data)
        versionapplealc = json_data["tag_name"]
        print("updating AppleALC to " + versionapplealc +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'AppleALC.zip')
        with zipfile.ZipFile('AppleALC.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AppleALC.kext", ignore_errors=True)
        shutil.copytree("AppleALC.kext", "/Volumes/EFI/EFI/OC/Kexts/AppleALC.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/IntelMausi.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/IntelMausi/releases/latest").read()
        json_data = json.loads(url_data)
        versionintelmausi = json_data["tag_name"]
        print("updating IntelMausi to " + versionintelmausi +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'IntelMausi.zip')
        with zipfile.ZipFile('IntelMausi.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/IntelMausi.kext", ignore_errors=True)
        shutil.copytree("IntelMausi.kext", "/Volumes/EFI/EFI/OC/Kexts/IntelMausi.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SmallTreeIntel82576.kext"):
        url_data = urlopen("https://api.github.com/repos/khronokernel/SmallTree-I211-AT-patch/releases/latest").read()
        json_data = json.loads(url_data)
        versionsmalltreei211 = json_data["tag_name"]
        print("updating SmallTreeIntel to " + versionsmalltreei211 +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'SmallTreeIntel82576.zip')
        with zipfile.ZipFile('SmallTreeIntel82576.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SmallTreeIntel82576.kext", ignore_errors=True)
        shutil.copytree("SmallTreeIntel82576.kext", "/Volumes/EFI/EFI/OC/Kexts/SmallTreeIntel82576.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AtherosE2200Ethernet.kext"):
        url_data = urlopen("https://api.github.com/repos/Mieze/AtherosE2200Ethernet/releases/latest").read()
        json_data = json.loads(url_data)
        versionatherose2200 = json_data["tag_name"]
        print("updating AtherosE2200Ethernet to " + versionatherose2200 +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'AtherosE2200Ethernet.zip')
        with zipfile.ZipFile('AtherosE2200Ethernet.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AtherosE2200Ethernet.kext", ignore_errors=True)
        shutil.copytree("AtherosE2200Ethernet-V2.2.2/Release/AtherosE2200Ethernet.kext", "/Volumes/EFI/EFI/OC/Kexts/AtherosE2200Ethernet.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8111.kext"):
        url_data = urlopen("https://api.github.com/repos/Mieze/RTL8111_driver_for_OS_X/releases/latest").read()
        json_data = json.loads(url_data)
        versionrtl8111 = json_data["tag_name"]
        print("updating RealtekRTL8111 to " + versionrtl8111 +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'RealtekRTL8111.zip')
        with zipfile.ZipFile('RealtekRTL8111.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8111.kext", ignore_errors=True)
        shutil.copytree("RealtekRTL8111-V2.4.0/Release/RealtekRTL8111.kext", "/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8111.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/LucyRTL8125Ethernet.kext"):
        url = 'https://www.insanelymac.com/forum/files/file/1004-lucyrtl8125ethernet/?do=download&csrfKey=9da7156f1e6ce2d23fee67731e9fc70b'
        urllib.request.urlretrieve(url, 'LucyRTL8125Ethernet.zip')
        print("Updating LucyRTL8125Ethernet to the newest version.....")
        with zipfile.ZipFile('LucyRTL8125Ethernet.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/LucyRTL8125Ethernet.kext", ignore_errors=True)
        shutil.copytree("Release/LucyRTL8125Ethernet.kext", "/Volumes/EFI/EFI/OC/Kexts/LucyRTL8125Ethernet.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8100.kext"):
        url = 'https://www.insanelymac.com/forum/files/file/259-realtekrtl8100-binary/?do=download&csrfKey=9da7156f1e6ce2d23fee67731e9fc70b'
        urllib.request.urlretrieve(url, 'RealtekRTL8100.zip')
        print("Updating RealtekRTL8100 to the newest version.....")
        with zipfile.ZipFile('RealtekRTL8100.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8100.kext", ignore_errors=True)
        shutil.copytree("Release/RealtekRTL8100.kext", "/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8100.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/itlwm.kext"):
        url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
        json_data = json.loads(url_data)
        versionitlwm = json_data["tag_name"]
        print("updating Itlwm to " + versionitlwm +".....")
        for asset in json_data["assets"]:
            if "itlwm" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'itlwm.zip')
        with zipfile.ZipFile('itlwm.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/itlwm.kext", ignore_errors=True)
        shutil.copytree("itlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/itlwm.kext")
    v, _, _ = platform.mac_ver()
    v = float('.'.join(v.split('.')[:2]))
    if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 11.2)):
        url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
        json_data = json.loads(url_data)
        versionitlwm = json_data["tag_name"]
        print("updating AirportItlwm to " + versionitlwm +".....")
        for asset in json_data["assets"]:
            if "BigSur" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'AirportItlwm.zip')
        with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
        shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
    if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 11.1)):
        url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
        json_data = json.loads(url_data)
        versionitlwm = json_data["tag_name"]
        print("updating AirportItlwm to " + versionitlwm +".....")
        for asset in json_data["assets"]:
            if "BigSur" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'AirportItlwm.zip')
        with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
        shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
    if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 11.0)):
        url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
        json_data = json.loads(url_data)
        versionitlwm = json_data["tag_name"]
        print("updating AirportItlwm to " + versionitlwm +".....")
        for asset in json_data["assets"]:
            if "BigSur" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'AirportItlwm.zip')
        with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
        shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
    if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.16)):
        url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
        json_data = json.loads(url_data)
        versionitlwm = json_data["tag_name"]
        print("updating AirportItlwm to " + versionitlwm +".....")
        for asset in json_data["assets"]:
            if "BigSur" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'AirportItlwm.zip')
        with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
        shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
    if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.15)):
        url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
        json_data = json.loads(url_data)
        versionitlwm = json_data["tag_name"]
        print("updating AirportItlwm to " + versionitlwm +".....")
        for asset in json_data["assets"]:
            if "Catalina" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'AirportItlwm.zip')
        with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
        shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
    if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.14)):
        url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
        json_data = json.loads(url_data)
        versionitlwm = json_data["tag_name"]
        print("updating AirportItlwm to " + versionitlwm +".....")
        for asset in json_data["assets"]:
            if "Mojave" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'AirportItlwm.zip')
        with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
        shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
    if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.13)):
        url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
        json_data = json.loads(url_data)
        versionitlwm = json_data["tag_name"]
        print("updating AirportItlwm to " + versionitlwm +".....")
        for asset in json_data["assets"]:
            if "HighSierra" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'AirportItlwm.zip')
        with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
        shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothFirmware.kext"):
        url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/intelbluetoothfirmware/releases/latest").read()
        json_data = json.loads(url_data)
        versionintelbluetoothfirmware = json_data["tag_name"]
        print("updating AirportItlwm to " + versionintelbluetoothfirmware +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'IntelBluetoothFirmware.zip')
        with zipfile.ZipFile('IntelBluetoothFirmware.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothFirmware.kext", ignore_errors=True)
        shutil.copytree("IntelBluetoothFirmware.kext", "/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothFirmware.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothInjector.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothInjector.kext", ignore_errors=True)
        shutil.copytree("IntelBluetoothInjector.kext", "/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothInjector.kext")
        print("updated IntelBluetoothInjector to version " + versionintelbluetoothfirmware +"......")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AirportBrcmFixup.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/AirportBrcmFixup/releases/latest").read()
        json_data = json.loads(url_data)
        versionairportbrcmfixup = json_data["tag_name"]
        print("updating AirportBrcmFixup to " + versionairportbrcmfixup +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'AirportBrcmFixup.zip')
        with zipfile.ZipFile('AirportBrcmFixup.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportBrcmFixup.kext", ignore_errors=True)
        shutil.copytree("AirportBrcmFixup.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportBrcmFixup.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjector.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
        json_data = json.loads(url_data)
        versionbrcmpatchram = json_data["tag_name"]
        print("updating BrcmPatchRAM to " + versionbrcmpatchram +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'BrcmBluetoothInjector.zip')
        with zipfile.ZipFile('BrcmBluetoothInjector.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjector.kext", ignore_errors=True)
        shutil.copytree("BrcmBluetoothInjector.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjector.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjectorLegacy.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
        json_data = json.loads(url_data)
        versionbrcmpatchram = json_data["tag_name"]
        print("updating BrcmBluetoothInjectorlegacy to " + versionbrcmpatchram +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'BrcmBluetoothInjectorlegacy.zip')
        with zipfile.ZipFile('BrcmBluetoothInjectorLegacy.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjectorLegacy.kext", ignore_errors=True)
        shutil.copytree("BrcmBluetoothInjectorLegacy.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjectorLegacy.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareData.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
        json_data = json.loads(url_data)
        versionbrcmpatchram = json_data["tag_name"]
        print("updating BrcmFirmwareData to " + versionbrcmpatchram +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'BrcmFirmwareData.zip')
        with zipfile.ZipFile('BrcmFirmwareData.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareData.kext", ignore_errors=True)
        shutil.copytree("BrcmFirmwareData.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareData.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareRepo.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
        json_data = json.loads(url_data)
        versionbrcmpatchram = json_data["tag_name"]
        print("updating BrcmFirmwareRepo to " + versionbrcmpatchram +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'BrcmFirmwareRepo.zip')
        with zipfile.ZipFile('BrcmFirmwareRepo.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareRepo.kext", ignore_errors=True)
        shutil.copytree("BrcmFirmwareRepo.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareRepo.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
        json_data = json.loads(url_data)
        versionbrcmpatchram = json_data["tag_name"]
        print("updating BrcmNonPatchRAM to " + versionbrcmpatchram +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'BrcmNonPatchRAM.zip')
        with zipfile.ZipFile('BrcmNonPatchRAM.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM.kext", ignore_errors=True)
        shutil.copytree("BrcmNonPatchRAM.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM2.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
        json_data = json.loads(url_data)
        versionbrcmpatchram = json_data["tag_name"]
        print("updating BrcmNonPatchRAM2 to " + versionbrcmpatchram +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'BrcmNonPatchRAM2.zip')
        with zipfile.ZipFile('BrcmNonPatchRAM2.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM2.kext", ignore_errors=True)
        shutil.copytree("BrcmNonPatchRAM2.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM2.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM2.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
        json_data = json.loads(url_data)
        versionbrcmpatchram = json_data["tag_name"]
        print("updating BrcmPatchRAM2 to " + versionbrcmpatchram +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'BrcmPatchRAM2.zip')
        with zipfile.ZipFile('BrcmPatchRAM2.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM2.kext", ignore_errors=True)
        shutil.copytree("BrcmPatchRAM2.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM2.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM3.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
        json_data = json.loads(url_data)
        versionbrcmpatchram = json_data["tag_name"]
        print("updating BrcmPatchRAM3 to " + versionbrcmpatchram +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'BrcmPatchRAM3.zip')
        with zipfile.ZipFile('BrcmPatchRAM3.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM3.kext", ignore_errors=True)
        shutil.copytree("BrcmPatchRAM3.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM3.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/XLNCUSBFix.kext"):
        url = 'https://cdn.discordapp.com/attachments/566705665616117760/566728101292408877/XLNCUSBFix.kext.zip'
        urllib.request.urlretrieve(url, 'XLNCUSBFix.zip')
        print("Updating XLNCUSBFix to the newest version.....")
        with zipfile.ZipFile('XLNCUSBFix.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/XLNCUSBFix.kext", ignore_errors=True)
        shutil.copytree("XLNCUSBFix.kext", "/Volumes/EFI/EFI/OC/Kexts/XLNCUSBFix.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooHDA.kext"):
        url = 'https://sourceforge.net/projects/voodoohda/files/VoodooHDA.kext-296.zip/download'
        urllib.request.urlretrieve(url, 'VoodooHDA.zip')
        time.sleep(6)
        with zipfile.ZipFile('VoodooHDA.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooHDA.kext", ignore_errors=True)
        shutil.copytree("VoodooHDA.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooHDA.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/CpuTscSync.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/CpuTscSync/releases/latest").read()
        json_data = json.loads(url_data)
        versioncputscsync = json_data["tag_name"]
        print("updating CpuTscSync to " + versioncputscsync +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'CpuTscSync.zip')
        with zipfile.ZipFile('CpuTscSync.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/CpuTscSync.kext", ignore_errors=True)
        shutil.copytree("CpuTscSync.kext", "/Volumes/EFI/EFI/OC/Kexts/CpuTscSync.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/NVMeFix.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/NVMeFix/releases/latest").read()
        json_data = json.loads(url_data)
        versionnvmefix = json_data["tag_name"]
        print("updating NVMeFix to " + versionnvmefix +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'NVMeFix.zip')
        with zipfile.ZipFile('NVMeFix.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/NVMeFix.kext", ignore_errors=True)
        shutil.copytree("NVMeFix.kext", "/Volumes/EFI/EFI/OC/Kexts/NVMeFix.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/HibernationFixup.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/HibernationFixup/releases/latest").read()
        json_data = json.loads(url_data)
        versiohibernation = json_data["tag_name"]
        print("updating HibernationFixup to " + versiohibernation +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'HibernationFixup.zip')
        with zipfile.ZipFile('HibernationFixup.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/HibernationFixup.kext", ignore_errors=True)
        shutil.copytree("HibernationFixup.kext", "/Volumes/EFI/EFI/OC/Kexts/HibernationFixup.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/NightShiftEnabler.kext"):
        url_data = urlopen("https://api.github.com/repos/cdf/NightShiftEnabler/releases/latest").read()
        json_data = json.loads(url_data)
        versionnightshift = json_data["tag_name"]
        print("updating NVMeFix to " + versionnightshift +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'NightShiftEnabler.zip')
        with zipfile.ZipFile('NightShiftEnabler.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/NightShiftEnabler.kext", ignore_errors=True)
        shutil.copytree("NightShiftEnabler.kext", "/Volumes/EFI/EFI/OC/Kexts/NightShiftEnabler.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/Innie.kext"):
        url_data = urlopen("https://api.github.com/repos/cdf/Innie/releases/latest").read()
        json_data = json.loads(url_data)
        versioninnie = json_data["tag_name"]
        print("updating Innie to " + versioninnie +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'Innie.zip')
        with zipfile.ZipFile('Innie.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/Innie.kext", ignore_errors=True)
        shutil.copytree("Innie.kext", "/Volumes/EFI/EFI/OC/Kexts/Innie.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SATA-unsupported.kext"):
        url = 'https://github.com/khronokernel/Legacy-Kexts/blob/master/Injectors/Zip/SATA-unsupported.kext.zip?raw=true'
        urllib.request.urlretrieve(url, 'SATA-unsupported.zip')
        print("Updating SATA-Unsupported.......")
        with zipfile.ZipFile('SATA-unsupported.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SATA-unsupported.kext", ignore_errors=True)
        shutil.copytree("SATA-unsupported.kext", "/Volumes/EFI/EFI/OC/Kexts/SATA-unsupported.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AHCIPortInjector.kext"):
        url = 'https://github.com/khronokernel/Legacy-Kexts/blob/master/Injectors/Zip/AHCIPortInjector.kext.zip?raw=true'
        urllib.request.urlretrieve(url, 'AHCIPortInjector.zip')
        print("Updating AHCIPortInjector.....")
        with zipfile.ZipFile('AHCIPortInjector.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AHCIPortInjector.kext", ignore_errors=True)
        shutil.copytree("AHCIPortInjector.kext", "/Volumes/EFI/EFI/OC/Kexts/AHCIPortInjector.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/ATAPortInjector.kext"):
        url = 'https://github.com/khronokernel/Legacy-Kexts/blob/master/Injectors/Zip/ATAPortInjector.kext.zip?raw=true'
        urllib.request.urlretrieve(url, 'ATAPortInjector.zip')
        print("Updating ATAPortInjector to newest version....")
        with zipfile.ZipFile('ATAPortInjector.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/ATAPortInjector.kext", ignore_errors=True)
        shutil.copytree("ATAPortInjector.kext", "/Volumes/EFI/EFI/OC/Kexts/ATAPortInjector.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/VoodooPS2/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodoops2 = json_data["tag_name"]
        print("updating VoodooPS2Controller to " + versionvoodoops2 +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'VoodooPS2Controller.zip')
        with zipfile.ZipFile('VoodooPS2Controller.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext", ignore_errors=True)
        shutil.copytree("VoodooPS2Controller.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooInput.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/Voodooinput/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodooinput = json_data["tag_name"]
        print("updating VoodooInput to " + versionvoodooinput +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'VoodooInput.zip')
        with zipfile.ZipFile('VoodooInput.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooInput.kext", ignore_errors=True)
        shutil.copytree("VoodooInput.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooInput.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooRMI.kext"):
        url_data = urlopen("https://api.github.com/repos/VoodooSmbus/VoodooRMI/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodoormi = json_data["tag_name"]
        print("updating VoodooRMI to " + versionvoodoormi +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'VoodooRMI.zip')
        with zipfile.ZipFile('VoodooRMI.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooRMI.kext", ignore_errors=True)
        shutil.copytree("VoodooRMI.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooRMI.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AMDRyzenCPUPowerManagement.kext"):
        url_data = urlopen("https://api.github.com/repos/trulyspinach/SMCAMDProcessor/releases/latest").read()
        json_data = json.loads(url_data)
        versionAMDRyzenCPUPowerManagement = json_data["tag_name"]
        print("updating AMDRyzenCPUPowerManagement to " + versionAMDRyzenCPUPowerManagement +".....")
        for asset in json_data["assets"]:
            if ".kext" not in asset["browser_download_url"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'AMDRyzenCPUPowerManagement.zip')
        with zipfile.ZipFile('AMDRyzenCPUPowerManagement.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AMDRyzenCPUPowerManagement.kext", ignore_errors=True)
        shutil.copytree("AMDRyzenCPUPowerManagement.kext", "/Volumes/EFI/EFI/OC/Kexts/AMDRyzenCPUPowerManagement.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AlpsT4USB.kext"):
        url = 'https://github.com/blankmac/AlpsT4USB/files/5933051/AlpsT4USB.zip'
        urllib.request.urlretrieve(url, 'AlpsT4USB.zip')
        print("Updating AlpsT4USB to the newest version....")
        with zipfile.ZipFile('AlpsT4USB.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AlpsT4USB.kext", ignore_errors=True)
        shutil.copytree("Release/AlpsT4USB.kext", "/Volumes/EFI/EFI/OC/Kexts/AlpsT4USB.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooSMBus.kext"):
        url_data = urlopen("https://api.github.com/repos/VoodooSmbus/VoodooSMBus/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodoosmbus = json_data["tag_name"]
        print("updating VoodooSMBus to " + versionvoodoosmbus +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'VoodooSMBus.zip')
        with zipfile.ZipFile('VoodooSMBus.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooSMBus.kext", ignore_errors=True)
        shutil.copytree("VoodooSMBus-v2.2/kext/VoodooSMBus.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooSMBus.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2C.kext"):
        url_data = urlopen("https://api.github.com/repos/VoodooI2C/VoodooI2C/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodooi2c = json_data["tag_name"]
        print("updating VoodooI2C to " + versionvoodooi2c +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'VoodooI2C.zip')
        with zipfile.ZipFile('VoodooI2C.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2C.kext", ignore_errors=True)
        shutil.copytree("VoodooI2C.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2C.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CAtmelMXT.kext"):
        url_data = urlopen("https://api.github.com/repos/VoodooI2C/VoodooI2C/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodooinput = json_data["tag_name"]
        print("updating VoodooI2CAtmelMXT to " + versionvoodooinput +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'VoodooI2CAtmelMXT.zip')
        with zipfile.ZipFile('VoodooI2CAtmelMXT.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CAtmelMXT.kext", ignore_errors=True)
        shutil.copytree("VoodooI2CAtmelMXT.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2CAtmelMXT.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CELAN.kext"):
        url_data = urlopen("https://api.github.com/repos/VoodooI2C/VoodooI2C/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodooinput = json_data["tag_name"]
        print("updating VoodooI2CELAN to " + versionvoodooinput +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'VoodooI2CELAN.zip')
        with zipfile.ZipFile('VoodooI2CELAN.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CELAN.kext", ignore_errors=True)
        shutil.copytree("VoodooI2CELAN.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2CELAN.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CFTE.kext"):
        url_data = urlopen("https://api.github.com/repos/VoodooI2C/VoodooI2C/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodooinput = json_data["tag_name"]
        print("updating VoodooI2CFTE to " + versionvoodooinput +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'VoodooI2CFTE.zip')
        with zipfile.ZipFile('VoodooI2CFTE.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CFTE.kext", ignore_errors=True)
        shutil.copytree("VoodooI2CFTE.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2CFTE.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CHID.kext"):
        url_data = urlopen("https://api.github.com/repos/VoodooI2C/VoodooI2C/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodooinput = json_data["tag_name"]
        print("updating VoodooI2CHID to " + versionvoodooinput +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'VoodooI2CHID.zip')
        with zipfile.ZipFile('VoodooI2CHID.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CHID.kext", ignore_errors=True)
        shutil.copytree("VoodooI2CHID.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2CHID.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CSynaptics.kext"):
        url_data = urlopen("https://api.github.com/repos/VoodooI2C/VoodooI2C/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodooinput = json_data["tag_name"]
        print("updating VoodooI2CSynaptics to " + versionvoodooinput +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'VoodooI2CSynaptics.zip')
        with zipfile.ZipFile('VoodooI2CSynaptics.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CSynaptics.kext", ignore_errors=True)
        shutil.copytree("VoodooI2CSynaptics.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2CSynaptics.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCAMDProcessor.kext"):
        url = 'https://github.com/trulyspinach/SMCAMDProcessor/releases/download/0.6.4/SMCAMDProcessor.kext.zip'
        urllib.request.urlretrieve(url, 'SMCAMDProcessor.zip')
        print("Updating SMCAMDProcessor to the newest version....")
        with zipfile.ZipFile('SMCAMDProcessor.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCAMDProcessor.kext", ignore_errors=True)
        shutil.copytree("SMCAMDProcessor.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCAMDProcessor.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/FakeSMC.kext"):
        url_data = urlopen("https://api.github.com/repos/CloverHackyColor/FakeSMC3_with_plugins/releases/latest").read()
        json_data = json.loads(url_data)
        versionfakesmc = json_data["tag_name"]
        print("updating FakeSMC to release " + versionfakesmc +".....")
        for asset in json_data["assets"]:
            url = asset["browser_download_url"]
            urllib.request.urlretrieve(url, 'FakeSMC.zip')
        with zipfile.ZipFile('FakeSMC.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/FakeSMC.kext", ignore_errors=True)
        shutil.copytree("FakeSMC.kext", "/Volumes/EFI/EFI/OC/Kexts/FakeSMC.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/ACPIMonitor.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/ACPIMonitor.kext", ignore_errors=True)
        shutil.copytree("ACPIMonitor.kext", "/Volumes/EFI/EFI/OC/Kexts/ACPIMonitor.kext")
        print("Updating FakeSMC Plugin ACPIMonitor....")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AmdCPUMonitor.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AmdCPUMonitor.kext", ignore_errors=True)
        shutil.copytree("AmdCPUMonitor.kext", "/Volumes/EFI/EFI/OC/Kexts/AmdCPUMonitor.kext")
        print("Updating FakeSMC Plugin AMDCPUMonitor....")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/F718x.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/F718x.kext", ignore_errors=True)
        shutil.copytree("F718x.kext", "/Volumes/EFI/EFI/OC/Kexts/F718x.kext")
        print("Updating FakeSMC Plugin F718x .....")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/GeforceSensor.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/GeforceSensor.kext", ignore_errors=True)
        shutil.copytree("GeforceSensor.kext", "/Volumes/EFI/EFI/OC/Kexts/GeforceSensor.kext")
        print("Updating FakeSMC Plugin GeforceSensor....")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/IntelCPUMonitor.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/IntelCPUMonitor.kext", ignore_errors=True)
        shutil.copytree("IntelCPUMonitor.kext", "/Volumes/EFI/EFI/OC/Kexts/IntelCPUMonitor.kext")
        print("Updating FakeSMC Plugin IntelCPUMonitor.....")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/IntelMCHMonitor.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/IntelMCHMonitor.kext", ignore_errors=True)
        shutil.copytree("IntelMCHMonitor.kext", "/Volumes/EFI/EFI/OC/Kexts/IntelMCHMonitor.kext")
        print("Updating FakeSMC Plugin IntelMCHMonitor.....")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/ITEIT87x.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/ITEIT87x.kext", ignore_errors=True)
        shutil.copytree("ITEIT87x.kext", "/Volumes/EFI/EFI/OC/Kexts/ITEIT87x.kext")
        print("Updating other FakeSMC plugins.....")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/NVClockX.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/NVClockX.kext", ignore_errors=True)
        shutil.copytree("NVClockX.kext", "/Volumes/EFI/EFI/OC/Kexts/NVClockX.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/RadeonMonitor.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/RadeonMonitor.kext", ignore_errors=True)
        shutil.copytree("RadeonMonitor.kext", "/Volumes/EFI/EFI/OC/Kexts/RadeonMonitor.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMIMonitor.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMIMonitor.kext", ignore_errors=True)
        shutil.copytree("SMIMonitor.kext", "/Volumes/EFI/EFI/OC/Kexts/SMIMonitor.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooBatterySMC.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooBatterySMC.kext", ignore_errors=True)
        shutil.copytree("VoodooBatterySMC.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooBatterySMC.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/W836x.kext"):
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/W836x.kext", ignore_errors=True)
        shutil.copytree("W836x.kext", "/Volumes/EFI/EFI/OC/Kexts/W836x.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AtherosL1cEthernet.kext"):
        url = 'https://www.insanelymac.com/applications/core/interface/file/attachment.php?id=115905'
        urllib.request.urlretrieve(url, 'AtherosL1cEthernet.zip')
        print("Updating AtherosL1cEthernet.....")
        with zipfile.ZipFile('AtherosL1cEthernet.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AtherosL1cEthernet.kext", ignore_errors=True)
        shutil.copytree("AtherosL1cEthernet.kext", "/Volumes/EFI/EFI/OC/Kexts/AtherosL1cEthernet.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AirPortAtheros40.kext"):
        url = 'https://i.applelife.ru/2018/12/442854_AirPortAtheros40.kext.zip'
        urllib.request.urlretrieve(url, 'AirPortAtheros40.zip')
        print("Updating AirPortAtheros40......")
        with zipfile.ZipFile('AirPortAtheros40.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirPortAtheros40.kext", ignore_errors=True)
        shutil.copytree("AirPortAtheros40.kext", "/Volumes/EFI/EFI/OC/Kexts/AirPortAtheros40.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/VoodooPS2/releases/latest").read()
        json_data = json.loads(url_data)
        versionvoodoops2 = json_data["tag_name"]
        print("updating VoodooPS2Controller to " + versionvoodoops2 +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'VoodooPS2Controller.zip')
        with zipfile.ZipFile('VoodooPS2Controller.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext", ignore_errors=True)
        shutil.copytree("VoodooPS2Controller.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext")
    if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrightnessKeys.kext"):
        url_data = urlopen("https://api.github.com/repos/acidanthera/BrightnessKeys/releases/latest").read()
        json_data = json.loads(url_data)
        versionbrightnesskeys = json_data["tag_name"]
        print("updating BrightnessKeys to " + versionbrightnesskeys +".....")
        for asset in json_data["assets"]:
            if "RELEASE" not in asset["name"]:
                continue
        url = asset["browser_download_url"]
        urllib.request.urlretrieve(url, 'BrightnessKeys.zip')
        with zipfile.ZipFile('BrightnessKeys.zip', 'r') as zip_ref:
            zip_ref.extractall()
        shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrightnessKeys.kext", ignore_errors=True)
        shutil.copytree("BrightnessKeys.kext", "/Volumes/EFI/EFI/OC/Kexts/BrightnessKeys.kext")
    os.chdir("..")
    if os.path.exists("downloadtemp"):
          shutil.rmtree(pathdownload)
          print("The kext downloads have been deleted... have a nice day!")
    else:
          print("The kext downloads have been deleted... have a nice day!")
    time.sleep(2)
    mainMenu()        
def mainMenu():
    print("1. Update everything")
    print("2. Update only Kexts")
    print("3. Update only OpenCore drivers")
    print("4. Only Mount EFI")
    print("5. Quit")
    selection = int(input("Choose the option you want: "))
    if selection == 1:
        print("Updating everything")
        time.sleep(1)
        everything()
    elif selection == 2:
        print("Updating Kexts")
        kextsupdate()
    elif selection == 3:
        print("Updating OpenCore Drivers")
        updatedrivers()
    elif selection == 4:
        print("Mounting EFI..")
        efimounting()
    elif selection == 5:
        print("Quiting....")
        os.chdir("..")
        if os.path.exists("downloadtemp"):
            shutil.rmtree(pathdownload)
        quit()
mainMenu()
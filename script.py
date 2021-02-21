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
os.chmod("/Volumes/EFI/EFI", stat.S_IRWXO)
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VirtualSMC.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/VirtualSMC/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'Virtualsmc.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('Virtualsmc.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VirtualSMC.kext", ignore_errors=True)
    shutil.copytree("Kexts/VirtualSMC.kext", "/Volumes/EFI/EFI/OC/Kexts/VirtualSMC.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCBatteryManager.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCBatteryManager.kext", ignore_errors=True)
    shutil.copytree("Kexts/SMCBatteryManager.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCBatteryManager.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCDellSensors.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCDellSensors.kext", ignore_errors=True)
    shutil.copytree("Kexts/SMCDellSensors.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCDellSensors.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCLightSensor.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCLightSensor.kext", ignore_errors=True)
    shutil.copytree("Kexts/SMCLightsensor.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCLightSensor.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCProcessor.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCProcessor.kext", ignore_errors=True)
    shutil.copytree("Kexts/SMCProcessor.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCProcessor.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMCSuperIO.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMCSuperIO.kext", ignore_errors=True)
    shutil.copytree("Kexts/SMCSuperIO.kext", "/Volumes/EFI/EFI/OC/Kexts/SMCSuperIO.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/Lilu.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/Lilu/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'Lilu.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('Lilu.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/Lilu.kext", ignore_errors=True)
    shutil.copytree("Lilu.kext", "/Volumes/EFI/EFI/OC/Kexts/Lilu.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/WhateverGreen.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/Whatevergreen/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'WhateverGreen.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('WhateverGreen.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/WhateverGreen.kext", ignore_errors=True)
    shutil.copytree("WhateverGreen.kext", "/Volumes/EFI/EFI/OC/Kexts/WhateverGreen.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/CPUFriend.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/CPUFriend/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'CPUFriend.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('CPUFriend.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/CPUFriend.kext", ignore_errors=True)
    shutil.copytree("CPUFriend.kext", "/Volumes/EFI/EFI/OC/Kexts/CPUFriend.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/Polaris22Fixup.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/osy/Polaris22Fixup/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'Polaris22Fixup.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('Polaris22Fixup.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/Polaris22Fixup.kext", ignore_errors=True)
    shutil.copytree("Polaris22Fixup.kext", "/Volumes/EFI/EFI/OC/Kexts/Polaris22Fixup.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AppleALC.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/AppleALC/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AppleALC.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AppleALC.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AppleALC.kext", ignore_errors=True)
    shutil.copytree("AppleALC.kext", "/Volumes/EFI/EFI/OC/Kexts/AppleALC.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/IntelMausi.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/IntelMausi/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'IntelMausi.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('IntelMausi.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/IntelMausi.kext", ignore_errors=True)
    shutil.copytree("IntelMausi.kext", "/Volumes/EFI/EFI/OC/Kexts/IntelMausi.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SmallTreeIntel82576.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/khronokernel/SmallTree-I211-AT-patch/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'SmallTreeIntel82576.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('SmallTreeIntel82576.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SmallTreeIntel82576.kext", ignore_errors=True)
    shutil.copytree("SmallTreeIntel82576.kext", "/Volumes/EFI/EFI/OC/Kexts/SmallTreeIntel82576.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AtherosE2200Ethernet.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/Mieze/AtherosE2200Ethernet/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AtherosE2200Ethernet.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AtherosE2200Ethernet.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AtherosE2200Ethernet.kext", ignore_errors=True)
    shutil.copytree("Release/AtherosE2200Ethernet.kext", "/Volumes/EFI/EFI/OC/Kexts/AtherosE2200Ethernet.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8111.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/Mieze/RTL8111_driver_for_OS_X/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'RealtekRTL8111.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('RealtekRTL8111.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8111.kext", ignore_errors=True)
    shutil.copytree("RealtekRTL8111-V2.4.0/Release/RealtekRTL8111.kext", "/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8111.kext")
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
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/LucyRTL8125Ethernet.kext", ignore_errors=True)
    shutil.copytree("Release/LucyRTL8125Ethernet.kext", "/Volumes/EFI/EFI/OC/Kexts/LucyRTL8125Ethernet.kext")
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
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8100.kext", ignore_errors=True)
    shutil.copytree("Release/RealtekRTL8100.kext", "/Volumes/EFI/EFI/OC/Kexts/RealtekRTL8100.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/itlwm.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "itlwm" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'itlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('itlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/itlwm.kext", ignore_errors=True)
    shutil.copytree("itlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/itlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 11.2)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "BigSur" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 11.1)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "BigSur" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 11.0)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "BigSur" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.15.7)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "Catalina" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.15.6)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "Catalina" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.15.5)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "Catalina" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.15.4)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "Catalina" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.15.3)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "Catalina" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.15.2)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "Catalina" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.15.1)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "Catalina" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.15.0)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "Catalina" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.14.6)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "Mojave" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.14.5)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "Mojave" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.14.4)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "Mojave" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.14.3)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "Mojave" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.14.2)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "Mojave" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.14.1)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "Mojave" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.14.0)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "Mojave" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.13.6)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "HighSierra" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.13.5)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "HighSierra" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.13.4)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "HighSierra" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.13.3)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "HighSierra" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.13.2)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "HighSierra" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.13.1)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "HighSierra" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, platform, time
v, _, _ = platform.mac_ver()
v = float('.'.join(v.split('.')[:2]))
print (v)
if (os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AiportItlwm.kext") and (v == 10.13.0)):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/itlwm/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "HighSierra" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportItlwm.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportItlwm.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext", ignore_errors=True)
    shutil.copytree("AirportItlwm.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportItlwm.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothFirmware.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/OpenIntelWireless/intelbluetoothfirmware/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'IntelBluetoothFirmware.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('IntelBluetoothFirmware.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothFirmware.kext", ignore_errors=True)
    shutil.copytree("IntelBluetoothFirmware.kext", "/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothFirmware.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothInjector.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothInjector.kext", ignore_errors=True)
    shutil.copytree("IntelBluetoothInjector.kext", "/Volumes/EFI/EFI/OC/Kexts/IntelBluetoothInjector.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AirportBrcmFixup.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/AirportBrcmFixup/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'AirportBrcmFixup.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AirportBrcmFixup.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirportBrcmFixup.kext", ignore_errors=True)
    shutil.copytree("AirportBrcmFixup.kext", "/Volumes/EFI/EFI/OC/Kexts/AirportBrcmFixup.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjector.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'BrcmBluetoothInjector.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('BrcmBluetoothInjector.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjector.kext", ignore_errors=True)
    shutil.copytree("BrcmBluetoothInjector.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjector.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjectorLegacy.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'BrcmBluetoothInjectorlegacy.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('BrcmBluetoothInjectorLegacy.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjectorLegacy.kext", ignore_errors=True)
    shutil.copytree("BrcmBluetoothInjectorLegacy.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmBluetoothInjectorLegacy.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareData.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'BrcmFirmwareData.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('BrcmFirmwareData.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareData.kext", ignore_errors=True)
    shutil.copytree("BrcmFirmwareData.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareData.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareRepo.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'BrcmFirmwareRepo.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('BrcmFirmwareRepo.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareRepo.kext", ignore_errors=True)
    shutil.copytree("BrcmFirmwareRepo.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmFirmwareRepo.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'BrcmNonPatchRAM.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('BrcmNonPatchRAM.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM.kext", ignore_errors=True)
    shutil.copytree("BrcmNonPatchRAM.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM2.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'BrcmNonPatchRAM2.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('BrcmNonPatchRAM2.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM2.kext", ignore_errors=True)
    shutil.copytree("BrcmNonPatchRAM2.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmNonPatchRAM2.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM2.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'BrcmPatchRAM2.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('BrcmPatchRAM2.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM2.kext", ignore_errors=True)
    shutil.copytree("BrcmPatchRAM2.kext", "/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM2.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM3.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/BrcmPatchRAM/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'BrcmPatchRAM3.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('BrcmPatchRAM3.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrcmPatchRAM3.kext", ignore_errors=True)
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
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/XLNCUSBFix.kext", ignore_errors=True)
    shutil.copytree("XLNCUSBFix.kext", "/Volumes/EFI/EFI/OC/Kexts/XLNCUSBFix.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooHDA.kext"):
    import urllib.request
    url = 'https://sourceforge.net/projects/voodoohda/files/latest/download'
    urllib.request.urlretrieve(url, 'VoodooHDA.zip')
    time.sleep(6)
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooHDA.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooHDA.kext", ignore_errors=True)
    shutil.copytree("VoodooHDA.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooHDA.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/CpuTscSync.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/CpuTscSync/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'CpuTscSync.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('CpuTscSync.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/CpuTscSync.kext", ignore_errors=True)
    shutil.copytree("CpuTscSync.kext", "/Volumes/EFI/EFI/OC/Kexts/CpuTscSync.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/NVMeFix.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/NVMeFix/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'NVMeFix.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('NVMeFix.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/NVMeFix.kext", ignore_errors=True)
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
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SATA-unsupported.kext", ignore_errors=True)
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
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AHCIPortInjector.kext", ignore_errors=True)
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
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/ATAPortInjector.kext", ignore_errors=True)
    shutil.copytree("ATAPortInjector.kext", "/Volumes/EFI/EFI/OC/Kexts/ATAPortInjector.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/VoodooPS2/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'VoodooPS2Controller.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooPS2Controller.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext", ignore_errors=True)
    shutil.copytree("VoodooPS2Controller.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooInput.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/Voodooinput/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'VoodooInput.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooInput.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooInput.kext", ignore_errors=True)
    shutil.copytree("VoodooInput.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooInput.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooRMI.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/VoodooSmbus/VoodooRMI/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'VoodooRMI.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooRMI.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooRMI.kext", ignore_errors=True)
    shutil.copytree("VoodooRMI.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooRMI.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AlpsT4USB.kext"):
    url = 'https://github.com/blankmac/AlpsT4USB/files/5933051/AlpsT4USB.zip'
    import urllib
    urllib.request.urlretrieve(url, 'AlpsT4USB.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('AlpsT4USB.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AlpsT4USB.kext", ignore_errors=True)
    shutil.copytree("Release/AlpsT4USB.kext", "/Volumes/EFI/EFI/OC/Kexts/AlpsT4USB.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooSMBus.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/VoodooSmbus/VoodooSMBus/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'VoodooSMBus.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooSMBus.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooSMBus.kext", ignore_errors=True)
    shutil.copytree("kext/VoodooSMBus.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooSMBus.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2C.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/VoodooI2C/VoodooI2C/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'VoodooI2C.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooI2C.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2C.kext", ignore_errors=True)
    shutil.copytree("VoodooI2C.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2C.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CAtmelMXT.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/VoodooI2C/VoodooI2C/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'VoodooI2CAtmelMXT.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooI2CAtmelMXT.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CAtmelMXT.kext", ignore_errors=True)
    shutil.copytree("VoodooI2CAtmelMXT.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2CAtmelMXT.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CELAN.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/VoodooI2C/VoodooI2C/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'VoodooI2CELAN.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooI2CELAN.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CELAN.kext", ignore_errors=True)
    shutil.copytree("VoodooI2CELAN.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2CELAN.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CFTE.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/VoodooI2C/VoodooI2C/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'VoodooI2CFTE.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooI2CFTE.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CFTE.kext", ignore_errors=True)
    shutil.copytree("VoodooI2CFTE.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2CFTE.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CHID.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/VoodooI2C/VoodooI2C/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'VoodooI2CHID.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooI2CHID.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CHID.kext", ignore_errors=True)
    shutil.copytree("VoodooI2CHID.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2CHID.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CSynaptics.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/VoodooI2C/VoodooI2C/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'VoodooI2CSynaptics.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooI2CSynaptics.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooI2CSynaptics.kext", ignore_errors=True)
    shutil.copytree("VoodooI2CSynaptics.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooI2CSynaptics.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/FakeSMC.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/CloverHackyColor/FakeSMC3_with_plugins/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'FakeSMC.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('FakeSMC.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/FakeSMC.kext", ignore_errors=True)
    shutil.copytree("FakeSMC.kext", "/Volumes/EFI/EFI/OC/Kexts/FakeSMC.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/ACPIMonitor.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/ACPIMonitor.kext", ignore_errors=True)
    shutil.copytree("ACPIMonitor.kext", "/Volumes/EFI/EFI/OC/Kexts/ACPIMonitor.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/AmdCPUMonitor.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AmdCPUMonitor.kext", ignore_errors=True)
    shutil.copytree("AmdCPUMonitor.kext", "/Volumes/EFI/EFI/OC/Kexts/AmdCPUMonitor.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/F718x.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/F718x.kext", ignore_errors=True)
    shutil.copytree("F718x.kext", "/Volumes/EFI/EFI/OC/Kexts/F718x.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/GeforceSensor.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/GeforceSensor.kext", ignore_errors=True)
    shutil.copytree("GeforceSensor.kext", "/Volumes/EFI/EFI/OC/Kexts/GeforceSensor.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/IntelCPUMonitor.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/IntelCPUMonitor.kext", ignore_errors=True)
    shutil.copytree("IntelCPUMonitor.kext", "/Volumes/EFI/EFI/OC/Kexts/IntelCPUMonitor.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/IntelMCHMonitor.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/IntelMCHMonitor.kext", ignore_errors=True)
    shutil.copytree("IntelMCHMonitor.kext", "/Volumes/EFI/EFI/OC/Kexts/IntelMCHMonitor.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/ITEIT87x.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/ITEIT87x.kext", ignore_errors=True)
    shutil.copytree("ITEIT87x.kext", "/Volumes/EFI/EFI/OC/Kexts/ITEIT87x.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/NVClockX.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/NVClockX.kext", ignore_errors=True)
    shutil.copytree("NVClockX.kext", "/Volumes/EFI/EFI/OC/Kexts/NVClockX.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/RadeonMonitor.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/RadeonMonitor.kext", ignore_errors=True)
    shutil.copytree("RadeonMonitor.kext", "/Volumes/EFI/EFI/OC/Kexts/RadeonMonitor.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/SMIMonitor.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/SMIMonitor.kext", ignore_errors=True)
    shutil.copytree("SMIMonitor.kext", "/Volumes/EFI/EFI/OC/Kexts/SMIMonitor.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooBatterySMC.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooBatterySMC.kext", ignore_errors=True)
    shutil.copytree("VoodooBatterySMC.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooBatterySMC.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/W836x.kext"):
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/W836x.kext", ignore_errors=True)
    shutil.copytree("W836x.kext", "/Volumes/EFI/EFI/OC/Kexts/W836x.kext")
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
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AtherosL1cEthernet.kext", ignore_errors=True)
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
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/AirPortAtheros40.kext", ignore_errors=True)
    shutil.copytree("AirPortAtheros40.kext", "/Volumes/EFI/EFI/OC/Kexts/AirPortAtheros40.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/VoodooPS2/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'VoodooPS2Controller.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('VoodooPS2Controller.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext", ignore_errors=True)
    shutil.copytree("VoodooPS2Controller.kext", "/Volumes/EFI/EFI/OC/Kexts/VoodooPS2Controller.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Kexts/BrightnessKeys.kext"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/BrightnessKeys/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'BrightnessKeys.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('BrightnessKeys.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil
    shutil.rmtree("/Volumes/EFI/EFI/OC/Kexts/BrightnessKeys.kext", ignore_errors=True)
    shutil.copytree("BrightnessKeys.kext", "/Volumes/EFI/EFI/OC/Kexts/BrightnessKeys.kext")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/OpenCore.efi"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'OpenCore.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('OpenCore.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil, os
    os.remove("/Volumes/EFI/EFI/OC/OpenCore.efi")
    shutil.copy2("X64/EFI/OC/OpenCore.efi", "/Volumes/EFI/EFI/OC/OpenCore.efi")
import os, time
if os.path.exists("/Volumes/EFI/EFI/BOOT/BOOTx64.efi"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'OpenCore.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('OpenCore.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil, os
    os.remove("/Volumes/EFI/EFI/BOOT/BOOTx64.efi")
    shutil.copy2("X64/EFI/BOOT/BOOTx64.efi", "/Volumes/EFI/EFI/BOOT/BOOTx64.efi")
import os, time
if os.path.exists("/Volumes/EFI/EFI/BOOT/BOOTIA32.efi"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'OpenCore.zip')
    import time
    time.sleep(1)
    import zipfile
    with zipfile.ZipFile('OpenCore.zip', 'r') as zip_ref:
      zip_ref.extractall()
    import shutil, os
    os.remove("/Volumes/EFI/EFI/BOOT/BOOTIA32.efi")
    shutil.copy2("IA32/EFI/BOOT/BOOTIA32.efi", "/Volumes/EFI/EFI/BOOT/BOOTIA32.efi")
import os, time
if os.path.exists("/Volumes/EFI/EFI/OC/Drivers/OpenRuntime.efi"):
    import json
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
url_data = urlopen("https://api.github.com/repos/acidanthera/OpenCorePkg/releases/latest").read()
import json
json_data = json.loads(url_data)
for asset in json_data["assets"]:
    if "RELEASE" not in asset["name"]:
        continue
    url = asset["browser_download_url"]
    import urllib
    urllib.request.urlretrieve(url, 'OpenRuntime.zip')
    import time
    time.sleep(1)
    import shutil, os
    os.remove("/Volumes/EFI/EFI/OC/Drivers/OpenRuntime.efi")
    shutil.copy2("X64/EFI/OC/Drivers/OpenRuntime.efi", "/Volumes/EFI/EFI/OC/Drivers/OpenRuntime.efi")


print("The script has been completed, if there are any bugs feel free to contact me. (Discord = Tijmen#9962 .)")

print("BYE BYE")

time.sleep(2)
exit()




































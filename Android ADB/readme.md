# Python: Using ADB for Android
----------

*Only works in CMD Windows atm.*

Playing around with subprocess, ADB executable for Android and returning the output.

I had tried some packages to do this but wanted something simpler and in my control.

Just basic tests.

You will need ADB (Android Debug Bridge) on your PC somewhere.

You only need the SDK Platform Tools here:

- [https://developer.android.com](https://developer.android.com/tools/releases/platform-tools)

Out of the zip file you only need these 3 files to make the scripts here work:

- adb.exe
- AdbWinApi.dll
- AdbWinUsbApi.dll

Make sure you have enabled USB Debugging on your phone \ tablet and are using a USB data cable.


---
<br>

File > `Push-Pull-ADB-Menu.py` is for use with the KeePass app. It checks date & time of both database.kdbx files and offers option to push or pull and overwrite the file on either PC or mobile. Edit as needed. (The .bat file does similar.)


<br>

*If you are using Windows 7 you will need an earlier version of ADB. Last version usable maybe 34.0.4 of platform tools?*



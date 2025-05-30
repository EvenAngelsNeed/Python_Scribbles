
:: Test DOS Menu
:: Remember to use back slashes for ADB.

ECHO OFF

CLS

:MENU
ECHO.
ECHO Current File Date On Device:
adb shell ls -l /sdcard/Documents/_Data/Database.kdbx

ECHO.
ECHO Local Date
::dir /T:W Database.kdbx
@FOR %%A IN ("Database.kdbx") DO @(ECHO=%%~tA)
ECHO.



ECHO ----------------------------
ECHO.
ECHO 1 - Copy File To Phone
ECHO 2 - Get File From Phone
ECHO 3 - EXIT
ECHO.
ECHO ----------------------------
ECHO.


:: Get input:

SET /P M=Type 1, 2 or 3 then press ENTER:


IF %M%==1 GOTO PUSH
IF %M%==2 GOTO PULL
IF %M%==3 GOTO EOF



:PUSH
::cd %somedir%\
CLS
ECHO.
ECHO Command Output:

call adb push "Database.kdbx" "/sdcard/Documents/_Data/"

GOTO MENU


:PULL
::cd %somedir%\
CLS
ECHO.
ECHO Command Output:

call adb pull -a "/sdcard/Documents/_Data/Database.kdbx" "Database.kdbx"

GOTO MENU



 

:: pause
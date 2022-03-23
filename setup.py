# This Python file uses the following encoding: utf-8
import sys

def install_on_linux():
    pass

def install_on_osx():
    pass

def install_on_windows():
    pass

if __name__ == "__main__":
    error = "{} is currently not supported"
    if sys.platform.startwith == 'aix':
        raise Exception(error.format(sys.platform))
    elif sys.platform.startwith == 'cygwin':
        raise Exception(error.format(sys.platform))
    elif sys.platform.startwith == 'darwin':
        pass
    elif sys.platform.startwith == 'linux':
        pass
    elif sys.platform.startwith == 'win32':
        pass

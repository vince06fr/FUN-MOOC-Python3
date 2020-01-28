# Program for utf-8 character encoding test 
# when running python3 code 

# CC0 CopyLeft - JRelland January 2020
# Tested on Python 3.8.0 on Windows 8.1 environment
# HP Pavilion i3-4040U CPU @ 1.90 GHz x64 12,0 Go

# ---------------------------------------------------

# Modules installation
import sys

# "utf-8" endocing test
if sys.getdefaultencoding() == "utf-8":
    # Right encoding, no need to communicate with the user
    pass
else:
    # Inform user its default encoding is not utf-8
    # Propose alternative
    #   Cancel : Keep your current encoding
    #   OK     : Initialise utf-8 encoding
    
    # to learn and to do: MessageBox, initialise caracter encoding 
    pass

# Jan. 28, 2020 propose pull request 

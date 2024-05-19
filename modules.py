import os
from os import remove
from os.path import exists
# external modules

# if os.path.exists("newfile"):
#     os.remove("newfile")

# file_name="newfile"

if exists("newfile"):
    remove("newfile")
#!/usr/bin/env python

# KeePass KeyFile Generator
# Version: 1.0 @ 2021-11-17
# Source: https://github.com/florianzeeb/keepass_keyfile_generator/

import os
import sys
import platform
import time
import datetime
import math
import secrets
from win32_setctime import setctime #pip install win32-setctime

# define max keyfiles
run_numbers = 10

# define script file and script path
script_file = os.path.realpath(__file__)
script_path = os.path.dirname(sys.argv[0])
script_path_absolute = os.path.abspath(script_path)

# calculcate max digits of integer: run_numbers
max_digits = int(math.log10(run_numbers))+1

# define the template
source_template = r'''<?xml version="1.0" encoding="utf-8"?>
<KeyFile>
    <Meta>
        <Version>2.0</Version>
    </Meta>
    <Key>
        <Data Hash="#KEY01##">
            #KEY02## #KEY03## #KEY04## #KEY05##
            #KEY06## #KEY07## #KEY08## #KEY09##
        </Data>
    </Key>
</KeyFile>'''

# loop per run_number
for x in range(0, run_numbers):

    # read template for run
    source_template_output = source_template

    # define random files
    secret_1 = secrets.token_hex(4).upper()
    secret_2 = secrets.token_hex(4).upper()
    secret_3 = secrets.token_hex(4).upper()
    secret_4 = secrets.token_hex(4).upper()
    secret_5 = secrets.token_hex(4).upper()
    secret_6 = secrets.token_hex(4).upper()
    secret_7 = secrets.token_hex(4).upper()
    secret_8 = secrets.token_hex(4).upper()
    secret_9 = secrets.token_hex(4).upper()

    # replace keys template with secrets
    source_template_output = source_template_output.replace('#KEY01##', secret_1)
    source_template_output = source_template_output.replace('#KEY02##', secret_2)
    source_template_output = source_template_output.replace('#KEY03##', secret_3)
    source_template_output = source_template_output.replace('#KEY04##', secret_4)
    source_template_output = source_template_output.replace('#KEY05##', secret_5)
    source_template_output = source_template_output.replace('#KEY06##', secret_6)
    source_template_output = source_template_output.replace('#KEY07##', secret_7)
    source_template_output = source_template_output.replace('#KEY08##', secret_8)
    source_template_output = source_template_output.replace('#KEY09##', secret_9)

    # add leading 0
    x_fix = str(x).zfill(max_digits)

    # define output file
    target_template_file = f"keepass.kdbx.{x_fix}.keyx"
    target = script_path_absolute + "\\" + target_template_file

    # write data to target file
    source_template_file = open(target, "w")
    source_template_file.writelines(source_template_output)
    source_template_file.close()

    # change file timestamp: last update date, last access date
    date = datetime.datetime(year=datetime.datetime.now().year, month=1, day=1, hour=10, minute=00, second=00)
    modTime = time.mktime(date.timetuple())
    os.utime(target, (modTime, modTime))

    # change file timestamp: create date (for windows OS)
    if platform.system() == 'Windows':
        setctime(target, modTime)

# output
print("Files created: {}".format(run_numbers))
print("Files location: " + script_path_absolute + "\\")
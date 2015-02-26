#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015��1��7��

@author: pan
'''
# Copyright (c) 2009, Giampaolo Rodola'. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""
List all mounted disk partitions a-la "df -h" command.

$ python examples/disk_usage.py
Device               Total     Used     Free  Use %      Type  Mount
/dev/sdb3            18.9G    14.7G     3.3G    77%      ext4  /
/dev/sda6           345.9G    83.8G   244.5G    24%      ext4  /home
/dev/sda1           296.0M    43.1M   252.9M    14%      vfat  /boot/efi
/dev/sda2           600.0M   312.4M   287.6M    52%   fuseblk  /media/Recovery
"""

import sys
import os
import psutil

def print_(s):
    sys.stdout.write(s + '\n')
    sys.stdout.flush()

def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

def disk_info(infolist):
    templ = "%-17s %8s %8s %8s %5s%% %9s  %s"
    print_(templ % ("Device", "Total", "Used", "Free", "Use ", "Type",
                    "Mount"))
    templist = list()
    for part in psutil.disk_partitions(all=False):
        tempdict =dict()
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                # skip cd-rom drives with no disk in it; they may raise
                # ENOENT, pop-up a Windows GUI error for a non-ready
                # partition or just hang.
                continue
        usage = psutil.disk_usage(part.mountpoint)
        tempdict["device"]=str(part.device)
        tempdict["dtotal"]=bytes2human(usage.total)
        tempdict["dused"]=bytes2human(usage.used)
        tempdict["free"] = bytes2human(usage.free)
        tempdict["percent"]=str(usage.percent)+"%"
        tempdict["fstype"]=str(part.fstype)
        tempdict["mountpoint"]=str(part.mountpoint)
        templist.append(tempdict)
        print_(templ % (
            part.device,
            bytes2human(usage.total),
            bytes2human(usage.used),
            bytes2human(usage.free),
            int(usage.percent),
            part.fstype,
            part.mountpoint))
    infolist.append(templist)

def main():
    infolist = list()
    disk_info(infolist)

if __name__ == '__main__':
    sys.exit(main())
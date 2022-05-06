# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 00:04:40 2022

@author: Huang
"""
import os
os.chdir(r'C:\Users\dream\Documents\Github\ReadWriteMemory')

from ReadWriteMemory import ReadWriteMemory

rwm = ReadWriteMemory()

# Get the list of running processes ID's from the current system
# process = rwm.get_process_by_id(1337)

process = rwm.get_process_by_name('elementclient.exe')

process.open()

help(process)
print(process.__dict__)


health_pointer = process.get_pointer(0x21048596, offsets=[60])
health = process.read(health_pointer)

health = process.readByte(health_pointer)
print(health)

process.write(health_pointer,5000)
# ammo_pointer = process.get_pointer(0x004df73c, offsets=[0x378, 0x14, 0x0])
# grenade_pointer = process.get_pointer(0x004df73c, offsets=[0x35c, 0x14, 0x0])
# print(health_pointer)



ammo = process.read(ammo_pointer)
grenade = process.read(grenade_pointer)

print('\nPrinting the current values.')
print({'Health': health, 'Ammo': ammo, 'Grenade': grenade})
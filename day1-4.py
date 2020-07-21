# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:06:15 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x,y,z=mc.player.setTilePos(x,y,z)

mc.player.setTilePos(x,y,z)
time.sleep(3)

x=x+100
mc.player.setTilePos(x,y,z)
time.sleep(3)

x=x+100
time.sleep(3)
mc.player.setTilePos(x,y,z)

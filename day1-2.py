# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 11:02:00 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()f
x=1
y=1
z=1
print(mc.player.setTilePos(x,y,z))
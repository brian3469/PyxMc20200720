# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:04:58 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

    x,y,z =mc.player.getTilePos()
    
    mc.postToChat("You are located on X:"+str(x)+
                  " Y:"+str(y)+" z:"+str(z))
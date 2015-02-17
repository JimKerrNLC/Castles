#!/usr/bin/env python

#import the minecraft.py module from the minecraft directory
import mcpi.minecraft as minecraft
#import minecraft block module
import mcpi.block as block
#import time, so delays can be used
import server

def main():
    mc = minecraft.Minecraft.create(server.address)
    # write the rest of your code here...
    mc.postToChat("Erasing a base for castle ...")
    mc.setBlocks(-30,-30,-30,120,120,120,block.AIR.id)
    mc.setBlocks(-30,-1,-30,120,-10,120,block.SANDSTONE.id)
    mc.postToChat("Done Erasing base!")



if __name__ == "__main__":
    main()

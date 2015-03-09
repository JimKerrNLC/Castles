#! /usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
import server
import castlekit

# These are the default values for the Floors and Walls and Doorframes
Floor = block.STONE
Door = block.STONE
Wall = block.STONE

if __name__ == "__main__":
    mc = minecraft.Minecraft.create( server.address )
    ck = castlekit
    # Your code goes below here
    # The indents are important align your text correctly
    
    # This line will draw a Turret using STONE as a texture
    # for the Floor and Wall in location x = 0, y= 0 level = 0
    ck.drawTurret(Floor,Wall,Door,0,0,0)

    


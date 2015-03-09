#! /usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
import server
import castlekit
# These are the default values for the key blocks
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
    # Turrent 1 Front
    ck.drawTurret(Floor,Wall,Door,0,0,0)
    ck.drawTurret(Floor,Wall,Door,0,0,1)
    # Add the Top of the turret (castellation)
    ck.drawTopTurret(Floor,Wall,Door,0,0,2)

    # Draw side wall
    ck.drawGroundFloorWall("NS",Floor,Wall,Door,0,1,0)
    ck.drawUpperFloorWall("NS",Floor,Wall,Door,0,1,1)
    # Add the Top of the Wall (castellation)
    ck.drawTopWall("NS",Floor,Wall,Door,0,1,2)

    # Turrent 3 back 
    ck.drawTurret(Floor,Wall,Door,0,2,0)
    # Add the Top of the turret (castellation)
    ck.drawTopTurret(Floor,Wall,Door,0,2,1)

    ck.drawGroundFloorWall("NS",block.OBSIDIAN, block.GOLD_BLOCK ,block.SANDSTONE ,0,1,0)

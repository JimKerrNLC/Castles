#! /usr/bin/python
import mcpi.minecraft as minecraft
import mcpi.block as block
import server
import castlekit

Floor = block.STONE
Door = block.STONE
Wall = block.STONE


if __name__ == "__main__":
    mc = minecraft.Minecraft.create( server.address )
    ck = castlekit

    # Castle Front

    # Draw 2 storey turret
    ck.drawTurret(Floor,Wall,Door,0,0,0)
    ck.drawTurret(Floor,Wall,Door,0,0,1)
    ck.drawTopTurret(Floor,Wall,Door,0,0,2)
    
    #Draw 1 base floor and 1 extra floors
    ck.drawGroundFloorWall("EW",Floor,Wall,Door,1,0,0)
    ck.drawTopWall("EW",Floor,Wall,Door,1,0,1)

    #Draw 1 base floor and 1 extra floors
    ck.drawGroundFloorWall("EW",Floor,Wall,Door,2,0,0)
    ck.drawTopWall("EW",Floor,Wall,Door,2,0,1)

    # Draw 2 storey turret
    ck.drawTurret(Floor,Wall,Door,3,0,0)
    ck.drawTurret(Floor,Wall,Door,3,0,1)
    ck.drawTopTurret(Floor,Wall,Door,3,0,2)
    


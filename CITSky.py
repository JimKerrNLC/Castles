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
    
    #Draw 1 base floor and 1 extra floors
    ck.drawGroundFloorWall("NS",Floor,Wall,Door,1,-1,1)
    ck.drawUpperFloorWall("NS",Floor,Wall,Door,1,4,1)

    # Draw castelations on top
    ck.drawTopWall("NS",Floor,Wall,Door,1,9,1)

    # Draw 2 storey turret
    ck.drawTurret(Floor,Wall,Door,11,-1,1)
    ck.drawTurret(Floor,Wall,Door,11,4,1)

    # Draw Turret top`
    ck.drawTopTurret(Floor,Wall,Door,11,9,1)
    
    # Draw 2 storey turret
    ck.drawTurret(Floor,Wall,Door,-9,-1,1)
    ck.drawTurret(Floor,Wall,Door,-9,4,1)

    # Draw Turret top
    ck.drawTopTurret(Floor,Wall,Door,-9,9,1)

    # Castle Walls
    ck.drawGroundFloorWall("EW",Floor,Wall,Door,-9,-1,11)
    ck.drawTopWall("EW",Floor,Wall,Door,-9,4,11)


    # Draw 2 storey turret
    ck.drawTurret(Floor,Wall,Door,-9,-1,21)
    # Draw Turret top
    ck.drawTopTurret(Floor,Wall,Door,-9,4,21)

    # Castle Walls
    ck.drawGroundFloorWall("NS",Floor,Wall,Door,1,-1,21)
    ck.drawTopWall("NS",Floor,Wall,Door,1,4,21)

    # Draw 2 storey turret
    ck.drawTurret(Floor,Wall,Door,11,-1,21)
    # Draw Turret top
    ck.drawTopTurret(Floor,Wall,Door,11,4,21)

    # Castle Walls
    ck.drawGroundFloorWall("EW",Floor,Wall,Door,11,-1,11)
    ck.drawTopWall("EW",Floor,Wall,Door,11,4,11)



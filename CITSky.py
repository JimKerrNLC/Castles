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

    # Set Start Point
    playerPos = mc.player.getPos()
    originX = int(playerPos.x)+1
    originY =int(playerPos.y)-1
    originZ =int(playerPos.z)+1

    
    
    ck.drawGroundFloorWall("NS",Floor,Wall,Door,1,-1,1)
    ck.drawUpperFloorWall("NS",Floor,Wall,Door,1,4,1)
    ck.drawUpperFloorWall("NS",Floor,Wall,Door,1,9,1)
    
    ck.drawTopWall("NS",Floor,Wall,Door,1,14,1)
    
    ck.drawTurret(Floor,Wall,Door,11,-1,1)
    ck.drawTurret(Floor,Wall,Door,11,4,1)
    ck.drawTurret(Floor,Wall,Door,11,9,1)
    ck.drawTurret(Floor,Wall,Door,11,14,1)

    ck.drawTopTurret(Floor,Wall,Door,11,19,1)
    
    ck.drawTurret(Floor,Wall,Door,-9,-1,1)
    ck.drawTurret(Floor,Wall,Door,-9,4,1)
    
    ck.drawTopTurret(Floor,Wall,Door,-9,9,1)

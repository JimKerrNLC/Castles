import mcpi.minecraft as minecraft
import mcpi.block as block
import server

    
"""
0 = Air
1 = Ground
2 = Floor
3 = Door Surround
4 = Wall
5 = Glowstone
6 = Glass
7 = Fence
"""
Floor = block.STONE
Door = block.STONE
Wall = block.STONE
grdFloorWall = [[[1,1,1,1,1], [1,1,1,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]],
                [[0,0,0,0,0], [0,0,0,3,0],[4,4,4,4,0],[4,0,0,0,0],[0,0,0,0,0]],
                [[0,0,0,0,0], [0,0,0,3,0],[4,4,4,4,0],[4,0,0,0,0],[0,0,0,0,0]],
                [[0,0,0,0,0], [0,0,0,3,0],[4,4,4,4,0],[4,5,0,0,0],[0,0,0,0,0]],
                [[0,0,0,0,0], [0,0,0,3,3],[4,4,4,4,4],[2,2,2,2,2],[2,2,2,2,2]]]

uprFloorWall = [[[0,0,0,0,0], [0,0,0,0,0],[4,4,4,4,4],[4,0,0,0,0],[0,0,0,0,0]],
                [[0,0,0,0,0], [0,0,0,0,0],[2,2,6,2,6],[4,0,0,0,0],[0,0,0,0,0]],
                [[0,0,0,0,0], [0,0,0,0,0],[2,2,6,2,6],[4,0,0,0,0],[0,0,0,0,0]],
                [[0,0,0,0,0], [0,0,0,0,0],[2,2,6,2,6],[4,5,0,0,0],[0,0,0,0,0]],
                [[0,0,0,0,0], [0,0,0,0,0],[4,4,4,4,4],[2,2,2,2,2],[2,2,2,2,2]]]


anyTurret = [[[0,0,2,2,2], [0,2,0,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]],
                [[0,0,2,2,0], [0,2,0,2,0],[2,0,0,2,0],[2,7,7,7,0],[0,0,0,0,0]],
                [[0,0,2,2,0], [0,2,0,2,0],[2,0,0,2,0],[2,7,7,7,0],[0,0,0,0,0]],
                [[0,0,2,2,0], [0,2,0,2,0],[2,0,0,2,0],[2,2,2,7,0],[0,0,0,0,0]],
                [[0,0,2,2,2], [0,7,0,2,2],[2,0,0,0,2],[2,0,0,2,2],[2,2,2,2,2]]]
  

#TODO
topWall = [[[0,0,0,0,0], [0,0,0,0,0],[4,4,4,4,4],[4,0,0,0,0],[4,0,0,0,0]],
                [[0,0,0,2,0], [0,2,0,0,0],[4,0,4,0,4],[0,0,0,0,0],[4,0,0,0,0]]]

topTurret = [[[0,0,4,4,4], [0,4,0,0,0],[4,0,0,0,0],[4,0,0,0,0],[4,0,0,0,0]],
                [[0,0,0,4,0], [0,4,0,0,0],[0,0,0,0,0],[4,0,0,0,0],[0,0,0,0,0]]]

def getBlock(num):
    global Floor
    global Wall
    global Door
    if num == 0:
        return block.AIR
    elif num == 1:
        return block.STONE
    elif num == 2:
        return Floor
    elif num == 3:
        return Door
    elif num == 4:
        return Wall
    elif num == 5:
        return block.GLOWSTONE
    elif num == 6:
        return block.GLASS_PANE
    elif num == 7:
        return block.FENCE
    else:
        return block.AIR
    
    

def drawObject(template,ox,oy,oz):
    #starting point
    y=0
    for layer in template:
        z = 0
        for row in layer:
            x=0
            for block in row:
                #plot row x
                # set block
                # material = block
                # xpos = ox+x
                # ypos = oy+y
                # zpos = oz+z
                mc.setBlock(x,y,z, getBlock(block))
                x+=1
            for block in reversed (row):
                #plot row x
                # set block
                # material = block
                # xpos = ox+x
                # ypos = oy+y
                # zpos = oz+z
                mc.setBlock(x,y,z, getBlock(block))
                x+=1
            z+=1
        for row in reversed(layer):
            x=0
            for block in row:
                #plot row x
                # set block
                # material = block
                # xpos = ox+x
                # ypos = oy+y
                # zpos = oz+z
                mc.setBlock(x,y,z, getBlock(block))
                x+=1
            for block in reversed (row):
                #plot row x
                # set block
                # material = block
                # xpos = ox+x
                # ypos = oy+y
                # zpos = oz+z
                mc.setBlock(x,y,z, getBlock(block))
                x+=1
            z+=1
        y+=1


#class CastleBlock:

def drawGroundFloorWall(nFloor, nWall, nDoor, x,y,z):
    global Floor
    global Wall
    global Door
    Floor = nFloor
    Wall = nWall
    Door = nDoor
    drawObject(grdFloorWall,x,y,z)
    
        
    

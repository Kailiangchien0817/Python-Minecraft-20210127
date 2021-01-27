#3-6 
from mcpi.minecraft import Minecraft
LC = Minecraft.create()

x,y,z = LC.player.getTilePos()
for i in range(0,20):
    LC.setBlock(x+i,y-1,z+i,79)
    LC.setBlock(x+i+1,y-1,z+i,79)
    LC.setBlock(x+i+2,y-1,z+i,79)
    LC.setBlock(x+i+3,y-1,z+i,79)
#3-5
from mcpi.minecraft import Minecraft
LC = Minecraft.create()

x,y,z = LC.player.getTilePos()
for i in range(0,20):
    LC.setBlock(x,y-1,z+i,79)
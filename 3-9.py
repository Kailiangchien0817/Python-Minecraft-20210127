#3-9
from mcpi.minecraft import Minecraft
LC = Minecraft.create()

x,y,z = LC.player.getTilePos()
base = 20
height = (base//2)+1

for i in range(height):
    x1 = x+i
    y1 = y+i
    z1 = z+i
    
    x2 = x + base - i
    #y與y2相同
    z2 = z + base - i 
    LC.setBlocks(x1, y1, z1, x2, y1, z2, 121)
    
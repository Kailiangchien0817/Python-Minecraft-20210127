#3-11
from mcpi.minecraft import Minecraft
LC = Minecraft.create()

x,y,z = LC.player.getTilePos()
number=1

for i in range(8):
    for j in range(number):
        LC.spawnEntity(x,y,z,60) 
    number = number*2
    
    LC.postToChat("你生成了"+str(number)+"隻蠹魚")
      
        
        
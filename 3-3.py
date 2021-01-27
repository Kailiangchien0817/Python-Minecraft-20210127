#3-3
from mcpi.minecraft import Minecraft
LC = Minecraft.create()
import random,time

while True:
    x,y,z = LC.player.getPos()
    a = random.uniform(-20,20)
    b = random.uniform(-20,20)
    y = y+30
    LC.spawnEntity(x+a,y,z+b,93)
    time.sleep(0.1)
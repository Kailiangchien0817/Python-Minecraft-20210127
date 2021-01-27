# 3-2
from mcpi.minecraft import Minecraft
LC = Minecraft.create()

while True:
    hits = LC.events.pollBlockHits()
    if len(hits)>0:
        a = hits[0]
        x,y,z = a.pos.x,a.pos.y,a.pos.z
        block = LC.getBlock(x,y,z)
        LC.postToChat("你打到了"+str(block))
        if block == 1:
          LC.setBlock(x,y,z,41)
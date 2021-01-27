#practice 2
from mcpi.minecraft import Minecraft
LC = Minecraft.create()

while True:
    hits = LC.events.pollProjectileHits()
    if len(hits)>0:
        a = hits[0]
        x,y,z = a.pos.x,a.pos.y,a.pos.z
        LC.player.setTilePos(x,y,z)
        LC.spawnEntity(x,y,z,99)
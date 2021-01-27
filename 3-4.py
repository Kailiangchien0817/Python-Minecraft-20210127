#3-4
from mcpi.minecraft import Minecraft
LC = Minecraft.create()

while True:
    hits = LC.events.pollProjectileHits()
    if len(hits)>0:
        a = hits[0]
        x,y,z = a.pos.x,a.pos.y,a.pos.z
        LC.createExplosion(x,y,z,power=150)
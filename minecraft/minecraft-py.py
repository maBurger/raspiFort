from mcpi import minecraft

mc = minecraft.Minecraft.create()
#mc.postToChat("Meine Position:")

x,y,z = mc.player.getPos()
mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, 1)

import Image, ImageDraw
import time
im = Image.open("kilosec.PNG")
draw = ImageDraw.Draw(im)

def kiloseconds():
    tm = time.localtime()
    return (tm.tm_hour*3600+tm.tm_min*60+tm.tm_sec)/1000.0
    #http://github.com/api/v2/json/blob/show/bavardage/kiloseconds/03fac33ed6be1f0a004319cf7b8449d6d5fb10f3

draw.line((im.size[0]/2, im.size[1]) + (im.size[0]/2,0), fill="#CED4C8", width=16)
draw.line((im.size[0]/2, im.size[1]) + (im.size[0]/2,im.size[1]-((kiloseconds()/86.4)*im.size[1])), fill="#88B0B8", width=10)
#del draw
im.save("kiloclock.png")
im.show()
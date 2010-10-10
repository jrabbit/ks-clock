import Image, ImageDraw
import time
import math

def kiloseconds():
    tm = time.localtime()
    return (tm.tm_hour*3600+tm.tm_min*60+tm.tm_sec)/1000.0
    # http://github.com/api/v2/json/blob/show/bavardage/kiloseconds/03fac33ed6be1f0a004319cf7b8449d6d5fb10f3

def kilo_gmt():
    tm = time.gmtime()
    return (tm.tm_hour*3600+tm.tm_min*60+tm.tm_sec)/1000.0


def clock(kind,**kwargs):
    if 'tz' in kwargs:
        shift = kwargs['tz']
        ks = kilo_gmt() + shift*3.6
    else:
        ks = kiloseconds()
    if kind is "line":
        im = Image.open("kilosec.PNG")
        draw = ImageDraw.Draw(im)
        draw.line((im.size[0]/2, im.size[1]) + (im.size[0]/2,0), fill="#CED4C8", width=16)
        draw.line((im.size[0]/2, im.size[1]) + (im.size[0]/2,im.size[1]-((ks/86.4)*im.size[1])), fill="#88B0B8", width=10)
    elif kind is "arc":
        im = Image.open("kilosec_round.PNG")
        draw = ImageDraw.Draw(im)
        draw.arc(im.size, 0, (kiloseconds()/86.4)*360, outline="#E67300")
    elif kind is "composite":
        im = Image.open("kscomposite.png")
        draw = ImageDraw.Draw(im)
        im.size
        # deg = 360*(ks/86.4)
        if im.size[0] > im.size[1]:
            smallside = im.size[1]
        elif im.size[1] > im.size[0]:
            smallside = im.size[0]
        else:
            smallside = im.size[0]
        radius = smallside*.80 #give 20% white space
        cord_h = radius*(2-math.cos(2*math.pi*(ks/86.4)))
    
    return im


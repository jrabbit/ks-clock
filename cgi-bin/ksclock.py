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
    
    if kind == "line":
        #print "making line"
        im = Image.open("kilosec.PNG")
        draw = ImageDraw.Draw(im)
        draw.line((im.size[0]/2, im.size[1]) + (im.size[0]/2,0), fill="#CED4C8", width=16)
        draw.line((im.size[0]/2, im.size[1]) + (im.size[0]/2,im.size[1]-((ks/86.4)*im.size[1])), fill="#88B0B8", width=10)
        return im
    
    elif kind == "arc":
        try:
            im = Image.open("kilosec_round.PNG")
        except IOError:
            im = Image.new("RGBA", (300,300), color=0)
        draw = ImageDraw.Draw(im)
        #center = (im.size[0]/2, im.size[1]/2)
        draw.arc((5,5,im.size[0]-5, im.size[1]-5),  0, int((kiloseconds()/86.4)*360), fill="#E67300")
        #90 degeres is bottom of circle.
        #draw.chord((5,5,im.size[0]-5, im.size[1]-5),  0, 120, fill="#E67300")
        return im
    
    elif kind == "chord":
        try:
            im = Image.open("kilosec_round.PNG")
        except IOError:
            im = Image.new("RGBA", (300,300), color=0)
        draw = ImageDraw.Draw(im)
        draw.chord((5,5,im.size[0]-5, im.size[1]-5),  0, int((kiloseconds()/86.4)*360), fill="#E67300")
        return im
    
    elif kind == "composite":
        try:
            im = Image.open("kscomposite.png")
        except IOError:
            im = Image.new("RGBA", (300,300), color=0)
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
        angle = math.degrees(2-math.cos(2*math.pi*(ks/86.4)/2))
        #ratio = .8*ks/86.4
        #angle = math.degrees(math.acos(ratio/2))
        #print angle
        langle = int(angle - 90)*-1
        rangle = int(angle + 90)
        draw.chord((int(.2*im.size[0]),int(.2*im.size[1]),int(im.size[0]*.8), int(im.size[1]*.8)), langle, rangle, outline="#E67300", fill="#E67300")
        return im
        
    else:
        pass


if __name__ == '__main__':
    import sys
    kind = str(sys.argv[1])
    print sys.argv
    #kind = "line"
    clock(kind).show()

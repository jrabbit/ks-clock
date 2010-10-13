#!/usr/bin/env python
import cgi
import cgitb
import ksclock
cgitb.enable()

def main():
    print "Content-type: image/png\n"
    #f = open("clock.png", "rw")
    if not kind:
        kind = "line"
    ksclock.clock(kind).save("clock.png")
    f = open("clock.png")
    print f.read()

main()
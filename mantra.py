#!/usr/bin/env python
import math
import cairo

WIDTH, HEIGHT = 720, 480


surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
ctx.scale (WIDTH/1.0, HEIGHT/1.0)

white = cairo.SolidPattern(1, 1, 1)
ctx.rectangle(0, 0, 1, 1)
ctx.set_source(white)
ctx.fill()


dx = 1.0/11.0
dy = 1.0/11.0

for i in range(1, 8):
    for j in range(1, 8):

        col = cairo.SolidPattern(i/10.0, 1-j/10.0, i*j/100.0)
        ctx.set_source(col)
        x = i/9.0
        y = j/9.0
        ctx.rectangle(x, y, dx, dy)
        ctx.fill()

surface.write_to_png('mantra.png')
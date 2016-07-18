#!/usr/bin/env python
import math
import cairo

WIDTH, HEIGHT  = 720, 480

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.scale (WIDTH/1.0, HEIGHT/1.0)

pat = cairo.LinearGradient (0.0, 0.0, 1.0, 1.0)
pat.add_color_stop_rgba (1, 0, 1, 0, 1)
pat.add_color_stop_rgba (0, 1, 0, 1, 1)


pat2 = cairo.LinearGradient (0.5, 0.0, 1.0, 0.0)
pat2.add_color_stop_rgba (1, 1, 0, 0, 1)
pat2.add_color_stop_rgba (0, 0, 1, 1, 1)

ctx.rectangle (0,0,.5,1)
ctx.set_source (pat)
ctx.fill ()

ctx.rectangle (0.5,0,1,1)
ctx.set_source (pat2)
ctx.fill ()


surface.write_to_png('bands.png')

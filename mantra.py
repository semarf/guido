#!/usr/bin/env python
import math
import cairo
from math import pow
from colorsys import hls_to_rgb
from random import randint as r
from math import fsum as s

WIDTH, HEIGHT = 1280, 720

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
ctx.scale (WIDTH/1.0, HEIGHT/1.0)

white = cairo.SolidPattern(1, 1, 1)
ctx.rectangle(0, 0, 1, 1)
ctx.set_source(white)
ctx.fill()

xpos = []
ypos = []

N = 11

XMUL = 1.9
YMUL = 1.6

XTABLE = [pow(XMUL, i) for i in range(1, 9)]
YTABLE = [pow(YMUL, j) for j in range(1, 9)]
CTABLE = [hls_to_rgb(c/16.0, .5, 1) for c in range(16)]

XSEQ = [XTABLE[r(0, 7)] for i in range(N)]
YSEQ = [YTABLE[r(0, 7)] for j in range(N)]

XMAX = s(XSEQ)
YMAX = s(YSEQ)


y = 0
for j in range(N):
    dy = YSEQ[j]/YMAX
    x = 0
    for i in range(N):
        ij = (i+j) % N
        rgb = CTABLE[r(0, 15)]
        col = cairo.SolidPattern(rgb[0], rgb[1], rgb[2])
        ctx.set_source(col)
        dx = XSEQ[ij]/XMAX
        ctx.rectangle(x, y, dx, dy)
        ctx.fill()
        x += dx
    y += dy

surface.write_to_png('mantra2.png')
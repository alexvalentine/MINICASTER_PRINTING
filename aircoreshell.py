from mecode import G
import numpy as np
import math

#outfile = r"/Volumes/group0/jlewis/User Files/Valentine/AFRL/my_print.pgm"
outfile = r'C:\Users\User\Documents\GitHub\MINICASTER_PRINTING\aircoreshell.pgm'


#Defining mecode parameters
g = G(
    direct_write=False,
    outfile=outfile,
    header=None,
    footer=None,
    print_lines=False,
    )

g=G(outfile='C:\Users\User\Documents\GitHub\MINICASTER_PRINTING\aircoreshell.pgm')
pressure_box = 4
lenseg=0.05
spacey=0.01
defspeed=0.001
speedincr=0.002

g.toggle_pressure(pressure_box)

for ni in range(0,5):
    g.feed(defspeed+speedincr*2*ni)
    g.move(x=lenseg)
    g.move(y=spacey)
    g.feed(defspeed+speedincr*(2*ni+1))
    g.move(x=-lenseg)
    g.move(y=spacey)

g.toggle_pressure(pressure_box)


g.view(backend='matplotlib')

g.teardown() 
from mecode import G
import numpy as np

outfile = r"C:\Users\Wyss User\Desktop\myprint.pgm" ## RUN ON DESKTOP (WINDOWS)

#outfile = r"/Volumes/jlewis/User Files/Valentine/AFRL/my_print.pgm"   ## RUN ON LAPTOP! (MAC)


g=G(
    direct_write=False,
    outfile=outfile,
    #header=r"/Users/alex/alexvalentine/AFRL-printing/mymegacasterheader.txt",
    #footer=r"/Users/alex/alexvalentine/AFRL-printing/mymegacasterfooter.txt",
    print_lines=False,
    aerotech_include=False,
)


pressure_box = 16  #megacaster pressure box com port

pressure = 55    #pressure needed for AG-TPU ink with 100um nozzle + high pressure adapter

#def square_base(length, height, connections, layer_height, theta = 45):
#    base_extra = height/np.tan(theta)  # x component of slope
#
#    base_length = length + 2*base_extra
#    
#    layers = height/layer_height
#    layers = int(round(layers))
#    
#    for i in range(layers):
#        if i==0:
#            g.meader(base_length, base_length, spacing=0.1,start='UL')
#            g.move(x = , y = , z = height)
#        elif i%2==1:
#            
#        else:
            

pad_positions=((0.1,0.4),(.1,0.7),(.1,1),(.1,1.3),(.1,1.6),(.1,1.9),
(0.4,2.2),(0.7,2.2),(1,2.2),(1.3,2.2),(1.6,2.2),(1.9,2.2),
(2.2,1.9),(2.2,1.6),(2.2,1.3),(2.2,1),(2.2,0.7),(2.2,0.4),
(1.9,0.1),(1.6,0.1),(1.3,0.1),(1,0.1),(0.7,0.1),(0.4,0.1))
#coordinates of the center of all contact pads, starting in LL (0,0) corner and going clockwise
#24 pads, 6 on each side

external_pad_positions=((-5.9,-2.6),(-5.9,-1.1),(-5.9,0.4),(-5.9,1.9),(-5.9,3.4),(-5.9,4.9),
(-2.6,6.95),(-1.1,6.95),(0.4,6.95),(1.9,6.95),(3.4,6.95),(4.9,6.95),
(6.95,4.9),(6.95,3.4),(6.95,1.9),(6.95,0.4),(6.95,-1.1),(6.95,-2.6),
(4.9,-5.9),(3.4,-5.9),(1.9,-5.9),(0.4,-5.9),(-1.1,-5.9),(-2.6,-5.9))
#coordinates of the center of all extermal connection pads, starting in LL (-5.9,-5.9) corner and going clockwise
#24 pads, 6 on each side

pyramid_positions=((0,0),(0,19.4-6),(0,38.8-12),(-19.4+6,19.4-6),(19.4-6,19.4-6))

#coordinates of the center of all contact pads, starting in LL corner and going clockwise
#24 pads, 6 on each side

def pyramids():

    for i in np.arange(10):
        if i%2==0:
            start1='LL'
            num=-1            
        else:
            start1='UR'
            num=1
        g.meander(4.4-(i*0.2),4.4-(i*0.2),0.1,start=start1)
        g.move(x=0.1*num,y=0.1*num,z=0.1)

    g.move(x=-3.6,y=3.4,z=2)
    g.abs_move(x=pyramid_positions[1][0],y=pyramid_positions[1][1])
    g.move(z=-3)
    
    for i in np.arange(10):
        if i%2==0:
            start1='LL'
            num=-1            
        else:
            start1='UR'
            num=1
        g.meander(4.4-(i*0.2),4.4-(i*0.2),0.1,start=start1)
        g.move(x=0.1*num,y=0.1*num,z=0.1)
    
    g.move(x=-3.6,y=3.4,z=2)
    g.abs_move(x=pyramid_positions[2][0],y=pyramid_positions[2][1])
    g.move(z=-3)
    
    for i in np.arange(10):
        if i%2==0:
            start1='LL'
            num=-1            
        else:
            start1='UR'
            num=1
        g.meander(4.4-(i*0.2),4.4-(i*0.2),0.1,start=start1)
        g.move(x=0.1*num,y=0.1*num,z=0.1)
    
    g.move(x=-3.6,y=3.4,z=2)
    g.abs_move(x=pyramid_positions[3][0],y=pyramid_positions[3][1])
    g.move(z=-3)

    for i in np.arange(10):
        if i%2==0:
            start1='LL'
            num=-1            
        else:
            start1='UR'
            num=1
        g.meander(4.4-(i*0.2),4.4-(i*0.2),0.1,start=start1)
        g.move(x=0.1*num,y=0.1*num,z=0.1)

    g.move(x=-3.6,y=3.4,z=2)
    g.abs_move(x=pyramid_positions[4][0],y=pyramid_positions[4][1])
    g.move(z=-3)

    for i in np.arange(10):
        if i%2==0:
            start1='LL'
            num=-1            
        else:
            start1='UR'
            num=1
        g.meander(4.4-(i*0.2),4.4-(i*0.2),0.1,start=start1)
        g.move(x=0.1*num,y=0.1*num,z=0.1)

    g.move(x=-3.6,y=3.4,z=2)

def serp_wires_pyramids():
    g.abs_move(x=1.55,y=3.2)
    g.move(z=-2.05)
    g.move(y=0.3)
    g.move(y=0.95,z=-0.95)
    
    g.move(y=0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=0,y=0.4,radius=-0.3,direction=dir)
    g.move(y=0.45)
    g.move(y=0.95,z=0.95)
    g.move(y=0.3)
    g.move(z=2.05)
   
    g.move(x=1.3)
    g.move(z=-2.05)
    g.move(y=-0.3)
    g.move(y=-0.95,z=-0.95)
    
    g.move(y=-0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=0,y=-0.4,radius=-0.3,direction=dir)
    g.move(y=-0.45)
    g.move(y=-0.95,z=0.95)
    g.move(y=-0.3)
    g.move(z=2.05)

    g.abs_move(x=pyramid_positions[3][0],y=pyramid_positions[3][1])
    g.move(x=3.2,y=1.55)
    g.move(z=-2.05)

    g.move(x=0.3)
    g.move(x=0.95,z=-0.95)

    g.move(x=0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=0.4,y=0,radius=-0.3,direction=dir)
    g.move(x=0.45)
    g.move(x=0.95,z=0.95)
    g.move(x=0.3)
    g.move(z=2.05)
   
    g.move(y=1.3)
    g.move(z=-2.05)
    g.move(x=-0.3)
    g.move(x=-0.95,z=-0.95)
    
    g.move(x=-0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=-0.4,y=0,radius=-0.3,direction=dir)
    g.move(x=-0.45)
    g.move(x=-0.95,z=0.95)
    g.move(x=-0.3)
    g.move(z=2.05)

    g.abs_move(x=pyramid_positions[1][0],y=pyramid_positions[1][1])
    g.move(x=1.55,y=3.2)
    g.move(z=-2.05)
    g.move(y=0.3)
    g.move(y=0.95,z=-0.95)
    
    g.move(y=0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=0,y=0.4,radius=-0.3,direction=dir)
    g.move(y=0.45)
    g.move(y=0.95,z=0.95)
    g.move(y=0.3)
    g.move(z=2.05)
   
    g.move(x=1.3)
    g.move(z=-2.05)
    g.move(y=-0.3)
    g.move(y=-0.95,z=-0.95)
    
    g.move(y=-0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=0,y=-0.4,radius=-0.3,direction=dir)
    g.move(y=-0.45)
    g.move(y=-0.95,z=0.95)
    g.move(y=-0.3)
    g.move(z=2.05)


    g.abs_move(x=pyramid_positions[1][0],y=pyramid_positions[1][1])
    g.move(x=3.2,y=1.55)
    g.move(z=-2.05)

    g.move(x=0.3)
    g.move(x=0.95,z=-0.95)

    g.move(x=0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=0.4,y=0,radius=-0.3,direction=dir)
    g.move(x=0.45)
    g.move(x=0.95,z=0.95)
    g.move(x=0.3)
    g.move(z=2.05)
   
    g.move(y=1.3)
    g.move(z=-2.05)
    g.move(x=-0.3)
    g.move(x=-0.95,z=-0.95)
    
    g.move(x=-0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=-0.4,y=0,radius=-0.3,direction=dir)
    g.move(x=-0.45)
    g.move(x=-0.95,z=0.95)
    g.move(x=-0.3)
    g.move(z=2.05)



    g.move(x=20,y=20)


    


def serpentine_encaps_pdms():
    g.abs_move(x=5,y=5)
    g.meander(x=12,y=10,spacing=0.3,start='LL')
    g.move(x=-6)
    g.move(y=2)
    for i in np.arange(10):
        if i%2==0:
            direc='CW'
        else:
            direc='CCW'
        g.arc(x=0,y=2.5,radius=-1.7,direction=direc)
    g.move(y=2)
    g.move(x=6)
    g.meander(x=12,y=10,spacing=0.3,start='LR')
 
      
def serpentine_encaps_wire():    
    g.abs_move(x=10,y=10)
    g.meander(x=2,y=2,spacing=0.08,start='LL')
    g.move(x=1)
    g.move(y=5)
    for i in np.arange(10):
        if i%2==0:
            direc='CW'
        else:
            direc='CCW'
        g.arc(x=0,y=2.5,radius=-1.7,direction=direc)
    g.move(y=5)
    g.move(x=-1)
    g.meander(x=2,y=2,spacing=0.08,start='LL')
    
         
                           
def MGH_print():
    #----print 4 electrodes 
    #g.set_home(x=0,y=0)
    #g.abs_move(x=3,y=24)
    #g.move(z=-5)
    #g.meander(x=3,y=3,spacing=0.3,start='UL')
    #g.move(z=5)
    #g.abs_move(x=3,y=18)
    #g.move(z=-5)
    #g.meander(x=3,y=3,spacing=0.3,start='UL')
    #g.move(z=5)
    #g.abs_move(x=3,y=12)
    #g.move(z=-5)
    #g.meander(x=3,y=3,spacing=0.3,start='UL')
    #g.move(z=5)
    #g.abs_move(x=3,y=6)
    #g.move(z=-5)
    #g.meander(x=3,y=3,spacing=0.3,start='UL')
    #g.move(z=5)
    #g.abs_move(x=0,y=0)

    #----print TPU around electrodes
    #g.move(z=-5)
    #g.meander(x=30,y=3,spacing=0.3,start='LL')
    #g.move(y=0.3)
    #g.meander(x=24,y=3,spacing=0.3,start='LR')
    #g.move(x=-3)
    #g.move(y=0.3)
    #g.meander(x=27,y=2.1,spacing=0.3,start='LL')
    #g.move(y=0.3)
    #g.meander(x=24,y=3,spacing=0.3,start='LR')
    #g.move(z=5)
    #g.abs_move(x=30,y=12.3)
    #g.move(z=-5)
    #g.meander(x=27,y=2.4,spacing=0.3,start='LR')
    #g.move(z=5)
    #g.abs_move(x=30,y=15.)
    #g.move(z=-5)
    #g.meander(x=24,y=3,spacing=0.3,start='LR')
    #g.move(z=5)
    #g.abs_move(x=30,y=18.3)
    #g.move(z=-5)
    #g.meander(x=27,y=2.4,spacing=0.3,start='LR')
    #g.move(z=5)
    #g.abs_move(x=30,y=21.)
    #g.move(z=-5)
    #g.meander(x=24,y=3,spacing=0.3,start='LR')
    #g.move(z=5)
    #g.abs_move(x=30,y=24.3)
    #g.move(z=-5)
    #g.meander(x=27,y=3,spacing=0.3,start='LR')
    #g.move(x=-0.3)
    #g.meander(x=2.7,y=24,spacing=0.3,start='UR',orientation='y')
    #g.move(z=5)

    #----print leads
#    g.abs_move(x=4.5,y=22.5)
#    g.move(z=-4.7)
#    g.move(x=6)
#    g.move(x=3,y=-5.5)
#    g.move(y=0.5)
#    g.meander(x=2,y=1,spacing=0.3,start='UL')
#    g.move(z=4.7)
#    
#    g.abs_move(x=4.5,y=16.5)
#    g.move(z=-4.7)
#    g.move(x=6)
#    g.move(x=3,y=-1.75)
#    g.move(y=0.5)
#    g.meander(x=2,y=1,spacing=0.3,start='UL')
#    g.move(z=4.7)
#
#    g.abs_move(x=4.5,y=10.5)
#    g.move(z=-4.7)
#    g.move(x=6)
#    g.move(x=3,y=1.75)
#    g.move(y=0.5)
#    g.meander(x=2,y=1,spacing=0.3,start='UL')
#    g.move(z=4.7)
#
#    g.abs_move(x=4.5,y=4.5)
#    g.move(z=-4.7)
#    g.move(x=6)
#    g.move(x=3,y=5.5)
#    g.move(y=0.5)
#    g.meander(x=2,y=1,spacing=0.3,start='UL')
#    g.move(z=4.7)


    #----print TPU cover
    g.abs_move(x=0,y=0)
    g.move(z=-4.4)
    g.meander(x=30,y=9.2,spacing=0.3,start='LL')
    g.move(y=0.3)
    g.meander(x=13.4,y=1,spacing=0.3,start='LL')
    g.move(z=4.4)
    g.move(x=-13.4,y=0.3)
    g.move(z=-4.4)
    g.meander(x=15.5,y=0.8,spacing=0.3,start='LL')
    g.move(y=0.3)
    g.meander(x=13.4,y=1,spacing=0.3,start='LL')
    g.move(x=2.1)
    g.move(y=0.3)
    g.meander(x=15.5,y=0.8,spacing=0.3,start='LR')
    g.move(z=4.4)
    g.move(x=-15.5,y=0.3)
    g.move(z=-4.4)
    g.meander(x=13.4,y=1,spacing=0.3,start='LL')
    g.move(z=4.4)
    g.move(x=-13.4,y=0.2)
    g.move(z=-4.4)
    g.meander(x=15.5,y=0.8,spacing=0.3,start='LL')
    g.move(y=0.3)
    g.meander(x=13.4,y=1,spacing=0.3,start='LL')
    g.move(x=-13.4)
    g.meander(x=30,y=10,spacing=0.3,start='LL')
    g.move(z=4.4)
    g.move(y=-10.3)
    g.move(z=-4.4)
    g.meander(x=14.5,y=8,spacing=0.3,start='UR')
    

    g.move(z=3)

def print_die():
    #g.abs_move(x=0,y=0)
    #g.abs_move(x=0.38,y=0.1)
    #g.move(x=0.1,y=0.1)
    #g.rect(x=0.2,y=0.2)
    #g.meander(x=0.2,y=0.2,spacing=0.05,start='LL',orientation='y')
    #g.move(x=-0.1) #x=380,y=200
    #
    #g.move(y=0.18) 
    #g.move(x=-0.18)
    #
    #g.move(y=0.1)
    #g.meander(x=0.2,y=0.2,spacing=0.05,start='UR',orientation='y')
    #g.clip(axis='z',direction='-x',height=1 )

    for i in np.arange(2):
        for j in np.arange(6):
            if i==0:
                g.move(z=0.5)
                g.abs_move(x=pad_positions[23-j][0],y=pad_positions[23-j][1])
                g.move(z=-0.5)
                g.move(x=0.075,y=0.075)
                g.rect(x=0.15,y=0.15,start='UR')
                g.move(x=-0.05,y=-0.05)
                g.rect(x=0.05,y=0.05,start='UR')
                g.move(x=-0.025,y=-0.025)
                if j<3:
                    g.move(y=pad_positions[j][1]-pad_positions[23-j][1])
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[j][0]))
                    g.move(x=0.025,y=0.025)
                    g.rect(x=0.05,y=0.05,start='UR')
                    g.move(x=0.05,y=0.05)
                    g.rect(x=0.15,y=0.15,start='UR')
                    g.move(x=-0.075,y=-0.075)
                else:
                    g.move(y=pad_positions[12+j][1]-pad_positions[23-j][1])
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[12+j][0]))
                    g.move(x=0.025,y=0.025)
                    g.rect(x=0.05,y=0.05,start='UR')
                    g.move(x=0.05,y=0.05)
                    g.rect(x=0.15,y=0.15,start='UR')
                    g.move(x=-0.075,y=-0.075)
            else:
                g.move(z=0.5)
                g.abs_move(x=pad_positions[6+j][0],y=pad_positions[6+j][1])
                g.move(z=-0.5)
                g.move(x=0.075,y=0.075)
                g.rect(x=0.15,y=0.15,start='UR')
                g.move(x=-0.05,y=-0.05)
                g.rect(x=0.05,y=0.05,start='UR')
                g.move(x=-0.025,y=-0.025)
                if j<3:
                    g.move(y=-(pad_positions[j][1]-pad_positions[23-j][1]))
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[j][0]))
                    g.move(x=0.025,y=0.025)
                    g.rect(x=0.05,y=0.05,start='UR')
                    g.move(x=0.05,y=0.05)
                    g.rect(x=0.15,y=0.15,start='UR')
                    g.move(x=-0.075,y=-0.075)
                else:
                    g.move(y=-(pad_positions[12+j][1]-pad_positions[23-j][1]))
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[12+j][0]))
                    g.move(x=0.025,y=0.025)
                    g.rect(x=0.05,y=0.05,start='UR')
                    g.move(x=0.05,y=0.05)
                    g.rect(x=0.15,y=0.15,start='UR')
                    g.move(x=-0.075,y=-0.075)
    g.move(z=0.5)
    
    
def print_die_wiring(valve,nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    #pressure_purge(delay = 2)
    for i in np.arange(2):        
        for j in np.arange(6):
                if i==0:
                    g.abs_move(**{nozzle:5})
                    g.abs_move(x=pad_positions[23-j][0],y=pad_positions[23-j][1])
                    g.abs_move(**{nozzle:height})
                    if valve is not None:
                        g.set_valve(num = valve, value = 1)
                    g.dwell(dwell)
                    g.feed(speed)
                    g.move(y=-3)
                    if j<3:
                        g.abs_move(x=external_pad_positions[23-j][0],y=external_pad_positions[23-j][1])
                        g.set_valve(num = valve, value = 0)
                        g.feed(15)
                        g.clip(axis=nozzle, height=5)
                    else:
                        g.abs_move(x=external_pad_positions[23-j][0],y=external_pad_positions[23-j][1])
                        g.set_valve(num = valve, value = 0)
                        g.feed(15)
                        g.clip(axis=nozzle, height=5)
                else:
                    g.abs_move(**{nozzle:5})
                    g.abs_move(x=pad_positions[6+j][0],y=pad_positions[6+j][1])
                    g.abs_move(**{nozzle:height})
                    if valve is not None:
                        g.set_valve(num = valve, value = 1)
                    g.dwell(dwell)
                    g.feed(speed)
                    g.move(y=3)
                    if j<3:
                        g.abs_move(x=external_pad_positions[6+j][0],y=external_pad_positions[6+j][1])
                        g.set_valve(num = valve, value = 0)
                        g.feed(15)
                        g.clip(axis=nozzle, height=5)
                    else:
                        g.abs_move(x=external_pad_positions[6+j][0],y=external_pad_positions[6+j][1])
                        g.set_valve(num = valve, value = 0)
                        g.feed(15)
                        g.clip(axis=nozzle, height=5)
    for i in np.arange(2):        
        for j in np.arange(6):
                if i==0:
                    g.abs_move(**{nozzle:5})
                    g.abs_move(x=pad_positions[j][0],y=pad_positions[j][1])
                    g.abs_move(**{nozzle:height})
                    if valve is not None:
                        g.set_valve(num = valve, value = 1)
                    g.dwell(dwell)
                    g.feed(speed)
                    g.move(x=-3)
                    if j<3:
                        g.abs_move(x=external_pad_positions[j][0],y=external_pad_positions[j][1])
                        g.set_valve(num = valve, value = 0)
                        g.feed(15)
                        g.clip(axis=nozzle, height=5)
                    else:
                        g.abs_move(x=external_pad_positions[j][0],y=external_pad_positions[j][1])
                        g.set_valve(num = valve, value = 0)
                        g.feed(15)
                        g.clip(axis=nozzle, height=5)
                else:
                    g.abs_move(**{nozzle:5})
                    g.abs_move(x=pad_positions[17-j][0],y=pad_positions[17-j][1])
                    g.abs_move(**{nozzle:height})
                    if valve is not None:
                        g.set_valve(num = valve, value = 1)
                    g.dwell(dwell)
                    g.feed(speed)
                    g.move(x=3)
                    if j<3:
                        g.abs_move(x=external_pad_positions[17-j][0],y=external_pad_positions[17-j][1])
                        g.set_valve(num = valve, value = 0)
                        g.feed(15)
                        g.clip(axis=nozzle, height=5)
                    else:
                        g.abs_move(x=external_pad_positions[17-j][0],y=external_pad_positions[17-j][1])
                        g.set_valve(num = valve, value = 0)
                        g.feed(15)
                        g.clip(axis=nozzle, height=5)
 
def bacteria_electrodes(valve,nozzle,height,speed,dwell,pressure,spacing):#
    g.feed(25)
    g.set_pressure(pressure_box, pressure)

    #########test line
    g.abs_move(x=2.5,y=3)
    #pressure_purge(delay = 2)
    g.abs_move(**{nozzle:height})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed)
    g.move(y=20)
    g.feed(20)
    g.clip(axis=nozzle, height=6, direction='-x')
    g.set_pressure(pressure_box, pressure)
    
    g.abs_move(x=10,y=1.5)
    g.set_home(x=0, y=0)
    g.move(y=2)   #starts first electrode farther up to avoid short circuit
    #g.move(x=14.4)
    #Print start
    if spacing=='400':    
        top_electrode_connection=20.4
        bottom_electrode_connection=0
        for i in range(25):
            g.abs_move(**{nozzle:height}) 
            g.feed(speed)
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.abs_move(y=top_electrode_connection)
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, height=2, direction='-y')
            g.move(x=0.4,y=-0.4)
            g.abs_move(**{nozzle:height})
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.abs_move(y=bottom_electrode_connection)
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, height=2, direction='+y')
            if i<24:
                g.move(x=0.4,y=0.4)
        #
        g.abs_move(x=0,y=0)
        g.abs_move(**{nozzle:height}) 
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.feed(speed*0.3)
        g.abs_move(x=20.4,y=0)
        g.move(x=4,y=-4)
        g.feed(speed*0.2)
        g.arc(x=1.,y=0,radius=0.5)
        g.arc(x=-1.,y=0,radius=0.5)
        g.move(x=0.2)
        g.arc(x=0.6,y=0,radius=0.3)
        g.arc(x=-0.6,y=0,radius=0.3)
        g.move(x=0.2)
        g.arc(x=0.2,y=0,radius=0.1)
        g.arc(x=-0.2,y=0,radius=0.1)
        g.set_valve(num = valve, value = 0)
        g.clip(axis=nozzle, height=2, direction='+y')

        
        g.abs_move(x=0.2,y=20.4)
        g.abs_move(**{nozzle:height}) 
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.feed(speed*0.3)
        g.dwell(dwell)
        g.feed(speed*0.2)
        g.abs_move(x=20.4)
        g.move(x=4,y=4)
        g.feed(speed*0.2)
        g.arc(x=1.,y=0,radius=0.5)
        g.arc(x=-1.,y=0,radius=0.5)
        g.move(x=0.2)
        g.arc(x=0.6,y=0,radius=0.3)
        g.arc(x=-0.6,y=0,radius=0.3)
        g.move(x=0.2)
        g.arc(x=0.2,y=0,radius=0.1)
        g.arc(x=-0.2,y=0,radius=0.1)
        g.set_valve(num = valve, value = 0)
        g.clip(axis=nozzle, height=2, direction='-y')
        #
    elif spacing=='200':
        top_electrode_connection=20.4
        bottom_electrode_connection=0
        for i in range(50):
            g.abs_move(**{nozzle:height}) 
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.abs_move(y=top_electrode_connection)
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, height=2, direction='+y')
            g.move(x=0.2,y=-0.4)
            g.abs_move(**{nozzle:height})
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.abs_move(y=bottom_electrode_connection)
            if i<49:
                g.move(x=0.2,y=0.4)
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, height=2, direction='-y')        
        g.abs_move(x=0,y=0)
        g.abs_move(**{nozzle:height}) 
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.feed(speed*0.4)
        g.abs_move(x=22.4)
        g.feed(speed*0.2)
        g.arc(x=1.,y=0,radius=0.5)
        g.arc(x=-1.,y=0,radius=0.5)
        g.move(x=0.2)
        g.arc(x=0.6,y=0,radius=0.3)
        g.arc(x=-0.6,y=0,radius=0.3)
        g.move(x=0.2)
        g.arc(x=0.2,y=0,radius=0.1)
        g.arc(x=-0.2,y=0,radius=0.1)
        g.set_valve(num = valve, value = 0)
        g.clip(axis=nozzle, height=2, direction='-y')

        g.feed(speed)
        g.abs_move(x=0,y=20.4)
        g.abs_move(**{nozzle:height}) 
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell*0.4)
        g.feed(speed)
        g.abs_move(x=22.4)
        g.feed(speed*0.2)
        g.arc(x=1.,y=0,radius=0.5)
        g.arc(x=-1.,y=0,radius=0.5)
        g.move(x=0.2)
        g.arc(x=0.6,y=0,radius=0.3)
        g.arc(x=-0.6,y=0,radius=0.3)
        g.move(x=0.2)
        g.arc(x=0.2,y=0,radius=0.1)
        g.arc(x=-0.2,y=0,radius=0.1)
        g.set_valve(num = valve, value = 0)
        g.clip(axis=nozzle, height=2, direction='-y')
    
    
def stretchy_matrix_circle(valve,nozzle,height,speed,dwell,pressure,nozzle_diameter,dye,stiffness):#
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    filament_diameter = nozzle_diameter*1.3
    global count

    if stiffness=='hard':
        if dye == 'yes':
            count=0                    
            g.abs_move(x=34,y=25)
            g.abs_move(**{nozzle:height})
            g.feed(speed)
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.set_valve(num = valve, value = 0)
            g.feed(25)
            g.abs_move(**{nozzle:5})
            count=1
            for i in range(3):            
                g.move(x=2*filament_diameter)
                g.abs_move(**{nozzle:height})
                g.feed(speed)
                if valve is not None:
                    g.set_valve(num = valve, value = 1)
                g.dwell(dwell)
                g.arc(x=0,y=0.0001,radius=-((2*filament_diameter)*(i+1)),direction='CW')
                g.set_valve(num = valve, value = 0)
                g.feed(25)
                g.abs_move(**{nozzle:5}) 
                count+=1          
            g.feed(25)
            g.clip(axis=nozzle, height=6, direction='-x')
            g.set_pressure(pressure_box, pressure)
    
        else:
            g.abs_move(x=34,y=25)
            g.abs_move(**{nozzle:5})
            g.move(x=filament_diameter)
            g.abs_move(**{nozzle:height})
            g.feed(speed)
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.arc(x=0,y=0.0001,radius=-((filament_diameter)),direction='CW')
            g.set_valve(num = valve, value = 0)
            g.feed(25)
            g.abs_move(**{nozzle:5}) 
            count+=1
            for i in range(1,7,2):            
                g.move(x=2*filament_diameter)            
                g.abs_move(**{nozzle:height})
                g.feed(speed)
                if valve is not None:
                    g.set_valve(num = valve, value = 1)
                g.dwell(dwell)
                g.arc(x=0,y=0.0001,radius=-((filament_diameter)*(i+2)),direction='CW')
                g.set_valve(num = valve, value = 0)
                g.feed(25)
                g.abs_move(**{nozzle:5}) 
                count+=1
            g.feed(25)
            g.clip(axis=nozzle, height=6, direction='-x')
            g.set_pressure(pressure_box, pressure)
    
    else:
        if dye == 'yes':
            g.abs_move(x=34,y=25)
            g.abs_move(**{nozzle:5})
            g.move(x=count*filament_diameter)
            g.abs_move(**{nozzle:height})
            g.feed(speed)
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.arc(x=0,y=0.0001,radius=-((filament_diameter)*count),direction='CW')
            g.set_valve(num = valve, value = 0)
            g.feed(25)
            g.abs_move(**{nozzle:5}) 

            for i in range(count,count+6,2):            
                g.move(x=2*filament_diameter)
                g.abs_move(**{nozzle:height})
                g.feed(speed)
                if valve is not None:
                    g.set_valve(num = valve, value = 1)
                g.dwell(dwell)
                g.arc(x=0,y=0.0001,radius=-((filament_diameter)*(i+2)),direction='CW')
                g.set_valve(num = valve, value = 0)
                g.feed(25)
                g.abs_move(**{nozzle:5})           
            g.feed(25)
            g.clip(axis=nozzle, height=6, direction='-x')
            g.set_pressure(pressure_box, pressure)
    
        else:
            g.abs_move(x=34,y=25)
            g.abs_move(**{nozzle:5})
            g.move(x=(count+1)*filament_diameter)
            g.abs_move(**{nozzle:height})
            g.feed(speed)
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.arc(x=0,y=0.0001,radius=-((filament_diameter)*(count+1)),direction='CW')
            g.set_valve(num = valve, value = 0)
            g.feed(25)
            g.abs_move(**{nozzle:5}) 

            for i in range((count+1),(count+1)+6,2):            
                g.move(x=2*filament_diameter)
                g.abs_move(**{nozzle:height})
                g.feed(speed)
                if valve is not None:
                    g.set_valve(num = valve, value = 1)
                g.dwell(dwell)
                g.arc(x=0,y=0.0001,radius=-((filament_diameter)*(i+2)),direction='CW')
                g.set_valve(num = valve, value = 0)
                g.feed(25)
                g.abs_move(**{nozzle:5})           
            g.feed(25)
            g.clip(axis=nozzle, height=6, direction='-x')
            g.set_pressure(pressure_box, pressure)

def stretchy_matrix_square(valve,nozzle,height,speed,dwell,pressure,nozzle_diameter,dye,stiffness):#
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    filament_diameter = nozzle_diameter*1.3
    global count

    if stiffness=='hard':
        if dye == 'yes':
            count=0                    
            g.abs_move(x=34,y=25)
            g.abs_move(**{nozzle:height})
            g.feed(speed)
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.set_valve(num = valve, value = 0)
            g.feed(25)
            g.abs_move(**{nozzle:5})
            count=1
            for i in range(3):            
                g.move(x=-2*filament_diameter*np.sqrt(2),y=-2*filament_diameter*np.sqrt(2))
                g.abs_move(**{nozzle:height})
                g.feed(speed)
                if valve is not None:
                    g.set_valve(num = valve, value = 1)
                g.dwell(dwell)
                g.rect(x=((2*filament_diameter)*(i+1)),y=((2*filament_diameter)*(i+1)))
                g.set_valve(num = valve, value = 0)
                g.feed(25)
                g.abs_move(**{nozzle:5}) 
                count+=1           
            g.feed(25)
            g.clip(axis=nozzle, height=6, direction='-x')
            g.set_pressure(pressure_box, pressure)
    
        else:
            g.abs_move(x=34,y=25)
            g.abs_move(**{nozzle:5})
            g.move(x=filament_diameter)
            g.abs_move(**{nozzle:height})
            g.feed(speed)
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.arc(x=0,y=0.0001,radius=-((filament_diameter)),direction='CW')
            g.set_valve(num = valve, value = 0)
            g.feed(25)
            g.abs_move(**{nozzle:5}) 
            count+=1
            for i in range(1,7,2):            
                g.move(x=2*filament_diameter)            
                g.abs_move(**{nozzle:height})
                g.feed(speed)
                if valve is not None:
                    g.set_valve(num = valve, value = 1)
                g.dwell(dwell)
                g.arc(x=0,y=0.0001,radius=-((filament_diameter)*(i+2)),direction='CW')
                g.set_valve(num = valve, value = 0)
                g.feed(25)
                g.abs_move(**{nozzle:5}) 
                count+=1
            g.feed(25)
            g.clip(axis=nozzle, height=6, direction='-x')
            g.set_pressure(pressure_box, pressure)
    
    else:
        if dye == 'yes':
            g.abs_move(x=34,y=25)
            g.abs_move(**{nozzle:5})
            g.move(x=count*filament_diameter)
            g.abs_move(**{nozzle:height})
            g.feed(speed)
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.arc(x=0,y=0.0001,radius=-((filament_diameter)*count),direction='CW')
            g.set_valve(num = valve, value = 0)
            g.feed(25)
            g.abs_move(**{nozzle:5}) 

            for i in range(count,count+6,2):            
                g.move(x=2*filament_diameter)
                g.abs_move(**{nozzle:height})
                g.feed(speed)
                if valve is not None:
                    g.set_valve(num = valve, value = 1)
                g.dwell(dwell)
                g.arc(x=0,y=0.0001,radius=-((filament_diameter)*(i+2)),direction='CW')
                g.set_valve(num = valve, value = 0)
                g.feed(25)
                g.abs_move(**{nozzle:5})           
            g.feed(25)
            g.clip(axis=nozzle, height=6, direction='-x')
            g.set_pressure(pressure_box, pressure)
    
        else:
            g.abs_move(x=34,y=25)
            g.abs_move(**{nozzle:5})
            g.move(x=(count+1)*filament_diameter)
            g.abs_move(**{nozzle:height})
            g.feed(speed)
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.arc(x=0,y=0.0001,radius=-((filament_diameter)*(count+1)),direction='CW')
            g.set_valve(num = valve, value = 0)
            g.feed(25)
            g.abs_move(**{nozzle:5}) 

            for i in range((count+1),(count+1)+6,2):            
                g.move(x=2*filament_diameter)
                g.abs_move(**{nozzle:height})
                g.feed(speed)
                if valve is not None:
                    g.set_valve(num = valve, value = 1)
                g.dwell(dwell)
                g.arc(x=0,y=0.0001,radius=-((filament_diameter)*(i+2)),direction='CW')
                g.set_valve(num = valve, value = 0)
                g.feed(25)
                g.abs_move(**{nozzle:5})           
            g.feed(25)
            g.clip(axis=nozzle, height=6, direction='-x')
            g.set_pressure(pressure_box, pressure)




 
##third line of notches
#g.move(0.1,0.1,0.1)
#g.move(1)
#g.move(y=0.1)
#g.move(0.2)
#g.move(y=-0.1)
#g.move(1.0)
#g.move(y=0.1)
#g.move(0.2)
#g.move(y=-0.1)
#g.move(1)
#g.move(y=0.1)
#
##third layer of fill
#g.meander(4.,3.9,0.1,start="LR")
#
#g.move(-0.1,-0.1,0.1)
#
##fourth layer of fill
#g.meander(3.8,3.7,0.1,start="UR")
#



#g.move(-0.1,-0.1,0.1)
#g.meander(4.2,4.2,0.1,start='UR')
#g.move(0.1,0.1,0.1)
#g.meander(4,4,0.1)
#g.move(-0.1,-0.1,0.1)
#g.meander(3.8,3.8,0.1,start='UR')
#g.move(0.1,0.1,0.1)
#g.meander(3.6,3.6,0.1)
#g.move(-0.1,-0.1,0.1)
#g.meander(3.4,3.4,0.1,start='UR')
#g.move(0.1,0.1,0.1)
#g.meander(3.2,3.2,0.1)
#g.move(-0.1,-0.1,0.1)
#g.meander(3.,3.,0.1,start='UR')
#g.move(0.1,0.1,0.1)
#g.meander(2.8,2.8,0.1)
#g.move(-0.1,-0.1,0.1)
#g.meander(2.6,2.6,0.1,start='UR')
#g.move(0.1,0.1,0.1)

#g.move(-1.1,-1.1,1)
#g.meander(2.4,2.4,0.1,start='UR')


#
#g.set_home(x=0, y=0, z=0)
##
#g.set_pressure(pressure_box, pressure)
#g.toggle_pressure(pressure_box)
#first_print()
#MGH_print()
#g.toggle_pressure(pressure_box)

#print_die()
#print_die_wiring(valve='1',nozzle='A',height=0.015,speed=0.6,dwell=0.7,pressure=16)
#pyramids()
#serp_wires_pyramids()
#serpentine_encaps_pdms()
#serpentine_encaps_wire()
#bacteria_electrodes(valve='1',nozzle='A',height=0.02,speed=3.5,dwell=0.3,pressure=54,spacing='400')

#stretchy_matrix_circle(valve='1',nozzle='z',height=0.02,speed=3.5,dwell=0.3,pressure=54,nozzle_diameter=.310,stiffness='hard',dye='yes')
#stretchy_matrix_circle(valve='1',nozzle='z',height=0.02,speed=3.5,dwell=0.3,pressure=54,nozzle_diameter=.310,stiffness='hard',dye='no')
#stretchy_matrix_circle(valve='1',nozzle='z',height=0.02,speed=3.5,dwell=0.3,pressure=54,nozzle_diameter=.310,stiffness='soft',dye='yes')
#stretchy_matrix_circle(valve='1',nozzle='z',height=0.02,speed=3.5,dwell=0.3,pressure=54,nozzle_diameter=.310,stiffness='soft',dye='no')
#stretchy_matrix_square(valve='1',nozzle='z',height=0.02,speed=3.5,dwell=0.3,pressure=54,nozzle_diameter=.310,stiffness='hard',dye='yes')

#g.view(backend='matplotlib')


g.teardown()

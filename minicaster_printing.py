from mecode import G
import numpy as np

#outfile = r"/Volumes/group0/jlewis/User Files/Valentine/AFRL/my_print.pgm"
outfile = r'C:\Users\User\Documents\GitHub\MINICASTER_PRINTING\myprint1.pgm'


#Defining mecode parameters
g = G(
    direct_write=False,
    outfile=outfile,
    header=None,
    footer=None,
    print_lines=False,
    )

pad_positions=((0.1,0.38+0.28*0),(.1,0.38+0.28*1),(.1,0.38+0.28*2),(.1,0.38+0.28*3),(.1,0.38+0.28*4),(.1,0.38+0.28*5),
(0.38+0.28*0,2.06),(0.38+0.28*1,2.06),(0.38+0.28*2,2.06),(0.38+0.28*3,2.06),(0.38+0.28*4,2.06),(0.38+0.28*5,2.06),
(2.06,0.38+0.28*5),(2.06,0.38+0.28*4),(2.06,0.38+0.28*3),(2.06,0.38+0.28*2),(2.06,0.38+0.28*1),(2.06,0.38+0.28*0),
(0.38+0.28*5,0.1),(0.38+0.28*4,0.1),(0.38+0.28*3,0.1),(0.38+0.28*2,0.1),(0.38+0.28*1,0.1),(0.38+0.28*0,0.1))



ATMEGA328_pad_positions = (

((0.2,7.3),(0.2,6.5),(0.2,5.7),(0.2,4.9),(0.2,4.1),(0.2,3.3),(0.2,2.5),(0.2,1.7)),
((1.7,0.2),(2.5,0.2),(3.3,0.2),(4.1,0.2),(4.9,0.2),(5.7,0.2),(6.5,0.2),(7.3,0.2)),
((8.8,1.7),(8.8,2.5),(8.8,3.3),(8.8,4.1),(8.8,4.9),(8.8,5.7),(8.8,6.5),(8.8,7.3)),
((7.3,8.8),(6.5,8.8),(5.7,8.8),(4.9,8.8),(4.1,8.8),(3.3,8.8),(2.5,8.8),(1.7,8.8))

)


pressure_box = 4
pdms_pressure = 13

def print_die(speed,dwell):
    g.set_home(x=0,y=0)
    g.set_pressure(pressure_box, pdms_pressure)   
    g.feed(5)
    g.move(z=2)
    for i in np.arange(2):
        for j in np.arange(6):
            if i==0:
                g.abs_move(x=pad_positions[23-j][0],y=pad_positions[23-j][1])
                g.move(z=-2)
                g.feed(speed)
                g.toggle_pressure(pressure_box)
                g.dwell(dwell)
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
                    g.toggle_pressure(pressure_box)
                    g.feed(10)
                    g.clip(height=2, direction='-x')
                else:
                    g.move(y=pad_positions[12+j][1]-pad_positions[23-j][1])
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[12+j][0]))
                    g.move(x=0.025,y=0.025)
                    g.rect(x=0.05,y=0.05,start='UR')
                    g.move(x=0.05,y=0.05)
                    g.rect(x=0.15,y=0.15,start='UR')
                    g.move(x=-0.075,y=-0.075)
                    g.toggle_pressure(pressure_box)
                    g.feed(10)
                    g.clip(height=2, direction='-x')
            else:
                g.abs_move(x=pad_positions[6+j][0],y=pad_positions[6+j][1])
                g.move(z=-2)
                g.feed(speed)
                g.toggle_pressure(pressure_box)
                g.dwell(dwell)
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
                    g.toggle_pressure(pressure_box)
                    g.feed(10)
                    g.clip(height=2, direction='-x')
                else:
                    g.move(y=-(pad_positions[12+j][1]-pad_positions[23-j][1]))
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[12+j][0]))
                    g.move(x=0.025,y=0.025)
                    g.rect(x=0.05,y=0.05,start='UR')
                    g.move(x=0.05,y=0.05)
                    g.rect(x=0.15,y=0.15,start='UR')
                    g.move(x=-0.075,y=-0.075)
                    g.toggle_pressure(pressure_box)
                    g.feed(10)
                    g.clip(height=2, direction='-x')
   # g.move(z=0.5)

def print_die_wiring(speed,dwell):
    #g.set_pressure(pressure_box, pdms_pressure)   
    g.feed(5)
    for i in np.arange(2):        
        for j in np.arange(6):
                if i==0:
                    g.abs_move(x=pad_positions[23-j][0],y=pad_positions[23-j][1])
                    g.move(z=-2)
                    g.feed(speed)
                    #g.toggle_pressure(pressure_box)
                    g.dwell(dwell)
                    g.move(y=-3)
                    if j<3:
                        g.move(x=-3/(j+1),y=-3)
                        #g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                    else:
                        g.move(x=(j+1)-3,y=-3)
                        #g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                else:
                    g.abs_move(x=pad_positions[6+j][0],y=pad_positions[6+j][1])
                    g.move(z=-2)
                    g.feed(speed)
                    #g.toggle_pressure(pressure_box)
                    g.dwell(dwell)
                    g.move(y=3)
                    if j<3:
                        g.move(x=-3/(j+1),y=3)
                        #g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                    else:
                        g.move(x=(j+1)-3,y=3)
                        #g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                        
    for i in np.arange(2):        
        for j in np.arange(6):
                if i==0:
                    g.abs_move(x=pad_positions[j][0],y=pad_positions[j][1])
                    g.move(z=-2)
                    g.feed(speed)
                    #g.toggle_pressure(pressure_box)
                    g.dwell(dwell)                    
                    g.move(x=-3)
                    if j<3:
                        g.move(x=-3,y=-3/(j+1))
                        #g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                    else:
                        g.move(x=-3,y=(j+1)-3)
                        #g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                else:
                    g.abs_move(x=pad_positions[17-j][0],y=pad_positions[17-j][1])
                    g.move(z=-2)
                    g.feed(speed)
                    #g.toggle_pressure(pressure_box)
                    g.dwell(dwell) 
                    g.move(x=3)
                    if j<3:
                        g.move(x=3,y=-3/(j+1))
                        #g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                    else:
                        g.move(x=3,y=(j+1)-3)
                        #g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
def LONG_serpentine_encaps_pdms(nozzle,valve,pressure,speed,height):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    g.abs_move(x=5,y=5)
    g.abs_move(**{nozzle:height})  
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.feed(speed)
    g.dwell(0.8)
    g.meander(x=10,y=12,spacing=0.26,start='LL',orientation='y')
    g.move(y=6)
    g.feed(speed/1.6)
    g.move(x=2)
    g.feed(speed/2)
    for i in np.arange(13):
        if i%2==0:
            direc='CW'
        else:
            direc='CCW'
        g.arc(y=0,x=2.5,radius=-1.7,direction=direc)
    for i in np.arange(4):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=0.8,x=2.5,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=1.5,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=0.8,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=0,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=-0.8,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=-1.5,radius=-1.7,direction=direc)
    for i in np.arange(4):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=0.8,x=-2.5,radius=-1.7,direction=direc)
    for i in np.arange(13):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=0,x=-2.5,radius=-1.7,direction=direc)
    g.move(x=-2)
    g.feed(speed)
    g.move(y=6)
    g.meander(x=10,y=-12,spacing=0.25,start='LR',orientation='y')
    g.set_valve(num = valve, value = 0)
    g.clip(axis=nozzle, direction='-y', height=20)
      
def SHORT_serpentine_encaps_wire(nozzle,valve,pressure,speed,height):    
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    g.abs_move(x=10,y=10)
    g.abs_move(**{nozzle:height})  
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.feed(speed)
    g.dwell(1.3)
    g.meander(x=2,y=2,spacing=0.08,start='LL',orientation='y')
    g.move(y=1)
    g.move(x=5)
    for i in np.arange(10):
        if i%2==0:
            direc='CW'
        else:
            direc='CCW'
        g.arc(x=2.5,y=0,radius=-1.7,direction=direc)
    g.move(x=5)
    g.move(y=-1)
    g.meander(x=2,y=2,spacing=0.08,start='LL',orientation='y')
    g.set_valve(num = valve, value = 0)
    g.clip(axis=nozzle, direction='-y', height=20)

def LONG_serpentine_encaps_wire(nozzle,valve,pressure,speed,height):    
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    g.abs_move(x=10,y=10)
    g.abs_move(**{nozzle:height})  
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.feed(speed)
    g.dwell(1.7)
    g.meander(x=2,y=2,spacing=0.08,start='LL',orientation='y')
    g.move(y=1)
    g.move(x=5)
    g.abs_move(**{nozzle:height-0.04})  
    for i in np.arange(13):
        if i%2==0:
            direc='CW'
        else:
            direc='CCW'
        g.arc(y=0,x=2.5,radius=-1.7,direction=direc)
    for i in np.arange(4):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=0.8,x=2.5,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=1.5,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=0.8,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=0,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=-0.8,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=-1.5,radius=-1.7,direction=direc)
    for i in np.arange(4):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=0.8,x=-2.5,radius=-1.7,direction=direc)
    for i in np.arange(13):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=0,x=-2.5,radius=-1.7,direction=direc)
    g.abs_move(**{nozzle:height+0.04})  
    g.move(x=-5)
    g.move(y=-1)
    g.meander(x=2,y=2,spacing=0.08,start='LR',orientation='y')
    g.set_valve(num = valve, value = 0)
    g.clip(axis=nozzle, direction='-y', height=20)

def bacteria_electrodes(valve,nozzle,height,speed,dwell,pressure,spacing):#
    g.feed(25)
    g.set_pressure(pressure_box, pressure)

    #########test line
    #g.abs_move(**{nozzle:5})
    #g.abs_move(x=2,y=25)
    ##pressure_purge(delay = 2)
    #g.abs_move(**{nozzle:height})
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.feed(speed)
    #g.move(y=-20)
    #g.feed(20)
    #g.toggle_pressure(pressure_box)
    #g.clip(axis=nozzle, height=6, direction='-x')
    #g.set_pressure(pressure_box, pressure)
    ##
    #g.abs_move(x=25,y=15)
    #g.set_home(x=0, y=0)
    g.abs_move(x=0,y=0)
    g.move(y=2)
    #g.move(y=2)   #starts first electrode farther up to avoid short circuit
    
    ######Print start
    if spacing=='400':    
        top_electrode_connection=20.4
        bottom_electrode_connection=0
        for i in range(25):
            g.abs_move(**{nozzle:height}) 
            g.feed(speed)
            g.toggle_pressure(pressure_box)
            g.dwell(dwell)
            g.feed(speed*0.7)
            g.move(y=3)
            g.feed(speed)
            g.abs_move(y=top_electrode_connection)
            g.toggle_pressure(pressure_box)
            g.feed(20)
            g.clip(axis=nozzle, height=2, direction='+y')
            g.move(x=0.4,y=-0.4)            
            g.abs_move(**{nozzle:height})
            g.feed(speed)            
            g.toggle_pressure(pressure_box)
            g.dwell(dwell)
            g.feed(speed*0.7)
            g.move(y=-3)
            g.feed(speed)            
            g.abs_move(y=bottom_electrode_connection)
            g.toggle_pressure(pressure_box)
            g.feed(20)
            g.clip(axis=nozzle, height=2, direction='-y')
            if i<24:
                g.move(x=0.4,y=0.4)
        
        g.abs_move(x=0,y=0)
        g.move(y=-0.1)
        g.abs_move(**{nozzle:height}) 
        g.toggle_pressure(pressure_box)
        g.dwell(dwell)
        g.feed(speed*0.3)
        g.abs_move(x=20.4)
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
        g.toggle_pressure(pressure_box)
        g.clip(axis=nozzle, height=2, direction='+y')
        g.feed(20)

        
        g.abs_move(x=0.2,y=20.4)
        g.move(y=0.1)
        g.abs_move(**{nozzle:height}) 
        g.toggle_pressure(pressure_box)
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
        g.toggle_pressure(pressure_box)
        g.clip(axis=nozzle, height=2, direction='-y')
        #
    elif spacing=='200':
        top_electrode_connection=20.4
        bottom_electrode_connection=0
        for i in range(50):
            g.abs_move(**{nozzle:height}) 
            g.toggle_pressure(pressure_box)
            g.dwell(dwell)
            g.abs_move(y=top_electrode_connection)
            g.toggle_pressure(pressure_box)
            g.clip(axis=nozzle, height=2, direction='+y')
            g.move(x=0.2,y=-0.4)
            g.abs_move(**{nozzle:height})
            g.toggle_pressure(pressure_box)
            g.dwell(dwell)
            g.abs_move(y=bottom_electrode_connection)
            if i<49:
                g.move(x=0.2,y=0.4)
            g.toggle_pressure(pressure_box)
            g.clip(axis=nozzle, height=2, direction='-y')        
        g.abs_move(x=0,y=0)
        g.abs_move(**{nozzle:height}) 
        g.toggle_pressure(pressure_box)
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
        g.toggle_pressure(pressure_box)
        g.clip(axis=nozzle, height=2, direction='-y')

        g.feed(speed)
        g.abs_move(x=0,y=20.4)
        g.move(y=0.1)
        g.abs_move(**{nozzle:height}) 
        g.toggle_pressure(pressure_box)
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
        g.toggle_pressure(pressure_box)
        g.clip(axis=nozzle, height=2, direction='-y')
    
    
def tpu_square(valve,nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    g.set_home(x=0,y=0,z=0)
    g.move(**{nozzle:3})
    #g.dwell(5)
   
 ########test line
    g.move(x=3,y=3)
    #pressure_purge(delay = 2)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=8)
    g.move(y=0.2)
    g.move(x=-8)
    g.move(y=0.2)
    g.feed(20)
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=3, direction='-x')
    

    g.move(x=2,y=2)  # move to the silver pattern's corner
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(x=1,y=1)   #offset for cover
    
    g.meander(x=25,y=25,start='LL',spacing=0.17,orientation='y')

    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=10, direction='-y')


def silver_square(valve,nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    g.move(**{nozzle:3})
    g.dwell(5)

    #######test line
    g.move(x=3,y=3)
    #pressure_purge(delay = 2)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=5)
    g.move(y=0.2)
    g.move(x=-5)
    g.feed(20)
    g.toggle_pressure(pressure_box)
    g.abs_move(**{nozzle:3}) 
    g.set_pressure(pressure_box, pressure)
    

    g.abs_move(x=0,y=0)  # move to the silver pattern's corner
    g.set_pressure(pressure_box, pressure*0.8)    
    g.abs_move(**{nozzle:height+0.07}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)    
    g.meander(x=3,y=-3.8,orientation='y',spacing=0.13,start='UR')    
    g.move(y=-1.9)
    g.feed(speed*0.5)
    g.move(x=-1)
    g.move(**{nozzle:-0.05})
    g.move(x=-9)
    g.abs_move(**{nozzle:0.15})
    g.arc(x=0,y=0.00001,radius=-0.2)
    g.move(x=0.2)
    g.arc(x=0,y=0.00001,radius=-0.4)
    g.move(x=0.2)
    g.arc(x=0,y=0.00001,radius=-0.6)
    g.move(x=0.2)
    g.arc(x=0,y=0.00001,radius=-0.8)
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=10, direction='-y')




def dielectric_square(valve,nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    g.move(**{nozzle:3})
    g.dwell(5)
    ########test line
    g.move(x=1,y=1)
    #pressure_purge(delay = 2)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(25)
    g.move(x=20)
    g.move(y=0.2)
    g.move(x=-20)
    g.feed(20)
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=6, direction='-x')
    g.set_pressure(pressure_box, pressure)
    

    g.abs_move(x=0,y=0)  # move to the silver pattern's corner, outside for cover
    g.abs_move(**{nozzle:height+0.4}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.meander(x=3.5,y=5,orientation='y',spacing=0.08,start='LL')
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=10, direction='-y')


def pick_and_place(nozzle,speed):
    g.feed(20)
    g.move(**{nozzle:5})
    g.abs_move(x=-19.587,y=-21.838)
    g.feed(speed)
    g.abs_move(**{nozzle:-13.528})
    g.dwell(5)
    g.move(**{nozzle:5})
    g.abs_move(x=28.833,y=-9.946)
    g.abs_move(**{nozzle:-14.17876})
    g.dwell(5)
    g.move(**{nozzle:5})
    g.feed(25)
    g.abs_move(x=-25.7133,y=23.85)
    g.feed(speed)
    g.abs_move(**{nozzle:-13.4317})
    g.dwell(5)
    g.move(**{nozzle:5})
    g.abs_move(x=28.833+1.4,y=-9.946)
    g.abs_move(**{nozzle:-13.7595})
    g.dwell(5)
    g.move(**{nozzle:5})


def oneD_arrays(nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    g.move(**{nozzle:10})
    g.dwell(10)

    #######test line
    g.move(x=3,y=3)
    #pressure_purge(delay = 2)

    for i in np.arange(3,25.5,.5):
        g.abs_move(**{nozzle:height})
        g.toggle_pressure(pressure_box)
        g.dwell(dwell)
        g.feed(i)
        g.move(y=5)
        g.toggle_pressure(pressure_box)
        g.feed(20)
        g.move(**{nozzle:3})
        g.move(x=0.5,y=-5)
        
def threeD_columns(nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    g.move(**{nozzle:10})
    g.dwell(10)

    #######test line
    g.move(x=3,y=3)
    #pressure_purge(delay = 2)

    for i in np.arange(0.05,.3,.05):
        g.abs_move(**{nozzle:height})
        g.toggle_pressure(pressure_box)
        g.dwell(dwell)
        g.feed(i)
        g.move(**{nozzle:3})
        g.toggle_pressure(pressure_box)
        g.feed(20)
        g.move(**{nozzle:20})
        g.move(y=-2)
        g.move(x=2)
        g.move(y=2)


def threeD_lattice(nozzle,height,speed,dwell,pressure,layers):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    g.move(**{nozzle:10})
    g.dwell(10)

    g.move(x=3,y=3)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    
    for i in range(layers):
        if i%2==1:
            myorient='x'
            x_=-5
            y_=-5
        else:
            myorient='y'
            x_=5
            y_=5
        g.meander(x=x_,y=y_,spacing=0.54,orientation=myorient)
        g.move(**{nozzle:0.2})
        
        
    g.toggle_pressure(pressure_box)
    g.feed(15)
    g.abs_move(**{nozzle:15})
    g.move(x=2)



def LED_Harvard(speed,dwell,pressure,height):
    g.set_pressure(pressure_box, pressure)   
    g.feed(10)
    zero=0.0
    g.set_home(x=0,y=0,z=0)
    g.abs_move(z=zero)
    g.move(z=2)
    g.abs_move(x=2,y=2)
    g.abs_move(z=height)
    g.toggle_pressure(pressure_box)
    g.feed(speed)
    g.dwell(dwell)
    
    #first wire
    g.move(y=33)
    g.move(x=5)
    g.move(y=-2.6)
    g.dwell(dwell)
    g.move(y=-0.8,z=1)
    g.move(y=-0.8,z=-1)
    g.move(y=-3.2)
    g.dwell(dwell)
    g.move(y=-0.8,z=1)
    g.move(y=-0.8,z=-1)
    g.move(y=-3.2)
    g.dwell(dwell)
    g.move(y=-0.8,z=1)
    g.move(y=-0.8,z=-1)
    g.move(y=-3.2)
    g.dwell(dwell)
    g.move(y=-0.8,z=1)
    g.move(y=-0.8,z=-1)
    g.move(y=-0.6)
    g.move(x=0.9)
    g.move(y=8.5)
    g.move(x=8.5)
    g.move(y=-10.)
    g.move(x=3.1)

    g.abs_move(y=2)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(height=2, direction='+x')
    #
    ##second wire
    g.abs_move(x=2,y=2)
    g.abs_move(z=height)
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(y=3)
    g.move(x=5)
    g.move(y=6.2)
    g.dwell(dwell)
    g.move(y=0.8,z=1)
    g.move(y=0.8,z=-1)
    g.move(y=1.2)
    g.move(x=1.6)
    g.move(y=8)
    g.move(x=1.25)
    g.dwell(dwell)
    g.move(x=0.8,z=1)
    g.move(x=0.8,z=-1)
    g.move(x=1.4)
    g.dwell(dwell)
    g.move(x=0.8,z=1)
    g.move(x=0.8,z=-1)
    g.move(x=1.25)
    g.move(y=-8.5)
    g.move(x=1.8)
    g.move(y=-0.6)
    g.dwell(dwell)
    g.move(y=-0.8,z=1)
    g.move(y=-0.8,z=-1)
    g.move(y=-0.6)
    g.move(x=2)
    g.abs_move(y=2)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(height=2, direction='+x')


    ##third wire
    g.abs_move(x=2,y=2)
    g.abs_move(z=height)
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(y=33)
    g.move(x=15.4)
    g.move(y=-2.6)
    g.dwell(dwell)
    g.move(y=-0.8,z=1)
    g.move(y=-0.8,z=-1)
    g.move(y=-3.2)
    g.dwell(dwell)
    g.move(y=-0.8,z=1)
    g.move(y=-0.8,z=-1)
    g.move(y=-3.2)
    g.dwell(dwell)
    g.move(y=-0.8,z=1)
    g.move(y=-0.8,z=-1)
    g.move(y=-3.2)
    g.dwell(dwell)
    g.move(y=-0.8,z=1)
    g.move(y=-0.8,z=-1)
    g.move(y=-0.8)
    g.move(x=2.1)
    g.abs_move(y=2)
    #g.toggle_pressure(pressure_box)
    #g.feed(10)
    #g.clip(height=2, direction='+x')

    #anode/cathode
    g.feed(speed*0.4)
    g.move(x=1.5)  
    g.arc(x=-2.8,y=0,radius=1.4)
    g.arc(x=2.8,y=0,radius=1.4)
    g.move(x=-0.2)
    g.arc(x=-2.4,y=0,radius=1.2)
    g.arc(x=2.4,y=0,radius=1.2)
    g.move(x=-0.2)
    g.arc(x=-2.0,y=0,radius=1)
    g.arc(x=2.0,y=0,radius=1)
    g.move(x=-0.2)
    g.arc(x=-1.6,y=0,radius=0.8)
    g.arc(x=1.6,y=0,radius=0.8)
    g.move(x=-0.2)
    g.arc(x=-1.2,y=0,radius=0.6)
    g.arc(x=1.2,y=0,radius=0.6)
    g.move(x=-0.2)
    g.arc(x=-0.8,y=0,radius=0.4)
    g.arc(x=0.8,y=0,radius=0.4)
    g.move(x=-0.2)
    g.arc(x=-0.4,y=0,radius=0.2)
    g.arc(x=0.4,y=0,radius=0.2)
    g.move(x=-0.2)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(height=2, direction='+x')

    g.abs_move(x=2,y=2)
    g.abs_move(z=height)
    g.feed(speed*0.4)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(x=1.4)
    g.arc(x=-2.8,y=0,radius=1.4)
    g.arc(x=2.8,y=0,radius=1.4)
    g.move(x=-0.2)
    g.arc(x=-2.4,y=0,radius=1.2)
    g.arc(x=2.4,y=0,radius=1.2)
    g.move(x=-0.2)
    g.arc(x=-2.0,y=0,radius=1)
    g.arc(x=2.0,y=0,radius=1)
    g.move(x=-0.2)
    g.arc(x=-1.6,y=0,radius=0.8)
    g.arc(x=1.6,y=0,radius=0.8)
    g.move(x=-0.2)
    g.arc(x=-1.2,y=0,radius=0.6)
    g.arc(x=1.2,y=0,radius=0.6)
    g.move(x=-0.2)
    g.arc(x=-0.8,y=0,radius=0.4)
    g.arc(x=0.8,y=0,radius=0.4)
    g.move(x=-0.2)
    g.arc(x=-0.4,y=0,radius=0.2)
    g.arc(x=0.4,y=0,radius=0.2)
    g.move(x=-0.2)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(height=2, direction='+x')



def arduino_gen1(nozzle,height,speed,dwell,pressure,startx,starty):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    g.set_home(x=0,y=0,z=0)
    g.move(**{nozzle:3})
   
 ########test line
    g.move(x=3,y=3)
    #pressure_purge(delay = 2)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=8)
    g.move(y=0.2)
    g.move(x=-8)
    g.move(y=0.2)
    g.feed(20)
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=3, direction='-x')
    

    g.write("POSOFFSET CLEAR X Y")    
    g.abs_move(x=startx,y=starty) ####bottom left corner of TPU square
    g.set_home(x=-8,y=-8)
    
    #for i in range(4):
    #    for j in range (8):
    #        g.abs_move(x = ATMEGA328_pad_positions[i][j][0], y = ATMEGA328_pad_positions[i][j][1])
    #        g.move(x = 0.2, y = 0.2)
    #        g.rect(x = 0.4, y = 0.4, start = 'UR')
    #
    
    ####### RESET WIRE, PIN 29
    
    g.abs_move(x=13.5,y=13.5)
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(x=-3,y=-3)
    g.move(x=-2.4)
    g.move(x=-0.6,**{nozzle:1})
    g.move(x=-0.6,**{nozzle:-1})
    g.abs_move(x = ATMEGA328_pad_positions[3][4][0])
    g.abs_move(y = ATMEGA328_pad_positions[3][4][1])
    g.abs_move(**{nozzle:height+0.05})
    g.move(y=1.7)
    g.move(y=1,**{nozzle:-0.05})
    g.abs_move(y=16)
    g.toggle_pressure(pressure_box)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='+y')

    ####### VCC WIRE, PIN 4
    ##
    g.abs_move(x=13.5,y=13.5)
    g.abs_move(**{nozzle:height+0.04})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(x=-3,y=-3)
    g.move(x=-1,y=-1,**{nozzle:-0.04})    
    g.move(x=-4,y=-4)
    g.abs_move(y = ATMEGA328_pad_positions[0][3][1])
    g.abs_move(x = ATMEGA328_pad_positions[0][3][0])
    g.move(x=-1)
    g.toggle_pressure(pressure_box)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='+x')
    #
#
    ###### Rx WIRE, PIN 30
    ##
    g.abs_move(x = -4, y=-4)
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)  
    g.move(y=2)
    g.move(x=-2)
    g.move(y=8)
    g.move(x=4.5,y=4.5)
    g.move(x=3.5,y=-3.5)
    g.abs_move(x = ATMEGA328_pad_positions[3][5][0])
    g.abs_move(y = ATMEGA328_pad_positions[3][5][1]+1)
    g.toggle_pressure(pressure_box)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='+y')
    
#    
    #### Tx WIRE, PIN 30
    #
    g.abs_move(x=-4,y=13.5)
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)  
    g.move(x=2,y=-2)
    g.abs_move(x = ATMEGA328_pad_positions[3][6][0])
    g.abs_move(y = ATMEGA328_pad_positions[3][6][1])
    g.toggle_pressure(pressure_box)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='+y')
    
#    
    ##### GND WIRE (LED), PIN 17
    
    g.abs_move(x=13.5,y=-4)
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)  
    g.move(x=-1.5,y=1.5)
    g.move(x=1)
    g.move(y=1.5)
    g.move(x=-1)
    g.move(x=-1,**{nozzle:1})
    g.move(x=-1,**{nozzle:-1})
    g.move(y=1.5)
    g.move(x=0.5)
    g.move(x=0.5,**{nozzle:1})
    g.move(x=0.5,**{nozzle:-1})
    g.abs_move(y = ATMEGA328_pad_positions[2][0][1])
    g.abs_move(x = ATMEGA328_pad_positions[2][0][0])
    g.toggle_pressure(pressure_box)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='+x')
    
#
#    ##### GND WIRE (cap, half of oscillator), PIN 20, 5, 7
    
    g.abs_move(x=13.5,y=-4)
    g.abs_move(**{nozzle:height+0.04})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)  
    g.move(x=-1.5,y=1.5)
    g.move(x=1,**{nozzle:-0.04})
    g.abs_move(y = ATMEGA328_pad_positions[2][4][1])
    g.move(x=-5)
    g.abs_move(y = ATMEGA328_pad_positions[0][4][1])
    g.move(x=-10)
    g.move(x=-0.8,**{nozzle:1})
    g.move(x=-0.8,**{nozzle:-1})
    g.move(x=-1)
    g.move(y=-0.8)
    g.move(x=2.5)
    g.abs_move(y = ATMEGA328_pad_positions[0][6][1])
    g.abs_move(x = ATMEGA328_pad_positions[0][6][0])
    g.toggle_pressure(pressure_box)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='-x')

#
#    ##### GND WIRE (other cap, other half of oscillator), PIN 8
#    
    g.abs_move(x=13.5,y=-4)
    g.abs_move(**{nozzle:height+0.08})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)  
    g.move(x=-1.5,y=1.5)
    g.move(1,**{nozzle:-0.04})
    g.abs_move(y = ATMEGA328_pad_positions[2][4][1])
    g.move(x=-5)
    g.move(y=-2,**{nozzle:-0.04})
    g.move(x=-4)
    g.abs_move(x=-1,y=-1)
    g.move(x=-1)
    g.move(x=-0.8,**{nozzle:1})
    g.move(x=-0.8,**{nozzle:-1})
    g.move(x=-1)
    g.move(y=2.6)
    g.move(y=-0.8)
    g.move(x=4)
    g.abs_move(y = ATMEGA328_pad_positions[0][7][1])
    g.abs_move(x = ATMEGA328_pad_positions[0][7][0])
    g.toggle_pressure(pressure_box)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='-x')
#
#    ##### Tx terminal
#
    g.abs_move(x=-4,y=13.5)
    g.abs_move(**{nozzle:height+0.09})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)  
    g.move(x=-0.75,y=-0.75)
    g.rect(x=1.5,y=1.5)
    g.toggle_pressure(pressure_box)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='-x')
#
#
#    ##### Rx terminal
#
    g.abs_move(x = -4, y=-4)
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)  
    g.move(x=-0.75,y=-0.75)
    g.rect(x=1.5,y=1.5)
    g.toggle_pressure(pressure_box)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='-x')

#
#
#    #### VCC terminal
    
    g.abs_move(x=13.5,y=13.5)
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)  
    g.move(x=-0.75,y=-0.75)
    g.rect(x=1.5,y=1.5)
    g.toggle_pressure(pressure_box)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='-x')
#    
     
#    #### RESET terminal
##    
    g.abs_move(x = ATMEGA328_pad_positions[3][4][0],y=16)
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)  
    g.move(x=-0.75,y=-0.75)
    g.rect(x=1.5,y=1.5)
    g.toggle_pressure(pressure_box)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='-x')

#    
#    ##### GND WIRE (LED), PIN 17
#    
    g.abs_move(x=13.5,y=-4)
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)  
    g.move(x=-0.75,y=-0.75)
    g.rect(x=1.5,y=1.5)
    g.toggle_pressure(pressure_box)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='-x')






#print_die(speed=1.4,dwell=0.1)
#print_die_wiring(speed=0.25,dwell=0.1)

#LONG_serpentine_encaps_pdms(nozzle='B',valve='2',pressure=22,speed=9,height=0.15+.24+.28)
#LONG_serpentine_encaps_wire(nozzle='A',valve='1',pressure=30,speed=0.7,height=0.4-0.15+0.1)
#g.abs_move(x=1.255,y=1.633)
#g.abs_move(z=-0.003)
#g.set_home(z=0)
#bacteria_electrodes(valve='1',nozzle='z',height=0.03,speed=2.3,dwell=0.6,pressure=48,spacing='400')

#silver_square(valve='1',nozzle='z',height=0.1,speed=0.8,dwell=2,pressure=52)

#dielectric_square(valve='1',nozzle='z',height=0.1,speed=11,dwell=0.6,pressure=3) #35A

#dielectric_square(valve='1',nozzle='z',height=0.1,speed=12,dwell=0.6,pressure=6) #1180
#
#dielectric_square(valve='1',nozzle='z',height=0.08,speed=8,dwell=0.6,pressure=12) #Sylgard

#silver_square(valve='1',nozzle='z',height=0.1,speed=0.8,dwell=2,pressure=52)

#pick_and_place(nozzle='z',speed=12)


#oneD_arrays(nozzle='z',height=0.025,speed=0.5,dwell=0.05,pressure=4)
#threeD_columns(nozzle='z',height=0.025,speed=0.5,dwell=0.05,pressure=10)
#threeD_lattice(nozzle='z',height=0.4,speed=2,dwell=0.1,pressure=10,layers=4)

#LED_Harvard(speed=3,dwell=0.1,pressure=9,height=0.02)


#tpu_square(valve='1',nozzle='z',height=0.05,speed=10,dwell=0.02,pressure=4) ###versamid_pur_1120_
#tpu_square(valve='1',nozzle='z',height=0.15,speed=13,dwell=0.02,pressure=55) ###1180A_

#arduino_gen1(nozzle='z',height=0.05,speed=3,dwell=0.1,pressure=23,startx=16.962,starty=48.286)

#g.set_pressure(pressure_box, pdms_pressure)   
#g.toggle_pressure(pressure_box)
#g.toggle_pressure(pressure_box)

#g.view(backend='matplotlib')

g.teardown() 
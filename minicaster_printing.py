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

def print_die_wiring(dwell,height,pressure,speed):
    
    g.set_pressure(pressure_box, pressure)   
    g.feed(5)
    g.abs_move(z=1)
    
    
    #######test line
    g.abs_move(x=-7,y=-7.2)
    #pressure_purge(delay = 2)
    g.abs_move(z=height)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=10)
    g.feed(10)
    g.toggle_pressure(pressure_box)
    g.clip(height=2, direction='+y')
   ##
    
    
    
    
    for i in [0,1]:        
        for j in [0,1,2,3,4,5]:
                if i==0:
                    if j<3:
                        g.abs_move(x=pad_positions[23-j][0],y=pad_positions[23-j][1])
                        g.move(x=-(2+(1-j)),y=-5)
                        g.abs_move(z=height) 
                        g.feed(speed)
                        g.toggle_pressure(pressure_box)
                        g.dwell(dwell)
                        g.abs_move(x=pad_positions[23-j][0],y=pad_positions[23-j][1]-3)
                        g.move(y=3-.2)
                        g.feed(10)
                        g.clip(height=2, direction='+y')
                        g.toggle_pressure(pressure_box)
                    else:
                        g.abs_move(x=pad_positions[23-j][0],y=pad_positions[23-j][1])
                        g.move(x=(2+(j-4)),y=-5)
                        g.abs_move(z=height)
                        g.feed(speed)
                        g.toggle_pressure(pressure_box)
                        g.dwell(dwell)
                        g.abs_move(x=pad_positions[23-j][0],y=pad_positions[23-j][1]-3)
                        g.move(y=3-.2)
                        g.feed(10)
                        g.clip(height=2, direction='+y')
                        g.toggle_pressure(pressure_box)
                else:
                    if j<3:
                        g.abs_move(x=pad_positions[6+j][0],y=pad_positions[6+j][1])
                        g.move(x=-(2+(1-j)),y=5)
                        g.abs_move(z=height) 
                        g.feed(speed)
                        g.toggle_pressure(pressure_box)
                        g.dwell(dwell)
                        g.abs_move(x=pad_positions[6+j][0],y=pad_positions[6+j][1]+3)
                        g.move(y=-3+.2)
                        g.feed(10)
                        g.clip(height=2, direction='-y')
                        g.toggle_pressure(pressure_box)
                    else:
                        g.abs_move(x=pad_positions[6+j][0],y=pad_positions[6+j][1])
                        g.move(x=(2+(j-4)),y=5)
                        g.abs_move(z=height)
                        g.feed(speed)
                        g.toggle_pressure(pressure_box)
                        g.dwell(dwell)
                        g.abs_move(x=pad_positions[6+j][0],y=pad_positions[6+j][1]+3)
                        g.move(y=-3+.2)
                        g.feed(10)
                        g.clip(height=2, direction='-y')
                        g.toggle_pressure(pressure_box)
                        
                        
                        
    for i in [0,1]:        
        for j in [0,1,2,3,4,5]:
                if i==0:
                    if j<3:
                        g.abs_move(x=pad_positions[j][0],y=pad_positions[j][1])
                        g.move(y=-(2+(1-j)),x=-5)
                        g.abs_move(z=height) 
                        g.feed(speed)
                        g.toggle_pressure(pressure_box)
                        g.dwell(dwell)
                        g.abs_move(y=pad_positions[j][1],x=pad_positions[j][0]-3)
                        g.move(x=3-.2)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                        g.toggle_pressure(pressure_box)
                    else:
                        g.abs_move(x=pad_positions[j][0],y=pad_positions[j][1])
                        g.move(y=(2+(j-4)),x=-5)
                        g.abs_move(z=height)
                        g.feed(speed)
                        g.toggle_pressure(pressure_box)
                        g.dwell(dwell)
                        g.abs_move(y=pad_positions[j][1],x=pad_positions[j][0]-3)
                        g.move(x=3-.2)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                        g.toggle_pressure(pressure_box)
                else:
                    if j<3:
                        g.abs_move(x=pad_positions[17-j][0],y=pad_positions[17-j][1])
                        g.move(y=-(2+(1-j)),x=5)
                        g.abs_move(z=height) 
                        g.feed(speed)
                        g.toggle_pressure(pressure_box)
                        g.dwell(dwell)
                        g.abs_move(y=pad_positions[17-j][1],x=pad_positions[17-j][0]+3)
                        g.move(x=-3+.2)
                        g.feed(10)
                        g.clip(height=2, direction='+x')
                        g.toggle_pressure(pressure_box)
                    else:
                        g.abs_move(x=pad_positions[17-j][0],y=pad_positions[17-j][1])
                        g.move(y=(2+(j-4)),x=5)
                        g.abs_move(z=height)
                        g.feed(speed)
                        g.toggle_pressure(pressure_box)
                        g.dwell(dwell)
                        g.abs_move(y=pad_positions[17-j][1],x=pad_positions[17-j][0]+3)
                        g.move(x=-3+.2)
                        g.feed(10)
                        g.clip(height=2, direction='+x')
                        g.toggle_pressure(pressure_box)                        
    #                    
    #for i in np.arange(2):        
    #    for j in np.arange(6):
    #            if i==0:
    #                g.abs_move(x=pad_positions[j][0],y=pad_positions[j][1])
    #                g.move(z=-2)
    #                g.feed(speed)
    #                #g.toggle_pressure(pressure_box)
    #                g.dwell(dwell)                    
    #                g.move(x=-3)
    #                if j<3:
    #                    g.move(x=-3,y=-3/(j+1))
    #                    #g.toggle_pressure(pressure_box)
    #                    g.feed(10)
    #                    g.clip(height=2, direction='-x')
    #                else:
    #                    g.move(x=-3,y=(j+1)-3)
    #                    #g.toggle_pressure(pressure_box)
    #                    g.feed(10)
    #                    g.clip(height=2, direction='-x')
    #            else:
    #                g.abs_move(x=pad_positions[17-j][0],y=pad_positions[17-j][1])
    #                g.move(z=-2)
    #                g.feed(speed)
    #                #g.toggle_pressure(pressure_box)
    #                g.dwell(dwell) 
    #                g.move(x=3)
    #                if j<3:
    #                    g.move(x=3,y=-3/(j+1))
    #                    #g.toggle_pressure(pressure_box)
    #                    g.feed(10)
    #                    g.clip(height=2, direction='-x')
    #                else:
    #                    g.move(x=3,y=(j+1)-3)
    #                    #g.toggle_pressure(pressure_box)
    #                    g.feed(10)
    #                    g.clip(height=2, direction='-x')

    
        

def print_electrodes(dwell,height,pressure,speed):
    
    g.set_pressure(pressure_box, pressure)   
    g.feed(5)
    g.abs_move(z=1)
    
    
    ########test line
    #g.abs_move(x=-1,y=2.5)
    ##pressure_purge(delay = 2)
    #g.abs_move(z=height)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.feed(speed)
    #g.move(x=-50)
    #g.feed(10)
    #g.toggle_pressure(pressure_box)
    #g.clip(height=2, direction='+y')
   ##
    
    
    
    #
    #
    #g.abs_move(x=-4,y=4)
    #g.abs_move(z=height) 
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.meander(x=-20,y=20,spacing=0.2,start='LL')
    #g.feed(10)
    #g.clip(height=2, direction='+x')
    #g.toggle_pressure(pressure_box) 
    ##
    #
    #g.abs_move(x=-4,y=4+21)
    #g.abs_move(z=height) 
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.meander(x=-20,y=20,spacing=0.2,start='LL')
    #g.feed(10)
    #g.clip(height=2, direction='+x')
    #g.toggle_pressure(pressure_box )
    ##  
    #   
    ##     
    g.abs_move(x=-26,y=4)
    g.abs_move(z=height) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.meander(x=-20,y=20,spacing=0.2,start='LL')
    g.feed(10)
    g.clip(height=2, direction='+x')
    g.toggle_pressure(pressure_box) 
    #
    #g.abs_move(x=-26-22,y=4)
    #g.abs_move(z=height) 
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.meander(x=-20,y=20,spacing=0.2,start='LL')
    #g.feed(10)
    #g.clip(height=2, direction='+x')
    #g.toggle_pressure(pressure_box) 
    #
    #g.abs_move(x=-26,y=4+21)
    #g.abs_move(z=height) 
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.meander(x=-20,y=20,spacing=0.2,start='LL')
    #g.feed(10)
    #g.clip(height=2, direction='+x')
    #g.toggle_pressure(pressure_box) 
    #
    #g.abs_move(x=-26-22,y=4+21)
    #g.abs_move(z=height) 
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.meander(x=-20,y=20,spacing=0.2,start='LL')
    #g.feed(10)
    #g.clip(height=2, direction='+x')
    #g.toggle_pressure(pressure_box)                                
                                        
                                            
                                                
                                                    
                                                        
                                                                
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





def agtpu_single_filaments_layered(nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
#    
#########test line
#    g.abs_move(x=2,y=2)
#    g.abs_move(**{nozzle:height})
#    g.toggle_pressure(pressure_box)
#    g.dwell(dwell)
#    g.feed(speed)
#    g.move(y=10)
#    g.move(x=-0.2)
#    g.move(y=-10)
#    g.move(x=-0.2)
#    g.move(y=10)
#    g.toggle_pressure(pressure_box)
#    g.feed(20)
#    g.clip(axis=nozzle, height=2, direction='+x')
####    
#########printing 
#    g.abs_move(10, 5)    
#    g.abs_move(**{nozzle:height}) 
#    g.feed(speed*0.6)
#    g.toggle_pressure(pressure_box)
#    g.dwell(dwell)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.move(x=-1)
#    g.feed(speed)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=0.5)
#    g.move(y=7)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=0.5)
#    g.feed(speed*0.6)
#    g.move(x=-1)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.toggle_pressure(pressure_box)
#    g.feed(10)
#    g.clip(axis=nozzle, height=3, direction='-y')
#
#    g.abs_move(20, 5)    
#    g.abs_move(**{nozzle:height}) 
#    g.feed(speed*0.6)
#    g.toggle_pressure(pressure_box)
#    g.dwell(dwell)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.move(x=-1)
#    g.feed(speed)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=0.5)
#    g.move(y=7)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=0.5)
#    g.feed(speed*0.6)
#    g.move(x=-1)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.toggle_pressure(pressure_box)
#    g.feed(10)
#    g.clip(axis=nozzle, height=3, direction='-y')
#
#    g.abs_move(30, 5)    
#    g.abs_move(**{nozzle:height}) 
#    g.feed(speed*0.6)
#    g.toggle_pressure(pressure_box)
#    g.dwell(dwell)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.move(x=-1)
#    g.feed(speed)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=0.5)
#    g.move(y=7)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=0.5)
#    g.feed(speed*0.6)
#    g.move(x=-1)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.toggle_pressure(pressure_box)
#    g.feed(10)
#    g.clip(axis=nozzle, height=3, direction='-y')
#
#    g.abs_move(40, 5)    
#    g.abs_move(**{nozzle:height}) 
#    g.feed(speed*0.6)
#    g.toggle_pressure(pressure_box)
#    g.dwell(dwell)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.move(x=-1)
#    g.feed(speed)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=0.5)
#    g.move(y=7)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=0.5)
#    g.feed(speed*0.6)
#    g.move(x=-1)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.toggle_pressure(pressure_box)
#    g.feed(10)
#    g.clip(axis=nozzle, height=3, direction='-y')
#
#    g.abs_move(50, 5)    
#    g.abs_move(**{nozzle:height}) 
#    g.feed(speed*0.6)
#    g.toggle_pressure(pressure_box)
#    g.dwell(dwell)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.move(x=-1)
#    g.feed(speed)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=0.5)
#    g.move(y=7)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=0.5)
#    g.feed(speed*0.6)
#    g.move(x=-1)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.toggle_pressure(pressure_box)
#    g.feed(10)
#    g.clip(axis=nozzle, height=3, direction='-y')
#
#    g.abs_move(60, 5)    
#    g.abs_move(**{nozzle:height}) 
#    g.feed(speed*0.6)
#    g.toggle_pressure(pressure_box)
#    g.dwell(dwell)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.move(x=-1)
#    g.feed(speed)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=0.5)
#    g.move(y=7)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=0.5)
#    g.feed(speed*0.6)
#    g.move(x=-1)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.toggle_pressure(pressure_box)
#    g.feed(10)
#    g.clip(axis=nozzle, height=3, direction='-y')
#
#
#
#########printing 
#    g.abs_move(10, 25)    
#    g.abs_move(**{nozzle:height}) 
#    g.feed(speed*0.6)
#    g.toggle_pressure(pressure_box)
#    g.dwell(dwell)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.move(x=-1)
#    g.feed(speed)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=0.5)
#    g.move(y=7)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=0.5)
#    g.feed(speed*0.6)
#    g.move(x=-1)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.toggle_pressure(pressure_box)
#    g.feed(10)
#    g.clip(axis=nozzle, height=3, direction='-y')
#
#    g.abs_move(20, 25)    
#    g.abs_move(**{nozzle:height}) 
#    g.feed(speed*0.6)
#    g.toggle_pressure(pressure_box)
#    g.dwell(dwell)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.move(x=-1)
#    g.feed(speed)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=0.5)
#    g.move(y=7)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=0.5)
#    g.feed(speed*0.6)
#    g.move(x=-1)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.toggle_pressure(pressure_box)
#    g.feed(10)
#    g.clip(axis=nozzle, height=3, direction='-y')
#
#    g.abs_move(30, 25)    
#    g.abs_move(**{nozzle:height}) 
#    g.feed(speed*0.6)
#    g.toggle_pressure(pressure_box)
#    g.dwell(dwell)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.move(x=-1)
#    g.feed(speed)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=0.5)
#    g.move(y=7)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=0.5)
#    g.feed(speed*0.6)
#    g.move(x=-1)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.toggle_pressure(pressure_box)
#    g.feed(10)
#    g.clip(axis=nozzle, height=3, direction='-y')
#
#    g.abs_move(40, 25)    
#    g.abs_move(**{nozzle:height}) 
#    g.feed(speed*0.6)
#    g.toggle_pressure(pressure_box)
#    g.dwell(dwell)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.move(x=-1)
#    g.feed(speed)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=0.5)
#    g.move(y=7)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=0.5)
#    g.feed(speed*0.6)
#    g.move(x=-1)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.toggle_pressure(pressure_box)
#    g.feed(10)
#    g.clip(axis=nozzle, height=3, direction='-y')
#
#    g.abs_move(50, 25)    
#    g.abs_move(**{nozzle:height}) 
#    g.feed(speed*0.6)
#    g.toggle_pressure(pressure_box)
#    g.dwell(dwell)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.move(x=-1)
#    g.feed(speed)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=0.5)
#    g.move(y=7)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=0.5)
#    g.feed(speed*0.6)
#    g.move(x=-1)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.toggle_pressure(pressure_box)
#    g.feed(10)
#    g.clip(axis=nozzle, height=3, direction='-y')
#
#    g.abs_move(60, 25)    
#    g.abs_move(**{nozzle:height}) 
#    g.feed(speed*0.6)
#    g.toggle_pressure(pressure_box)
#    g.dwell(dwell)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.move(x=-1)
#    g.feed(speed)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=0.5)
#    g.move(y=7)
#    g.move(x=0.5)
#    g.move(x=-0.5,y=-0.5)
#    g.move(x=-0.5,y=0.5)
#    g.move(x=0.5)
#    g.feed(speed*0.6)
#    g.move(x=-1)
#    g.meander(x=2,y=2,spacing=0.2,start='LL',orientation='x')
#    g.toggle_pressure(pressure_box)
#    g.feed(10)
#    g.clip(axis=nozzle, height=3, direction='-y')




#

    ##
    #g.abs_move(20, 5)
    #g.move(x=1,y=2)    
    #g.abs_move(**{nozzle:height}) 
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.move(y=7)
    #g.toggle_pressure(pressure_box)
    #g.feed(10)
    #g.clip(axis=nozzle, height=3, direction='-y')
    #
    #g.abs_move(30, 5)
    #g.move(x=1,y=2)    
    #g.abs_move(**{nozzle:height}) 
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.move(y=7)
    #g.toggle_pressure(pressure_box)
    #g.feed(10)
    #g.clip(axis=nozzle, height=3, direction='-y')
    #
    #g.abs_move(40, 5)
    #g.move(x=1,y=2)    
    #g.abs_move(**{nozzle:height}) 
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.move(y=7)
    #g.toggle_pressure(pressure_box)
    #g.feed(10)
    #g.clip(axis=nozzle, height=3, direction='-y')
    #
    #g.abs_move(50, 5)
    #g.move(x=1,y=2)    
    #g.abs_move(**{nozzle:height}) 
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.move(y=7)
    #g.toggle_pressure(pressure_box)
    #g.feed(10)
    #g.clip(axis=nozzle, height=3, direction='-y')
    
    g.abs_move(60, 5)
    g.move(x=1,y=2)    
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(y=7)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')
    


    #g.abs_move(20, 25)
    #g.move(x=1,y=2)    
    #g.abs_move(**{nozzle:height}) 
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.move(y=7)
    #g.toggle_pressure(pressure_box)
    #g.feed(10)
    #g.clip(axis=nozzle, height=3, direction='-y')
    #
    #g.abs_move(30, 25)
    #g.move(x=1,y=2)    
    #g.abs_move(**{nozzle:height}) 
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.move(y=7)
    #g.toggle_pressure(pressure_box)
    #g.feed(10)
    #g.clip(axis=nozzle, height=3, direction='-y')
    #
    #g.abs_move(40, 25)
    #g.move(x=1,y=2)    
    #g.abs_move(**{nozzle:height}) 
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.move(y=7)
    #g.toggle_pressure(pressure_box)
    #g.feed(10)
    #g.clip(axis=nozzle, height=3, direction='-y')
    
    #g.abs_move(50, 25)
    #g.move(x=1,y=2)    
    #g.abs_move(**{nozzle:height}) 
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.move(y=7)
    #g.toggle_pressure(pressure_box)
    #g.feed(10)
    #g.clip(axis=nozzle, height=3, direction='-y')
    
    g.abs_move(60, 25)
    g.move(x=1,y=2)    
    g.abs_move(**{nozzle:height+0.03}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(y=7)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')


def Ag_pu_HOAC(nozzle,height,speed,pressure,dwell):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
#########test line
    g.abs_move(**{nozzle:2})
    g.abs_move(x=2,y=2)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=10)
    g.move(x=-0.2)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')

#########print

    g.abs_move(x=5,y=10)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=1)
    g.arc(x=0,y=0.00001,radius=-1)
    g.move(x=-0.4)
    g.arc(x=0,y=0.00001,radius=-0.6)
    g.move(x=0.4)
    g.move(x=30)
    g.move(x=2)
    g.arc(x=0,y=0.00001,radius=-1)
    g.move(x=-0.4)
    g.arc(x=0,y=0.00001,radius=-0.6)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')

    g.abs_move(x=5,y=16)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=1)
    g.arc(x=0,y=0.00001,radius=-1)
    g.move(x=-0.4)
    g.arc(x=0,y=0.00001,radius=-0.6)
    g.move(x=0.4)
    g.move(x=30)
    g.move(x=2)
    g.arc(x=0,y=0.00001,radius=-1)
    g.move(x=-0.4)
    g.arc(x=0,y=0.00001,radius=-0.6)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')

    g.abs_move(x=5,y=22)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=1)
    g.arc(x=0,y=0.00001,radius=-1)
    g.move(x=-0.4)
    g.arc(x=0,y=0.00001,radius=-0.6)
    g.move(x=0.4)
    g.move(x=30)
    g.move(x=2)
    g.arc(x=0,y=0.00001,radius=-1)
    g.move(x=-0.4)
    g.arc(x=0,y=0.00001,radius=-0.6)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')

    g.abs_move(x=5,y=28)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=1)
    g.arc(x=0,y=0.00001,radius=-1)
    g.move(x=-0.4)
    g.arc(x=0,y=0.00001,radius=-0.6)
    g.move(x=0.4)
    g.move(x=30)
    g.move(x=2)
    g.arc(x=0,y=0.00001,radius=-1)
    g.move(x=-0.4)
    g.arc(x=0,y=0.00001,radius=-0.6)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')

    g.abs_move(x=5,y=34)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=1)
    g.arc(x=0,y=0.00001,radius=-1)
    g.move(x=-0.4)
    g.arc(x=0,y=0.00001,radius=-0.6)
    g.move(x=0.4)
    g.move(x=30)
    g.move(x=2)
    g.arc(x=0,y=0.00001,radius=-1)
    g.move(x=-0.4)
    g.arc(x=0,y=0.00001,radius=-0.6)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')

    g.abs_move(x=5,y=40)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=1)
    g.arc(x=0,y=0.00001,radius=-1)
    g.move(x=-0.4)
    g.arc(x=0,y=0.00001,radius=-0.6)
    g.move(x=0.4)
    g.move(x=30)
    g.move(x=2)
    g.arc(x=0,y=0.00001,radius=-1)
    g.move(x=-0.4)
    g.arc(x=0,y=0.00001,radius=-0.6)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')



def TPU_spacing_tests(nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    #
    #######test line
    g.abs_move(**{nozzle:2})
    g.abs_move(x=-2,y=1)
    g.abs_move(**{nozzle:height}) 
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=-10)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')
    
    my_space = [0.55,0.55,0.55,0.55,0.55,0.55,0.55,0.55]
    my_xstarts = [-3.0, -11.825, -20.65, -29.474999999999998, -38.3, -47.125, -55.949999999999996, -64.77499999999999]
#
    for i in range(8):
          g.abs_move(x=my_xstarts[i],y=3)
          g.abs_move(**{nozzle:height}) 
          g.toggle_pressure(pressure_box)
          g.feed(speed)
          g.dwell(dwell)
          g.meander(x=-7,y=43,orientation='y',spacing=my_space[i],start='LL')
          g.toggle_pressure(pressure_box)
          g.feed(20)
          g.clip(axis=nozzle, height=3, direction='-y')
#
    #for i in range(8):
    #      g.abs_move(x=my_xstarts[i],y=23)
    #      g.abs_move(**{nozzle:height}) 
    #      g.toggle_pressure(pressure_box)
    #      g.feed(speed)
    #      g.dwell(dwell)
    #      g.meander(x=-7,y=20,orientation='y',spacing=my_space[i],start='LL')
    #      g.toggle_pressure(pressure_box)
    #      g.feed(20)
    #      g.clip(axis=nozzle, height=3, direction='-y')





        
def AgTPU_strain_gauge(nozzle,height,speed,dwell,pressure,xstart,ystart):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    #
    ######test line
    #g.abs_move(x=0,y=0)
    #g.abs_move(**{nozzle:height})
    #g.toggle_pressure(pressure_box)
    #g.feed(speed)
    #g.dwell(dwell)    
    #g.move(x=-5)
    #g.toggle_pressure(pressure_box)
    #g.feed(20)
    #g.clip(axis=nozzle, height=3, direction='-y')
    ##
#     

 ########## thick

    g.abs_move(x=xstart,y=ystart)   #bottom left corner
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.feed(speed)
    g.dwell(dwell) 
    g.feed(speed/4)
    g.meander(x=-4,y=3,spacing=0.45,orientation='x',start='LR')
    g.move(x=-3) 
    g.feed(speed)
    g.meander(x=-30,y=15,spacing = 1.05, orientation='x',start='LL') 

    g.feed(speed/4)
    g.move(x=3)   
    g.meander(x=4,y=3,spacing=0.45,orientation='x',start='LL')
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis=nozzle, height=3, direction='-y')   

######### extra layer
##
#    g.abs_move(x=xstart,y=ystart)   #bottom left corner
#    
#    g.move(x=-4,y=3)
#    g.move(x=1)
#    g.abs_move(**{nozzle:height})
#    g.toggle_pressure(pressure_box)
#    g.feed(speed)
#    g.dwell(dwell) 
#    #g.feed(speed/4)
#    #g.meander(x=-4,y=3,spacing=0.45,orientation='x',start='LR')
#    #g.move(x=-3) 
#    #g.feed(speed)
#    
#    g.meander(x=-30,y=15,spacing = 1.05, orientation='x',start='LL') 
#    
#    #g.feed(speed/4)
#    #g.move(x=3)   
#    #g.meander(x=4,y=3,spacing=0.45,orientation='x',start='LL')
#    g.toggle_pressure(pressure_box)
#    g.feed(20)
#    g.clip(axis=nozzle, height=3, direction='-y')   





#    ############# thin 
#
#    g.abs_move(x=xstart,y=ystart)   #bottom left corner
#    g.move(x=-3,y=4)
#    g.abs_move(**{nozzle:height})
#    g.toggle_pressure(pressure_box)
#    g.feed(speed)
#    g.dwell(dwell) 
#    g.meander(x=3,y=-4,spacing=0.32,orientation='y',start='UL')
#    g.feed(speed/2)
#    g.move(y=3) 
#    g.feed(speed)
#    g.meander(x=-8.2,y=20,spacing = 0.8, orientation='y',start='LL') 
#    g.feed(speed/2)
#    g.move(y=-3) 
#    g.feed(speed)  
#    g.meander(x=3,y=-4,spacing=0.32,orientation='y',start='LL')
#    g.toggle_pressure(pressure_box)
#    g.feed(20)
#    g.clip(axis=nozzle, height=3, direction='-y')          
                     
   
                 
   
    

def AgTPU_MEA_5x5(nozzle,height,speed,dwell,pressure,xstart,ystart):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    

    my_grid = (
              ((0,0),(0,4),(0,8),(0,12),(0,16)),
              ((-4,0),(-4,4),(-4,8),(-4,12),(-4,16)),    
              ((-8,0),(-8,4),(-8,8),(-8,12),(-8,16)),
              ((-12,0),(-12,4),(-12,8),(-12,12),(-12,16)),
              ((-16,0),(-16,4),(-16,8),(-16,12),(-16,16)),
    )
    

    ###test line
    #g.abs_move(x=-56,y=7)
    #g.abs_move(**{nozzle:height})
    #g.toggle_pressure(pressure_box)
    #g.feed(speed)
    #g.dwell(dwell)    
    #g.move(y=6)
    #g.toggle_pressure(pressure_box)
    #g.feed(20)
    #g.clip(axis=nozzle, height=3, direction='-y')
    #
#     
#
    for i in range(5):
        for j in range(5):
            
            g.abs_move(x=my_grid[i][j][0],y=my_grid[i][j][1])   #bottom left corner
            g.abs_move(**{nozzle:height})
            g.toggle_pressure(pressure_box)
            g.feed(speed)
            g.dwell(dwell) 
            g.move(x=0.4,y=-0.4)
            g.rect(x=-0.8,y=0.8,start='LL')
            g.move(x=-0.2,y=0.2)
            g.rect(x=-0.4,y=0.4,start='LL')
            g.toggle_pressure(pressure_box)
            g.feed(20)
            g.clip(axis=nozzle, height=3, direction='-y')
     
            
    

def AgTPU_MEA_wires_5x5(nozzle,height,speed,dwell,pressure,xstart,ystart):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    

    my_grid = (
              ((0,0),(0,4),(0,8),(0,12),(0,16)),
              ((-4,0),(-4,4),(-4,8),(-4,12),(-4,16)),    
              ((-8,0),(-8,4),(-8,8),(-8,12),(-8,16)),
              ((-12,0),(-12,4),(-12,8),(-12,12),(-12,16)),
              ((-16,0),(-16,4),(-16,8),(-16,12),(-16,16)),
    )
    

    ####test line
    #g.abs_move(x=-59,y=7)
    #g.abs_move(**{nozzle:height})
    #g.toggle_pressure(pressure_box)
    #g.feed(speed)
    #g.dwell(dwell)    
    #g.move(y=8)
    #g.move(x=-1)
    #g.move(y=-4)
    #g.toggle_pressure(pressure_box)
    #g.feed(20)
    #g.clip(axis=nozzle, height=3, direction='-y')
    ##
#          
            
    for i in [0,1,2,3,4]:
        for j in [0,1,2,3,4]:
            
            g.abs_move(x=my_grid[i][j][0],y=my_grid[i][j][1])   #bottom left corner
            g.abs_move(**{nozzle:height})
            g.toggle_pressure(pressure_box)
            g.feed(speed)
            g.dwell(dwell)
            
            if j==0:
                 
                g.move(y=-6-3,)
                g.toggle_pressure(pressure_box)
                g.feed(20)
                g.clip(axis=nozzle, height=3, direction='-y')          
                                 
            if j==1: 
                
                g.move(x=-0.8,y=-1)
                g.move(y=-9-3)
                g.toggle_pressure(pressure_box)
                g.feed(20)
                g.clip(axis=nozzle, height=3, direction='-y')  
                
            if j==2: 
                
                g.move(x=-1.4,y=-1)
                g.move(y=-13-3)
                g.toggle_pressure(pressure_box)
                g.feed(20)
                g.clip(axis=nozzle, height=3, direction='-y')   

            if j==3: 
                
                g.move(x=-2.0,y=-1)
                g.move(y=-17-3)
                g.toggle_pressure(pressure_box)
                g.feed(20)
                g.clip(axis=nozzle, height=3, direction='-y')  

            if j==4: 
                
                g.move(x=-2.6,y=-1)
                g.move(y=-21-3)
                g.toggle_pressure(pressure_box)
                g.feed(20)
                g.clip(axis=nozzle, height=3, direction='-y')  

    



def AgTPU_MEA_6x6(nozzle,height,speed,dwell,pressure,xstart,ystart):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    

    my_grid = (
              ((0,0),(0,4),(0,8),(0,12),(0,16),(0,20)),
              ((-4,0),(-4,4),(-4,8),(-4,12),(-4,16),(-4,20)),    
              ((-8,0),(-8,4),(-8,8),(-8,12),(-8,16),(-8,20)),
              ((-12,0),(-12,4),(-12,8),(-12,12),(-12,16),(-12,20)),
              ((-16,0),(-16,4),(-16,8),(-16,12),(-16,16),(-16,20)),
              ((-20,0),(-20,4),(-20,8),(-20,12),(-20,16),(-20,20)),
    )
    

    ####test line
    g.abs_move(x=25,y=-5.)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.feed(speed)
    g.dwell(dwell)    
    g.move(x=-10)
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis=nozzle, height=3, direction='-y')
    ##
#     

    for i in range(6):
        for j in range(6):
            
            g.abs_move(x=my_grid[i][j][0],y=my_grid[i][j][1])   #bottom left corner
            g.abs_move(**{nozzle:height})
            g.toggle_pressure(pressure_box)
            g.feed(speed)
            g.dwell(dwell) 
            g.move(x=0.4,y=-0.4)
            g.rect(x=-0.8,y=0.8,start='LL')
            g.move(x=-0.2,y=0.2)
            g.rect(x=-0.4,y=0.4,start='LL')
            g.toggle_pressure(pressure_box)
            g.feed(20)
            g.clip(axis=nozzle, height=3, direction='-y')
     
            
    

def AgTPU_MEA_wires_6x6(nozzle,height,speed,dwell,pressure,xstart,ystart):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    

    my_grid = (
              ((0,0),(0,4),(0,8),(0,12),(0,16),(0,20)),
              ((-4,0),(-4,4),(-4,8),(-4,12),(-4,16),(-4,20)),    
              ((-8,0),(-8,4),(-8,8),(-8,12),(-8,16),(-8,20)),
              ((-12,0),(-12,4),(-12,8),(-12,12),(-12,16),(-12,20)),
              ((-16,0),(-16,4),(-16,8),(-16,12),(-16,16),(-16,20)),
              ((-20,0),(-20,4),(-20,8),(-20,12),(-20,16),(-20,20)),
    )
    

    ####test line
    g.abs_move(x=30,y=-2.)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.feed(speed)
    g.dwell(dwell)    
    g.move(x=-20)
    g.move(y=-2)
    g.move(x=15)
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis=nozzle, height=3, direction='-y')
    ##
#          
            
    for i in range(6):
        for j in [0,1,2,3,4,5]:
            
            g.abs_move(x=my_grid[i][j][0],y=my_grid[i][j][1])   #bottom left corner
            g.abs_move(**{nozzle:height})
            g.toggle_pressure(pressure_box)
            g.feed(speed)
            g.dwell(dwell)
            
            if j==0:
                 
                g.move(y=-6-3,)
                g.toggle_pressure(pressure_box)
                g.feed(20)
                g.clip(axis=nozzle, height=3, direction='-y')          
                                 
            if j==1: 
                
                g.move(x=-0.8,y=-1)
                g.move(y=-9-3)
                g.toggle_pressure(pressure_box)
                g.feed(20)
                g.clip(axis=nozzle, height=3, direction='-y')  
                
            if j==2: 
                
                g.move(x=-1.4,y=-1)
                g.move(y=-13-3)
                g.toggle_pressure(pressure_box)
                g.feed(20)
                g.clip(axis=nozzle, height=3, direction='-y')   

            if j==3: 
                
                g.move(x=-2.0,y=-1)
                g.move(y=-17-3)
                g.toggle_pressure(pressure_box)
                g.feed(20)
                g.clip(axis=nozzle, height=3, direction='-y')  

            if j==4: 
                
                g.move(x=-2.6,y=-1)
                g.move(y=-21-3)
                g.toggle_pressure(pressure_box)
                g.feed(20)
                g.clip(axis=nozzle, height=3, direction='-y')  

            if j==5: 
                
                g.move(x=-3.2,y=-1)
                g.move(y=-25-3)
                g.toggle_pressure(pressure_box)
                g.feed(20)
                g.clip(axis=nozzle, height=3, direction='-y') 


def pdms_pillars(nozzle,height,speed,dwell,pressure,layers):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    g.move(**{nozzle:3})
    #g.dwell(5)
    ########test line
    #g.abs_move(x=1,y=1)
    ##pressure_purge(delay = 2)
    #g.abs_move(**{nozzle:height})
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.feed(speed)
    #g.move(x=20)
    #g.move(y=0.2)
    #g.move(x=-20)
    #g.feed(20)
    #g.toggle_pressure(pressure_box)
    #g.clip(axis=nozzle, height=6, direction='-x')
    #g.set_pressure(pressure_box, pressure)
    layers=np.zeros(layers)

    g.abs_move(x=0,y=0)  # move to the silver pattern's corner, outside for cover
    #g.move(x=10,y=10)
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    for i in layers:
        g.meander(x=7,y=2,orientation='x',spacing=0.5,start='LL')
        g.move(**{nozzle:0.25})
        g.meander(x=7,y=2,orientation='x',spacing=0.5,start='UR')
        g.move(**{nozzle:0.25})
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=2, direction='-y')
    
    g.abs_move(x=0,y=10)  # move to the silver pattern's corner, outside for cover
    #g.move(x=10,y=10)
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    for i in layers:
        g.meander(x=7,y=2,orientation='x',spacing=0.5,start='LL')
        g.move(**{nozzle:0.25})
        g.meander(x=7,y=2,orientation='x',spacing=0.5,start='UR')
        g.move(**{nozzle:0.25})
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=10, direction='-y')
    
    g.abs_move(x=0,y=25)  # move to the silver pattern's corner, outside for cover
    #g.move(x=10,y=10)
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    for i in layers:
        g.meander(x=7,y=2,orientation='x',spacing=0.5,start='LL')
        g.move(**{nozzle:0.25})
        g.meander(x=7,y=2,orientation='x',spacing=0.5,start='UR')
        g.move(**{nozzle:0.25})
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=10, direction='-y')
    
    g.abs_move(x=0,y=35)  # move to the silver pattern's corner, outside for cover
    #g.move(x=10,y=10)
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    for i in layers:
        g.meander(x=7,y=2,orientation='x',spacing=0.5,start='LL')
        g.move(**{nozzle:0.25})
        g.meander(x=7,y=2,orientation='x',spacing=0.5,start='UR')
        g.move(**{nozzle:0.25})
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=10, direction='-y')

    
    
    g.abs_move(x=25,y=0)  # move to the silver pattern's corner, outside for cover
    #g.move(x=10,y=10)
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    for i in layers:
        g.meander(x=7,y=2,orientation='x',spacing=0.5,start='LL')
        g.move(**{nozzle:0.25})
        g.meander(x=7,y=2,orientation='x',spacing=0.5,start='UR')
        g.move(**{nozzle:0.25})
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=10, direction='-y')
    
    g.abs_move(x=25,y=10)  # move to the silver pattern's corner, outside for cover
    #g.move(x=10,y=10)
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    for i in layers:
        g.meander(x=7,y=2,orientation='x',spacing=0.5,start='LL')
        g.move(**{nozzle:0.25})
        g.meander(x=7,y=2,orientation='x',spacing=0.5,start='UR')
        g.move(**{nozzle:0.25})
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=10, direction='-y')
    
    g.abs_move(x=25,y=25)  # move to the silver pattern's corner, outside for cover
    #g.move(x=10,y=10)
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    for i in layers:
        g.meander(x=7,y=2,orientation='x',spacing=0.5,start='LL')
        g.move(**{nozzle:0.25})
        g.meander(x=7,y=2,orientation='x',spacing=0.5,start='UR')
        g.move(**{nozzle:0.25})
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=10, direction='-y')
    
    g.abs_move(x=25,y=35)  # move to the silver pattern's corner, outside for cover
    #g.move(x=10,y=10)
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    for i in layers:
        g.meander(x=7,y=2,orientation='x',spacing=0.5,start='LL')
        g.move(**{nozzle:0.25})
        g.meander(x=7,y=2,orientation='x',spacing=0.5,start='UR')
        g.move(**{nozzle:0.25})
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=10, direction='-y')   



def ionic_lines(nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)

    g.dwell(5)

    #######test line
    g.abs_move(x=0,y=0)
    #pressure_purge(delay = 2)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    
    g.move(x=14.4)
    
    #g.move(x=5,**{nozzle:-0.2})
    #g.move(x=3.8)
    #g.move(x=5,**{nozzle:0.2})
    
    
    g.dwell(dwell)
    g.feed(20)
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=3, direction='-x')
    g.set_pressure(pressure_box, pressure)



def agtpu_lapshear(nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    #g.move(**{nozzle:3})
    #g.dwell(5)
    ########test line
    #g.abs_move(x=1,y=1)
    ##pressure_purge(delay = 2)
    #g.abs_move(**{nozzle:height})
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.feed(speed)
    #g.move(x=20)
    #g.move(y=0.2)
    #g.move(x=-20)
    #g.feed(20)
    #g.toggle_pressure(pressure_box)
    #g.clip(axis=nozzle, height=6, direction='-x')
    #g.set_pressure(pressure_box, pressure)
   
    #layers=np.zeros(layers)

    g.abs_move(x=0,y=0)  # move to the silver pattern's corner, outside for cover
    #g.move(x=10,y=10)
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.meander(x=-6,y=6,orientation='x',spacing=0.3)
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=2, direction='-y')
    
    g.abs_move(x=-11.34,y=0.89)  # move to the silver pattern's corner, outside for cover
    #g.move(x=10,y=10)
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.meander(x=-6,y=6,orientation='x',spacing=0.3)
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=2, direction='-y')
    
    g.abs_move(x=-22.86,y=.58)  # move to the silver pattern's corner, outside for cover
    #g.move(x=10,y=10)
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.meander(x=-6,y=6,orientation='x',spacing=0.3)
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=2, direction='-y')
    #
    g.abs_move(x=-34.72,y=1.39)  # move to the silver pattern's corner, outside for cover
    #g.move(x=10,y=10)
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.meander(x=-6,y=6,orientation='x',spacing=0.3)
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=2, direction='-y')
    #
    g.abs_move(x=-46.69,y=1.67)  # move to the silver pattern's corner, outside for cover
    #g.move(x=10,y=10)
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.meander(x=-6,y=6,orientation='x',spacing=0.3)
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=2, direction='-y')


def agtpu_pillars(nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    #g.move(**{nozzle:3})
    #g.dwell(5)
    ########test line
    #g.abs_move(x=1,y=1)
    ##pressure_purge(delay = 2)
    #g.abs_move(**{nozzle:height})
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.feed(speed)
    #g.move(x=20)
    #g.move(y=0.2)
    #g.move(x=-20)
    #g.feed(20)
    #g.toggle_pressure(pressure_box)
    #g.clip(axis=nozzle, height=6, direction='-x')
    #g.set_pressure(pressure_box, pressure)
   
    #layers=np.zeros(layers)

    g.abs_move(x=26.49-4.06,y=-26.83)  # move to the silver pattern's corner, outside for cover
    #g.move(x=10,y=10)
    g.abs_move(**{nozzle:-2.42+height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(x=4)
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=2, direction='-y')
    
    g.abs_move(x=26.12-4.06,y=-16.71)  # move to the silver pattern's corner, outside for cover
    #g.move(x=10,y=10)
    g.abs_move(**{nozzle:-2.65+height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(x=4)
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=2, direction='-y')
    
    g.abs_move(x=26.10-4.06,y=-1.11)  # move to the silver pattern's corner, outside for cover
    #g.move(x=10,y=10)
    g.abs_move(**{nozzle:-2.95+height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(x=4,y=0.5)
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=2, direction='-y')
    
    
    g.abs_move(x=25.22-4.06,y=8.29)  # move to the silver pattern's corner, outside for cover
    #g.move(x=10,y=10)
    g.abs_move(**{nozzle:-2.84+height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(x=4)
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=2, direction='-y')
    
    ########

    g.abs_move(x=45.87,y=9.24)  # move to the silver pattern's corner, outside for cover
    #g.move(x=10,y=10)
    g.abs_move(**{nozzle:-2.94+height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(x=4)
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=2, direction='-y')
    
    g.abs_move(x=46.35,y=-0.76)  # move to the silver pattern's corner, outside for cover
    #g.move(x=10,y=10)
    g.abs_move(**{nozzle:-2.9+height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(x=4)
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=2, direction='-y')
    
    g.abs_move(x=46.84,y=-16.05)  # move to the silver pattern's corner, outside for cover
    #g.move(x=10,y=10)
    g.abs_move(**{nozzle:-2.76+height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(x=4)
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=2, direction='-y')
    
    
    g.abs_move(x=47.08,y=-25.08)  # move to the silver pattern's corner, outside for cover
    #g.move(x=10,y=10)
    g.abs_move(**{nozzle:-2.74+height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(x=4)
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=2, direction='-y')



def tpu_bottom(nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
#########test line
#    g.abs_move(x=-1,y=-2.51)
#    g.abs_move(**{nozzle:height})
#    g.toggle_pressure(pressure_box)
#    g.dwell(dwell)
#    g.feed(speed)
#    g.move(x=-60)
#    g.toggle_pressure(pressure_box)
#    g.feed(20)
#    g.clip(axis=nozzle, height=2, direction='+x')
#    
########printing 
    g.abs_move(0, 0)    
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.meander(x=-65,y=32,spacing=0.25,start='LL',orientation='x')
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')


def filament_pic_tests(nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    #
#
    g.abs_move(**{nozzle:2}) 
    g.abs_move(x=39,y=21)
    g.abs_move(**{nozzle:height}) 
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(y=-20)
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis=nozzle, height=2, direction='-y')    
##    
    g.abs_move(x=40,y=21)
    g.abs_move(**{nozzle:height}) 
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(y=-20)
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis=nozzle, height=2, direction='-y')    
    
    g.abs_move(x=41,y=21)
    g.abs_move(**{nozzle:height}) 
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(y=-20)
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis=nozzle, height=2, direction='-y')    
#

    g.abs_move(**{nozzle:2}) 
    g.abs_move(x=42,y=21)
    g.abs_move(**{nozzle:height}) 
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(y=-20)
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis=nozzle, height=2, direction='-y')    
    
    g.abs_move(x=43,y=21)
    g.abs_move(**{nozzle:height}) 
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(y=-20)
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis=nozzle, height=2, direction='-y')    
    
    g.abs_move(x=44,y=21)
    g.abs_move(**{nozzle:height}) 
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(y=-20)
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis=nozzle, height=2, direction='-y')    

    g.abs_move(x=45,y=21)
    g.abs_move(**{nozzle:height}) 
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(y=-20)
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis=nozzle, height=2, direction='-y')  

def TPU_film(nozzle,height,speed,dwell,pressure,start):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    #
    ########test line
    #g.abs_move(**{nozzle:2})
    #g.abs_move(x=-1,y=1)
    #g.abs_move(**{nozzle:height})
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.feed(speed)
    #g.move(x=-20)
    #g.toggle_pressure(pressure_box)
    #g.feed(10)
    #g.clip(axis=nozzle, height=3, direction='-y')
    #
    
    if start=='BR':
        #######test line
        g.abs_move(**{nozzle:2})
        g.abs_move(x=-1,y=1)
        g.abs_move(**{nozzle:height})
        g.toggle_pressure(pressure_box)
        g.dwell(dwell)
        g.feed(speed)
        g.move(x=-20)
        g.toggle_pressure(pressure_box)
        g.feed(10)
        g.clip(axis=nozzle, height=3, direction='-y')
        
        
        g.abs_move(x=-3,y=4)
        g.abs_move(**{nozzle:height})
        g.toggle_pressure(pressure_box)
        g.feed(speed)
        g.dwell(dwell)
        g.meander(x=-66,y=42,orientation='y',spacing=0.59,start='LL')
        g.toggle_pressure(pressure_box)
        g.feed(20)
        g.clip(axis=nozzle, height=3, direction='-y')
    else:
        g.abs_move(x=-69,y=46)
        g.abs_move(**{nozzle:height})
        g.toggle_pressure(pressure_box)
        g.feed(speed)
        g.dwell(dwell)
        g.meander(x=66,y=42,orientation='y',spacing=0.55,start='UL')
        g.toggle_pressure(pressure_box)
        g.feed(20)
        g.clip(axis=nozzle, height=3, direction='-y')


def soft_TPU_rect_full(nozzle,height,speed,dwell,pressure,start):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    #
    
#######test line
    g.abs_move(**{nozzle:2})
    g.abs_move(x=-5,y=4)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=-10)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')

    my_xstarts = [-3.0, -11.825, -20.65, -29.474999999999998, -38.3, -47.125, -55.949999999999996, -64.77499999999999]


#######print
    for i in [0,1,2,3,4,5,6,7]:
        g.abs_move(x=my_xstarts[i]-3,y=8)
        g.abs_move(**{nozzle:height})
        g.toggle_pressure(pressure_box)
        g.feed(speed)
        g.dwell(dwell)
        
        g.meander(x=-5.8,y=40,orientation='y',spacing=0.5,start='LL')

        g.toggle_pressure(pressure_box)
        g.feed(20)
        g.clip(axis=nozzle, height=3, direction='+y')
        g.move(x=-5,y=5)
        
        
def soft_TPU_rect(nozzle,height,speed,dwell,pressure,start):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    #
    
#######test line
    g.abs_move(**{nozzle:2})
    g.abs_move(x=-5,y=4)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=-10)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')

    my_xstarts = [-3.0, -11.825, -20.65, -29.474999999999998, -38.3, -47.125, -55.949999999999996, -64.77499999999999]


#######print
    for i in [0,1,2,3]:
        g.abs_move(x=my_xstarts[i]-3,y=8)
        g.abs_move(**{nozzle:height})
        g.toggle_pressure(pressure_box)
        g.feed(speed)
        g.dwell(dwell)
        g.meander(x=-1.5,y=40,orientation='y',spacing=0.5,start='LL')
        
        g.meander(x=-2.5,y=18,orientation='y',spacing=0.5,start='LL')

        g.meander(x=-1.8,y=40,orientation='y',spacing=0.55,start='LL')
        g.move(x=1.8)
        g.meander(x=2.1,y=-18,orientation='y',spacing=0.55,start='LL')

        g.toggle_pressure(pressure_box)
        g.feed(20)
        g.clip(axis=nozzle, height=3, direction='+y')
        g.move(x=-5,y=5)

def stiff_TPU_island(nozzle,height,speed,dwell,pressure,start):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    #
    
#######test line
    g.abs_move(**{nozzle:2})
    g.abs_move(x=-20,y=4)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=-10)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')

    my_xstarts = [-3.0, -11.825, -20.65, -29.474999999999998, -38.3, -47.125, -55.949999999999996, -64.77499999999999]


#######print
    for i in [0,1,2,3]:
        g.abs_move(x=my_xstarts[i]-3,y=8)
        g.move(x=-2,y=17.5)
        g.abs_move(**{nozzle:height})
        g.toggle_pressure(pressure_box)
        g.feed(speed)
        g.dwell(dwell)
        g.meander(x=-1.75,y=5,orientation='y',spacing=0.5,start='LL')

        g.toggle_pressure(pressure_box)
        g.feed(20)
        g.clip(axis=nozzle, height=3, direction='-y')


def TPU_film(nozzle,height,speed,dwell,pressure,start):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    #
    #######test line
    g.abs_move(**{nozzle:2})
    g.abs_move(x=-1,y=1.8)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=-20)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')
    
    
    g.abs_move(x=-3,y=4)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.feed(speed)
    g.dwell(dwell)
    g.meander(x=-67,y=42,orientation='y',spacing=0.45,start='LL')
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis=nozzle, height=3, direction='-y')
#

def agtpu_line_soft_stiff(nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    ##
    #######test line
    g.abs_move(**{nozzle:2})
    g.abs_move(x=-10,y=0)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=-7)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')

    x_res = [-2.56,-11.475,-20.392,-29.129,-37.853,-46.644,-55.384,-64.312]
    y_res = [24.3,24.3,24.245,24.245,24.206,24.299,24.328,24.397]

    for i in [0,1,2,3,4,5]:
        g.abs_move(x=x_res[i],y=9)
        g.abs_move(**{nozzle:height})
        g.toggle_pressure(pressure_box)
        g.feed(speed)
        g.dwell(dwell)
        g.move(y=0.4)        
        g.arc(x=0,y=-0.8,radius=0.4)
        g.arc(x=0,y=0.8,radius=0.4)
        g.move(y=0.4)        
        g.arc(x=0,y=-1.6,radius=0.8)
        g.arc(x=0,y=1.6,radius=0.8)
        g.abs_move(y=y_res[i]-0.75)  
        g.toggle_pressure(pressure_box)
        g.feed(10)
        g.clip(axis=nozzle, height=2, direction='+y')
        
        g.abs_move(x=x_res[i],y=38)
        g.abs_move(**{nozzle:height})
        g.toggle_pressure(pressure_box)
        g.feed(speed)
        g.dwell(dwell)
        g.move(y=-0.4)        
        g.arc(x=0,y=0.8,radius=0.4)
        g.arc(x=0,y=-0.8,radius=0.4)
        g.move(y=-0.4)        
        g.arc(x=0,y=1.6,radius=0.8)
        g.arc(x=0,y=-1.6,radius=0.8)
        g.abs_move(y=y_res[i]+0.75)  
        g.toggle_pressure(pressure_box)
        g.feed(10)
        g.clip(axis=nozzle, height=2, direction='-y')
        
        #g.move(x=0.2)
        #g.arc(x=0.6,y=0,radius=0.3)
        #g.arc(x=-0.6,y=0,radius=0.3)
        #g.move(x=0.2)
        #g.arc(x=0.2,y=0,radius=0.1)
        #g.arc(x=-0.2,y=0,radius=0.1)


def TPU_sensor(nozzle,height,speed,dwell,pressure,start):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    ##
    ########test line
    #g.abs_move(**{nozzle:2})
    #g.abs_move(x=-1,y=1)
    #g.abs_move(**{nozzle:height})
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.feed(speed)
    #g.move(x=-20)
    #g.toggle_pressure(pressure_box)
    #g.feed(10)
    #g.clip(axis=nozzle, height=3, direction='-y')
    
    
    if start=='BR':
        #######test line
        g.abs_move(**{nozzle:2})
        g.abs_move(x=-1,y=1)
        g.abs_move(**{nozzle:height})
        g.toggle_pressure(pressure_box)
        g.dwell(dwell)
        g.feed(speed)
        g.move(x=-20)
        g.toggle_pressure(pressure_box)
        g.feed(10)
        g.clip(axis=nozzle, height=3, direction='-y')
        
        
#        g.abs_move(x=-3,y=4)
#        g.abs_move(**{nozzle:height})
#        g.toggle_pressure(pressure_box)
#        g.feed(speed)
#        g.dwell(dwell)
#        g.meander(x=-12,y=42,orientation='y',spacing=0.59,start='LL')
#        g.toggle_pressure(pressure_box)
#        g.feed(20)
#        g.clip(axis=nozzle, height=3, direction='-y')
#
#        g.abs_move(x=-17,y=4)
#        g.abs_move(**{nozzle:height})
#        g.toggle_pressure(pressure_box)
#        g.feed(speed)
#        g.dwell(dwell)
#        g.meander(x=-12,y=42,orientation='y',spacing=0.59,start='LL')
#        g.toggle_pressure(pressure_box)
#        g.feed(20)
#        g.clip(axis=nozzle, height=3, direction='-y')
#
#        g.abs_move(x=-31,y=4)
#        g.abs_move(**{nozzle:height})
#        g.toggle_pressure(pressure_box)
#        g.feed(speed)
#        g.dwell(dwell)
#        g.meander(x=-12,y=42,orientation='y',spacing=0.59,start='LL')
#        g.toggle_pressure(pressure_box)
#        g.feed(20)
#        g.clip(axis=nozzle, height=3, direction='-y')
#
#        g.abs_move(x=-45,y=4)
#        g.abs_move(**{nozzle:height})
#        g.toggle_pressure(pressure_box)
#        g.feed(speed)
#        g.dwell(dwell)
#        g.meander(x=-12,y=42,orientation='y',spacing=0.59,start='LL')
#        g.toggle_pressure(pressure_box)
#        g.feed(20)
#        g.clip(axis=nozzle, height=3, direction='-y')

        g.abs_move(x=-59,y=4)
        g.abs_move(**{nozzle:height})
        g.toggle_pressure(pressure_box)
        g.feed(speed)
        g.dwell(dwell)
        g.meander(x=-8,y=20,orientation='y',spacing=0.59,start='LL')
        g.toggle_pressure(pressure_box)
        g.feed(20)
        g.clip(axis=nozzle, height=3, direction='-y')
        
        g.abs_move(x=-59,y=26)
        g.abs_move(**{nozzle:height})
        g.toggle_pressure(pressure_box)
        g.feed(speed)
        g.dwell(dwell)
        g.meander(x=-8,y=20,orientation='y',spacing=0.59,start='LL')
        g.toggle_pressure(pressure_box)
        g.feed(20)
        g.clip(axis=nozzle, height=3, direction='-y')
        
def AgTPU_epidermal_sensors(nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    
    ####test line
    g.abs_move(x=0,y=-1.6)
    g.abs_move(**{nozzle:height-0.16})
    g.toggle_pressure(pressure_box)
    g.feed(speed)
    g.dwell(dwell)    
    g.move(x=-10)
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis=nozzle, height=3, direction='-y')
    ##
    ############BOTTOM LAYER
    #        
    
    g.abs_move(x=-0.5,y=0.75+21.5)
    g.rect(x=-7,y=16)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.feed(speed*0.7)
    g.dwell(dwell)
    g.meander(x=-2,y=2,spacing=0.25,orientation='y')   
    g.move(y=2)
    g.feed(speed)
    g.meander(x=-3,y=12,spacing=0.48,orientation='y')   
    g.feed(speed*0.7)
    g.move(y=-2)      
    g.meander(x=-2,y=-2,spacing=0.25,orientation='y')   
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis=nozzle,height=2, direction='+x')
        
                          
def AgTPU_strain_speciman_LED(nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    
    ####test line
    g.abs_move(x=0,y=-1)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.feed(speed)
    g.dwell(dwell)    
    g.move(x=-25)
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis=nozzle, height=3, direction='-y')
    
    my_xstarts = [-3.0, -11.825, -20.65, -29.474999999999998, -38.3, -47.125, -55.949999999999996, -64.77499999999999]
    my_xstarts = np.subtract(my_xstarts,-3)
    
    ###########BOTTOM LAYER
            
    for i in [0,1,2,3,4,5,6,7]:
          g.abs_move(x=my_xstarts[i]-1,y=3+2+3-2)
          g.abs_move(**{nozzle:height})
          g.toggle_pressure(pressure_box)
          g.feed(speed*0.7)
          g.dwell(dwell)
          g.meander(x=-5,y=4,spacing=0.32,orientation='y')
          g.move(x=2.5)
          g.move(y=1.5)
          g.move(x=0.8,y=-1.3)
          g.move(x=-1.6)
          g.move(x=0.8,y=1.3)          
          g.feed(speed)        
          g.move(y=9.7)
          
          g.toggle_pressure(pressure_box)
          g.feed(speed*3)
          g.dwell(0.5)
          g.move(y=0.8,**{nozzle:2.0})
          g.move(**{nozzle:2})
          g.dwell(0.5)
          g.move(**{nozzle:-2})
          g.move(y=0.8,**{nozzle:-2.0})
          g.feed(speed)
          g.toggle_pressure(pressure_box)
          g.dwell(0.4)
          
          g.move(y=9.7)
          
          g.feed(speed*0.7)
          g.move(x=0.8,y=1.3)
          g.move(x=-1.6)
          g.move(x=0.8,y=-1.3)
          g.move(y=1.5)
          g.move(x=2.5)
          g.meander(x=-5,y=4,spacing=0.32,orientation='y')
          g.toggle_pressure(pressure_box)
          g.feed(20)
          g.clip(axis=nozzle,height=2, direction='+x')
        
   ##########2nd LAYER     
    for i in [0,1,2,3,4,5,6,7]:
          g.abs_move(x=my_xstarts[i]-1-2.5,y=3+2+3-2+4)
          g.abs_move(**{nozzle:height+0.1})
          g.toggle_pressure(pressure_box)
          g.feed(speed)
          g.dwell(dwell)

          g.move(y=11.2)
#          
          g.toggle_pressure(pressure_box)
          g.feed(speed*3)
          g.dwell(0.5)
          g.move(y=0.8,**{nozzle:2.0})
          g.move(**{nozzle:2})
          g.dwell(0.5)
          g.move(**{nozzle:-2})
          g.move(y=0.8,**{nozzle:-2.0})
          g.feed(speed)
          g.toggle_pressure(pressure_box)
          g.dwell(0.4)
          
          g.move(y=11.2)

          g.toggle_pressure(pressure_box)
          g.feed(20)
          g.clip(axis=nozzle, height=2, direction='-y')
    
     ##########3rd LAYER     
    for i in [0,1,2,3,4,5,6,7]:
          g.abs_move(x=my_xstarts[i]-1-2.5,y=3+2+3-2+4)
          g.abs_move(**{nozzle:height+0.2})
          g.toggle_pressure(pressure_box)
          g.feed(speed)
          g.dwell(dwell)

          g.move(y=11.2)
#          
          g.toggle_pressure(pressure_box)
          g.feed(speed*3)
          g.dwell(0.5)
          g.move(y=0.8,**{nozzle:2.0})
          g.move(**{nozzle:2})
          g.dwell(0.5)
          g.move(**{nozzle:-2})
          g.move(y=0.8,**{nozzle:-2.0})
          g.feed(speed)
          g.toggle_pressure(pressure_box)
          g.dwell(0.4)
          
          g.move(y=11.2)


          g.toggle_pressure(pressure_box)
          g.feed(20)
          g.clip(axis=nozzle, height=2, direction='-y') 
          
##    ############3rd LAYER
#    #g.dwell(20)
#    for i in [0,1,2,3,4,5,6,7]:
#          g.abs_move(x=my_xstarts[i]+1+2.5,y=3+2+7)
#          g.abs_move(C=-27.969,**{nozzle:height+0.2}) 
#          g.feed(speed)
#          if valve is not None:
#              g.set_valve(num = valve, value = 1)
#          g.dwell(dwell)
#
#          g.move(y=11.2)
#          
#          g.set_valve(num = valve, value = 0)
#          g.feed(speed*3)
#          g.dwell(0.5)
#          g.move(y=0.8,**{nozzle:2.0})
#          g.move(**{nozzle:2})
#          g.dwell(0.5)
#          g.move(**{nozzle:-2})
#          g.move(y=0.8,**{nozzle:-2.0})
#          g.feed(speed)
#          g.set_valve(num = valve, value = 1)
#          g.dwell(0.4)
#          
#          g.move(y=11.2)
#
#          g.set_valve(num = valve, value = 0)
#          g.feed(40)
#          g.clip(axis=nozzle,height=5, direction='+y')
###          


def AgTPU_filament(nozzle,height,speed,dwell,pressure,xstart,ystart):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    #
    #####test line
    g.abs_move(x=-3,y=3)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.feed(speed)
    g.dwell(dwell)    
    g.move(x=-5)
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis=nozzle, height=3, direction='-y')
    #
#     
    g.abs_move(x=xstart,y=ystart)
 ########## thick

      #bottom left corner
   
    for i in [2,3,4,5,6,7]:
        g.abs_move(y=ystart)
        g.abs_move(**{nozzle:height})
        g.toggle_pressure(pressure_box)
        g.feed(speed)
        g.dwell(dwell) 
        g.move(y=30)
        g.toggle_pressure(pressure_box)
        g.feed(20)
        g.clip(axis=nozzle, height=3, direction='-y')  
        g.move(x=-6)
        

        
def AgTPU_strain_rectangle_y(nozzle,height,speed,dwell,pressure,x,y):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    
    ####test line
    g.abs_move(x=-5,y=1)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.feed(speed)
    g.dwell(dwell)    
    g.move(x=-10)
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis=nozzle, height=3, direction='-y')    

    #g.abs_move(x=-3,y=4)

    my_y_starts = [3,10,17,24,31,38,42]   #
    
#####    ############BOTTOM LAYER 
##            
    for i in [0,1,2]:
          g.abs_move(y=my_y_starts[i],x=-10)
          g.abs_move(**{nozzle:height})
          g.toggle_pressure(pressure_box)
          g.feed(speed)
          g.dwell(dwell)
          g.meander(x=-x,y=y,spacing=0.47,orientation='x')
          g.toggle_pressure(pressure_box)
          g.feed(20)
          g.clip(axis=nozzle,height=3, direction='+x')

    g.move(y=-5)                
 
def AgTPU_single_filament(nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    xstart= -17
    ystart= 3

#####    ############BOTTOM LAYER 
    g.abs_move(x=xstart)
        
    for i in [0,1,2]:
          g.abs_move(y=ystart)
          g.abs_move(**{nozzle:height})
          g.toggle_pressure(pressure_box)
          g.feed(speed)
          g.dwell(dwell)
          g.move(y=15)
          g.toggle_pressure(pressure_box)
          g.feed(20)
          g.clip(axis=nozzle,height=3, direction='-x')
          g.move(x=-1)
      
    g.abs_move(x=xstart)
        
    for i in [0,1,2]:
          g.abs_move(y=ystart)
          g.abs_move(**{nozzle:height+0.08})
          g.toggle_pressure(pressure_box)
          g.feed(speed)
          g.dwell(dwell)
          g.move(y=15)
          g.toggle_pressure(pressure_box)
          g.feed(20)
          g.clip(axis=nozzle,height=3, direction='+x')
          g.move(x=-1)                      
    
    g.abs_move(x=xstart)
        
    for i in [0,1,2]:
          g.abs_move(y=ystart)
          g.abs_move(**{nozzle:height+0.16})
          g.toggle_pressure(pressure_box)
          g.feed(speed)
          g.dwell(dwell)
          g.move(y=15)
          g.toggle_pressure(pressure_box)
          g.feed(20)
          g.clip(axis=nozzle,height=3, direction='+x')
          g.move(x=-1)                                                  
    #                                                                              
def AgTPU_strain_rectangle(nozzle,height,speed,dwell,pressure,x,y):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    
    ####test line
    g.abs_move(x=-2,y=2)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.feed(speed)
    g.dwell(dwell)    
    g.move(x=-10)
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis=nozzle, height=3, direction='-y')    

    #g.abs_move(x=-3,y=4)

    my_x_starts = [-3,-9.2,-15.4,-21.6,-27.8,-34,-40.2,-46.4,-52.6,-49.8,-55,-60.2]   #spacing to fit 12 rect (2mmx34mm) samples on a TPU flim

#####    ############BOTTOM LAYER 
##            
    for i in [0,1,2,3,4,5,6,7,8]:
          g.abs_move(x=my_x_starts[i],y=4)
          g.abs_move(**{nozzle:height})
          g.toggle_pressure(pressure_box)
          g.feed(speed)
          g.dwell(dwell)
          g.meander(x=-x,y=y,spacing=0.3,orientation='y')
          #g.abs_move(**{nozzle:height+height})
          #g.meander(x=x,y=-y,spacing=0.3,orientation='y')
          #g.abs_move(**{nozzle:height+height+height})
          #g.meander(x=-x,y=y,spacing=0.3,orientation='y')
          #g.abs_move(**{nozzle:height+height+height+height})
          #g.meander(x=x,y=-y,spacing=0.3,orientation='y')
          g.toggle_pressure(pressure_box)
          g.feed(20)
          g.clip(axis=nozzle,height=3, direction='+x')

    g.move(y=-5)

def AgTPU_strain_speciman_filament(nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
#    
    ####test line
    g.abs_move(x=-2,y=2)
    g.abs_move(**{nozzle:height-.04})
    g.toggle_pressure(pressure_box)
    g.feed(speed)
    g.dwell(dwell)    
    g.move(x=-25)
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis=nozzle, height=3, direction='-y')
    
####    
    my_xstarts = [-3.0, -11.825, -20.65, -29.474999999999998, -38.3, -47.125, -55.949999999999996, -64.77499999999999]
###
#####    ############BOTTOM LAYER
##            
#    for i in [0,1,2,3,4,5,6,7]:
#          g.abs_move(x=my_xstarts[i]+0.3-4.5-0.75+3.5,y=3+6+1)
#          g.abs_move(**{nozzle:height})
#          g.toggle_pressure(pressure_box)
#          g.feed(speed*0.5)
#          g.dwell(dwell)
##
#          g.meander(x=-5,y=4,spacing=0.32,orientation='y')
#          g.move(x=2.5)
#          g.move(y=1.5)
#          g.move(x=0.8,y=-1.3)
#          g.move(x=-1.6)
#          g.move(x=0.8,y=1.3)
#          
#          g.abs_move(**{nozzle:height})
#          g.feed(speed)
#          g.move(y=21)
#          
#          g.feed(speed*0.5)
#          g.abs_move(**{nozzle:height})
#          g.move(x=0.8,y=1.3)
#          g.move(x=-1.6)
#          g.move(x=0.8,y=-1.3)
#          g.move(y=1.5)
#          g.move(x=2.5)
#          g.meander(x=-5,y=4,spacing=0.32,orientation='y')
#          g.toggle_pressure(pressure_box)
#          g.feed(20)
#          g.clip(axis=nozzle,height=3, direction='+x')
##          
    #g.dwell(90)
    ##########2nd LAYER     
    for i in [5,6,7]:
          g.abs_move(x=my_xstarts[i]-2.5+0.3-4.5-0.75+3.5-.1,y=3+6+4+1)
          g.abs_move(**{nozzle:height+0.08})
          g.toggle_pressure(pressure_box)
          g.feed(speed)
          g.dwell(dwell)

          g.move(y=24)  


          g.toggle_pressure(pressure_box)
          g.feed(20)
          g.clip(axis=nozzle, height=3, direction='-y')
#    
    g.dwell(90)
##   
###    ############3rd LAYER
    for i in [5,6,7]:
          g.abs_move(x=my_xstarts[i]-2.5+0.3-4.5-0.75+3.5-.1,y=3+6+4+1)
          g.abs_move(**{nozzle:height+0.16})
          g.toggle_pressure(pressure_box)
          g.feed(speed)
          g.dwell(dwell)

          g.move(y=24)

          g.toggle_pressure(pressure_box)
          g.feed(20)
          g.clip(axis=nozzle, height=3, direction='-y')
####          
###          
##    ############4th LAYER
#    g.dwell(20)
#    for i in [0,1,2,3,4,5,6,7]:
#          g.abs_move(x=my_xstarts[i]-1-2.5-1+.8,y=3+4+7)
#          g.abs_move(**{nozzle:height+.6})
#          g.toggle_pressure(pressure_box)
#          g.feed(speed)
#          g.dwell(dwell)
#
#          g.move(y=25)
#
#          g.toggle_pressure(pressure_box)
#          g.feed(20)
#          g.clip(axis=nozzle, height=1, direction='-y')
#          
#    ############5th LAYER
#    g.dwell(20)
#    for i in [0,1,2,3,4,5,6,7]:
#          g.abs_move(x=my_xstarts[i]-1-2.5-1+.8,y=3+4+7)
#          g.abs_move(**{nozzle:height+.8})
#          g.toggle_pressure(pressure_box)
#          g.feed(speed)
#          g.dwell(dwell)
#
#          g.move(y=25)
#
#          g.toggle_pressure(pressure_box)
#          g.feed(20)
#          g.clip(axis=nozzle, height=1, direction='-y')
#
#    ############6th LAYER
#    g.dwell(20)
#    for i in [0,1,2,3,4,5,6,7]:
#          g.abs_move(x=my_xstarts[i]-1-2.5-1+.8,y=3+4+7)
#          g.abs_move(**{nozzle:height+1.})
#          g.toggle_pressure(pressure_box)
#          g.feed(speed)
#          g.dwell(dwell)
#          g.move(y=25)
#
#          g.toggle_pressure(pressure_box)
#          g.feed(20)
#          g.clip(axis=nozzle, height=3, direction='-y')






def arduino_gen2(nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
   

    #
    ##########test line
    #g.abs_move(x=-2,y=2.5)
    #g.abs_move(**{nozzle:height})
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.feed(speed)
    #g.move(x=-15)
    #g.toggle_pressure(pressure_box)
    #g.feed(20)
    #g.clip(axis=nozzle, height=2, direction='-x')
    #########test line
    
    g.abs_move(x=-30,y=15)
    g.set_home(x=0,y=0)
    
    #for i in range(4):
    #    for j in range (8):
    #        g.abs_move(x = -ATMEGA328_pad_positions[i][j][0], y = ATMEGA328_pad_positions[i][j][1])
    #        g.move(x = 0.2, y = 0.2)
    #        g.rect(x = 0.4, y = 0.4, start = 'UR')
    
#    #### SENSOR_VCC, PIN 29
#    
    g.abs_move(x=-20,y=15)                        ###sensor vcc contact
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(x=2,y=-2)
    g.abs_move(x=-ATMEGA328_pad_positions[3][4][0])
    g.move(y=-1)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=-0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.abs_move(y=ATMEGA328_pad_positions[3][4][1])   ##pin 29
    g.abs_move(**{nozzle:height+0.1})
    g.move(y=1.6)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.move(y=1)
    g.dwell(0.1)
    g.abs_move(**{nozzle:height})
    g.abs_move(x=10)
    g.move(x=2,y=2)                                ##VCC contact
    g.abs_move(**{nozzle:height+0.1})
    g.move(x=-2,y=-2)
    g.abs_move(x=-(ATMEGA328_pad_positions[0][3][0]-1))
    g.dwell(0.1)
    g.abs_move(**{nozzle:height})
    g.abs_move(y=ATMEGA328_pad_positions[0][3][1])   
    g.abs_move(x=-ATMEGA328_pad_positions[0][3][0])   ##pin 4
    g.toggle_pressure(pressure_box)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='-x')



#    ##### SENSOR_GND, PIN 29
    
    g.abs_move(x=-20,y=-6)                         ###sensor gnd contact
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(x=2,y=2)
    g.abs_move(x=-(ATMEGA328_pad_positions[2][4][0]+4))
    g.abs_move(y=ATMEGA328_pad_positions[2][6][1])
    g.abs_move(x=-ATMEGA328_pad_positions[2][6][0])   ###pin 23, A0
    g.abs_move(**{nozzle:height+0.1})
    g.move(x=-4)
    g.abs_move(y=ATMEGA328_pad_positions[2][4][1])
    g.dwell(0.1)
    g.abs_move(**{nozzle:height})
    g.move(x=1)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(x=0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(x=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.abs_move(x=-ATMEGA328_pad_positions[2][4][0])   ####pin 21, GND
    g.abs_move(x=-4.4,y=4.4)
    g.abs_move(x=-0,y=0)
    
    ####5 OUTPUT LEDs
    
    g.abs_move(y=-6)
    g.move(x=-2)
    g.move(y=0.1)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.move(y=0.5)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.move(y=1.7)
    g.abs_move(x=-ATMEGA328_pad_positions[1][4][0])
    g.abs_move(y=ATMEGA328_pad_positions[1][4][1])   ###pin 13, DIGITAL OUT1
    g.abs_move(**{nozzle:height+0.1})
    g.move(y=-0.7)
    g.move(x=2.9)
    g.move(y=-1.7)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=-0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.move(y=-0.5)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=-0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.move(y=-0.1)
    g.dwell(0.1)
    g.abs_move(**{nozzle:height})
    g.move(x=-2.0)

    g.move(y=0.1)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.move(y=0.5)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.move(y=1.3-.2)
    g.abs_move(x=-ATMEGA328_pad_positions[1][5][0])
    g.abs_move(y=ATMEGA328_pad_positions[1][5][1])   ###pin 14, DIGITAL OUT2
    g.abs_move(**{nozzle:height+0.1})
    g.move(y=-1.1-.2)
    g.move(x=1.7)
    g.move(y=-1.3+.2)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=-0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.move(y=-0.5)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=-0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.move(y=-0.1)
    g.dwell(0.1)
    g.abs_move(**{nozzle:height})
    g.move(x=-2.0)
    
    g.move(y=0.1)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.move(y=0.5)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.move(y=0.9)
    g.abs_move(x=-ATMEGA328_pad_positions[1][6][0])
    g.abs_move(y=ATMEGA328_pad_positions[1][6][1])   ###pin 15, DIGITAL OUT3
    g.abs_move(**{nozzle:height+0.1})
    g.move(y=-1.5)
    g.move(x=0.5)
    g.move(y=-0.9)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=-0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.move(y=-0.5)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=-0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.move(y=-0.1)
    g.dwell(0.1)
    g.abs_move(**{nozzle:height})
    g.move(x=-2)
    
    g.move(y=0.1)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.move(y=0.5)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.move(y=0.9)
    g.abs_move(x=-ATMEGA328_pad_positions[1][7][0])
    g.abs_move(y=ATMEGA328_pad_positions[1][7][1])   ###pin 16. DIGITAL OUT4
    g.abs_move(**{nozzle:height+0.1})
    g.move(y=-1.5)
    g.move(x=-0.7)
    g.move(y=-0.9)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=-0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.move(y=-0.5)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=-0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.move(y=-0.1)
    g.dwell(0.1)
    g.abs_move(**{nozzle:height})
    g.move(x=-2)
    
    g.move(y=0.1)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.move(y=0.5)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.abs_move(y=ATMEGA328_pad_positions[2][0][1])
    g.abs_move(x=-ATMEGA328_pad_positions[2][0][0])   ###pin 17. DIGITAL OUT5
    g.abs_move(**{nozzle:height+0.1})
    g.move(x=-1.2)
    g.move(y=-3.9)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=-0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.move(y=-0.5)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=-0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.move(y=-0.1)
    g.toggle_pressure(pressure_box)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='+y')
#    
    
    g.abs_move(x=-4.4,y=4.4)
    g.abs_move(**{nozzle:height})
    g.feed(speed) 
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.abs_move(x=1,y=-1)
    g.move(x=1)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(x=0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(x=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.move(x=1)
    g.abs_move(y=ATMEGA328_pad_positions[0][7][1])
    g.abs_move(x=-ATMEGA328_pad_positions[0][7][0])  ####pin 8, bottom crystal pin
    g.abs_move(**{nozzle:height+0.1})
    g.move(x=5)
    g.dwell(0.1)
    g.abs_move(**{nozzle:height})
    g.move(x=2)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(y=1.0,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=1.0,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.abs_move(y=ATMEGA328_pad_positions[0][4][1])
    g.move(x=-1.5)
    g.abs_move(y=ATMEGA328_pad_positions[0][6][1])
    g.abs_move(x=-ATMEGA328_pad_positions[0][6][0])
    g.abs_move(**{nozzle:height+0.1})
    g.move(x=5.5)
    g.abs_move(y=ATMEGA328_pad_positions[0][4][1])
    g.move(x=-1.5)
    g.toggle_pressure(pressure_box)
    g.feed(speed*3)
    g.dwell(0.5)
    g.move(x=-0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(x=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(0.2)
    g.abs_move(x=-ATMEGA328_pad_positions[0][4][0])   ####pin 5, top crystal pin
    g.toggle_pressure(pressure_box)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='-x')


    g.abs_move(x=12,y=-6)                    ###GND
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(x=-2,y=2)
    g.abs_move(x=-0)
    g.toggle_pressure(pressure_box)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='-x')        
            
def AgTPU_pulse_sensor(nozzle,height,speed,dwell,pressure,startx,starty,orientation):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    ##
    ########test line
    #g.abs_move(**{nozzle:2})
    #g.abs_move(x=0,y=0.5)
    #g.abs_move(**{nozzle:height})
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.feed(speed)
    #g.move(x=-7)
    #g.toggle_pressure(pressure_box)
    #g.feed(10)
    #g.clip(axis=nozzle, height=3, direction='-y')                
    
    if orientation=='up':
        g.abs_move(x=startx,y=starty)
        g.abs_move(**{nozzle:height})
        g.toggle_pressure(pressure_box)
        g.feed(speed)
        g.dwell(dwell)
        g.move(x=-3,y=3.2)
        g.move(y=-3.2)
        g.move(x=3,y=3.2)
        g.move(x=-3.2)

        g.move(x=-5,y=5)
        g.meander(x=-5,y=10,spacing=1.0,orientation='y')                ###strain gauge 
        g.move(x=-5,y=-5)
        
        g.move(x=-3.2)
        g.move(x=3,y=-3.2)
        g.move(y=3.2)
        g.move(x=-3,y=-3.2)
  
        g.toggle_pressure(pressure_box)
        g.feed(10)
        g.clip(axis=nozzle, height=3, direction='-y')    
    else:
        g.abs_move(x=startx,y=starty)
        g.abs_move(**{nozzle:height})
        g.toggle_pressure(pressure_box)
        g.feed(speed)
        g.dwell(dwell)
        
        g.move(x=-3,y=-3.2)
        g.move(y=3.2)
        g.move(x=3,y=-3.2)
        g.move(x=-3.2)
                
        g.move(x=-5,y=-5)
        g.meander(x=-5,y=-10,spacing=1.0,orientation='y')
        g.move(x=-5,y=5)
        
        g.move(x=-3.2)
        g.move(x=3,y=3.2)
        g.move(y=-3.2)
        g.move(x=-3,y=3.2)

        g.toggle_pressure(pressure_box)
        g.feed(10)
        g.clip(axis=nozzle, height=3, direction='-y')       


def AgTPU_pulse_sensor_electrode(nozzle,height,speed,dwell,pressure,startx,starty,orientation):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    ##
    ########test line
    #g.abs_move(**{nozzle:2})
    #g.abs_move(x=0,y=0.5)
    #g.abs_move(**{nozzle:height})
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #g.feed(speed)
    #g.move(x=-7)
    #g.toggle_pressure(pressure_box)
    #g.feed(10)
    #g.clip(axis=nozzle, height=3, direction='-y')                
    
    if orientation=='up':
        g.abs_move(x=startx,y=starty)
        g.abs_move(**{nozzle:height})
        g.toggle_pressure(pressure_box)
        g.feed(speed)
        g.dwell(dwell)
        g.meander(x=-3,y=3.2,spacing=0.32,orientation='x')
        g.toggle_pressure(pressure_box)
        g.feed(10)
        g.clip(axis=nozzle, height=3, direction='-y') 

        g.move(x=-15)

        g.abs_move(**{nozzle:height})
        g.toggle_pressure(pressure_box)
        g.feed(speed)
        g.dwell(dwell)
        g.meander(x=-3,y=-3.2,spacing=0.2,orientation='x')
        g.toggle_pressure(pressure_box)
        g.feed(10)
        g.clip(axis=nozzle, height=3, direction='-y') 
   
    else:
        g.abs_move(x=startx,y=starty)
        g.abs_move(**{nozzle:height})
        g.toggle_pressure(pressure_box)
        g.feed(speed)
        g.dwell(dwell)
        g.meander(x=-3,y=-3.2,spacing=0.2,orientation='x')
        g.toggle_pressure(pressure_box)
        g.feed(10)
        g.clip(axis=nozzle, height=3, direction='-y') 

        g.move(x=-15)
       
        g.abs_move(**{nozzle:height})
        g.toggle_pressure(pressure_box)
        g.feed(speed)
        g.dwell(dwell)
        g.meander(x=-3,y=3.2,spacing=0.2,orientation='x')
        g.toggle_pressure(pressure_box)
        g.feed(10)
        g.clip(axis=nozzle, height=3, direction='-y')       




#print_die(speed=1.4,dwell=0.1)

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


#agtpu_single_filaments_layered(nozzle='z',height=0.38,speed=5,dwell=0.02,pressure=40)



#TPU_spacing_tests(nozzle='z',height=0.4+0.3+0.3,speed=11,dwell=0.2,pressure=6)
#TPU_spacing_tests(nozzle='z',height=0.4,speed=12,dwell=0.2,pressure=2)   ####pdms



#AgTPU_strain_speciman(nozzle='z',height=0.2,speed=4,dwell=0.1,pressure=15)


#AgTPU_MEA_5x5(nozzle='z',height=0.1,speed=3.5,dwell=0.1,pressure=3,xstart=-4,ystart=4)
##2
#AgTPU_MEA_wires_5x5(nozzle='z',height=0.13,speed=12,dwell=0.1,pressure=16,xstart=-4,ystart=4)


#AgTPU_MEA_6x6(nozzle='z',height=0.1,speed=3.5,dwell=0.1,pressure=3,xstart=-4,ystart=4)
#2
#AgTPU_MEA_wires_6x6(nozzle='z',height=0.15,speed=8,dwell=0.1,pressure=12,xstart=-4,ystart=4)

#pdms_pillars(nozzle='z',height=0.4,speed=5,dwell=0.2,pressure=20,layers=60)
#agtpu_pillars(nozzle='z',height=0.2,speed=4,dwell=0.3,pressure=15)


#agtpu_lapshear(nozzle='z',height=0.15,speed=4,dwell=0.3,pressure=22)

#ionic_lines(nozzle='z',height=0.2,speed=4,dwell=3, pressure=8)

#print_die_wiring(dwell=0.1,height=0.05,pressure=4,speed=8)
#
#g.abs_move(x=0,y=0)
#g.move(x=18)
#g.set_home(x=0,y=0)
#
#print_die_wiring(dwell=0.1,height=0.05,pressure=4,speed=8)
#g.abs_move(x=0,y=0)
#g.move(x=18)
#g.set_home(x=0,y=0)

#print_die_wiring(dwell=0.1,height=0.05,pressure=4,speed=8)
#g.abs_move(x=0,y=0)
#g.move(y=-22)
#g.set_home(x=0,y=0)
#
#print_die_wiring(dwell=0.1,height=0.05,pressure=2,speed=8)
#g.abs_move(x=0,y=0)
#g.move(x=18)
#g.set_home(x=0,y=0)
#
#print_die_wiring(dwell=0.1,height=0.05,pressure=2,speed=8)
#g.abs_move(x=0,y=0)
#g.move(y=22)
#g.set_home(x=0,y=0)
#
#print_die_wiring(dwell=0.1,height=0.05,pressure=2,speed=8)
#
#g.abs_move(x=0,y=0)
#g.move(y=22)
#g.set_home(x=0,y=0)



#print_electrodes(dwell=0.1,height=0.05,pressure=22,speed=10)




#tpu_bottom(nozzle='z',height=0.15,speed=15,dwell=0.2,pressure=40)

#filament_pic_tests(nozzle='z',height=0.41,speed=3.,dwell=0.2,pressure=15)
#TPU_film(nozzle='z',height=0.35,speed=10,dwell=0.2,pressure=37,start='BR')

#TPU_film(nozzle='z',height=0.9,speed=12,dwell=0.2,pressure=17,start='UL')
#TPU_spacing_tests(nozzle='z',height=0.41,speed=3.,dwell=0.2,pressure=15)


#AgTPU_strain_speciman_LED(nozzle='z',height=0.2,speed=4.,dwell=0.2,pressure=21)
#AgTPU_strain_speciman_filament(nozzle='z',height=0.18,speed=4.,dwell=0.2,pressure=11)
#arduino_gen2(nozzle='z',height=0.18,speed=5,dwell=0.2,pressure=16)


#TPU_sensor(nozzle='z',height=0.35,speed=10,dwell=0.2,pressure=37,start='BR')
#AgTPU_epidermal_sensors(nozzle='z',height=0.14,speed=3.,dwell=0.2,pressure=9)

#
#AgTPU_strain_gauge(nozzle='z',height=0.18,speed=4,dwell=0.1,pressure=18,xstart=-3,ystart=3)

#Ag_pu_HOAC(nozzle='z',height=0.3,speed=9,pressure=20,dwell=0.5)
#g.rect(x=-66,y=40)

#TPU_film(nozzle='z',height=0.25,speed=12,dwell=0.2,pressure=43,start='BR')

#AgTPU_filament(nozzle='z',height=0.23,speed=4,dwell=0.1,pressure=18,xstart=-5,ystart=6)

#g.rect(x=-67,y=42)

AgTPU_strain_rectangle(nozzle='z',height=0.15,speed=8.,dwell=0.2,pressure=55,x=3,y=30)

#AgTPU_single_filament(nozzle='z',height=0.2,speed=14.,dwell=0.2,pressure=25)

#AgTPU_strain_rectangle_y(nozzle='z',height=0.35,speed=8.,dwell=0.2,pressure=11,x=40,y=3)   ###no surf

#AgTPU_strain_rectangle_y(nozzle='z',height=0.35,speed=8.,dwell=0.2,pressure=4,x=40,y=3)     ###surf

xoffset=12.272
yoffset=59.133
#soft_TPU_rect(nozzle='z',height=0.35,speed=12,dwell=0.2,pressure=48,start='BR')
#soft_TPU_rect_full(nozzle='z',height=0.35,speed=12,dwell=0.2,pressure=48,start='BR')

#g.abs_move(x=xoffset,y=yoffset)
#g.set_home(x=0,y=0)
#stiff_TPU_island(nozzle='z',height=0.35,speed=3,dwell=0.2,pressure=55,start='BR')

#agtpu_line_soft_stiff(nozzle='z',height=0.42,speed=3,dwell=0.2,pressure=8)
##g.rect(x=-68,y=40)
#AgTPU_pulse_sensor(nozzle='z',height=0.2,speed=6,dwell=0.2,pressure=25,startx=-3,starty=3,orientation='up')
#AgTPU_pulse_sensor(nozzle='z',height=0.2,speed=6,dwell=0.2,pressure=25,startx=-16,starty=37,orientation='down')
#AgTPU_pulse_sensor(nozzle='z',height=0.2,speed=6,dwell=0.2,pressure=25,startx=-29,starty=3,orientation='up')
#AgTPU_pulse_sensor(nozzle='z',height=0.2,speed=6,dwell=0.2,pressure=25,startx=-42,starty=37,orientation='dpwn')

#AgTPU_pulse_sensor_electrode(nozzle='z',height=0.3,speed=5,dwell=0.2,pressure=20,startx=-3,starty=3,orientation='up')
#AgTPU_pulse_sensor_electrode(nozzle='z',height=0.3,speed=5,dwell=0.2,pressure=17,startx=-16,starty=37,orientation='down')
#AgTPU_pulse_sensor_electrode(nozzle='z',height=0.3,speed=5,dwell=0.2,pressure=17,startx=-29,starty=3,orientation='up')
#AgTPU_pulse_sensor_electrode(nozzle='z',height=0.3,speed=5,dwell=0.2,pressure=17,startx=-42,starty=37,orientation='dpwn')

g.view(backend='matplotlib')

g.teardown() 
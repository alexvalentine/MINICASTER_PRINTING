from mecode import G
import numpy as np


#myz = 2.82357
g=G(
    direct_write=False,
    outfile=r'C:\Users\LewisLab\Documents\myprint.pgm',
    header=None,
    footer=None,
    print_lines=False,
    aerotech_include=True,
) 


pad_positions=((0.1,0.38+0.29*0),(.1,0.38+0.29*1),(.1,0.38+0.29*2),(.1,0.38+0.29*3),(.1,0.38+0.29*4),(.1,0.38+0.29*5),
(0.38+0.29*0,2.06),(0.38+0.29*1,2.06),(0.38+0.29*2,2.06),(0.38+0.29*3,2.06),(0.38+0.29*4,2.06),(0.38+0.29*5,2.06),
(2.06,0.38+0.29*5),(2.06,0.38+0.29*4),(2.06,0.38+0.29*3),(2.06,0.38+0.29*2),(2.06,0.38+0.29*1),(2.06,0.38+0.29*0),
(0.38+0.29*5,0.1),(0.38+0.29*4,0.1),(0.38+0.29*3,0.1),(0.38+0.29*2,0.1),(0.38+0.29*1,0.1),(0.38+0.29*0,0.1))

well_position = ((10.5, 25.245), (24, 25.245), (37.5, 25.245), (51, 25.245), 
                       (10.5, 24.245), (24, 24.245), (37.5, 24.245), (51, 24.245))


pressure_box = 9

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
    g.set_pressure(pressure_box, pdms_pressure)   
    g.feed(5)
    for i in np.arange(2):        
        for j in np.arange(6):
                if i==0:
                    g.abs_move(x=pad_positions[23-j][0],y=pad_positions[23-j][1])
                    g.move(z=-2)
                    g.feed(speed)
                    g.toggle_pressure(pressure_box)
                    g.dwell(dwell)
                    g.move(y=-3)
                    if j<3:
                        g.move(x=-3/(j+1),y=-3)
                        g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                    else:
                        g.move(x=(j+1)-3,y=-3)
                        g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                else:
                    g.abs_move(x=pad_positions[6+j][0],y=pad_positions[6+j][1])
                    g.move(z=-2)
                    g.feed(speed)
                    g.toggle_pressure(pressure_box)
                    g.dwell(dwell)
                    g.move(y=3)
                    if j<3:
                        g.move(x=-3/(j+1),y=3)
                        g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                    else:
                        g.move(x=(j+1)-3,y=3)
                        g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                        
    for i in np.arange(2):        
        for j in np.arange(6):
                if i==0:
                    g.abs_move(x=pad_positions[j][0],y=pad_positions[j][1])
                    g.move(z=-2)
                    g.feed(speed)
                    g.toggle_pressure(pressure_box)
                    g.dwell(dwell)                    
                    g.move(x=-3)
                    if j<3:
                        g.move(x=-3,y=-3/(j+1))
                        g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                    else:
                        g.move(x=-3,y=(j+1)-3)
                        g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                else:
                    g.abs_move(x=pad_positions[17-j][0],y=pad_positions[17-j][1])
                    g.move(z=-2)
                    g.feed(speed)
                    g.toggle_pressure(pressure_box)
                    g.dwell(dwell) 
                    g.move(x=3)
                    if j<3:
                        g.move(x=3,y=-3/(j+1))
                        g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')
                    else:
                        g.move(x=3,y=(j+1)-3)
                        g.toggle_pressure(pressure_box)
                        g.feed(10)
                        g.clip(height=2, direction='-x')

def LED_Harvard(speed,dwell,pressure,height):
    g.set_pressure(pressure_box, pressure)   
    g.feed(10)
    zero=0.0
    g.abs_move(z=zero)
    g.set_home(x=0,y=0,z=0)
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
    g.move(x=7)
    g.move(y=-5.8)
    g.dwell(dwell)
    g.move(y=-1.3,z=1)
    g.move(y=-1.3,z=-1)
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
    g.move(x=1.4)
    g.move(y=-0.6)
    g.dwell(dwell)
    g.move(y=-0.8,z=1)
    g.move(y=-0.8,z=-1)
    g.move(y=-0.6)
    g.move(x=3)
    g.move(y=-2)
    g.dwell(dwell)
    g.move(y=-1.3,z=1)
    g.move(y=-1.3,z=-1)
    g.abs_move(y=2)
    g.move(x=3)
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
    g.move(x=9)
    g.move(y=-7)
    g.dwell(dwell)
    g.move(y=-1.3,z=1)
    g.move(y=-1.3,z=-1)
    g.abs_move(y=2)
    #g.toggle_pressure(pressure_box)
    #g.feed(10)
    #g.clip(height=2, direction='+x')

    #anode/cathode
    g.feed(speed*0.4)
    g.move(x=-1.5)  
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


def LED_line(speed,dwell,pressure,height):
    g.set_pressure(pressure_box, pressure)   
    g.feed(10)
    zero=0.0
    g.abs_move(z=zero)
    g.set_home(x=0,y=0,z=0)
    g.move(z=5)
    g.dwell(5)
    

    #wire
    g.abs_move(x=2,y=2)
    g.abs_move(z=height)
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(y=-5)
    #g.move(y=-2)
    g.move(y=-0.5,z=1.5)
    g.move(y=-0.5,z=-1.5)
    g.move(y=-2)
    g.dwell(0.1)
    g.move(y=-0.5,z=1.5)
    g.move(y=-0.5,z=-1.5)
    g.move(y=-2)
    g.dwell(0.1)
    g.move(y=-0.5,z=1.5)
    g.move(y=-0.5,z=-1.5)
    g.move(y=-2)
    g.dwell(0.1)
    g.move(y=-0.5,z=1.5)
    g.move(y=-0.5,z=-1.5)
    g.move(y=-5)
    
    #g.move(x=2)
    #g.move(y=-1)
    #g.dwell(0.7)
    #g.move(y=-1.3,z=0.5)
    #g.move(y=-1.3,z=-0.5)
    #g.move(y=-1)
    #g.move(x=-2)
    #g.move(y=-2)
    g.move(x=-2)
    g.feed(speed*0.4)
    g.abs_move(z=height+0.05)
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
    
    g.move(y=20)
    
    g.abs_move(z=height+0.05)
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed*0.4)
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

def stacked_rectangle(x, y, layer_height, layers, nozzle = 'Z'):
    
    for i in range(layers):
        g.move(x=x)
        g.move(y=-y)
        g.move(x=-x)
        g.move(y=y)
        g.move(**{nozzle:layer_height})

def print_single_well(x, y, layer_height, layers, speed, pressure, filament = 1, nozzle = 'Z'):
    g.feed(speed)
    g.set_pressure(pressure_box, pressure)   
    g.toggle_pressure(pressure_box)
    g.dwell(0.25)
    stacked_rectangle(x=x, y=y, layer_height = layer_height, layers = layers, nozzle = nozzle)
    g.toggle_pressure(pressure_box)

def print_all_single_wells(layer_height, layer_increments, total_increments, pressure, speed, nozzle):
    #
    for i in range(0,2):      
        g.feed(15)
        g.abs_move(*well_position[i])
        g.abs_move(**{nozzle:0.05})
        print_single_well(x = 12.5, y = -14, layer_height = layer_height ,  layers = layer_increments, speed = speed, pressure = pressure, filament = 1, nozzle = nozzle)
        g.clip(axis=nozzle, direction='+y', height=3)
    
    #for i in range(4,8):      
    #    g.feed(15)
    #    g.abs_move(*well_position[i])
    #    g.abs_move(**{nozzle:0.05})
    #    print_single_well(x = 12.5, y = 14, layer_height = layer_height ,  layers = layer_increments, speed = speed, pressure = pressure, filament = 1, nozzle = nozzle)
    #    g.clip(axis=nozzle, direction='-y', height=3)
     
    count = 0
    repeats = (total_increments)-1     
    
    
    for i in range(repeats-1):
        
        count = count + layer_increments
        for i in range(0,2):
           
            g.feed(15)
            g.abs_move(*well_position[i])
            g.abs_move(**{nozzle:(15*count*layer_height)/(repeats)})
            print_single_well(x = 12.5, y = -14, layer_height = layer_height ,  layers = layer_increments, speed = speed, pressure = pressure, filament = 1, nozzle = nozzle)
            g.clip(axis=nozzle, direction='+y', height=3)

        print count 
        print count*layer_height
        print (15*count*layer_height)/(repeats)
       
        #for i in range(4,8):      
        #    g.feed(15)
        #    g.abs_move(*well_position[i])
        #    g.abs_move(**{nozzle:count*layer_height})
        #    print_single_well(x = 12.5, y = 14, layer_height = layer_height ,  layers = layer_increments, speed = speed, pressure = pressure, filament = 1, nozzle = nozzle)
        #    g.clip(axis=nozzle, direction='-y', height=3)

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
    
    #####first wire
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
    #####second wire
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


    ######third wire
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


    #####anode/cathode
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




def tpu_square(speed,dwell,pressure,height,side):
    g.set_pressure(pressure_box, pressure)   
    g.feed(20)
    g.move(z=2)

    ########test line
    g.abs_move(x=1.5,y=2)
    #pressure_purge(delay = 2)
    g.abs_move(z=height)
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.move(y=20)
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis='z', height=3, direction='-x')    

    if side == "L":
        g.abs_move(x=3,y=3)
    elif side == "C":
        g.abs_move(x=30,y=3)
    else:
        g.abs_move(x=59,y=3)

    g.abs_move(z=height)
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.meander(x=23,y=40,spacing=0.6,start='LL',orientation='y')
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis='z', height=6, direction='-x')    
    

def LED_AFRL(speed,dwell,pressure,height):
    g.set_pressure(pressure_box, pressure)   
    g.feed(10)
    g.set_home(z=0)
    g.move(z=2)
    
    
    
    #########################    A    #########################    

    ####FIRST WIRE

    g.abs_move(x=3,y=38.1)
    g.dwell(10)
    g.abs_move(z=height+0.06)
    g.toggle_pressure(pressure_box)
    g.feed(speed)
    g.dwell(dwell)


    g.move(x=1,y=1,z=-0.06)
    g.move(x=0.592,y=2.39)  #2.5

    g.move(x=0.192,y=0.76,z=1) #0.8
    #g.move(x=-0.5,y=-0.5)
    #g.rect(x=1,y=1)
    #g.move(x=0.5,y=0.5)
    g.move(x=0.192,y=0.76,z=-1) #0.8

    g.move(x=1.2,y=4.87)  #5.1

    g.move(x=0.192,y=0.76,z=1) #0.8
    #g.move(x=-0.5,y=-0.5)
    #g.rect(x=1,y=1)
    #g.move(x=0.5,y=0.5)
    g.move(x=0.192,y=0.76,z=-1) #0.8

    g.move(x=1.2,y=4.87)  #5.1

    g.move(x=0.192,y=0.76,z=1) #0.8
    #g.move(x=-0.5,y=-0.5)
    #g.rect(x=1,y=1)
    #g.move(x=0.5,y=0.5)
    g.move(x=0.192,y=0.76,z=-1) #0.8

    g.move(x=0.472,y=1.91)  #2.0
    g.move(x=1)
    g.move(y=-2.6)
    g.move(x=1.5)

    g.move(x=0.8,z=1)
    #g.move(x=-0.5,y=-0.5)
    #g.rect(x=1,y=1)
    #g.move(x=0.5,y=0.5)
    g.move(x=0.8,z=-1)

    g.move(x=1.5)
    g.toggle_pressure(pressure_box)
    g.clip(height=4,direction='-x')
    g.feed(10)
#
    #SECOND WIRE

    g.abs_move(x=3,y=38.1)
    g.dwell(5)
    g.abs_move(z=height+0.06)
    g.toggle_pressure(pressure_box)
    g.feed(speed)
    g.dwell(dwell)



    g.move(x=2,z=-0.06)
    g.move(x=19.4)
    g.move(y=1)

    g.move(x=-0.592,y=2.39)  #2.5

    g.move(x=-0.192,y=0.76,z=1) #0.8
    #g.move(x=-0.5,y=-0.5)
    #g.rect(x=1,y=1)
    #g.move(x=0.5,y=0.5)
    g.move(x=-0.192,y=0.76,z=-1) #0.8

    g.move(x=-1.2,y=4.87)  #5.1

    g.move(x=-0.192,y=0.76,z=1) #0.8
    #g.move(x=-0.5,y=-0.5)
    #g.rect(x=1,y=1)
    #g.move(x=0.5,y=0.5)
    g.move(x=-0.192,y=0.76,z=-1) #0.8

    g.move(x=-1.2,y=4.87)  #5.1

    g.move(x=-0.192,y=0.76,z=1) #0.8
    #g.move(x=-0.5,y=-0.5)
    #g.rect(x=1,y=1)
    #g.move(x=0.5,y=0.5)
    g.move(x=-0.192,y=0.76,z=-1) #0.8

    g.move(x=-0.472,y=1.91)  #2.0
    g.move(x=-1)
    g.move(y=-2.6)
    g.move(x=-1.5)

    g.move(x=-0.8,z=1)
    #g.move(x=-0.5,y=-0.5)
    #g.rect(x=1,y=1)
    #g.move(x=0.5,y=0.5)
    g.move(x=-0.8,z=-1)

    g.move(x=-1.5)
    
    g.move(y=1.5)
    g.move(x=3.5)
    g.move(y=2.85)
    g.move(x=1.8)
    g.toggle_pressure(pressure_box)
    g.clip(height=4,direction='-x')
    g.feed(10)

    #THIRD WIRE

    g.abs_move(x=3,y=38.1)
    g.dwell(5)
    g.abs_move(z=height+0.06)
    g.toggle_pressure(pressure_box)
    g.feed(speed)
    g.dwell(dwell)

    g.move(y=2.02,z=-0.06)
    g.move(x=4.42,y=17.88)   #20.5
    g.move(x=0.36,y=1.46)     #1.5
    g.move(x=1.2)
    g.move(x=0.38,y=1.55)     #1.6


    g.move(x=0.24,y=0.76,z=1) #0.8
    #g.move(x=-0.5,y=-0.5)
    #g.rect(x=1,y=1)
    #g.move(x=0.5,y=0.5)
    g.move(x=0.24,y=0.76,z=-1) #0.8
    

    g.move(x=1.08,y=4.37)    #4.5


    g.move(x=0.24,y=0.76,z=1) #0.8
    #g.move(x=-0.5,y=-0.5)
    #g.rect(x=1,y=1)
    #g.move(x=0.5,y=0.5)
    g.move(x=0.24,y=0.76,z=-1) #0.8
    
    g.arc(x=2.79,y=3.1,radius=3.9,direction='CW')
    g.arc(x=2.79,y=-3.1,radius=3.9,direction='CW')

    g.move(x=0.24,y=-0.76,z=1) #0.8
    #g.move(x=-0.5,y=-0.5)
    #g.rect(x=1,y=1)
    #g.move(x=0.5,y=0.5)
    g.move(x=0.24,y=-0.76,z=-1) #0.8

    g.move(x=1.08,y=-4.37)    #4.5
    
    
    g.move(x=0.24,y=-0.76,z=1) #0.8
    #g.move(x=-0.5,y=-0.5)
    #g.rect(x=1,y=1)
    #g.move(x=0.5,y=0.5)
    g.move(x=0.24,y=-0.76,z=-1) #0.8

    g.move(x=0.38,y=-1.55)     #1.6

    g.move(x=6)
    g.move(y=13.74)
    g.move(x=22.4)
    g.move(y=-70.2)
    g.move(x=-18)
    g.toggle_pressure(pressure_box)
    g.clip(height=4,direction='+x')
    g.feed(10)
#
#
#    #########################    F    #########################    
#
#    #FIRST WIRE
#
#    g.abs_move(x=3,y=38.1)
#    g.dwell(5)
#    g.abs_move(z=height+0.12)
#    g.toggle_pressure(pressure_box)
#    g.feed(speed)
#    g.dwell(dwell)
#
#
#    g.move(x=2,z=-0.12)
#    g.move(x=20.4)
#    g.move(x=3,y=1)
#
#    g.move(y=2)
#    
#    g.move(y=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=0.8,z=-1) #0.8
#
#    g.move(y=3.13)
#    
#    g.move(y=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=0.8,z=-1) #0.8
#
#    g.move(y=3.13)
#    
#    g.move(y=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=0.8,z=-1) #0.8
#
#    g.move(y=3.13)
#    
#    g.move(y=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=0.8,z=-1) #0.8
#    
#    g.move(y=1)
#    g.move(x=-3)
#    g.move(y=15.3)
#    g.move(z=0.06)
#    g.move(x=22.4)
#    g.move(y=-70.2)
#    g.move(x=-18)
#    g.toggle_pressure(pressure_box)
#    g.clip(height=4,direction='+x')
#    g.feed(10)
#   
#    
#    #SECOND WIRE
#
#    g.abs_move(x=3,y=38.1)
#    g.dwell(5)
#    g.abs_move(z=height+0.12)
#    g.toggle_pressure(pressure_box)
#    g.feed(speed)
#    g.dwell(dwell)
#
#
#    g.move(x=2,z=-0.12)
#    g.move(x=20.4)
#    g.move(x=3,y=1)
#    g.move(x=1,y=0.33)
#
#    g.move(y=18)
#    g.move(x=9)
#    g.move(y=1)
#    g.move(x=-1)
#    
#    g.move(x=-0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=-0.8,z=-1) #0.8
#
#    g.move(x=-3.13)
#
#    g.move(x=-0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=-0.8,z=-1) #0.8
#    
#    g.move(x=-2.67)
#    g.move(y=1.13)
#
#    g.move(y=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=0.8,z=-1) #0.8
#
#    g.move(y=3.13)
#
#    g.move(y=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=0.8,z=-1) #0.8
#
#    g.move(y=0.8)
#    g.move(x=-3)
#    g.move(y=6.5)
#    g.toggle_pressure(pressure_box)
#    g.clip(height=4,direction='-y')
#    g.feed(10)
#    
#    #THIRD WIRE
#
#    g.abs_move(x=3,y=38.1)
#    g.dwell(5)
#    g.abs_move(z=height+0.12)
#    g.toggle_pressure(pressure_box)
#    g.feed(speed)
#    g.dwell(dwell)
#
#    g.move(x=2,z=-0.12)
#    g.move(x=20.4)
#    g.move(x=3,y=1)
#    g.move(x=1,y=0.33)
#
#    g.move(y=18)
#    g.move(x=9)
#    g.move(y=2)
#    g.move(x=-9)
#    g.move(y=6.2+1.9)
#    g.move(x=-1)
#    g.move(y=1.23)
#    
#    g.move(y=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=0.8,z=-1) #0.8
#
#    g.move(x=3.5)
#
#    g.move(x=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=0.8,z=-1) #0.8
#
#    g.move(x=3.5)
#    
#    g.move(x=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=0.8,z=-1) #0.8
#
#    g.move(x=3.5)
#
#    g.move(x=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=0.8,z=-1) #0.8
#
#    g.move(x=1.5)
#    g.move(y=2.84)
#    g.toggle_pressure(pressure_box)
#    g.clip(height=4,direction='-y')
#    g.feed(10)
#   
#    #g.move(x=-2,y=-2)
#    #g.rect(x=4,y=4)
#    #g.move(x=2,y=2)
#    
##
##
############################    R    #########################    
##
#    #FIRST WIRE
#
#    g.abs_move(x=3,y=38.1-1.5)
#    g.dwell(5)
#    g.abs_move(z=height+0.15)
#    g.toggle_pressure(pressure_box)
#    g.feed(speed)
#    g.dwell(dwell)
#
#    g.move(y=-2,z=-0.15)
#    g.move(y=-33.1+1.5)
#    g.move(z=0.07)
#    g.move(y=10.5)    
#    
#    g.move(x=4)
#    g.move(z=-0.07)
#    g.move(y=1.5)
#    
#    g.move(y=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=0.8,z=-1) #0.8
#
#    g.move(y=5)
#    
#    g.move(y=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=0.8,z=-1) #0.8
#
#    g.move(y=5)
#    
#    g.move(y=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=0.8,z=-1) #0.8
#
#    g.move(y=5)
#    
#    g.move(y=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=0.8,z=-1) #0.8
#
#    g.move(x=1)
#    g.move(y=-12.7)
#    g.move(x=6)
#    g.move(x=9.5,y=-16)
#    g.move(y=-1)
#    g.move(x=6.5)
#    g.move(y=-3.3)
#
#    g.toggle_pressure(pressure_box)
#    g.clip(height=4,direction='+x')
#    g.feed(10)
#    g.move(x=-19)
#    
#    #SECOND WIRE
#
#    g.abs_move(x=3,y=38.1-1.5)
#    g.dwell(5)
#    g.abs_move(z=height+0.22)
#    g.toggle_pressure(pressure_box)
#    g.feed(speed)
#    g.dwell(dwell)
#   
#    g.move(y=-2,z=-0.15)
#    g.move(y=-33.1+1.5)
#    
#    #g.move(x=-2,y=-2)
#    #g.rect(x=4,y=4)
#    #g.move(x=2,y=2)
#    
#    g.move(z=0.07)
#    g.move(y=10.5)
#    
#    g.move(x=2)
#    g.move(z=-0.14)
#    g.move(y=-6.1)
#    g.move(x=2)    
#    g.move(y=1)
#    
#    g.move(y=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=0.8,z=-1) #0.8
#
#    g.move(y=1.5)
#    g.move(x=1)
#    g.move(y=11)
#    g.move(x=4)
#    
#    g.move(x=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=0.8,z=-1) #0.8
#
#    g.move(x=3.58,y=-6.01)
#
#    g.move(x=0.41,y=-0.69,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=0.41,y=-0.69,z=-1) #0.8
#
#    g.move(x=3.12,y=-5.24)    #6.1
#
#    g.move(x=0.41,y=-0.69,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=0.41,y=-0.69,z=-1) #0.8
#
#    
#    g.move(x=1.1)
#    g.toggle_pressure(pressure_box)
#    g.clip(height=4,direction='-x')
#    g.feed(10)
#    
#    #THIRD WIRE
#
#    g.abs_move(x=3,y=38.1-1.5)
#    g.dwell(5)
#    g.abs_move(z=height+0.15)
#    g.toggle_pressure(pressure_box)
#    g.feed(speed)
#    g.dwell(dwell)
#    
#    g.move(x=2,y=1.5,z=-0.15)    
#    g.move(x=4)
#    g.move(y=-2.5)
#    g.move(x=3)
#
#    g.move(x=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=0.8,z=-1) #0.8
#
# 
#    g.move(x=1)
#    g.arc(x=3.,y=-1.2,radius=10,direction='CW')
#    
#    g.move(x=0.7,y=-0.4,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=0.5,y=-0.4,z=-1) #0.8
#    
#    g.arc(x=2.,y=-4.,radius=8,direction='CW')
#
#    g.move(y=-0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=-0.8,z=-1) #0.8
#
#    g.arc(x=-2.,y=-4.,radius=8,direction='CW')
#
#    g.move(x=-0.5,y=-0.4,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=-0.7,y=-0.4,z=-1) #0.8
#
#    g.arc(x=-2.828,y=-0.8,radius=10,direction='CW')
#
#    g.move(x=8.728,y=-14.7)
#    g.move(y=-1)
#
#    g.toggle_pressure(pressure_box)
#    g.clip(height=4,direction='+x')
#    g.feed(10)

##########################    L    #########################    
##
#    #FIRST WIRE
#
#    g.abs_move(x=3,y=38.1-1.5)
#    g.dwell(5)
#    g.abs_move(z=height+0.19)
#    g.toggle_pressure(pressure_box)
#    g.feed(speed)
#    g.dwell(dwell)
#    
#    g.move(x=2,y=1.5,z=-0.19)
#    g.move(x=23.38)
#    g.move(y=-2)   
#
#    g.move(y=-0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=-0.8,z=-1) #0.8
#
#    g.move(y=-2.8)
#    
#    g.move(y=-0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=-0.8,z=-1) #0.8
#
#
#    g.move(y=-2.8)
#
#    g.move(y=-0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=-0.8,z=-1) #0.8
#
#    g.move(y=-2.8)
#
#    g.move(y=-0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=-0.8,z=-1) #0.8
#
#    g.move(y=-1.)
#    g.move(x=-1)
#    g.move(y=-13.6)
#    #g.move(x=5.5)
#
#    g.toggle_pressure(pressure_box)
#    g.clip(height=4,direction='+x')
#    g.feed(10)

    #SECOND WIRE

#    g.abs_move(x=3,y=38.1-1.5)
#    g.dwell(5)
#    g.abs_move(z=height+0.19)
#    g.toggle_pressure(pressure_box)
#    g.feed(speed)
#    g.dwell(dwell)
#
#    g.move(x=2,y=1.5,z=-0.19)
#    g.move(x=24.38)
#    g.move(y=-18.5)
#    g.move(x=-1)   
#    g.move(y=-1.)
#
#    g.move(y=-0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=-0.8,z=-1) #0.8
#
#    g.move(y=-2.8)
#    
#    g.move(y=-0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=-0.8,z=-1) #0.8
#
#    g.move(y=-2.8)
#    
#    g.move(y=-0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=-0.8,z=-1) #0.8
#
#    g.move(x=2)
#    
#    g.move(x=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=0.8,z=-1) #0.8
#
#    g.move(x=0.6)
#    g.move(y=-1.5)
#    g.move(x=-4)
#    g.toggle_pressure(pressure_box)
#    g.clip(height=4,direction='+y')
#    g.feed(10)
#
#    #THIRD WIRE
#
#    g.abs_move(x=3,y=38.1-1.5)
#    g.dwell(5)
#    g.abs_move(z=height+0.19)
#    g.toggle_pressure(pressure_box)
#    g.feed(speed)
#    g.dwell(dwell)
#    
#    
#    g.move(x=2,y=1.5,z=-0.19)
#    g.move(x=24.38)
#    g.move(y=-29)
#    g.move(x=3.9)
#    g.move(y=-0.9)
#    g.move(x=0.6)
#    
#    g.move(x=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=0.8,z=-1) #0.8
#
#    g.move(x=1.8)
#    
#    g.move(x=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=0.8,z=-1) #0.8
#
#    g.move(x=1.8)
#
#    g.move(x=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=0.8,z=-1) #0.8
#
#    g.move(x=1.8)
#    
#    g.move(x=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=0.8,z=-1) #0.8
#
#    g.move(x=2.12)
#    g.toggle_pressure(pressure_box)
#    g.clip(height=4,direction='-x')
#    g.feed(10)


#    g.arc(x=-0.4,y=-1.8,radius=8,direction='CW')
#    g.move(x=1)
#    g.arc(x=-2.,y=-4.1,radius=8,direction='CW')    
#    
#    g.move(x=-0.5,y=-0.4,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=-0.7,y=-0.4,z=-1) #0.8
#
#    g.arc(x=-4,y=-1.3,radius=10,direction='CW')
#    g.move(x=-0.5)
#    
#    g.move(x=-0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=-0.8,z=-1) #0.8
#
#    g.move(x=9.03,y=-11.9)
#    g.move(x=3)



#    g.move(x=-0.8,y=-1.1,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=-1.1,y=-1.1,z=-1) #0.8
#    
#    g.arc(x=-5,y=-2,radius=8,direction='CW')

#    g.move(y=3.13)
#
#    g.move(y=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=0.8,z=-1) #0.8
#    
#    g.move(y=3.13)
#    
#    g.move(y=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=0.8,z=-1) #0.8
#    
#    g.move(y=3.13)
#    
#    g.move(y=0.8,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(y=0.8,z=-1) #0.8
    
    #g.move(y=3.13)

    #g.move(x=2)
    #g.move(x=1,y=1)
    #g.move(x=0.592,y=2.39)  #2.5











#g.move(x=1.18,y=3.82)    #4


    #g.arc(x=6,y=0,radius=3.5,direction='CW')
    #g.move(x=3)


#    g.move(x=2)
#    g.move(x=21.4)
#    g.move(y=1)
#
#
#
#    g.move(x=-0.74,y=2.39)  #2.5
#
#    g.move(x=-0.24,y=0.76,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=-0.24,y=0.76,z=-1) #0.8
#
#    g.move(x=-1.5,y=4.87)  #5.1
#
#    g.move(x=-0.24,y=0.76,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=-0.24,y=0.76,z=-1) #0.8
#
#    g.move(x=-1.5,y=4.87)  #5.1
#
#    g.move(x=-0.24,y=0.76,z=1) #0.8
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=-0.24,y=0.76,z=-1) #0.8
#
#    g.move(x=-0.59,y=1.91)  #2.0
#    g.move(x=-1)
#    g.move(y=-2.6)
#    g.move(x=-0.8)
#
#    g.move(x=-0.8,z=1)
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=-0.8,z=-1)
#
#    g.move(x=-1)







#    g.move(x=2)
#
#    g.move(x=0.8,z=1)
#    #g.move(x=-0.5,y=-0.5)
#    #g.rect(x=1,y=1)
#    #g.move(x=0.5,y=0.5)
#    g.move(x=0.8,z=-1)


    #g.move(x=0.24,y=0.76,z=1)
    #g.move(x=1)
    #g.move(x=-1)
    #g.move(x=0.24,y=0.76,z=-1)
    #g.move(x=1.5,y=4.87)
    




#    g.move(y=33)
#    g.move(x=5)
#    g.move(y=-2.6)
#    g.dwell(dwell)
#    g.move(y=-0.8,z=1)
#    g.move(y=-0.8,z=-1)
#    g.move(y=-3.2)
#    g.dwell(dwell)
#    g.move(y=-0.8,z=1)
#    g.move(y=-0.8,z=-1)
#    g.move(y=-3.2)
#    g.dwell(dwell)
#    g.move(y=-0.8,z=1)
#    g.move(y=-0.8,z=-1)
#    g.move(y=-3.2)
#    g.dwell(dwell)
#    g.move(y=-0.8,z=1)
#    g.move(y=-0.8,z=-1)
#    g.move(y=-0.6)
#    g.move(x=0.9)
#    g.move(y=8.5)
#    g.move(x=8.5)
#    g.move(y=-10.)
#    g.move(x=7)
#    g.move(y=-5.8)
#    g.dwell(dwell)
#    g.move(y=-1.3,z=1)
#    g.move(y=-1.3,z=-1)
#    g.abs_move(y=2)
#    g.toggle_pressure(pressure_box)
#    g.feed(10)
#    g.clip(height=2, direction='+x')
#    #
#    ##second wire
#    g.abs_move(x=2,y=2)
#    g.abs_move(z=height)
#    g.feed(speed)
#    g.toggle_pressure(pressure_box)
#    g.dwell(dwell)
#    g.move(y=3)
#    g.move(x=5)
#    g.move(y=6.2)
#    g.dwell(dwell)
#    g.move(y=0.8,z=1)
#    g.move(y=0.8,z=-1)
#    g.move(y=1.2)
#    g.move(x=1.6)
#    g.move(y=8)
#    g.move(x=1.25)
#    g.dwell(dwell)
#    g.move(x=0.8,z=1)
#    g.move(x=0.8,z=-1)
#    g.move(x=1.4)
#    g.dwell(dwell)
#    g.move(x=0.8,z=1)
#    g.move(x=0.8,z=-1)
#    g.move(x=1.25)
#    g.move(y=-8.5)
#    g.move(x=1.4)
#    g.move(y=-0.6)
#    g.dwell(dwell)
#    g.move(y=-0.8,z=1)
#    g.move(y=-0.8,z=-1)
#    g.move(y=-0.6)
#    g.move(x=3)
#    g.move(y=-2)
#    g.dwell(dwell)
#    g.move(y=-1.3,z=1)
#    g.move(y=-1.3,z=-1)
#    g.abs_move(y=2)
#    g.move(x=3)
#    g.toggle_pressure(pressure_box)
#    g.feed(10)
#    g.clip(height=2, direction='+x')
#
#
#    ##third wire
#    g.abs_move(x=2,y=2)
#    g.abs_move(z=height)
#    g.feed(speed)
#    g.toggle_pressure(pressure_box)
#    g.dwell(dwell)
#    g.move(y=33)
#    g.move(x=15.4)
#    g.move(y=-2.6)
#    g.dwell(dwell)
#    g.move(y=-0.8,z=1)
#    g.move(y=-0.8,z=-1)
#    g.move(y=-3.2)
#    g.dwell(dwell)
#    g.move(y=-0.8,z=1)
#    g.move(y=-0.8,z=-1)
#    g.move(y=-3.2)
#    g.dwell(dwell)
#    g.move(y=-0.8,z=1)
#    g.move(y=-0.8,z=-1)
#    g.move(y=-3.2)
#    g.dwell(dwell)
#    g.move(y=-0.8,z=1)
#    g.move(y=-0.8,z=-1)
#    g.move(y=-0.8)
#    g.move(x=9)
#    g.move(y=-7)
#    g.dwell(dwell)
#    g.move(y=-1.3,z=1)
#    g.move(y=-1.3,z=-1)
#    g.abs_move(y=2)
#    #g.toggle_pressure(pressure_box)
#    #g.feed(10)
#    #g.clip(height=2, direction='+x')
#
#    #anode/cathode
#    g.feed(speed*0.4)
#    g.move(x=-1.5)  
#    g.arc(x=-2.8,y=0,radius=1.4)
#    g.arc(x=2.8,y=0,radius=1.4)
#    g.move(x=-0.2)
#    g.arc(x=-2.4,y=0,radius=1.2)
#    g.arc(x=2.4,y=0,radius=1.2)
#    g.move(x=-0.2)
#    g.arc(x=-2.0,y=0,radius=1)
#    g.arc(x=2.0,y=0,radius=1)
#    g.move(x=-0.2)
#    g.arc(x=-1.6,y=0,radius=0.8)
#    g.arc(x=1.6,y=0,radius=0.8)
#    g.move(x=-0.2)
#    g.arc(x=-1.2,y=0,radius=0.6)
#    g.arc(x=1.2,y=0,radius=0.6)
#    g.move(x=-0.2)
#    g.arc(x=-0.8,y=0,radius=0.4)
#    g.arc(x=0.8,y=0,radius=0.4)
#    g.move(x=-0.2)
#    g.arc(x=-0.4,y=0,radius=0.2)
#    g.arc(x=0.4,y=0,radius=0.2)
#    g.move(x=-0.2)
#    g.toggle_pressure(pressure_box)
#    g.feed(10)
#    g.clip(height=2, direction='+x')
#
#    g.abs_move(x=2,y=2)
#    g.abs_move(z=height)
#    g.feed(speed*0.4)
#    g.toggle_pressure(pressure_box)
#    g.dwell(dwell)
#    g.move(x=1.4)
#    g.arc(x=-2.8,y=0,radius=1.4)
#    g.arc(x=2.8,y=0,radius=1.4)
#    g.move(x=-0.2)
#    g.arc(x=-2.4,y=0,radius=1.2)
#    g.arc(x=2.4,y=0,radius=1.2)
#    g.move(x=-0.2)
#    g.arc(x=-2.0,y=0,radius=1)
#    g.arc(x=2.0,y=0,radius=1)
#    g.move(x=-0.2)
#    g.arc(x=-1.6,y=0,radius=0.8)
#    g.arc(x=1.6,y=0,radius=0.8)
#    g.move(x=-0.2)
#    g.arc(x=-1.2,y=0,radius=0.6)
#    g.arc(x=1.2,y=0,radius=0.6)
#    g.move(x=-0.2)
#    g.arc(x=-0.8,y=0,radius=0.4)
#    g.arc(x=0.8,y=0,radius=0.4)
#    g.move(x=-0.2)
#    g.arc(x=-0.4,y=0,radius=0.2)
#    g.arc(x=0.4,y=0,radius=0.2)
#    g.move(x=-0.2)
#    g.toggle_pressure(pressure_box)
#    g.feed(10)
#    g.clip(height=2, direction='+x')



def tpu_bottom(nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
########test line
    g.abs_move(x=1+73,y=1)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(y=20)
    g.move(x=0.2)
    g.move(y=-20)
    g.move(x=0.2)
    g.move(y=20)
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis=nozzle, height=2, direction='+x')
    
########printing slide 1

    g.abs_move(4+75, 2+.5)    
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.meander(x=25,y=45,spacing=0.25,start='LL',orientation='y')
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')
    
    g.abs_move(35, 2+.5)    
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.meander(x=25,y=45,spacing=0.25,start='LL',orientation='y')
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')

########printing slide 2
    g.abs_move(x=4+152.8, y=2-0.22+.5)    
    g.abs_move(**{nozzle:height-0.0235})
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.meander(x=25,y=45,spacing=0.25,start='LL',orientation='y')
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')
    
    g.move(x=6,y=-45+.5)    
    g.abs_move(**{nozzle:height-0.0235}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.meander(x=25,y=45,spacing=0.25,start='LL',orientation='y')
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')


########printing slide 3
    g.abs_move(x=4+282.93, y=2-6.37+.5)    
    g.abs_move(**{nozzle:height-0.033}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.meander(x=25,y=45,spacing=0.25,start='LL',orientation='y')
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')
    
    g.move(x=6, y=-45+.5)    
    g.abs_move(**{nozzle:height-0.033}) 
    g.feed(speed)
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.meander(x=25,y=45,spacing=0.25,start='LL',orientation='y')
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')





def AgTPU_strain_speciman(nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    #
    #####test line
    g.abs_move(x=2,y=1.)
    g.abs_move(**{nozzle:height-.08})
    g.toggle_pressure(pressure_box)
    g.feed(speed)
    g.dwell(dwell)    
    g.move(x=25)
    g.toggle_pressure(pressure_box)
    g.feed(20)
    g.clip(axis=nozzle, height=3, direction='-y')
    
    my_xstarts = [3.0, 11.825, 20.65, 29.474999999999998, 38.3, 47.125, 55.949999999999996, 64.77499999999999]
##
#    ############BOTTOM LAYER
#            
#    for i in [0,1,2,3,4,5,6,7]:
#          g.abs_move(x=my_xstarts[i]+1,y=3+4)
#          g.abs_move(**{nozzle:height+.2})
#          g.toggle_pressure(pressure_box)
#          g.feed(speed)
#          g.dwell(dwell)
##
#          g.meander(x=5,y=7,spacing=0.32,orientation='y')
#          g.move(x=-2.5)
#          g.move(y=1.5)
#          g.move(x=-0.8,y=-1.3)
#          g.move(x=1.6)
#          g.move(x=-0.8,y=1.3)
#          g.move(y=-1.5)
#
#          g.move(y=25)
#          
#          g.move(y=1.5)
#          g.move(y=-3)
#          g.move(x=-0.8,y=1.3)
#          g.move(x=1.6)
#          g.move(x=-0.8,y=-1.3)
#          g.move(y=1.5)
#          g.move(x=-2.5)
#          g.meander(x=5,y=7,spacing=0.32,orientation='y')
#          g.toggle_pressure(pressure_box)
#          g.feed(20)
#          g.clip(axis=nozzle, height=3, direction='-y')
#          
##    ############2nd LAYER     
##    #g.dwell(20)            
#    for i in [0,1,2,3,4,5,6,7]:
#          g.abs_move(x=my_xstarts[i]+1+2.5,y=3+4+7)
#          g.abs_move(**{nozzle:height+.1})
#          g.toggle_pressure(pressure_box)
#          g.feed(speed)
#          g.dwell(dwell)
#
#          g.move(y=25)  
#
#
#          g.toggle_pressure(pressure_box)
#          g.feed(20)
#          g.clip(axis=nozzle, height=3, direction='-y')
#    
#    
####    ############3rd LAYER
#    #g.dwell(20)
#    for i in [0,1,2,3,4,5,6,7]:
#          g.abs_move(x=my_xstarts[i]+1+2.5,y=3+4+7)
#          g.abs_move(**{nozzle:height+.2})
#          g.toggle_pressure(pressure_box)
#          g.feed(speed)
#          g.dwell(dwell)
#
#          g.move(y=25)
#
#          g.toggle_pressure(pressure_box)
#          g.feed(20)
#          g.clip(axis=nozzle, height=3, direction='-y')
#####          
####          
###    ############4th LAYER
#    #g.dwell(20)
#    for i in [0,1,2,3,4,5,6,7]:
#          g.abs_move(x=my_xstarts[i]+1+2.5,y=3+4+7)
#          g.abs_move(**{nozzle:height+.3})
#          g.toggle_pressure(pressure_box)
#          g.feed(speed)
#          g.dwell(dwell)
#
#          g.move(y=25)
#
#          g.toggle_pressure(pressure_box)
#          g.feed(20)
#          g.clip(axis=nozzle, height=3, direction='-y')
#          
    ############5th LAYER
    #g.dwell(20)
    for i in [0,1,2,3,4,5,6,7]:
          g.abs_move(x=my_xstarts[i]+1+2.5,y=3+4+7)
          g.abs_move(**{nozzle:height+.4})
          g.toggle_pressure(pressure_box)
          g.feed(speed)
          g.dwell(dwell)

          g.move(y=25)

          g.toggle_pressure(pressure_box)
          g.feed(20)
          g.clip(axis=nozzle, height=3, direction='-y')

    ############6th LAYER
    #g.dwell(20)
    for i in [0,1,2,3,4,5,6,7]:
          g.abs_move(x=my_xstarts[i]+1+2.5,y=3+4+7)
          g.abs_move(**{nozzle:height+.5})
          g.toggle_pressure(pressure_box)
          g.feed(speed)
          g.dwell(dwell)
          g.move(y=25)

          g.toggle_pressure(pressure_box)
          g.feed(20)
          g.clip(axis=nozzle, height=3, direction='-y')


def pdms_pillars(nozzle,height,speed,dwell,pressure,layers):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    g.move(**{nozzle:3})
    #g.dwell(5)
    #######test line
    g.abs_move(x=-13.5,y=1)
    #pressure_purge(delay = 2)
    g.abs_move(**{nozzle:height})
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(y=30)
    g.feed(20)
    g.toggle_pressure(pressure_box)
    g.clip(axis=nozzle, height=6, direction='-x')
    g.set_pressure(pressure_box, pressure)
    layers=np.zeros(layers)

    #g.abs_move(x=0,y=0)  # move to the silver pattern's corner, outside for cover
    ##g.move(x=10,y=10)
    #g.abs_move(**{nozzle:height}) 
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #for i in layers:
    #    g.meander(x=7,y=2,orientation='x',spacing=0.5,start='LL')
    #    g.move(**{nozzle:0.25})
    #    g.meander(x=7,y=2,orientation='x',spacing=0.5,start='UR')
    #    g.move(**{nozzle:0.25})
    #g.toggle_pressure(pressure_box)
    #g.clip(axis=nozzle, height=2, direction='-y')
    #
    #g.abs_move(x=0,y=10)  # move to the silver pattern's corner, outside for cover
    ##g.move(x=10,y=10)
    #g.abs_move(**{nozzle:height}) 
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #for i in layers:
    #    g.meander(x=7,y=2,orientation='x',spacing=0.5,start='LL')
    #    g.move(**{nozzle:0.25})
    #    g.meander(x=7,y=2,orientation='x',spacing=0.5,start='UR')
    #    g.move(**{nozzle:0.25})
    #g.toggle_pressure(pressure_box)
    #g.clip(axis=nozzle, height=2, direction='-y')
    
    #g.abs_move(x=0,y=25)  # move to the silver pattern's corner, outside for cover
    ##g.move(x=10,y=10)
    #g.abs_move(**{nozzle:height}) 
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #for i in layers:
    #    g.meander(x=7,y=2,orientation='x',spacing=0.5,start='LL')
    #    g.move(**{nozzle:0.25})
    #    g.meander(x=7,y=2,orientation='x',spacing=0.5,start='UR')
    #    g.move(**{nozzle:0.25})
    #g.toggle_pressure(pressure_box)
    #g.clip(axis=nozzle, height=2, direction='-y')
    
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
    g.clip(axis=nozzle, height=2, direction='-y')

    
    
    #g.abs_move(x=25,y=0)  # move to the silver pattern's corner, outside for cover
    ##g.move(x=10,y=10)
    #g.abs_move(**{nozzle:height}) 
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #for i in layers:
    #    g.meander(x=7,y=2,orientation='x',spacing=0.5,start='LL')
    #    g.move(**{nozzle:0.25})
    #    g.meander(x=7,y=2,orientation='x',spacing=0.5,start='UR')
    #    g.move(**{nozzle:0.25})
    #g.toggle_pressure(pressure_box)
    #g.clip(axis=nozzle, height=2, direction='-y')
    #
    #g.abs_move(x=25,y=10)  # move to the silver pattern's corner, outside for cover
    ##g.move(x=10,y=10)
    #g.abs_move(**{nozzle:height}) 
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #for i in layers:
    #    g.meander(x=7,y=2,orientation='x',spacing=0.5,start='LL')
    #    g.move(**{nozzle:0.25})
    #    g.meander(x=7,y=2,orientation='x',spacing=0.5,start='UR')
    #    g.move(**{nozzle:0.25})
    #g.toggle_pressure(pressure_box)
    #g.clip(axis=nozzle, height=2, direction='-y')
    #
    #g.abs_move(x=25,y=25)  # move to the silver pattern's corner, outside for cover
    ##g.move(x=10,y=10)
    #g.abs_move(**{nozzle:height}) 
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #for i in layers:
    #    g.meander(x=7,y=2,orientation='x',spacing=0.5,start='LL')
    #    g.move(**{nozzle:0.25})
    #    g.meander(x=7,y=2,orientation='x',spacing=0.5,start='UR')
    #    g.move(**{nozzle:0.25})
    #g.toggle_pressure(pressure_box)
    #g.clip(axis=nozzle, height=2, direction='-y')
    #
    #g.abs_move(x=25,y=35)  # move to the silver pattern's corner, outside for cover
    ##g.move(x=10,y=10)
    #g.abs_move(**{nozzle:height}) 
    #g.feed(speed)
    #g.toggle_pressure(pressure_box)
    #g.dwell(dwell)
    #for i in layers:
    #    g.meander(x=7,y=2,orientation='x',spacing=0.5,start='LL')
    #    g.move(**{nozzle:0.25})
    #    g.meander(x=7,y=2,orientation='x',spacing=0.5,start='UR')
    #    g.move(**{nozzle:0.25})
    #g.toggle_pressure(pressure_box)
    #g.clip(axis=nozzle, height=2, direction='-y')    



def TPU_spacing_tests(nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    #
    #######test line
    g.abs_move(**{nozzle:2})
    g.abs_move(x=1,y=1)
    g.abs_move(**{nozzle:height}) 
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=10)
    g.toggle_pressure(pressure_box)
    g.feed(10)
    g.clip(axis=nozzle, height=3, direction='-y')
    
    my_space = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
    my_xstarts = [3.0, 11.825, 20.65, 29.474999999999998, 38.3, 47.125, 55.949999999999996, 64.77499999999999]


    for i in range(8):
          g.abs_move(x=my_xstarts[i],y=2)
          g.abs_move(**{nozzle:height}) 
          g.toggle_pressure(pressure_box)
          g.feed(speed)
          g.dwell(dwell)
          g.meander(x=7,y=44,orientation='y',spacing=my_space[i],start='LL')
          g.toggle_pressure(pressure_box)
          g.feed(20)
          g.clip(axis=nozzle, height=3, direction='-y')



#print_die(speed=1.4,dwell=0.1)
#print_die_wiring(speed=0.25,dwell=0.1)
#LED_Harvard(speed=2,dwell=0.1,pressure=36,height=0.06)
#LED_line(speed=4,dwell=1.5,pressure=15,height=0.04)
#
#g.set_home(x=0,y=0,z=0)
#print_all_single_wells(layer_height = 0.04, layer_increments=5, total_increments=20, pressure=32, speed=5, nozzle = 'Z')

#g.set_home(x=2,y=2)

#g.rect(x=50.8,y=76.2)
#g.move(x=3,y=3)
#g.rect(x=44.8,y=70.2)
#g.move(x=22.4)
#g.move(y=70.2)
#g.move(x=22.4)
#g.move(y=-35.1)
#g.move(x=-44.8)
#g.move(x=11.2)

#LED_AFRL(speed=4.5,dwell=0.1,pressure=25,height=0.03)

#tpu_square(speed=12,dwell=0.2,pressure=12,height=0.4,side='L')
####FIX 1.5 OFFSET WHEN I WAS REDOING R AND L

#LED_Harvard(speed=3,dwell=0.1,pressure=14,height=0.04)


#print_die_wiring_DIE_CONNECTIONS(nozzle='z',height=0.04,speed=1.8,dwell=0.02,pressure=8)




#tpu_bottom(nozzle='z',height=0,speed=20,dwell=0.2,pressure=50)

#AgTPU_strain_speciman(nozzle='z',height=0.088,speed=4,dwell=0.1,pressure=20)

#pdms_pillars(nozzle='z',height=0.3,speed=5,dwell=0.2,pressure=17,layers=30)

TPU_spacing_tests(nozzle='z',height=0.4,speed=11,dwell=0.2,pressure=6)

g.view(backend='matplotlib')


g.teardown() 


    



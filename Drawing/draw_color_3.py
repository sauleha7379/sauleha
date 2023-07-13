from Focus_Roots import *


#Rocket
draw_rect(170,100,150,300,0,color=color_firebrick)#Rocket Body

draw_circle(240,150,30,0,color=color_banana)#Rocket window
draw_circle(240,250,30,0,color=color_banana)#Rocket window
draw_circle(240,350,30,0,color=color_banana)#Rocket window

draw_polygon([ [100,100] , [390,100] , [240,10]   ],0,color=color_sky_blue)#Rocket head
draw_polygon([ [170,200] , [100,400] , [170,400]   ],0,color=color_sky_blue)#Rocket side wing
draw_polygon([ [320,200] , [390,400] , [320,400]   ],0,color=color_sky_blue)#Rocket side wing

def change():
    pass

draw(change)
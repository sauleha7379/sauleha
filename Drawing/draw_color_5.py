from Focus_Roots import *


#ship
draw_rect(150,300,200,70,0,color=color_orchid)
draw_polygon([ [150,300] ,[150,370], [100,300] ],0,color=color_orchid)
draw_polygon([ [350,300] ,[350,370], [400,300] ],0,color=color_orchid)

draw_rect(250,100,5,200,0,color=color_gray)

draw_polygon([ [255,100] , [400,280], [255,280] ],0,color=color_dark_gold)
draw_polygon([ [250,150] , [100,280], [250,280] ],0,color=color_khaki)

draw_circle(180,335,20,0,color=color_banana)
draw_circle(250,335,20,0,color=color_banana)
draw_circle(320,335,20,0,color=color_banana)
write_text("THIS IS SHIP",250,80,size=25)

def change():
    pass

draw(change)
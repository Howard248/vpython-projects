from vpython import *
#GlowScript 3.2 VPython
from vpython import *

def add():
    ball = sphere(pos=vec(-0.5, 0.1, 0), radius=0.01, color=color.red, v=vec(vslider.value, 0, 0), a=vec(0, 0, 0))
    t=0
    while (ball.pos.x<0.6 and ball.pos.x>-0.6):
        rate(1000) 
        ball.pos.x += vslider.value*dt
        t+=dt 
        
    ball.radius=0
    
        
def setv(vslider):
    ball.v.x=vslider.value
    vtext.text = '{:1.1f} cm/s'.format(vslider.value)

scene = canvas(title="project1",width=1200,height=1000,x=0,y=0,center=vec(0,0,0),background=vec(0,0,0))
floor = box(pos=vec(0, 0, 0), size=vec(1,0.01,0.5), color=color.blue)
t=0
dt=0.01
b1 = button(text="add ball",pos=scene.title_anchor,bind=add)
vslider = slider(min=-0.5, max=0.5, value=0.0, length=200, bind=setv, right=15,pos=scene.title_anchor)
vtext = wtext(text='{:1.1f} cm/s'.format(vslider.value), pos=scene.title_anchor)
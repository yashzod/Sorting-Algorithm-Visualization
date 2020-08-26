import pygame
import prime
import random

pygame.init()


surface=pygame.display.set_mode((900,600))
rect0=(75,30,750,80)
############   BOOLS    #################
main_frame =True
frame0=frame1=frame2=frame3=frame4=False
size_bool=speed_bool=False
class Button():
    def __init__(self,surface=surface,color=(55,55,55)):
        self.surface=surface
        self.color=color
    def place(self,rect):
        self.rect=rect
        pygame.draw.rect(self.surface,self.color,rect,0)
##########################################
keys={pygame.K_0,pygame.K_1,pygame.K_2,pygame.K_3,pygame.K_4,pygame.K_5,pygame.K_6,pygame.K_7,pygame.K_8,pygame.K_9}

x,y,bw,bh=75,180,300,50
y1=80
size,speed='',''
##########################################
font_head=pygame.font.Font(None,56)
text_head=font_head.render('SORTING ALGORITHM VISUALIZATION',True,(200,200,200))
###########################################
font=pygame.font.Font(None,44)
text_button0=font.render('Insertion Sort',True,(200,200,200))
text_button1=font.render('Merge Sort',True,(200,200,200))
text_button2=font.render('Bubble Sort',True,(200,200,200))
text_button3=font.render('Quick Sort',True,(200,200,200))
text_button4=font.render('Heap Sort',True,(200,200,200))
##########################################
font0=pygame.font.Font(None,40)
text_entry0=font0.render('Size of Array(10-150)',True,(200,200,200))
text_entry1=font0.render('Speed(1-100)',True,(200,200,200))

################################################
################ MAIN FRAME ####################
################################################
while main_frame:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            main_frame= False
            
        if events.type == pygame.MOUSEBUTTONDOWN:
            (i,j)=pygame.mouse.get_pos()
            if x+380+240<=i<=x+380+240+80 and y<=j<=y+50:
                size_bool = True
            else:
                size_bool = False
                
            if x+380+240<=i<=x+380+240+80 and y+y1<=j<=y+y1+50:
                speed_bool = True
            else:
                speed_bool = False
                
            if x<=i<=x+bw and y<=j<=y+bh:
                main_frame,frame0=False,True
                surface.fill((0,0,0))
            elif x<=i<=x+bw and y+y1<=j<=y+y1+bh:
                main_frame,frame1=False,True
                surface.fill((0,0,0))
            elif x<=i<=x+bw and y+y1*2<=j<=y+y1*2+bh:
                main_frame,frame2=False,True
                surface.fill((0,0,0))
            elif x<=i<=x+bw and y+y1*3<=j<=y+y1*3+bh:
                main_frame,frame3=False,True
                surface.fill((0,0,0))
            elif x<=i<=x+bw and y+y1*4<=j<=y+y1*4+bh:
                main_frame,frame4=False,True
                surface.fill((0,0,0))
                
        if size_bool and events.type == pygame.KEYDOWN:
            if events.key in keys and len(size)<3:
                size=size+events.unicode
            elif events.key == pygame.K_BACKSPACE:
                size=size[:-1]
            surface.fill((0,0,0))
        if speed_bool and events.type == pygame.KEYDOWN:
            if events.key in keys and len(speed)<3:
                speed=speed+events.unicode
            elif events.key == pygame.K_BACKSPACE:
                speed=speed[:-1]
            surface.fill((0,0,0))

    #mainframe head
    pygame.draw.rect(surface,(20,20,20),rect0)
    surface.blit(text_head,(75,50))
    #buttons
    rect_button0=rect_button1=rect_button2=rect_button3=rect_button4=Button()
    #####################
    rect_button0.place((x,y,bw,bh))
    rect_button1.place((x,y+y1,bw,bh))
    rect_button2.place((x,y+y1*2,bw,bh))
    rect_button3.place((x,y+y1*3,bw,bh))
    rect_button4.place((x,y+y1*4,bw,bh))
    ###########################
    surface.blit(text_button0,(x+10,y+10))
    surface.blit(text_button1,(x+10,y+y1+10))
    surface.blit(text_button2,(x+10,y+y1*2+10))
    surface.blit(text_button3,(x+10,y+y1*3+10))
    surface.blit(text_button4,(x+10,y+y1*4+10))
    ###############################
    surface.blit(text_entry0,(x+bw+50,y+10))
    surface.blit(text_entry1,(x+bw+50,y+y1+10))
    ##########################################
    text_size=font0.render(size,True,(200,200,200))
    text_speed=font0.render(speed,True,(200,200,200))
    surface.blit(text_size,(x+380+250,y+10))
    surface.blit(text_speed,(x+380+250,y+10+y1))
    #################################
    if size_bool:
        pygame.draw.rect(surface,(200,0,0),(x+380+240,y,80,50),1)
    else:
        pygame.draw.rect(surface,(200,200,200),(x+380+240,y,80,50),1)
        
    if speed_bool:
        pygame.draw.rect(surface,(200,0,0),(x+380+240,y+y1,80,50),1)
    else:
        pygame.draw.rect(surface,(200,200,200),(x+380+240,y+y1,80,50),1)
    pygame.display.update()
    surface.fill((0,0,0))

if size=='':
    size=20
if speed=='':
    speed=80

size=int(size)
if size<10:
    size=10
elif size>150:
    size=150
speed=int(speed)
if size<1:
    size=1
elif size>100:
    size=100
arr=list(range(1,size+2))
random.shuffle(arr)
while frame0:
    prime.insertion(surface,arr,speed)
    frame0=False
while frame1:
    prime.merge(surface,arr,speed)
    frame1=False
while frame2:
    prime.bubble(surface,arr,speed)
    frame2=False
while frame3:
    prime.quick(surface,arr,speed)
    frame3=False
while frame4:
    prime.heap(surface,arr,speed)
    frame4=False






    

pygame.quit()
quit()


















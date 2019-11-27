import time
import os
import json
import pygame
from pygame.locals import *
import urllib.request
from pygame.color import THECOLORS
pygame.init()
Brack=[0,0,0]
White=[255,255,255]
Green=[0,255,0]
Red=[255,0,0]
Gray=[169,169,169]
width=pygame.display.Info().current_w
height=pygame.display.Info().current_h
height0=int((height-117)/3)
size=int((width-400)/2)
button_text=["开 始","开 始","开 始","开 始","开 始","开 始","开 始"]
line=['http://192.168.0.101:80/mixer/000','http://192.168.0.101:80/mixer/100','http://192.168.0.101:80/mixer/200','http://192.168.0.101:80/mixer/300','http://192.168.0.101:80/mixer/400','http://192.168.0.101:80/mixer/500','http://192.168.0.101:80/mixer/600']
line0=['http://192.168.0.101:80/carrier/moveto/0','http://192.168.0.101:80/carrier/moveto/1','http://192.168.0.101:80/carrier/moveto/2','http://192.168.0.101:80/carrier/moveto/3','http://192.168.0.101:80/carrier/moveto/4']
CGQ=[[0,1,1,1,1],[1,0,1,1,1],[1,1,0,1,1],[1,1,1,0,1],[1,1,1,1,0]]
color=[Green,Green,Green,Green,Green,Green,Green]
button_text0="手动状态:"
button_text1=["工位0","工位1","工位2","工位3","工位4"]
Num=['0','1','2','3','4']
B0=[size+32,size+102,size+172,size+242,size+312]
os.environ['SDL_VIDEO_WINDOW_POS']= "%d,%d" % (67,height0+57)
#screen = pygame.display.set_mode((width-67,height0))
screen = pygame.display.set_mode((width-67,620))
screen.fill(Brack)
text=["接        粉        体:","粉     体     混     合:","粉 体 倒 下 锅 混 合:","制  作  润  湿  剂:","磨   料   混   合:","润 湿 剂 泵 进 磨 料:","磨料下锅混合后倒入小车:"]
text_0=pygame.font.Font("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",24)
text_1=pygame.font.Font("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",20)
text_fmt0=text_0.render("操     作     界     面",2,White)
screen.blit(text_fmt0,(size+106,10))
pygame.display.update()
def Process(num,x,y,button_text,color):
    text_fmt1=text_1.render(text[num],1,White)
    screen.blit(text_fmt1,(x-127,y))
    pygame.draw.rect(screen,color,[x+100,y,65,28],0)
    button=text_1.render(button_text,1,Brack)
    screen.blit(button,(x+113,y+3))
    pygame.display.update()
def Station(num,x,y,a):
    pygame.draw.rect(screen,Green,[x,y,65,28],0)
    button=text_1.render(button_text1[num],1,Brack)
    screen.blit(button,(x+9,y+4))
    img=pygame.image.load('cgq.jpg')
    img=pygame.transform.smoothscale(img,(52,50))
    screen.blit(img,(x,y+80))
    button=text_1.render((Num[a]),1,White)
    screen.blit(button,(x+20,556))
    pygame.display.update()
def state():
    button=text_1.render(button_text0,1,White)
    screen.blit(button,(size+86,384))
    #button_text=["结 束","开 始","开 始","开 始","开 始","开 始","开 始"]
if __name__ == '__main__':
    while True:
        time.sleep(1.5)
        pygame.draw.rect(screen,Brack,[size+86,380,85,28],0)
        pygame.draw.rect(screen,Green,[size+177,382,62,25],0)
        button1=text_1.render("切 换",1,Brack)
        screen.blit(button1,(size+191,384))
        button=text_1.render(button_text0,1,White)
        screen.blit(button,(size+86,384))
        B=[[0,size+187,66,button_text[0],color[0]],[1,size+187,112,button_text[1],color[1]],[2,size+187,158,button_text[2],color[2]],[3,size+187,204,button_text[3],color[3]],[4,size+187,250,button_text[4],color[4]],[5,size+187,296,button_text[5],color[5]],[6,size+187,342,button_text[6],color[6]]]
        if button_text==["开 始","开 始","开 始","开 始","开 始","开 始","开 始"]:
            response2=urllib.request.urlopen('http://192.168.0.101:80/carrier/status')
            html2=response2.read()
            text2=json.loads(html2)
        else:
            text2={'pos': 0, 'sensors': [0, 1, 1, 1, 1]}
        a=text2['sensors']
        b=text2['pos']
        C=[[0,size+32,426,a[0]],[1,size+102,426,a[1]],[2,size+172,426,a[2]],[3,size+242,426,a[3]],[4,size+312,426,a[4]]]
        pygame.draw.rect(screen,Brack,[size,461,400,50],0)
        pygame.draw.rect(screen,Brack,[size,551,400,25],0)
        img=pygame.image.load('car.jpg')
        img=pygame.transform.smoothscale(img,(52,50))
        screen.blit(img,(B0[b],461))
        if button_text0=="手动状态:":
            for t in range(7):
                if button_text[t]=="结 束":
                    button_text[t]="开 始"
                    pygame.display.update()
                    color[t]=Green
        elif button_text0=="自动状态:":
            state()
            if button_text[0]=="结 束":
                response0=urllib.request.urlopen(line[0])
                #html0=response0.read()
                #text0=json.loads(html0)
                button_text[0]="开 始"
                button_text[1]="结 束"
            elif button_text[1]=="结 束":
                response0=urllib.request.urlopen(line[1])
                #html0=response0.read()
                #text0=json.loads(html0)
                button_text[1]="开 始"
                button_text[2]="结 束"
            elif button_text[2]=="结 束":
                response0=urllib.request.urlopen(line[2])
                #html0=response0.read()
                #text0=json.loads(html0)
                button_text[2]="开 始"
                button_text[3]="结 束"
            elif button_text[3]=="结 束":
                response0=urllib.request.urlopen(line[3])
                #html0=response0.read()
                #text0=json.loads(html0)
                button_text[3]="开 始"
                button_text[4]="结 束"
            elif button_text[4]=="结 束":
                response0=urllib.request.urlopen(line[4])
                #html0=response0.read()
                #text0=json.loads(html0)
                button_text[4]="开 始"
                button_text[5]="结 束"
            elif button_text[5]=="结 束":
                response0=urllib.request.urlopen(line[5])
                #html0=response0.read()
                #text0=json.loads(html0)
                button_text[5]="开 始"
                button_text[6]="结 束"
            elif button_text[6]=="结 束":
                response0=urllib.request.urlopen(line[6])
                #html0=response0.read()
                #text0=json.loads(html0)
                button_text[6]="开 始"
        for i in B:
            Process(i[0],i[1],i[2],i[3],i[4])
        for v in C:
            Station(v[0],v[1],v[2],v[3])
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
            elif event.type == QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                pos = pygame.mouse.get_pos()
                for index in range(len(pressed_array)):
                    if pressed_array[index]:
                        if index==0:
                            if size+177<=pos[0]<=size+242 and 376<=pos[1]<=404:
                                if button_text0=="自动状态:" and button_text==["开 始","开 始","开 始","开 始","开 始","开 始","开 始"]:
                                    button_text0="手动状态:"
                                    color=[Green,Green,Green,Green,Green,Green,Green]
                                elif button_text0=="手动状态:" and button_text==["开 始","开 始","开 始","开 始","开 始","开 始","开 始"]:
                                    button_text0="自动状态:"
                                    button_text[0]="结 束"
                                    color=[Gray,Gray,Gray,Gray,Gray,Gray,Gray]
                            for i in B:
                                if i[1]+100<=pos[0]<=i[1]+165 and i[2]<=pos[1]<=i[2]+28:
                                    if button_text==["开 始","开 始","开 始","开 始","开 始","开 始","开 始"] and button_text0=="手动状态:":
                                        color[i[0]]=Red
                                        button_text[i[0]]="结 束"
                                        pygame.display.update()
                                        time.sleep(1)
                                        response1=urllib.request.urlopen(line[i[0]])
                                        #html1=response1.read()
                                        #text1=json.loads(html1)
                            for v in C:
                                if v[1]<=pos[0]<=v[1]+65 and v[2]<=pos[1]<=v[2]+28:
                                    response3=urllib.request.urlopen(line0[v[0]])
                                    html3=response3.read()
                                    text3=json.loads(html3)
                                    pygame.draw.rect(screen,Brack,[size,461,400,50],0)
                                    pygame.draw.rect(screen,Brack,[size,551,400,25],0)
                                    img=pygame.image.load('car.jpg')
                                    img=pygame.transform.smoothscale(img,(52,50))
                                    screen.blit(img,(B0[int(text3)],461))
                                    C=[[0,size+32,426,CGQ[v[0]][0]],[1,size+102,426,CGQ[v[0]][1]],[2,size+172,426,CGQ[v[0]][2]],[3,size+242,426,CGQ[v[0]][3]],[4,size+312,426,CGQ[v[0]][4]]]
                                    for f in C:
                                        Station(f[0],f[1],f[2],f[3])
                                    pygame.display.update()

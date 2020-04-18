import pygame
import time
import random
from bidi import algorithm
import arabic_reshaper



import arabic_reshaper
from bidi.algorithm import get_display


pygame.init()

crashed_sound = pygame.mixer.Sound("fail.ogg")
pygame.mixer.music.load("mari.wav")

#size safe

display_width=800                                 
display_height=600
gameDisplay=pygame.display.set_mode((display_width,display_height))    


#color
red=(255, 0,0)
black=(0,0,0)
red2 = (255, 102, 0)
white=(255,255,255)
perple = (204, 0, 255)
pink=(255, 51, 153)
pink2 = (255, 0, 128)
pink3 = (230, 0, 115)
pink4=(255, 77, 166)
blue1=(0, 204, 255)
blue2=(0, 163, 204)
yellow2 = (255, 204, 0)
green1=(0, 255, 0)
green2=(0, 204, 0)
yellow =(255, 255, 0)
orang =(255, 102, 0)
golbehi =(255, 102, 102)
sormeee=(51, 51, 204)
gblue=(0, 204, 153)
yellow1 =(255, 255, 102)

colors=[red,perple,yellow1,orang,golbehi,sormeee,gblue]

#image
ballImg = pygame.image.load('ball1.png')
heartImg = pygame.image.load('heart.png')
bachgroundImg1 = pygame.image.load('b1.png')
bachgroundImg2 = pygame.image.load('b2.png')
bachgroundImg3 = pygame.image.load('b3.png')

ball_width=32  
heart_width=65
heart_height = 65

def button(msg,x,y,w,h,incolor,outcolor,acrion=None):
    mouse = pygame.mouse.get_pos()                #mokhtasat mouse ro befahme
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y :    
        pygame.draw.rect(gameDisplay,incolor,(x,y,w,h)) 
        if click[0] == 1 and acrion != None:
            if acrion == "play1":
                game_loop()
            elif acrion == "play2":
                game_loop2()
            elif acrion == "exit":
                pygame.quit()

    else:
        pygame.draw.rect(gameDisplay,outcolor,(x,y,w,h))
        
    small_Txt1 = pygame.font.Font('ziba.ttf',20)
    TextSurf,TextRect = text_object(msg,small_Txt1)   #migim ke besorat ye moraba dar nazar begire, text_object ham ye tabe ke text va font midim behesh
    TextRect.center =(x + (w/2)),(y + (h/2))
    gameDisplay.blit(TextSurf,TextRect)
        
    
           

def gameIntro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)                      #safe sefid besh
        gameDisplay.blit(bachgroundImg1,(0,0))
        largeText = pygame.font.Font('ziba.ttf',40)
        TextSurf,TextRect = text_object("سلام:)",largeText)   #migim ke besorat ye moraba dar nazar begire, text_object ham ye tabe ke text va font midim behesh
        TextRect.center =((display_width/2),(display_height/6))
        gameDisplay.blit(TextSurf,TextRect)

        button("easy",150,200,130,60,pink4,pink,"play1")    # kalame play bayad moshabeh play bala bashad chon darim baraye action esm mizarim
        button("Exit",150,400,130,60,pink4,pink3,"exit")
        button("hard",150,300,130,60,pink4,pink2,"play2")
       
        pygame.display.update() 


def stuff_dodged(count):                               #tabe mohasebe emtiaz
    font = pygame.font.SysFont(None , 25)              #tabe barkhod  ( dodged yani barkhord)
    text = font.render("socre : " + str(count) , True , black)
    gameDisplay.blit(text,(0,0))                       #gameDisplay.blit yani neshonesh bede    0,0 yani goshe chap 

def stuff_heart(count2):                               #tabe mohasebe emtiaz
    font = pygame.font.SysFont(None , 25)              #tabe barkhod  ( dodged yani barkhord)
    text = font.render("heart : " + str(count2) , True , red)
    gameDisplay.blit(text,(0,20))                       #gameDisplay.blit yani neshonesh bede    0,0 yani goshe chap 
 
def stuff_hesab(count2):
    count2 = count2 + 1
    

def stuff(stuff_x,stuff_y,stuff_w,stuff_h,color):      #baraye keshidan moraba ya... ham x va y mikhaim ham arz va ertefa
    pygame.draw.rect(gameDisplay,color,[stuff_x,stuff_y,stuff_w,stuff_h])      #mitonim x,y,w,h va color ro bedim besh vali chon moteghaiere nemidim

def ball(x,y):                                        #x va y page
    gameDisplay.blit(ballImg,(x,y))

def ghalb(x2,y2):                                        #x va y page
    gameDisplay.blit(heartImg,(x2,y2))

def text_object(bidi_text,font):
    #largeText.render(algorithm.get_display(arabic_reshaper.reshape(u'bidi_text')), True, (255, 255, 255))
    textSurface = font.render(algorithm.get_display(arabic_reshaper.reshape(bidi_text)) , True ,black)
    return textSurface,textSurface.get_rect()         #font va matn dakhel moraba bashe va bad paiin mirim migim moraba vasat bashe

def missage_display(bidi_text):                            #be sorat tabe minevisim ta ha vaght ke text khastim az hamin estefade konim
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf,TextRect = text_object(bidi_text,largeText)   #migim ke besorat ye moraba dar nazar begire, text_object ham ye tabe ke text va font midim behesh
    TextRect.center =((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update() 

    time.sleep(2)
    game_loop()

def crash():
    
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crashed_sound)

    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf,TextRect = text_object("you Crashed :(",largeText)   #migim ke besorat ye moraba dar nazar begire, text_object ham ye tabe ke text va font midim behesh
    TextRect.center =((display_width/2),(display_height/4))
    gameDisplay.blit(TextSurf,TextRect)
    while True:                                       #ta zamani ke tasadof nakardi bia in kara ro bokon
        for event in pygame.event.get():              #ketabkhone event to pygame hast ma in ja migim evenr ro begir
            if event.type == pygame.QUIT:             #Quit baraye birin omadane
                game_Exit= True                       #age True shod tabe pygame.quit() farakhani beshe va biad biron
                pygame.quit()
                quit()
        button("Try again",150,350,120,70,green2,green1,"play1")    # kalame play bayad moshabeh play bala bashad chon darim baraye action esm mizarim
        button("hard",350,350,140,70,green2,green1,"play2")
        button("Exit",550,350,120,70,green2,green1,"exit")

        pygame.display.update() 

def crash2():
    
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crashed_sound)

    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf,TextRect = text_object("you Crashed :(",largeText)   #migim ke besorat ye moraba dar nazar begire, text_object ham ye tabe ke text va font midim behesh
    TextRect.center =((display_width/2),(display_height/4))
    gameDisplay.blit(TextSurf,TextRect)
    while True:                                       #ta zamani ke tasadof nakardi bia in kara ro bokon
        for event in pygame.event.get():              #ketabkhone event to pygame hast ma in ja migim evenr ro begir
            if event.type == pygame.QUIT:             #Quit baraye birin omadane
                game_Exit= True                       #age True shod tabe pygame.quit() farakhani beshe va biad biron
                pygame.quit()
                quit()
        button("Try again",150,350,120,70,yellow2,yellow,"play2")    # kalame play bayad moshabeh play bala bashad chon darim baraye action esm mizarim
        button("easy",350,350,140,70,yellow2,yellow,"play1")
        button("Exit",550,350,120,70,yellow2,yellow,"exit")

        pygame.display.update() 

def game_loop():    
    pygame.mixer.music.play(-1)                                  #peyda kardan vasat safe
    x = (display_width * 0.45)                        #0.45 az ghabl baraye vasat safe moshakhs shode
    y = (display_height * 0.8)                        #0.8 az ghabl baraye vasat safe moshakhs shode

    x_change =0                                       #chon ke to bazi faghad gharare chap va rast bere bala va paiin nmire pas y taghir nemikone

    stuff_start_x = random.randrange(0,display_width) #ashya az bala az noghte 0 ta entehaye arz bian
    stuff_start_y = -600                              #- dadim ke az balaye bala biad
    stuff_speed =8
    stuff_width = 100   
    stuff_height=80

    pygame.display.set_caption('Ball Game (easy)')           #caption

    clock=pygame.time.Clock()                         #frame per second sorat moshakhas mione

    dodged = 0

    game_Exit = False                                 #tasadof ba ashia

    while not game_Exit:                              #ta zamani ke tasadof nakardi bia in kara ro bokon
        for event in pygame.event.get():              #ketabkhone event to pygame hast ma in ja migim evenr ro begir
            if event.type == pygame.QUIT:             #Quit baraye birin omadane
                game_Exit= True                       #age True shod tabe pygame.quit() farakhani beshe va biad biron
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:            #chek kone bebine key zade shode ya na
                if event.key==pygame.K_LEFT:          #klid chap
                    x_change=-5                       #5 ta pixel harkat kone
                elif event.key==pygame.K_RIGHT:
                    x_change=5
            
            if event.type==pygame.KEYUP:              #baraye in ke kontrol beshe va ta abad nare rast va chap
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
        x= x+x_change           
            
        gameDisplay.fill(white)                      #safe sefid besh
        gameDisplay.blit(bachgroundImg2,(0,0))

        #stuff_x,stuff_y,stuff_w,stuff_h,color
        stuff(stuff_start_x,stuff_start_y,stuff_width,stuff_height,red)  #hala bayad moteghayer ha ro be tabe bedim
        stuff_start_y += stuff_speed

        stuff_dodged(dodged)

        ball(x,y)                                     #farakhani tabe ball bara namayesh ball
        
        if x > display_width - ball_width or x < 0:
            crash()

        if stuff_start_y > display_height:           #baraye in ke ye moraba ha raft biron bazam byad
            stuff_start_y = 0 - stuff_height
            stuff_start_x = random.randrange(0,display_width-stuff_width) 
            dodged = dodged + 1

            if dodged % 5 == 0 :                    #5 ta ke rad kard speed ziad beshe
                stuff_speed += 2

        if y < stuff_start_y + stuff_height:         #age sar rect az sar ball gozasht

            if x > stuff_start_x and x < stuff_start_x +stuff_width or x + ball_width > stuff_start_x and x + ball_width < stuff_start_x + stuff_width:
                 crash()

        pygame.display.update()                       #ta zamani ke nazanim riydad haye posht safe ro nemibinim
        clock.tick(60)                                #yani 30 frame bar sanie update kon (30 bar dar sanie)

def game_loop2():    
    pygame.mixer.music.play(-1)                                  #peyda kardan vasat safe
    x = (display_width * 0.45)                        #0.45 az ghabl baraye vasat safe moshakhs shode
    y = (display_height * 0.8)                        #0.8 az ghabl baraye vasat safe moshakhs shode
 
    rang =random.choice(colors)
    x2 = random.randrange(0,display_width)                        #0.45 az ghabl baraye vasat safe moshakhs shode
    y2 = -400

    y2_change = 4
    x_change =0                                       #chon ke to bazi faghad gharare chap va rast bere bala va paiin nmire pas y taghir nemikone
    
    stuff_start_x = random.randrange(0,display_width) #ashya az bala az noghte 0 ta entehaye arz bian
    stuff_start_y = -600                              #- dadim ke az balaye bala biad
    stuff_speed = 9
    stuff_width = random.randrange(90,140)   
    stuff_height= random.randrange(50,90)

    pygame.display.set_caption('Ball Game (hard)')           #caption

    clock=pygame.time.Clock()                         #frame per second sorat moshakhas mione

    dodged = 0
    count_heart = 0
    game_Exit = False                                 #tasadof ba ashia

    while not game_Exit:                              #ta zamani ke tasadof nakardi bia in kara ro bokon
        for event in pygame.event.get():              #ketabkhone event to pygame hast ma in ja migim evenr ro begir
            if event.type == pygame.QUIT:             #Quit baraye birin omadane
                game_Exit= True                       #age True shod tabe pygame.quit() farakhani beshe va biad biron
                pygame.quit()
                quit()

            if event.type==pygame.KEYDOWN:            #chek kone bebine key zade shode ya na
                if event.key==pygame.K_LEFT:          #klid chap
                    x_change = -5                       #5 ta pixel harkat kone
                elif event.key==pygame.K_RIGHT:
                    x_change = 5
            
            if event.type==pygame.KEYUP:              #baraye in ke kontrol beshe va ta abad nare rast va chap
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0

        x= x+x_change        
        y2= y2 + y2_change 
  
        gameDisplay.fill(white)                      #safe sefid besh
        gameDisplay.blit(bachgroundImg3,(0,0))
        
        
        #stuff_x,stuff_y,stuff_w,stuff_h,color
        
        stuff(stuff_start_x,stuff_start_y,stuff_width,stuff_height,rang)  #hala bayad moteghayer ha ro be tabe bedim
        stuff_start_y += stuff_speed

        stuff_dodged(dodged)
        stuff_heart(count_heart)
        ball(x,y)                                     #farakhani tabe ball bara namayesh ball
        ghalb(x2,y2) 
        #omadan on ghermeza       

        if x > display_width - ball_width or x < 0:
            crash2()

        if stuff_start_y > display_height:           #baraye in ke ye moraba ha raft biron bazam byad
            stuff_start_y = 0 - stuff_height
            stuff_start_x = random.randrange(0,display_width-stuff_width) 
            stuff_width = random.randrange(90,140)   
            stuff_height= random.randrange(50,90)
            rang =random.choice(colors)
            dodged = dodged + 1

            if dodged % 5 == 0 :                     #5 ta ke rad kard speed ziad beshe
                stuff_speed += 2  

        if y2 > display_height:           #baraye in ke ye moraba ha raft biron bazam byad
            if dodged % 3 == 0 :  
                y2 = 0 - heart_height
                x2 = random.randrange(0,display_width-heart_width)            


        if y < stuff_start_y + stuff_height:         #age sar rect az sar ball gozasht
            if x > stuff_start_x and x < stuff_start_x +stuff_width or x + ball_width > stuff_start_x and x + ball_width < stuff_start_x + stuff_width:
                crash2()


        if y < y2 + heart_height:
            if x > x2 and x < x2 + heart_width or x +heart_width > x2 and x + heart_width < x2 +heart_width:
                count_heart+=1
                


        pygame.display.update()                       #ta zamani ke nazanim riydad haye posht safe ro nemibinim
        clock.tick(60)                                #yani 30 frame bar sanie update kon (30 bar dar sanie)



gameIntro()
game_loop()

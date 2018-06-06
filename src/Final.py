# Team Petey's Picnic People
# Jaegeun Lee, Jocelyn Bohr, Danny Pasternak, Jeffrey Morris
# 7th November 2012
# All images obtained from 'www.clker.com/clipart'
# Sound obtained from 'www.PlayOnLoop.com'

import pygame, sys, warnings, random
from pygame.locals import *

warnings.filterwarnings("ignore", category=DeprecationWarning)
################################## Set up #############################################################################

white = [255,255,255]
black = [0,0,0]
pygame.init()
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Petey's Picnic Party")
state = 0
mini_startTime = 0
global startTime

# press variable used to check if an object is already being clicked on
press = [False, False, False, False, False]

# variable used to control when objects in level 4 are displayed
# they will not be displayed if the object has been moved under the tent
level4_blit = [False, False, False, False, False]
level4_blit3 = [False, False, False]
level5_blit = [False, False, False, False, False]
level1_sounds = False

level1_checks = [False, False, False, False, False]
level2_checks = [False, False, False, False]
level3_checks = [False, False, False, False]
level4_checks = [False, False, False, False]
level4_checks3 = [False, False, False]
level5_checks = [False, False, False, False]

# initial positions of all objects
pos1 = [595,5]
pos2 = [575,105]
pos3 = [593,205]
pos4 = [605,305]
pos5 = [597,413]
pos6 = [565,3]
pos7 = [600,175]
pos8 = [573,280]
pos9 = [573,380]
pos10 = [635,380]
pos11 = [585,50]
pos12 = [587,190]
pos13 = [583,340]

# different fonts and texts used throughout all the levels
font1 = pygame.font.SysFont('Courier New', 20, True,True) 
font2 = pygame.font.SysFont('Courier New', 10, True, True)
font3 = pygame.font.SysFont('Courier New', 14, True, True)
font4 = pygame.font.SysFont('Courier New', 18, True, True)
font5 = pygame.font.SysFont('Helvetica', 44, True, False)
level1Text = font1.render('Drag the objects into the basket!', True, (0,0,0))
level2Text = font1.render('First drag the blanket to the park!', True, (0,0,0))
level4Text = font1.render('It is raining! Move the picnic!', True, (0,0,0))
level4Text3 = font1.render('It keeps raining! What do we need?', True, (0,0,0))
level5Text = font1.render('Pack the car, it is time to go home!', True, (0,0,0))
level2Blanket = font2.render('BLANKET',True, (0,0,0))
level2Basket = font2.render('BASKET', True, (0,0,0))
level2Table = font2.render('TABLE', True, (0,0,0))
level2Chairs = font2.render('CHAIRS', True, (0,0,0))
level4Umbrella = font2.render('UMBRELLA', True, (0,0,0))
level4Jacket = font2.render('JACKET', True, (0,0,0))
level4Boots = font2.render('BOOTS', True, (0,0,0))


# each level has 2-3 parts, with different event occurring in different parts
level2_part = 1
level3_part = 1
level4_part = 1
level5_part = 1
################################## Minigame Setup ####################################################################
# This is the setup for the minigame
score_txt1 = font5.render('Score:', True, (0,0,0))
x = 300
x_locations = [60,176,292,408,524,640]
movey = 7
movex = 9
y = -80
blit = [True, False, False, False, False]
score = 0

################################## Minigame Methods ##################################################################
# This returns a random number for the x position of the fruit
def get_randpos():
    
    global x_fruit
    x_fruit = random.randrange(0,5)

# Class for the basket    
class main(pygame.sprite.Sprite):
    
    def __init__(self, filename, size, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image = pygame.transform.scale(self.image, size)
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        
        global rectangle
        rectangle = (self.rect.x,(self.rect.y+45),109,45)

# Increases the score and resets the y position once it reaches the bottom
def reset_y_score():
    global score
    global y
    y = -80
    pygame.display.flip()
    score += 10

# When the fruit reaches the bottom, the state is changed              
def lose():
    if y > 505:
        global state
        state = 12

# Class for fruit        
class fruit(pygame.sprite.Sprite):
    
    def __init__(self, filename, size, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image = pygame.transform.scale(self.image, size)
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        
    # Method to detect collision
    def getCollisionApple(self, block2):
        if pygame.sprite.collide_rect(self, block2):
            global blit
            reset_y_score()
            get_randpos()
            blit = [False, True, False, False, False]
            
    def getCollisionJuice(self, block2):
        if pygame.sprite.collide_rect(self, block2):
            global blit
            reset_y_score()
            get_randpos()
            blit = [False, False, True, False, False]
            
    def getCollisionBanana(self, block2):
        if pygame.sprite.collide_rect(self, block2):
            global blit
            reset_y_score()
            get_randpos()
            blit = [False, False, False, True, False]
            
    def getCollisionCupcake(self, block2):
        if pygame.sprite.collide_rect(self, block2):
            global blit
            reset_y_score()
            get_randpos()
            blit = [False, False, False, False, True]
            
    def getCollisionSandwich(self, block2):
        if pygame.sprite.collide_rect(self, block2):
            global blit
            reset_y_score()
            blit = [True, False, False, False, False]
            
get_randpos()

################################## Background - Method ################################################################
# A class to set the background and will be used throughout the game
class background(pygame.sprite.Sprite):
    
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image = pygame.transform.scale(self.image, (700,500))
        self.image.set_colorkey()
        self.rect = self.image.get_rect()
        
################################### Home Button - Method ##############################################################
# A class for the home button that would be located throughout the game to switch screen to the main menu
class homeButton(pygame.sprite.Sprite):
    
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../resources/HomeButton.png").convert()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]

homeButtonCredit = homeButton((0,0))        
homeButtonIntro = homeButton((540,450))
homeButtonLevel1 = homeButton((0,0))

################################### Main Menu - Methods ###############################################################
#A class that creates the buttons on the main menu
class mainMenuButtons(pygame.sprite.Sprite):
    
    def __init__(self, filename, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image = pygame.transform.scale(self.image, (150,50))
        self.image.set_colorkey([255,255,255])
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]

startButton = mainMenuButtons("../resources/StartButton.png",(80,140))
instructionButton = mainMenuButtons("../resources/AboutButton.png",(80,200))
optionButton = mainMenuButtons("../resources/OptionsButton.png",(80,260))
creditButton = mainMenuButtons("../resources/CreditsButton.png",(80,320))
exitButton = mainMenuButtons("../resources/ExitButton.png",(80,380))
mainMenuBackground = background("../resources/menu_bg.png")
level4 = background("../resources/level4.png")

#################################### Options - Methods#########################################################
options_background = background("../resources/options_bg.png") 

# Class for regarding different sizes
class OptionsImages2(pygame.sprite.Sprite): 
    
    def __init__(self, filename, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image = pygame.transform.scale(self.image, (200,50))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
class OptionsImages3(pygame.sprite.Sprite): 
    
    def __init__(self, filename, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
class OptionsImages4(pygame.sprite.Sprite):
    
    def __init__(self, filename, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image = pygame.transform.scale(self.image, (15,15))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]

#optionsName = OptionsImages1("../resources/yourName.jpg",(200,120))
optionsStart = OptionsImages2("../resources/start.jpg",(35,220))
optionsLevel1 = OptionsImages3("../resources/lvl1.jpg",(280, 220))
optionsLevel2 = OptionsImages3("../resources/lvl2.jpg",(355, 220))
optionsLevel3 = OptionsImages3("../resources/lvl3.jpg",(430, 220))
optionsLevel4 = OptionsImages3("../resources/lvl4.jpg",(505, 220))
optionsLevel5 = OptionsImages3("../resources/lvl5.jpg",(580, 220))
optionsVolume = OptionsImages2("../resources/volume.jpg",(35, 320))
optionsSoundOn = OptionsImages3("../resources/speaker_on.png",(280, 320))
optionsSoundOff = OptionsImages3("../resources/speaker_off.png",(280, 320))
optionsStartButton = mainMenuButtons("../resources/StartButton.png",(525,435)) 
optionsDot1 = OptionsImages4("../resources/dot.png",(285,238))
optionsDot2 = OptionsImages4("../resources/dot.png",(360,238)) 
optionsDot3 = OptionsImages4("../resources/dot.png",(435,238))
optionsDot4 = OptionsImages4("../resources/dot.png",(510,238))  
optionsDot5 = OptionsImages4("../resources/dot.png",(585,238)) 

################################### Introduction - Methods ############################################################
# A button that will replay the introduction
class replayButton(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../resources/ReplayButton.png").convert()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = 480
        self.rect.y = 450

# A button that allows the game to move from the introduction to the main game
class introButton(pygame.sprite.Sprite):
    
    def __init__(self,filename,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image = pygame.transform.scale(self.image, (100,50))
        self.image.set_colorkey()
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]

# A class that creates the text box for the introduction screen.    
class textbox(pygame.sprite.Sprite):
    
    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey()
        self.rect = self.image.get_rect()
        self.rect.x = 180
        self.rect.y = 30
            
    # A method to make the images appear with a certain time delay               
    def flash(self):
        screen.blit(self.image, self)
        pygame.display.update()
        pygame.time.delay(3500)
        check_exit()
      
text1 = textbox("../resources/textbox1.png")
text2 = textbox("../resources/textbox2.png")
text3 = textbox("../resources/textbox3.png")
text4 = textbox("../resources/textbox4.png")
text5 = textbox("../resources/textbox5.png")
text6 = textbox("../resources/textbox6.png")

intro_background = background("../resources/intro_background.png")
next_button = introButton("../resources/intro_button.png", (600,450))
replayButton = replayButton()

###################################### Level 1 - Methods ##############################################################
# A class for the objects that appear in all levels
class objects(pygame.sprite.Sprite):
    
    def __init__(self, filename, size, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert()
        self.image = pygame.transform.scale(self.image, size)
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
    
    # Determines when the apple is clicked and will follow the mouse while it is clicked
    def Apple_click(self):
        mousepos = pygame.mouse.get_pos()
        [button1, button2, button3] = pygame.mouse.get_pressed()
        global press
        # if the button is not pressed, all the press variables are false and any image can be clicked
        if button1 == False:
            press = [False, False, False, False, False]
        
        # checking if first press is false
        if press[0] == False:    
            
            if button1 == True and mousepos[0] > (self.rect.x-70) and mousepos[0] < (120+self.rect.x) and mousepos[1] > (self.rect.y-70) and mousepos[1] < (self.rect.y+100):
                pos1[0] = mousepos[0] - 32
                pos1[1] = mousepos[1] - 32
                # sets all other press variables to true, so the other images cannot be pressed if this image is being pressed
                press = [False, True, True, True, True]
    
    # Determines when the sandwich is pressed, and will follow the mouse while it is clicked.            
    def Sandwich_click(self):
        mousepos = pygame.mouse.get_pos()
        [button1, button2, button3] = pygame.mouse.get_pressed()
        global press
        if button1 == False:
            press = [False, False, False, False, False]
        
        if press[1] == False:
            
            if button1 == True and mousepos[0] > (self.rect.x-70) and mousepos[0] < (150+self.rect.x) and mousepos[1] > (self.rect.y-70) and mousepos[1] < (self.rect.y+120):
                pos2[0] = mousepos[0] - 51
                pos2[1] = mousepos[1] - 34
                press = [True, False, True, True, True]
            
    # Determines when the banana is pressed, and will follow the mouse while it is clicked. 
    def Banana_click(self):
        mousepos = pygame.mouse.get_pos()
        [button1, button2, button3] = pygame.mouse.get_pressed()
        global press
        if button1 == False:
            press = [False, False, False, False, False]
        
        if press[2] == False:
            
            if button1 == True and mousepos[0] > (self.rect.x-70) and mousepos[0] < (140+self.rect.x) and mousepos[1] > (self.rect.y-70) and mousepos[1] < (self.rect.y+130):
                pos3[0] = mousepos[0] - 40
                pos3[1] = mousepos[1] - 45
                press = [True, True, False, True, True]
    
    # Determines when the juice is pressed, and will follow the mouse while it is clicked.          
    def Juice_click(self):
        mousepos = pygame.mouse.get_pos()
        [button1, button2, button3] = pygame.mouse.get_pressed()
        global press
        if button1 == False:
            press = [False, False, False, False, False]

        
        if press[3] == False:
            
            if button1 == True and mousepos[0] > (self.rect.x-70) and mousepos[0] < (130+self.rect.x) and mousepos[1] > (self.rect.y-70) and mousepos[1] < (self.rect.y+110):
                    pos4[0] = mousepos[0] - 27.5
                    pos4[1] = mousepos[1] - 40
                    press = [True, True, True, False, True]
    
    # Determines when the cake is pressed, and will follow the mouse while it is clicked.            
    def Cake_click(self):

        mousepos = pygame.mouse.get_pos()
        [button1, button2, button3] = pygame.mouse.get_pressed()
        global press
        if button1 == False:
            press = [False, False, False, False, False]
        
        if press[4] == False:
            if button1 == True and mousepos[0] > (self.rect.x-70) and mousepos[0] < (130+self.rect.x) and mousepos[1] > (self.rect.y-70) and mousepos[1] < (self.rect.y+120):
                pos5[0] = mousepos[0] - 32
                pos5[1] = mousepos[1] - 32
                press = [True, True, True, True, False]
                
    # Determines when the blanket is pressed, and will follow the mouse while it is clicked.             
    def Blanket_click(self):
        mousepos = pygame.mouse.get_pos()
        [button1, button2, button3] = pygame.mouse.get_pressed()
        global press
        # if the button is not pressed, all the press variables are false and any image can be clicked
        if button1 == False:
            press = [False, False, False, False, False]
        
        # checking if first press is false
        if press[0] == False:    
                
            if button1 == True and mousepos[0] > (self.rect.x-40) and mousepos[0] < (160+self.rect.x) and mousepos[1] > (self.rect.y-25) and mousepos[1] < (self.rect.y+160):
                pos6[0] = mousepos[0] - 68
                pos6[1] = mousepos[1] - 73
                # sets all other press variables to true, so the other images cannot be pressed if this image is being pressed
                press = [False, True, True, True, True]
               
    # Determines when the basket is pressed, and will follow the mouse while it is clicked. 
    def Basket_click(self):
        mousepos = pygame.mouse.get_pos()
        [button1, button2, button3] = pygame.mouse.get_pressed()
        global press
        if button1 == False:
            press = [False, False, False, False, False]
        
        
        if press[1] == False:

            if button1 == True and mousepos[0] > (self.rect.x-70) and mousepos[0] < (130+self.rect.x) and mousepos[1] > (self.rect.y-50) and mousepos[1] < (self.rect.y+110):
                pos7[0] = mousepos[0] - 34
                pos7[1] = mousepos[1] - 37
                press = [True, False, True, True, True]     
              
    # Determines when the table is pressed, and will follow the mouse while it is clicked. 
    def Table_click(self):
        mousepos = pygame.mouse.get_pos()
        [button1, button2, button3] = pygame.mouse.get_pressed()
        global press
        if button1 == False:
            press = [False, False, False, False, False]
        
        if press[2] == False:
            
            if button1 == True and mousepos[0] > (self.rect.x-30) and mousepos[0] < (145+self.rect.x) and mousepos[1] > (self.rect.y-50) and mousepos[1] < (self.rect.y+100):
                pos8[0] = mousepos[0] - 61
                pos8[1] = mousepos[1] - 34
                press = [True, True, False, True, True]
       
    # Determines when the blue chair is pressed, and will follow the mouse while it is clicked.          
    def b_chair_click(self):
        mousepos = pygame.mouse.get_pos()
        [button1, button2, button3] = pygame.mouse.get_pressed()
        global press
        if button1 == False:
            press = [False, False, False, False, False]
        
        if press[3] == False:
            
            if button1 == True and mousepos[0] > (self.rect.x-50) and mousepos[0] < (90+self.rect.x) and mousepos[1] > (self.rect.y-45) and mousepos[1] < (self.rect.y+120):
                pos9[0] = mousepos[0] - 26
                pos9[1] = mousepos[1] - 40
                press = [True, True, True, False, True]

    # Determines when the yellow chair is pressed, and will follow the mouse while it is clicked. 
    def y_chair_click(self):
        mousepos = pygame.mouse.get_pos()
        [button1, button2, button3] = pygame.mouse.get_pressed()
        global press
        if button1 == False:
            press = [False, False, False, False, False]
        
        if press[4] == False:
            if button1 == True and mousepos[0] > (self.rect.x-50) and mousepos[0] < (100+self.rect.x) and mousepos[1] > (self.rect.y-45) and mousepos[1] < (self.rect.y+120):
                pos10[0] = mousepos[0] - 26
                pos10[1] = mousepos[1] - 40
                press = [True, True, True, True, False]

    # Determines when the umbrella is pressed, and will follow the mouse while it is clicked. 
    def Umbrella_click(self):

        mousepos = pygame.mouse.get_pos()
        [button1, button2, button3] = pygame.mouse.get_pressed()
        global press
        if button1 == False:
            press = [False, False, False, False, False]
        
        
        
        if press[0] == False:

            if button1 == True and mousepos[0] > (self.rect.x-60) and mousepos[0] < (140+self.rect.x) and mousepos[1] > (self.rect.y-50) and mousepos[1] < (self.rect.y+130):
                pos11[0] = mousepos[0] - 50
                pos11[1] = mousepos[1] - 47
                press = [False, True, True, True, True]
                
    # Determines when the jacket is pressed, and will follow the mouse while it is clicked. 
    def Jacket_click(self):

        mousepos = pygame.mouse.get_pos()
        [button1, button2, button3] = pygame.mouse.get_pressed()
        global press
        if button1 == False:
            press = [False, False, False, False, False]
    
        
        if press[1] == False:

            if button1 == True and mousepos[0] > (self.rect.x-60) and mousepos[0] < (120+self.rect.x) and mousepos[1] > (self.rect.y-50) and mousepos[1] < (self.rect.y+130):
                pos12[0] = mousepos[0] - 45
                pos12[1] = mousepos[1] - 50
                press = [True, False, True, True, True]
                
    # Determines when the boots is pressed, and will follow the mouse while it is clicked. 
    def Boots_click(self):

        mousepos = pygame.mouse.get_pos()
        [button1, button2, button3] = pygame.mouse.get_pressed()
        global press
        if button1 == False:
            press = [False, False, False, False, False]
        
        if press[2] == False:

            if button1 == True and mousepos[0] > (self.rect.x-60) and mousepos[0] < (130+self.rect.x) and mousepos[1] > (self.rect.y-50) and mousepos[1] < (self.rect.y+120):
                pos13[0] = mousepos[0] - 50
                pos13[1] = mousepos[1] - 47
                press = [True, True, False, True, True]
                
# A class to create checkmarks
class checkMark(pygame.sprite.Sprite):
    
    def __init__(self,location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../resources/check.png").convert()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.image.set_colorkey(white)
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        
class wrongMark(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("../resources/wrong.png").convert()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = location[0]
        self.rect.y = location[1]
        
# checkmarks located in various positions       
check1 = checkMark((605,20))
check2 = checkMark((605,125))
check3 = checkMark((605,230))
check4 = checkMark((605,335))
check5 = checkMark((605,430))
check6 = checkMark((605,80))
check7 = checkMark((605,190))
check8 = checkMark((605,285))
check9 = checkMark((575,400))
check10 = checkMark((640,400))
check11 = checkMark((605,90))
check12 = checkMark((605,230))
check13 = checkMark((605,375))

wrong1 = wrongMark((605,20))  
wrong2 = wrongMark((605,125))
wrong3 = wrongMark((605,230))
wrong4 = wrongMark((605,335))
wrong5 = wrongMark((605,430))
wrong6 = wrongMark((605,80))
wrong7 = wrongMark((605,190))
wrong8 = wrongMark((605,285))
wrong9 = wrongMark((575,400))
wrong10 = wrongMark((640,400))
wrong11 = wrongMark((605,90))
wrong12 = wrongMark((605,230))
wrong13 = wrongMark((605,375))
################################## Minigame Methods ##################################################################
################################## Location Check Method ##############################################################
# A method that would check if the images are in the basket in level 1
def locationCheck1():
    
    [button15,button16,button17] = pygame.mouse.get_pressed()
    # If the button is released, and the objects is in the basket, a check is displayed and only

    global level1_checks

    if button15 == False and pos1[0] > 185 and pos1[0] < 342 and pos1[1]> 125 and pos1[1]<240:
        level1_checks[0] = True
        
    if button15 == False and pos2[0] > 185 and pos2[0] < 320 and pos2[1]> 125 and pos2[1]<225:
        level1_checks[1] = True

    if button15 == False and pos3[0] > 180 and pos3[0] < 335 and pos3[1]> 120 and pos3[1]<240:
        level1_checks[2] = True

    if button15 == False and pos4[0] > 185 and pos4[0] < 350 and pos4[1]> 120 and pos4[1]<230:
        level1_checks[3] = True

    if button15 == False and pos5[0] > 185 and pos5[0] < 342 and pos5[1]> 125 and pos5[1]<240:
        level1_checks[4] = True

    if level1_checks == [True, True, True, True, True]:
        screen.blit(next_text.image, next_text)
        screen.blit(next_button1.image,next_button1)
        [button150,button250,button350] = pygame.mouse.get_pressed()
        mousepos50 = pygame.mouse.get_pos()
        # Checks for click on next button
        if button150 == True and mousepos50[0]<550 and mousepos50[0]>450 and mousepos50[1]<500 and mousepos50[1]>450:
            global state
            state = 6
############################## Second location check method ######################################
# checks for when the picnic supplies are on the blanket
def blanket_locationCheck():
    
    [button16, button26, button36] = pygame.mouse.get_pressed()
    global state
    global pos6
    global pos7
    global pos8
    global pos9
    global pos10
    global pos11
    global pos12
    global pos13
    
    global level2_checks
    global level3_checks
    global level4_blit

    # Checks if button is released and basket is on the blanket
    if button16 == False and pos7[0] > (pos6[0]-25) and pos7[0] < (pos6[0]+95) and pos7[1] > (pos6[1]-50) and pos7[1] < (pos6[1]+106):
        
        if state == 6:
            level2_checks[0] = True
        if state == 7:
            level3_checks[0] = True
        if state == 8:
            level4_checks[0] = True
            level4_blit[0] = True
    
    # Checks if button is released and table is on the blanket
    if button16 == False and pos8[0] > (pos6[0]-25) and pos8[0] < (pos6[0]+30) and pos8[1] > (pos6[1]-25) and pos8[1] < (pos6[1]+106):
        
        if state == 6:
            level2_checks[1] = True
        if state == 7:
            level3_checks[1] = True
        if state == 8:
            level4_checks[1] = True
            level4_blit[1] = True
    
    # Checks if button is released and blue chair is on the blanket
    if button16 == False and pos9[0] > (pos6[0]-25) and pos9[0] < (pos6[0]+110) and pos9[1] > (pos6[1]-60) and pos9[1] < (pos6[1]+90):

        if state == 6:
            level2_checks[2] = True
        if state == 7:
            level3_checks[2] = True
        if state == 8:
            level4_checks[2] = True
            level4_blit[2] = True
    
    # Checks if button is released and yellow chair is on the blanket
    if button16 == False and  pos10[0] > (pos6[0]-25) and pos10[0] < (pos6[0]+110) and pos10[1] > (pos6[1]-60) and pos10[1] < (pos6[1]+90):
        
        if state == 6:
            level2_checks[3] = True
        if state == 7:
            level3_checks[3] = True
        if state == 8:
            level4_checks[3] = True
            level4_blit[3] = True
            
    # If level 2, all positions of picnic supplies are reset to original positions and next button is displayed
    if state == 6:
        if level2_checks == [True, True, True, True]:
            screen.blit(next_text.image, next_text)
            screen.blit(next_button1.image,next_button1)
            [button160,button260,button360] = pygame.mouse.get_pressed()
            mousepos60 = pygame.mouse.get_pos()
            
            # Checks for click on next button
            if button160 == True and mousepos60[0]<550 and mousepos60[0]>450 and mousepos60[1]<500 and mousepos60[1]>450:
                # Resets positions and goes to level 3
         
                pos6 = [565,3]
                pos7 = [600,175]
                pos8 = [573,280]
                pos9 = [573,380]
                pos10 = [635,380]
                state = 7

# image for next button                
next_button1 = introButton("../resources/intro_button.png", (450,450))

# Method that will detect when the objects collide with the car
def car_locationCheck():
    [button19, button29, button39] = pygame.mouse.get_pressed()
    global state
    global pos7
    global pos8
    global pos9
    global pos10
    
    global level5_checks
    global level5_blit
    
    if button19 == False and pos7[0] > 370 and pos7[0] < 535 and pos7[1] > 290 and pos7[1] < 355:
        level5_checks[0] = True
        level5_blit[0] = True
    
    if button19 == False and pos8[0] > 350 and pos8[0] < 480 and pos8[1] > 315 and pos8[1] < 390:
        level5_checks[1] = True
        level5_blit[1] = True
    
    if button19 == False and pos9[0] > 370 and pos9[0] < 525 and pos9[1] > 285 and pos9[1] < 375:
        level5_checks[2] = True
        level5_blit[2] = True
    
    if button19 == False and  pos10[0] > 370 and pos10[0] < 525 and pos10[1] > 285 and pos10[1] < 375:
        level5_checks[3] = True
        level5_blit[3] = True
      
################################## Exit Function - Applicable #########################################################
# A method to exit the program when required
def check_exit():
    
    for event in pygame.event.get():
    
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

################################# Background Music ####################################################################
################################# Background Music ####################################################################
bg_music = pygame.mixer.music
bg_music.load("../resources/backgroundmusic.wav")
music = True
def PlayMusic():
    if music == True:
        bg_music.play(-1, 0.0) 
    elif music == False:
        bg_music.stop()
Level1SoundOn = OptionsImages3("../resources/speaker_on.png",(50, 0))
Level1SoundOff = OptionsImages3("../resources/speaker_off.png",(50, 0)) 
OtherLevelsSoundOn = OptionsImages3("../resources/speaker_on.png",(500, 0))
OtherLevelsSoundOff = OptionsImages3("../resources/speaker_off.png",(500, 0))
IntroSoundOn = OptionsImages3("../resources/speaker_on.png",(0,0))
IntroSoundOff = OptionsImages3("../resources/speaker_off.png",(0,0))
ready = True 
clock = pygame.time.Clock()
################################## Game Play ##########################################################################
levelSwitch = 0
PlayMusic()

while True:
################################## Main Menu - Game ###################################################################
    clock.tick(60)
    if state == 0:
        check_exit()
        screen.blit(mainMenuBackground.image, mainMenuBackground)
        pygame.display.update()
        
        # Resets all positions, parts, and first variables at main menu
        level4_blit = [False, False, False, False, False]
        level4_blit3 = [False, False, False]
        level5_blit = [False, False, False, False, False]
        
        level1_checks = [False, False, False, False, False]
        level2_checks = [False, False, False, False]
        level3_checks = [False, False, False, False]
        level4_checks = [False, False, False, False]
        level4_checks3 = [False, False, False]
        level5_checks = [False, False, False, False]
        
        level2_part = 1
        level3_part = 1
        level4_part = 1
        level5_part = 1
        
        pos1 = [595,5]
        pos2 = [575,105]
        pos3 = [593,205]
        pos4 = [605,305]
        pos5 = [595,420]
        pos5 = [597,413]
        pos6 = [565,3]
        pos7 = [600,175]
        pos8 = [573,280]
        pos9 = [573,380]
        pos10 = [635,380]
        pos11 = [585,50]
        pos12 = [587,190]
        pos13 = [583,340]
        
        mousepos0 = pygame.mouse.get_pos()
        [button10,button20,button30] = pygame.mouse.get_pressed()
       
        # This is for the start button
        if button10 == True and mousepos0[0] < 284 and mousepos0[0] > 136 and mousepos0[1] < 214 and mousepos0[1] > 167: 
            intro_startTime = pygame.time.get_ticks()
            state = 4   
        # This is for the About
        if button10 == True and mousepos0[0] < 284 and mousepos0[0] > 136 and mousepos0[1] < 274 and mousepos0[1] > 227:
            state = 2
        # This is for the Options
        if button10 == True and mousepos0[0] < 284 and mousepos0[0] > 136 and mousepos0[1] < 331 and mousepos0[1] > 285:
            state = 1
        # This is for the Credits
        if button10 == True and mousepos0[0] < 284 and mousepos0[0] > 136 and mousepos0[1] < 393 and mousepos0[1] > 345:
            state = 3
        # This is for the Exit
        if button10 == True and mousepos0[0] < 284 and mousepos0[0] > 136 and mousepos0[1] < 455 and mousepos0[1] > 406:
            pygame.quit()
            sys.exit()
            
############################################### Options - Game ######################################################
    if state == 1:
        check_exit()
        screen.blit(options_background.image, options_background)
        screen.blit(homeButtonLevel1.image,homeButtonLevel1)
        screen.blit(optionsStart.image, optionsStart)
        screen.blit(optionsLevel1.image, optionsLevel1)
        screen.blit(optionsLevel2.image, optionsLevel2)
        screen.blit(optionsLevel3.image, optionsLevel3)
        screen.blit(optionsLevel4.image, optionsLevel4)
        screen.blit(optionsLevel5.image, optionsLevel5)
        screen.blit(optionsVolume.image, optionsVolume)
        screen.blit(optionsSoundOn.image, optionsSoundOn)
        screen.blit(optionsStartButton.image, optionsStartButton)
        mousepos1 = pygame.mouse.get_pos()
        [button11,button21,button31] = pygame.mouse.get_pressed()
        if button11 == True and mousepos1[0]>0 and mousepos1[0]<50 and mousepos1[1]>0 and mousepos1[1]<50:
            state = 0
        #These if statements just determine what levels the user chooses and assigns levelswitch a number to add
        #to the current state. For example levelswitch = 4 plus state = 1 will give state = 5 which is Level 1    
        if button11 == True and mousepos1[0] < 330 and mousepos1[0] > 280 and mousepos1[1] < 270 and mousepos1[1] > 220:
            startTime = pygame.time.get_ticks()/1000
            levelSwitch = 4
        if levelSwitch == 4:    
            screen.blit(optionsDot1.image, optionsDot1)
        if button11 == True and mousepos1[0] < 405 and mousepos1[0] > 355 and mousepos1[1] < 270 and mousepos1[1] > 220:
            startTime = pygame.time.get_ticks()/1000
            levelSwitch = 5
        if levelSwitch == 5:
            screen.blit(optionsDot2.image, optionsDot2)
        if button11 == True and mousepos1[0] < 480 and mousepos1[0] > 430 and mousepos1[1] < 270 and mousepos1[1] > 220:
            startTime = pygame.time.get_ticks()/1000
            levelSwitch = 6
        if levelSwitch == 6:
            screen.blit(optionsDot3.image, optionsDot3)
        if button11 == True and mousepos1[0] < 555 and mousepos1[0] > 505 and mousepos1[1] < 270 and mousepos1[1] > 220:
            startTime = pygame.time.get_ticks()/1000
            levelSwitch = 7
        if levelSwitch == 7:
            screen.blit(optionsDot4.image, optionsDot4)
        if button11== True and mousepos1[0] < 630 and mousepos1[0] > 580 and mousepos1[1] < 270 and mousepos1[1] > 220:
            startTime = pygame.time.get_ticks()/1000
            levelSwitch = 8
        if levelSwitch == 8:
            screen.blit(optionsDot5.image, optionsDot5)
        #These if statements control the sound, whether it is on or off
        if button11 == True and mousepos1[0] < 330 and mousepos1[0] > 280 and mousepos1[1] < 370 and mousepos1[1] > 320 and ready == True and music == True:
            music = False
            ready = False
            PlayMusic()
        if music == False:
            screen.blit(optionsSoundOff.image, optionsSoundOff)
        if button11 == False:
            ready = True
        if button11 == True and mousepos1[0] < 330 and mousepos1[0] > 280 and mousepos1[1] < 370 and mousepos1[1] > 320 and ready == True and music == False:
            music = True
            ready = False
            PlayMusic()
        if music == True:
            screen.blit(optionsSoundOn.image, optionsSoundOn)
        if button11 == True and mousepos1[0] < 675 and mousepos1[0] > 525 and mousepos1[1] < 485 and mousepos1[1] > 435:
            state += levelSwitch   
        pygame.display.update()       
       
################################################# About - Game #################################################
    if state == 2:
        about_bg = background("../resources/about_bg.png")
        check_exit()
        screen.blit(about_bg.image, about_bg)
        screen.blit(homeButtonLevel1.image,homeButtonLevel1)
        mousepos2 = pygame.mouse.get_pos()
        [button12,button22,button32] = pygame.mouse.get_pressed()
        if button12 == True and mousepos2[0]>0 and mousepos2[0]<50 and mousepos2[1]>0 and mousepos2[1]<50:
            state = 0
        pygame.display.update()
            
################################## Credits - Game ######################################################################
    if state == 3:
        
        check_exit() 
        credits_bg = background("../resources/credits_bg.png")
        screen.blit(credits_bg.image, credits_bg)
        screen.blit(homeButtonCredit.image, homeButtonCredit)
        pygame.display.update()
        mousepos3 = pygame.mouse.get_pos()
        [button13,button23,button33] = pygame.mouse.get_pressed()
        # This is a home button
        if button13 == True and mousepos3[0] < 50 and mousepos3[0] > 0 and mousepos3[1] < 50 and mousepos3[1] > 0:
            state = 0
            
################################### Introduction - Game ###############################################################
    if state == 4:

        check_exit()
        screen.blit(intro_background.image, intro_background)
        intro_currentTime = pygame.time.get_ticks()
        introTime = intro_currentTime - intro_startTime
        if introTime > 21000:
            state = 40
        elif introTime > 17500:
            screen.blit(text6.image, text6)
        elif introTime > 14000:
            screen.blit(text5.image, text5)
        elif introTime > 10500:
            screen.blit(text4.image, text4)
        elif introTime > 7000:
            screen.blit(text3.image, text3)
        elif introTime > 3500:
            screen.blit(text2.image, text2)
        if introTime > 0 and introTime < 3500:
            screen.blit(text1.image, text1)
        
        
        [button14, button24, button34] = pygame.mouse.get_pressed()
        mousepos40 = pygame.mouse.get_pos()
        
        if button14 == True and mousepos40[0] < 50 and mousepos40[0] > 0 and mousepos40[1] < 50 and mousepos40[1] > 0 and ready == True and music == True:
            music = False
            ready = False
            PlayMusic()
        if music == False:
            screen.blit(IntroSoundOff.image, IntroSoundOff)
        if button14 == False:
            ready = True
        if button14 == True and mousepos40[0] < 50 and mousepos40[0] > 0 and mousepos40[1] < 50 and mousepos40[1] > 0 and ready == True and music == False:
            music = True
            ready = False
            PlayMusic()
        if music == True:
            screen.blit(IntroSoundOn.image, IntroSoundOn)  
        pygame.display.update()
 
    
    # Another state which waits for use input
    if state == 40:
        
        check_exit()
        screen.blit(intro_background.image, intro_background)
        screen.blit(text6.image,text6)
        screen.blit(next_button.image,next_button)
        screen.blit(homeButtonIntro.image,homeButtonIntro)
        
        mousepos40 = pygame.mouse.get_pos()
        [button14, button24, button34] = pygame.mouse.get_pressed()
        
        # This is the next button
        if button14 == True and mousepos40[0]<700 and mousepos40[0]>600 and mousepos40[1]<500 and mousepos40[1]>450:
            startTime = pygame.time.get_ticks()/1000
            state = 5              
        # This is the home button
        if button14 == True and mousepos40[0]<590 and mousepos40[0]>540 and mousepos40[1]<500 and mousepos40[1]>450:
            state = 0
            
        if button14 == True and mousepos40[0] < 50 and mousepos40[0] > 0 and mousepos40[1] < 50 and mousepos40[1] > 0 and ready == True and music == True:
            music = False
            ready = False
            PlayMusic()
        if music == False:
            screen.blit(IntroSoundOff.image, IntroSoundOff)
        if button14 == False:
            ready = True
        if button14 == True and mousepos40[0] < 50 and mousepos40[0] > 0 and mousepos40[1] < 50 and mousepos40[1] > 0 and ready == True and music == False:
            music = True
            ready = False
            PlayMusic()
        if music == True:
            screen.blit(IntroSoundOn.image, IntroSoundOn)
        pygame.display.update()

            
#################################### Level 1 - Game ###################################################################
    if state == 5:

        [button15,button25,button35] = pygame.mouse.get_pressed()
        
        level1 = background("../resources/level1.png")
        apple = objects("../resources/apple.png", (63,63), (pos1))
        sandwich = objects("../resources/sandwich.png", (102,68), (pos2))
        banana = objects("../resources/banana.png", (74,74), (pos3))
        juicebox = objects("../resources/juicebox.png", (55,80.5), (pos4))
        cupcake = objects("../resources/cupcake.png", (63,63), (pos5))
        next_text = objects("../resources/next_text.png", (446,49), (8,452))
        screen.blit(level1.image, level1) 
        screen.blit(level1Text, (10,460))
        check_exit()       
        
        if level1_checks[0] == True:
            screen.blit(check1.image, check1)
        elif level1_checks[0] == False and button15 == False and pos1[0]>-100 and pos1[0]<535:
            screen.blit(wrong1.image, wrong1)
            
        if level1_checks[1] == True:
            screen.blit(check2.image, check2)
        elif level1_checks[1] == False and button15 == False and pos2[0]>-100 and pos2[0] < 535:
            screen.blit(wrong2.image, wrong2)
            
        if level1_checks[2] == True:
            screen.blit(check3.image, check3)
        elif level1_checks[2] == False and button15 == False and pos3[0]>-100 and pos3[0] < 535:
            screen.blit(wrong3.image, wrong3)
            
        if level1_checks[3] == True:
            screen.blit(check4.image, check4)
        elif level1_checks[3] == False and button15 == False and pos4[0]>-100 and pos4[0] < 535:
            screen.blit(wrong4.image, wrong4)
            
        if level1_checks[4] == True:
            screen.blit(check5.image, check5)
        elif level1_checks[4] == False and button15==False and pos5[0]>-100 and pos5[0] < 535:
            screen.blit(wrong5.image, wrong5)
            
        screen.blit(apple.image, apple)
        screen.blit(sandwich.image, sandwich)
        screen.blit(banana.image, banana)
        screen.blit(juicebox.image, juicebox)
        screen.blit(cupcake.image, cupcake)
        screen.blit(homeButtonLevel1.image,homeButtonLevel1)
        screen.blit(Level1SoundOn.image, Level1SoundOn)
        locationCheck1()
        
        if level1_checks[0] == False:
            apple.Apple_click()
        if level1_checks[1] == False:
            sandwich.Sandwich_click()
        if level1_checks[2] == False:
            banana.Banana_click()
        if level1_checks[3] == False:
            juicebox.Juice_click()
        if level1_checks[4] == False:
            cupcake.Cake_click()
        
        
        mousepos5 = pygame.mouse.get_pos()
        
        # This is for the home button
        if press == [False, False, False, False, False]:
            if button15 == True and mousepos5[0]>0 and mousepos5[0]<50 and mousepos5[1]>0 and mousepos5[1]<50:
                state = 0
            if button15 == True and mousepos5[0] < 100 and mousepos5[0] > 50 and mousepos5[1] < 50 and mousepos5[1] > 0 and ready == True and music == True:
                music = False
                ready = False
                PlayMusic()
        if music == False:
            screen.blit(Level1SoundOff.image, Level1SoundOff)
        if press == [False, False, False, False, False]:
            if button15 == False:
                ready = True
            if button15 == True and mousepos5[0] < 100 and mousepos5[0] > 50 and mousepos5[1] < 50 and mousepos5[1] > 0 and ready == True and music == False:
                music = True
                ready = False
                PlayMusic()
        if music == True:
            screen.blit(Level1SoundOn.image, Level1SoundOn)  
        pygame.display.update()   
            
#################################### Level 2 - Game ###############################################################            

    if state == 6:

        [button16, button26, button36] = pygame.mouse.get_pressed()       
        
        level2 = background("../resources/level2.png")
        blanket = objects("../resources/blanket.png", (135,146), (pos6))
        basket2 = objects("../resources/basket.png", (68,74), (pos7))
        table = objects("../resources/table.png", (121,67), (pos8))
        b_chair = objects("../resources/bluechair.png", (51,79), (pos9))
        y_chair = objects("../resources/yellowchair.png", (51,79), (pos10))
        level2Text2 = objects("../resources/text2.png", (333,54), (8,440))
        next_text = objects("../resources/next_text.png", (446,49), (8,452))
        check_exit()
        screen.blit(level2.image, level2)
        
        # Text
        screen.blit(level2Blanket, (613,150))
        screen.blit(level2Basket, (616,255))
        screen.blit(level2Table, (618,352))
        screen.blit(level2Chairs, (615,465))
        
        if level2_checks[0] == True:
            screen.blit(check7.image, check7)
        elif level3_checks[0] == False and button16 == False and pos7[0]>-100 and pos7[0]<498:
            screen.blit(wrong7.image, wrong7)
            
        if level2_checks[1] == True:
            screen.blit(check8.image, check8)
        elif level2_checks[1] == False and button16 == False and pos8[0]>-100 and pos8[0]<447:
            screen.blit(wrong8.image, wrong8)
        
        if level2_checks[2] == True:
            screen.blit(check9.image, check9)
        elif level2_checks[2] == False and button16 == False and pos9[0]>-100 and pos9[0] < 515:
            screen.blit(wrong9.image, wrong9)
        
        if level2_checks[3] == True:
            screen.blit(check10.image, check10)
        elif level2_checks[3] == False and button16 == False and pos10[0]>-100 and pos10[0]<515:
            screen.blit(wrong10.image,wrong10)
        
        
        # Part 1 is moving the blanket to the park
        if level2_part == 1:
            blanket.Blanket_click()
            screen.blit(level2Text, (10,450))
            if button16 == False and pos6[0]<428 and pos6[0]>-5 and pos6[1]<280 and pos6[1]>0:
                level2_part = 2
        # Part 2 is moving the objects to the blanket       
        if level2_part == 2:
            
            screen.blit(check6.image, check6)
            if level2_checks[0] == False:
                basket2.Basket_click()
            if level2_checks[2] == False:
                b_chair.b_chair_click()
            if level2_checks[3] == False:
                y_chair.y_chair_click()
            if level2_checks[1] == False:
                table.Table_click()
            
            screen.blit(level2Text2.image, level2Text2)
            blanket_locationCheck()
            
        screen.blit(homeButtonLevel1.image,homeButtonLevel1)
        screen.blit(blanket.image, blanket)
        screen.blit(table.image, table)
        screen.blit(y_chair.image, y_chair)
        screen.blit(b_chair.image, b_chair)
        screen.blit(basket2.image, basket2)
        mousepos6 = pygame.mouse.get_pos()
        [button16,button26,button36] = pygame.mouse.get_pressed()
        
        # This is for the home button
        if press == [False, False, False, False, False]:
            if button16 == True and mousepos6[0]>0 and mousepos6[0]<50 and mousepos6[1]>0 and mousepos6[1]<50:
                state= 0
            if button16 == True and mousepos6[0] < 550 and mousepos6[0] > 500 and mousepos6[1] < 50 and mousepos6[1] > 0 and ready == True and music == True:
                music = False
                ready = False
                PlayMusic()
        if music == False:
            screen.blit(OtherLevelsSoundOff.image, OtherLevelsSoundOff)
        if press == [False, False, False, False, False]:
            if button16 == False:
                ready = True
            if button16 == True and mousepos6[0] < 550 and mousepos6[0] > 500 and mousepos6[1] < 50 and mousepos6[1] > 0 and ready == True and music == False:
                music = True
                ready = False
                PlayMusic()
        if music == True:
            screen.blit(OtherLevelsSoundOn.image, OtherLevelsSoundOn)
        pygame.display.update()
################################## Level 3 - Game ################################################################
        
    if state == 7:

        [button17, button26, button37] = pygame.mouse.get_pressed()
        check_exit()
        level3 = background("../resources/level3.png")
        blanket = objects("../resources/blanket.png", (135,146), (pos6))
        basket2 = objects("../resources/basket.png", (68,74), (pos7))
        table = objects("../resources/table.png", (121,67), (pos8))
        b_chair = objects("../resources/bluechair.png", (51,79), (pos9))
        y_chair = objects("../resources/yellowchair.png", (51,79), (pos10))
        level3Text2 = objects("../resources/text2.png", (333,54), (8,440))
        
        # Part 1 is moving the blanket to the park
        if level3_part == 1:
            
            screen.blit(level3.image, level3)
            screen.blit(homeButtonLevel1.image,homeButtonLevel1)
            screen.blit(blanket.image, blanket)
            screen.blit(table.image, table)
            screen.blit(y_chair.image, y_chair)
            screen.blit(b_chair.image, b_chair)
            screen.blit(basket2.image, basket2)
            blanket.Blanket_click()
            screen.blit(level2Text, (10,450))
            
                # This is if the blanket is in the middle area of the screen, avoiding river and tree again
            if pos6[0]<278 and pos6[0]>209 and pos6[1]>-2 and pos6[1]<280 and button17 == False:
                level3_part = 2
            elif pos6[0]>-100 and pos6[0]<445 and button17 == False:
                screen.blit(wrong6.image,wrong6)
                
                # This is if the blanket is on the right side of the park, avoiding the tree
            if pos6[0]<428 and pos6[0]>209 and pos6[1]>142 and pos6[1]<280 and button17==False:
                level3_part = 2
            elif pos6[0]>-100 and pos6[0]<445 and button17 == False:
                screen.blit(wrong6.image,wrong6)
                    
        # Part 2 is moving the objects to the blanket
        if level3_part == 2:
            [button17, button26, button37] = pygame.mouse.get_pressed()
            screen.blit(level3.image, level3)
            screen.blit(check6.image, check6)
            screen.blit(homeButtonLevel1.image,homeButtonLevel1)
            
            
            if level3_checks[0] == False:
                basket2.Basket_click()
            if level3_checks[2] == False:
                b_chair.b_chair_click()
            if level3_checks[3] == False:
                y_chair.y_chair_click()
            if level3_checks[1] == False:
                table.Table_click()
            
            screen.blit(level3Text2.image, level3Text2)
            blanket_locationCheck()
            # Checks if all objects are on the blanket
            if level3_checks == [True, True, True, True]:
                screen.blit(next_button1.image,next_button1)
                [button170,button270,button370] = pygame.mouse.get_pressed()
                mousepos70 = pygame.mouse.get_pos()
                # Checks for click on next button
                if button170 == True and mousepos70[0]<550 and mousepos70[0]>450 and mousepos70[1]<500 and mousepos70[1]>450:
                    state = 8
        
            if level3_checks[0] == True:
                screen.blit(check7.image, check7)
            elif level3_checks[0] == False and button17 == False and pos7[0]>-100 and pos7[0]<498:
                screen.blit(wrong7.image, wrong7)
                
            if level3_checks[1] == True:
                screen.blit(check8.image, check8)
            elif level3_checks[1] == False and button17 == False and pos8[0]>-100 and pos8[0]<447:
                screen.blit(wrong8.image,wrong8)
                
            if level3_checks[2] == True:
                screen.blit(check9.image, check9)
            elif level3_checks[2]==False and button17 == False and pos9[0]>-100 and pos9[0]<515:
                screen.blit(wrong9.image,wrong9)
                
            if level3_checks[3] == True:
                screen.blit(check10.image, check10)
            elif level3_checks[3] == False and button17==False and pos10[0]>-100 and pos10[0]<515:
                screen.blit(wrong10.image,wrong10)
            
            screen.blit(blanket.image, blanket)
            screen.blit(table.image, table)
            screen.blit(y_chair.image, y_chair)
            screen.blit(b_chair.image, b_chair)
            screen.blit(basket2.image, basket2)
            
        
        # Updating part of the screen
        mousepos7 = pygame.mouse.get_pos()
        [button17,button27,button37] = pygame.mouse.get_pressed()
        
        # This is checking for a click on the home button
        if press == [False, False, False, False, False]:
            if button17 == True and mousepos7[0]>0 and mousepos7[0]<50 and mousepos7[1]>0 and mousepos7[1]<50:
                state = 0
            if button17 == True and mousepos7[0] < 550 and mousepos7[0] > 500 and mousepos7[1] < 50 and mousepos7[1] > 0 and ready == True and music == True:
                music = False
                ready = False
                PlayMusic()
        if music == False:
            screen.blit(OtherLevelsSoundOff.image, OtherLevelsSoundOff)
        if press == [False, False, False, False, False]:
            if button17 == False:
                ready = True
            if button17 == True and mousepos7[0] < 550 and mousepos7[0] > 500 and mousepos7[1] < 50 and mousepos7[1] > 0 and ready == True and music == False:
                music = True
                ready = False
                PlayMusic()
        if music == True:
            screen.blit(OtherLevelsSoundOn.image, OtherLevelsSoundOn) 
        pygame.display.update()    
########################################### Level 4 - Game ###########################################################
    if state == 8:

        [button18, button28, button38] = pygame.mouse.get_pressed()
        
        check_exit()
        tent = objects("../resources/tent.png", (138,153), (-1,219))
        rain = objects("../resources/rain.png", (88,80), (220,2))
        umbrella = objects("../resources/umbrella.png", (100,94), (pos11))
        jacket = objects("../resources/jacket.png", (91,100), (pos12))
        boots = objects("../resources/boots.png", (99,93), (pos13))
        
        level4text2 = objects("../resources/level4text2.png", (386,50), (8,440))
        
        screen.blit(level4.image, level4)
        screen.blit(homeButtonLevel1.image,homeButtonLevel1)
        # Checking if objects have been placed under tent. If they have not been placed under tent,
        # object will be displayed. If they have been placed under tent, they will not be displayed
                
        # Part 1 moves the blanket from the position on the park from level 2 to under the tent
        if level4_part == 1:
            screen.blit(level2Blanket, (613,150))
            screen.blit(level2Basket, (616,255))
            screen.blit(level2Table, (618,352))
            screen.blit(level2Chairs, (615,465))
            if level4_blit[4] == False:
                blanket = objects("../resources/blanket.png", (135,146), (pos6))
                screen.blit(blanket.image, blanket)
            blanket.Blanket_click()
            screen.blit(level4Text, (10,450))

            if pos6[0]>-15 and pos6[0]<7 and pos6[1]<245 and pos6[1]>200 and button18 == False:
                level4_blit[4] = True
                screen.blit(tent.image, tent)
                pygame.display.update()
                level4_part = 2
            elif pos6[0]>-100 and pos6[0]<450 and button18 == False:
                    screen.blit(wrong6.image,wrong6)
        
        # Part 3 moves the objects to the blanket, which is under the tent
        if level4_part == 2:
            screen.blit(check6.image, check6)
            screen.blit(level4text2.image, level4text2)
            screen.blit(level2Blanket, (613,150))
            screen.blit(level2Basket, (616,255))
            screen.blit(level2Table, (618,352))
            screen.blit(level2Chairs, (615,465))

            if level4_checks[0] == False:
                basket2.Basket_click()
            if level4_checks[2] == False:
                b_chair.b_chair_click()
            if level4_checks[3] == False:
                y_chair.y_chair_click()
            if level4_checks[1] == False:
                table.Table_click()
            
            
            blanket_locationCheck()
            

        # Checks if all objects are on the blanket
            if button18 == False and level4_checks == [True, True, True, True]:
                level4_part = 3
            if level4_checks[0] == True:
                screen.blit(check7.image, check7)
            elif level4_checks[0] == False and button18==False and pos7[0]>-100 and pos7[0]<498:
                screen.blit(wrong7.image,wrong7)
                
            if level4_checks[1] == True:
                screen.blit(check8.image, check8)
            elif level4_checks[1] == False and button18==False and pos8[0]>-100 and pos8[0]<447:
                screen.blit(wrong8.image,wrong8)
                
            if level4_checks[2] == True:
                screen.blit(check9.image, check9)
            elif level4_checks[2] == False and button18==False and pos9[0]>-100 and pos9[0]<515:
                screen.blit(wrong9.image,wrong9)
                
            if level4_checks[3] == True:
                screen.blit(check10.image, check10)
            elif level4_checks[3] == False and button18==False and pos10[0]>-100 and pos10[0]<515:
                screen.blit(wrong10.image,wrong10)
            
                    
        # Part 3 moves the new rain objects to under the tent
        if level4_part == 3:
            
            screen.blit(rain.image, rain)
            screen.blit(level4Umbrella, (606,149))
            screen.blit(level4Jacket, (615,293))
            screen.blit(level4Boots, (620,440))
            screen.blit(level4Text3, (10,450))
            
            if button18 == False and pos11[0] > (pos6[0]-25) and pos11[0]< (pos6[0]+60) and pos11[1] > (pos6[1]-60) and pos11[1] < (pos6[1]+80):
                level4_checks3[0] = True
                level4_blit3[0] = True
            if button18 == False and pos12[0] > (pos6[0]-25) and pos12[0] < (pos6[0]+75) and pos12[1] > (pos6[1]-60) and pos12[1] < (pos6[1]+75):
                level4_checks3[1] = True
                level4_blit3[1] = True
            if button18 == False and pos13[0] > (pos6[0]-25) and pos13[0] < (pos6[0]+65) and pos13[1] > (pos6[1]-60) and pos13[1] < (pos6[1]+85):
                level4_checks3[2] = True
                level4_blit3[2] = True
            
            if level4_checks3 == [True, True, True]:
                screen.blit(next_button1.image,next_button1)
                mousepos80 = pygame.mouse.get_pos()
                if button18 == True and mousepos80[0]<550 and mousepos80[0]>450 and mousepos80[1]<500 and mousepos80[1]>450:
                    state = 9     
            
            if level4_checks3[0] == True:
                screen.blit(check11.image, check11)
            elif level4_checks3[0] == False and button18 == False and pos11[0]>-100 and pos11[0]<475:
                screen.blit(wrong11.image,wrong11)
                
            if level4_checks3[1] == True:
                screen.blit(check12.image, check12)
            elif level4_checks3[1] == False and button18 == False and pos12[0]>-100 and pos12[0]<480:
                screen.blit(wrong12.image,wrong12)
                
            if level4_checks3[2] == True:
                screen.blit(check13.image, check13)
            elif level4_checks3[2] == False and button18 == False and pos13[0]>-100 and pos13[0]<475:
                screen.blit(wrong13.image,wrong13)
                
            if level4_blit3[0] == False:
                screen.blit(umbrella.image, umbrella)
                umbrella.Umbrella_click()
                
            if level4_blit3[1] == False:
                screen.blit(jacket.image, jacket)
                jacket.Jacket_click()
                
            if level4_blit3[2] == False:
                screen.blit(boots.image, boots)
                boots.Boots_click()
                
        
        if level4_blit[1] == False:
            table = objects("../resources/table.png", (121,67), (pos8))
            screen.blit(table.image, table)
        if level4_blit[2] == False:
            b_chair = objects("../resources/bluechair.png", (51,79), (pos9))
            screen.blit(b_chair.image, b_chair)
        if level4_blit[3] == False:
            y_chair = objects("../resources/yellowchair.png", (51,79), (pos10))
            screen.blit(y_chair.image, y_chair)
        if level4_blit[0] == False:
            basket2 = objects("../resources/basket.png", (68,74), (pos7))
            screen.blit(basket2.image, basket2)
        
        mousepos8 = pygame.mouse.get_pos()
        [button18,button28,button38] = pygame.mouse.get_pressed()
        # Home button
        if press == [False, False, False, False, False]:
            if button18 == True and mousepos8[0]>0 and mousepos8[0]<50 and mousepos8[1]>0 and mousepos8[1]<50:
                state = 0
            if button18 == True and mousepos8[0] < 550 and mousepos8[0] > 500 and mousepos8[1] < 50 and mousepos8[1] > 0 and ready == True and music == True:
                music = False
                ready = False
                PlayMusic()
        if music == False:
            screen.blit(OtherLevelsSoundOff.image, OtherLevelsSoundOff)
        if press == [False, False, False, False, False]:
            if button18 == False:
                ready = True
            if button18 == True and mousepos8[0] < 550 and mousepos8[0] > 500 and mousepos8[1] < 50 and mousepos8[1] > 0 and ready == True and music == False:
                music = True
                ready = False
                PlayMusic()
        if music == True:
            screen.blit(OtherLevelsSoundOn.image, OtherLevelsSoundOn) 
        pygame.display.update()      
################################################# Level 5 - Game ################################################
    if state == 9:

        [button19, button29, button39] = pygame.mouse.get_pressed()
        
        check_exit()
        level5 = background("../resources/level5.png")
        blanket = objects("../resources/blanket.png", (135,146), (pos6))
        basket2 = objects("../resources/basket.png", (68,74), (pos7))
        table = objects("../resources/table.png", (121,67), (pos8))
        b_chair = objects("../resources/bluechair.png", (51,79), (pos9))
        y_chair = objects("../resources/yellowchair.png", (51,79), (pos10))
        
        screen.blit(level5.image, level5)
        screen.blit(homeButtonLevel1.image,homeButtonLevel1)
        
        screen.blit(level2Blanket, (613,150))
        screen.blit(level2Basket, (616,255))
        screen.blit(level2Table, (618,352))
        screen.blit(level2Chairs, (615,465))
        screen.blit(level5Text, (10,450))
            
        if level5_checks[0] == True:
            screen.blit(check7.image, check7)
        elif level5_checks[0] == False and button19 == False and pos7[0]>-100 and pos7[0]<498:
            screen.blit(wrong7.image, wrong7)
            
        if level5_checks[1] == True:
            screen.blit(check8.image, check8)
        elif level5_checks[1] == False and button19 == False and pos8[0]>-100 and pos8[0]<447:
            screen.blit(wrong8.image, wrong8)
            
        if level5_checks[2] == True:
            screen.blit(check9.image, check9)
        elif level5_checks[2] == False and button19 == False and pos9[0]>-100 and pos9[0]<515:
            screen.blit(wrong9.image, wrong9)
            
        if level5_checks[3] == True:
            screen.blit(check10.image, check10)
        elif level5_checks[3] == False and button19 == False and pos10[0]>-100 and pos10[0]<515:
            screen.blit(wrong10.image, wrong10)
        
        if level5_part == 1:
            blanket.Blanket_click()
            if button19 == False:
                if pos6[0]>380 and pos6[0]<470 and pos6[1]<350 and pos6[1]>275:
                    level5_blit[4] = True
                    level5_part = 2
                elif pos6[0]>-100 and pos6[0]<450:
                    screen.blit(wrong6.image,wrong6)
        
        if level5_part == 2:
            
            screen.blit(check6.image, check6)
            
            if level5_checks[0] == False:
                basket2.Basket_click()
            if level5_checks[2] == False:
                b_chair.b_chair_click()
            if level5_checks[3] == False:
                y_chair.y_chair_click()
            if level5_checks[1] == False:
                table.Table_click()
                
            car_locationCheck()
            
            if level5_checks == [True, True, True, True]:
                screen.blit(next_button1.image,next_button1)
                mousepos90 = pygame.mouse.get_pos()
                if button19 == True and mousepos90[0]<550 and mousepos90[0]>450 and mousepos90[1]<500 and mousepos90[1]>450:
                    endTime  = pygame.time.get_ticks()/1000
                    state = 10
                    
        if level5_blit[4] == False:
            screen.blit(blanket.image, blanket)
        if level5_blit[1] == False:
            screen.blit(table.image, table)
        if level5_blit[3] == False:
            screen.blit(y_chair.image, y_chair)
        if level5_blit[2] == False:
            screen.blit(b_chair.image, b_chair)
        if level5_blit[0] == False:
            screen.blit(basket2.image, basket2)
        
        mousepos9 = pygame.mouse.get_pos()
        [button19,button29,button39] = pygame.mouse.get_pressed()
        if press == [False, False, False, False, False]:
            if button19 == True and mousepos9[0]>0 and mousepos9[0]<50 and mousepos9[1]>0 and mousepos9[1]<50:
                state = 0
            if button19 == True and mousepos9[0] < 550 and mousepos9[0] > 500 and mousepos9[1] < 50 and mousepos9[1] > 0 and ready == True and music == True:
                music = False
                ready = False
                PlayMusic()
        if music == False:
            screen.blit(OtherLevelsSoundOff.image, OtherLevelsSoundOff)
        if press == [False, False, False, False, False]:
            if button19 == False:
                ready = True
            if button19 == True and mousepos9[0] < 550 and mousepos9[0] > 500 and mousepos9[1] < 50 and mousepos9[1] > 0 and ready == True and music == False:
                music = True
                ready = False
                PlayMusic()
        if music == True:
            screen.blit(OtherLevelsSoundOn.image, OtherLevelsSoundOn) 
        pygame.display.update()  
################################################ ENDGAME #######################################################
    if state == 10:
        
        totalTime = endTime - startTime
        totalTime_str = str(totalTime)
        
        time = font4.render(totalTime_str, True, (0,0,0))
        time_txt = font3.render('Your time was       seconds', True, (0,0,0))
        
        check_exit()
        gold = objects("../resources/gold.png", (101,177), (305,170))
        silver = objects("../resources/silver.png", (101,177), (305,170))
        bronze = objects("../resources/bronze.png", (101,177), (305,170))
        gold_txt = objects("../resources/gold_txt.png", (133,79), (240,96))
        silver_txt = objects("../resources/silver_txt.png", (159,69), (229,94))
        bronze_txt = objects("../resources/bronze_txt.png", (200,67), (207,95))
        end = background("../resources/final_bg.png")
        screen.blit(end.image, end)
        
        
        if totalTime < 180:
            screen.blit(gold_txt.image, gold_txt)
            screen.blit(gold.image, gold)
            
        elif totalTime < 240:
            screen.blit(silver_txt.image, silver_txt)
            screen.blit(silver.image, silver)
        else:
            screen.blit(bronze_txt.image, bronze_txt)
            screen.blit(bronze.image, bronze)
            
        screen.blit(time, (362,361))
        screen.blit(time_txt, (245,363))
        pygame.display.update()
        mousepos10 = pygame.mouse.get_pos()
        [button11,button21,button31] = pygame.mouse.get_pressed()
        if button11 == True:
            if mousepos10[0]>300 and mousepos10[0]<414 and mousepos10[1]>398 and mousepos10[1]<473:
                state = 0
            if mousepos10[0]>609 and mousepos10[0]<667 and mousepos10[1]>417 and mousepos10[1]<471:
                mini_startTime = pygame.time.get_ticks()/1000
                score = 0
                y = -80
                state = 11
            
############################################### Minigame ##########################################################
    
    if state == 11:
        
        check_exit()
        mini_currentTime = pygame.time.get_ticks()/1000
        mini_totalTime = mini_currentTime - mini_startTime
        # as time increases, speed of objects increases
        if mini_totalTime > 90:
            movey = 20
        elif mini_totalTime > 60:
            movey = 15
        elif mini_totalTime > 45:
            movey = 13
        elif mini_totalTime > 30:
            movey = 11
        elif mini_totalTime > 15:
            movey = 9
        else:
            movey = 7
            
        basket = main('../resources/mini_basket.png', (140,106), (x,360))
        apple = fruit('../resources/apple.png', (75,79), (x_locations[x_fruit], y))
        juice = fruit('../resources/juicebox.png', (66,95), (x_locations[x_fruit], y))
        banana = fruit('../resources/banana.png', (80,59), (x_locations[x_fruit], y))
        cupcake = fruit('../resources/cupcake.png', (80,68), (x_locations[x_fruit], y))
        sandwich = fruit('../resources/sandwich.png', (108,72), (x_locations[x_fruit], y))
        mini_bg = background('../resources/generic_bg.png')

        screen.blit(mini_bg.image, mini_bg)
        lose()
        screen.blit(basket.image, basket)
        
        # allow player to move basket
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= 12
        elif keys[pygame.K_RIGHT]:
            x += 12

        # if basket goes off screen, the movement is set to 0 and position is adjusted
        if x < 0:
            x = 1
        if x > 560:
            x = 559
        
        # allows for movement
        y+=movey
        
        score_str = str(score)
        score_txt = font5.render(score_str, True, (0,0,0))
        screen.blit(score_txt1, (490,13))
        screen.blit(score_txt, (630,15))
        
        screen.blit(homeButtonLevel1.image,homeButtonLevel1)
        
        # varies what object is displayed
        if blit[0] == True:
            screen.blit(apple.image, apple)
            apple.getCollisionApple(basket)
            
        elif blit[1] == True:
            screen.blit(juice.image, juice)
            juice.getCollisionJuice(basket)
            
        elif blit[2] == True:
            screen.blit(banana.image, banana)
            banana.getCollisionBanana(basket)
            
        elif blit[3] == True:
            screen.blit(cupcake.image, cupcake)
            cupcake.getCollisionCupcake(basket)
            
        elif blit[4] == True:
            screen.blit(sandwich.image, sandwich)
            sandwich.getCollisionSandwich(basket)
        
        mousepos9 = pygame.mouse.get_pos()
        [button19,button29,button39] = pygame.mouse.get_pressed()
        if press == [False, False, False, False, False]:
            if button19 == True and mousepos9[0]>0 and mousepos9[0]<50 and mousepos9[1]>0 and mousepos9[1]<50:
                state = 0
            if button19 == True and mousepos9[0] < 100 and mousepos9[0] > 50 and mousepos9[1] < 50 and mousepos9[1] > 0 and ready == True and music == True:
                music = False
                ready = False
                PlayMusic()
        if music == False:
            screen.blit(Level1SoundOff.image, Level1SoundOff)
        if press == [False, False, False, False, False]:
            if button19 == False:
                ready = True
            if button19 == True and mousepos9[0] < 100 and mousepos9[0] > 50 and mousepos9[1] < 50 and mousepos9[1] > 0 and ready == True and music == False:
                music = True
                ready = False
                PlayMusic()
        if music == True:
            screen.blit(Level1SoundOn.image, Level1SoundOn)  
            
        pygame.display.update()
###############################################Last Screen##################################################                
    if state == 12:
        
        score_txt = font5.render(score_str, True, (0,0,0))
        check_exit()
        miniFinalBg = background("../resources/minigame_final_bg.png")
        
        screen.blit(miniFinalBg.image, miniFinalBg)
        screen.blit(score_txt, (460,198))
        pygame.display.update()
        
        mousepos10 = pygame.mouse.get_pos()
        [button11,button21,button31] = pygame.mouse.get_pressed()
        if button11 == True:
            if mousepos10[0]>300 and mousepos10[0]<414 and mousepos10[1]>398 and mousepos10[1]<473:
                state = 0
            if mousepos10[0]>609 and mousepos10[0]<667 and mousepos10[1]>417 and mousepos10[1]<471:
                mini_startTime = pygame.time.get_ticks()/1000
                score = 0
                y = -80
                state = 11
       
##################################### Final #######################################################################    
pygame.quit()
sys.exit()
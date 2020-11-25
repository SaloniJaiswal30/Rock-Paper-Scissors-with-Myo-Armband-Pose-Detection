from __future__ import print_function
import pygame
import speech_recognition as sr
#import tkinter as tk
import random

import myo as libmyo
import msvcrt

pygame.init()
width, height = 1000, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Rock-Paper-Scissor-using-MYO')

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
lime=(127,255,0)
blue = (61,89,171)
yellow =(255,255,0)


libmyo.init('C:/sj/secondsem/multimedia/project/myo-sdk-win-0.9.0/bin')
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def draw_image(x, y):
    if (x == "rock"):
        print("rock image")
        rock1 = pygame.image.load("rock.png")
        screen.blit(pygame.transform.scale(rock1, (190, 150)), (550, 160))

    if (y == "rock"):
        rock2 = pygame.image.load("rock.png")
        surf = pygame.transform.flip(rock2,True,False)
        screen.blit(pygame.transform.scale(surf, (190, 150)), (150, 160))

    if (y == "scissors"):
        rock3 = pygame.image.load("scr.png")
        screen.blit(pygame.transform.scale(rock3, (190, 150)), (150, 160))
    if (x == "scissors"):
        rock4 = pygame.image.load("scr.png")
        surf = pygame.transform.flip(rock4, True, False)
        screen.blit(pygame.transform.scale(surf, (190, 150)), (550, 160))
    if (x == "paper"):
        rock6 = pygame.image.load("paper.png")
        surf = pygame.transform.flip(rock6, True, False)
        screen.blit(pygame.transform.scale(surf, (190, 150)), (550, 160))
    if (y == "paper"):
        rock5 = pygame.image.load("paper.png")
        screen.blit(pygame.transform.scale(rock5, (190, 150)), (150, 160))
    pygame.display.update()

def message_display(text, color, x, y,fsize):
    largeText = pygame.font.SysFont('gautami.ttf', fsize)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = (x, y)
    screen.blit(TextSurf, TextRect)
class Listener(libmyo.DeviceListener):
    
    def on_pose(self, myo, timestamp, pose):
        global p,r
        message_display('You',lime,650,100,70)
        message_display('Computer', blue, 190, 100,70)
        mylist = ["rock","paper","scissors"]
        y=random.choice (mylist)
        r='scissors' 
        p=pose
        print("Pose:", pose)
        if(str(p)=='<Pose: fist>'):
            x='rock'
            print("rock")
            
            #message_display(x,green,250,650,115 )
           
            draw_image(x,y)
            print("comp bola ",y)
            msg=algo(x,y)
            message_display(msg,yellow,450,350,115)
            return r
        elif(str(p)=='<Pose: fingers_spread>'):
            x='paper'
            print("paper")
            
            draw_image(x,y)
            print("comp bola ",y)
            msg=algo(x,y)
            message_display(msg,yellow,450,350,115)
            return r
        elif str(p)== '<Pose: rest>':
                r='scissors'
                print("scissors")
                return r
        
        else:
            return False



    # pygame.display.update()


def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")
        # listen for 5 seconds and create the ambient noise energy level
        r.adjust_for_ambient_noise(source, duration=.01)
        print("Say something!")
        audio = r.listen(source)
        print("done")

    try:
        p = r.recognize_google(audio)
        print("You said " + p)
        return p
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    return "Wrong Voice Input. Try again !!!"


def clear():
    screen.fill([0, 0, 255])
    black1 = pygame.image.load("black.jpg")
    screen.blit(black1, (0, 0))
    pygame.display.flip()



def myo():
      print ('myo')
      clear()
      pygame.display.set_caption('Rock-Paper-Scissors-using-MYO')
      hub = libmyo.Hub()
      listener = Listener()
      try:
          w=hub.run_once(2000, listener)
          if w==True:
                x="scissors"
                print ("scissors")
                message_display('You',lime,650,100,70)
                message_display('Computer', blue, 190, 100,70)
                #message_display(x,green,250,650,115 )
                mylist = ["rock","paper","scissors"]
                y=random.choice (mylist)
                draw_image(x,y)
                print("computer ",y)
                msg=algo(x,y)
                message_display(msg,yellow,450,350,115)
          elif w==False:
              print ("")
      finally:

          hub.shutdown()
          
        
def algo(x,y):
    if (x == "rock" and y == "paper"):
        print("comp wins")
        msg = 'Computer Won'
    elif (y == "rock" and x == "paper"):
        print("user wins")
        msg = 'You Won'
    elif (y == "scissors" and x == "paper"):
        print("comp wins")
        msg = 'Computer Won'
    elif (x == "scissors" and y == "paper"):
        print("user wins")
        msg = 'You Won'
    elif (x == "scissors" and y == "rock"):
        print("comp wins")
        msg = 'Computer Won'
    elif (y == "scissors" and x == "rock"):
        print("user wins")
        msg = 'You Won'
    elif (y == x):
        print("tie")
        msg = 'tie'
    else:
        print("hurr")
        msg = 'hurr'
    return msg

def voice():
    pygame.display.set_caption('Rock-Paper-Scissors-using-VOICE')
    clear()

    #message_display('USER says', white, 450, 650)
    #pygame.display.update()

    x =speech()
    #x = "scissors"
    print (str(x))

    if x == None:
            message_display("NO AUDIO",red,115)
            pygame.quit()
    else :
            message_display('You',lime,650,100,70)
            message_display('Computer', blue, 190, 100,70)
            #message_display(x,green,250,650,115 )
            mylist = ["rock","paper","scissors"]
            y=random.choice (mylist)
            draw_image(x,y)
            print("computer said ",y)
            msg=algo(x,y)
            message_display(msg,yellow,450,350,115)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)


def button(msg, x, y, w, h, ic, ac, action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText, white)
    textRect.center = ((x + (w / 2)), (450 + (h / 2)))
    screen.blit(textSurf, textRect)
    return 0


def main():
    home = pygame.image.load("rps.png")
    screen.blit(pygame.transform.scale(home, (370, 180)), (300, 100))
    pygame.draw.rect(home, bright_green, (150, 450, 100, 50))
    message_display('Lets Play GAMYO!!!', white, 450, 350,115)
    pygame.display.flip()

    # pygame.draw.rect(screen, green, (150, 450, 150, 50))
    # pygame.draw.rect(screen, red, (550, 450, 150, 50))


    f = 1
    while (f == 1):
        pygame.display.update()
        # 8 - loop through the events
        for event in pygame.event.get():
            # check if the event is the X button

            button1 = button("Using MYO", 150, 450, 150, 50, green, bright_green, myo)
            button2 = button("Using VOICE!", 550, 450, 150, 50, red, bright_red, voice)

            if event.type == pygame.QUIT:
                # if it is quit the game
                pygame.quit()
                exit(0)


if __name__ == '__main__':
    main()
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 12:40 2018

@author: Mathew Sherry, Michael Pickett
"""

import sys
import random
import snake
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Canvas, ALL, NW


class Cons:
        
    BOARD_WIDTH = 300
    BOARD_HEIGHT = 300
    DELAY = 100
    BODY_SIZE = 10
    MAX_RAND_POS = 27
    
#Load the images for use in our simulation
try:
    bodyImage = Image.open("body.png")
    headImage = Image.open("head.png")
    appleImage = Image.open("apple.png")

except IOError as e:
    
    print(e)
    sys.exit(1)
    




class Board(Canvas):

    def __init__(self):
        super().__init__(width=Cons.BOARD_WIDTH, height=Cons.BOARD_HEIGHT, 
            background="black", highlightthickness=0)
         
        self.initGame()
        self.pack()
        
    def initGame(self):
        '''Initializes and starts the game simulation'''

        self.inGame = True
        self.dots = 3
        self.score = 0
        
        # variables used to move snake object
        self.moveX = Cons.BODY_SIZE
        self.moveY = 0
        
        # starting apple coordinates
        self.appleX = 100
        self.appleY = 190

        
        self.createApples()
        self.locateApple()
        self.bind_all("<Key>", self.onKeyPressed)
        self.after(Cons.DELAY, self.onTimer)
        
        
    def createSnakes(self):
        
        
    def createApples(self):
        self.apple = ImageTk.PhotoImage(appleImage) 
        self.create_image(self.appleX, self.appleY, image=self.apple,
            anchor=NW, tag="apple")


   

    def checkAppleCollision(self):
        '''checks if the head of snake collides with apple'''

        apple = self.find_withtag("apple")
        head = self.find_withtag("head")
        
        print(self.bbox(head))
        
        x1, y1, x2, y2 = self.bbox(head)
        overlap = self.find_overlapping(x1, y1, x2, y2)
            
        for ovr in overlap:
          
            if apple[0] == ovr:
                
                self.score += 1
                x, y = self.coords(apple)
                self.create_image(x, y, image=self.dot, anchor=NW, tag="dot")
                self.locateApple() 
            

    def checkCollisions(self):
        '''checks for collisions'''

        dots = self.find_withtag("dot")
        head = self.find_withtag("head")
        
        x1, y1, x2, y2 = self.bbox(head)
        overlap = self.find_overlapping(x1, y1, x2, y2)
        
        for dot in dots:
            for over in overlap:
                if over == dot:
                  self.inGame = False
            
        if x1 < 0:
            self.inGame = False
        
        if x1 > Cons.BOARD_WIDTH - Cons.BODY_SIZE:
            self.inGame = False

        if y1 < 0:
            self.inGame = False
        
        if y1 > Cons.BOARD_HEIGHT - Cons.BODY_SIZE:
            self.inGame = False
        

    def locateApple(self):
        '''places the apple object on Canvas'''
    
        apple = self.find_withtag("apple")
        self.delete(apple[0])
    
        r = random.randint(0, Cons.MAX_RAND_POS)
        self.appleX = r * Cons.BODY_SIZE
        r = random.randint(0, Cons.MAX_RAND_POS)
        self.appleY = r * Cons.BODY_SIZE
        
        self.create_image(self.appleX, self.appleY, anchor=NW,
            image=self.apple, tag="apple")
                
   
    def onKeyPressed(self, e): 
        '''controls direction variables with cursor keys'''
    
        key = e.keysym

        LEFT_CURSOR_KEY = "Left"
        RIGHT_CURSOR_KEY = "Right"
        UP_CURSOR_KEY = "Up"
        DOWN_CURSOR_KEY = "Down"
        
        if key == LEFT_CURSOR_KEY and self.moveX <= 0:
            
            self.moveX = -Cons.BODY_SIZE
            self.moveY = 0
            
        elif key == RIGHT_CURSOR_KEY and self.moveX >= 0:
            
            self.moveX = Cons.BODY_SIZE
            self.moveY = 0
            
        elif key == UP_CURSOR_KEY and self.moveY <= 0:
                        
            self.moveX = 0
            self.moveY = -Cons.BODY_SIZE
            
        elif key == DOWN_CURSOR_KEY and self.moveY >= 0:
            
            self.moveX = 0
            self.moveY = Cons.BODY_SIZE

            
            
    def onTimer(self):
        '''creates a game cycle each timer event '''

        self.draw()
        self.checkCollisions()

        if self.inGame:
            self.checkAppleCollision()
            self.moveSnake()
            self.after(Cons.DELAY, self.onTimer)
        else:
            self.gameOver()            

            
    def draw(self):
        '''Draws everything to the screen and calls other draw functions'''
        
        score = self.find_withtag("score")
        self.itemconfigure(score, text="Score: {0}".format(self.score))
                                                                                                                                                                                        
             
    def gameOver(self):
        '''deletes all objects and draws game over message'''

        self.delete(ALL)
        self.create_text(self.winfo_width() /2, self.winfo_height()/2, 
            text="Game Over with score {0}".format(self.score), fill="white")            


class GameWindow(Frame):

    def __init__(self):
        super().__init__()
                
        self.master.title('Snekolution')
        self.board = Board()
        self.pack()
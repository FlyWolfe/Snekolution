# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 12:40 2018

@author: Mathew Sherry, Michael Pickett
"""

import sys
import random
from PIL import Image, ImageTk
from tkinter import Tk, Frame, Canvas, ALL, NW



class Snake():
    def __init__(self, x, y, size, score, maxLength, moveX, moveY, bodyImage, headImage, imageSize):
        self.x = x
        self.y = y
        self.size = size
        self.score = score
        self.yDir = 0
        self.bodyImage = bodyImage
        self.headImage = headImage
        self.imageSize = imageSize
        self.moveX = moveX
        self.moveY = moveY
            
    def load(self):
        self.loadImages()
        self.createOnScreen()
    
    def loadImages(self):
        '''Loads images to draw the snake'''
        
        try:
            self.body = ImageTk.PhotoImage(self.bodyImage)
            self.head = ImageTk.PhotoImage(self.headImage)

        except IOError as e:
            
            print(e)
            sys.exit(1)
            
    def createOnScreen(self):
        '''creates objects on Canvas'''
    
        #self.create_text(30, 10, text="Score: {0}".format(self.score), 
        #                 tag="score", fill="white")
        
        self.create_image(self.x, self.y, image=self.head, anchor=NW,  tag="head")
        for i in range(self.size):
            self.create_image(self.x + self.moveX, self.y + self.moveY, image=self.body, anchor=NW, tag="body")
    
    def drawSnake(self):
        '''Draws the current snake to the screen'''
        
    def moveSnake(self, dir):
        '''Movement function for controlling the snake'''
        
        body = self.find_withtag("body")
        head = self.find_withtag("head")
        
        bodyParts = body + head
        
        if dir == 'left':
            self.moveX = -self.imageSize
            self.moveY = 0
        elif dir == 'right':
            self.moveX = self.imageSize
            self.moveY = 0
        elif dir == 'up':
            self.moveX = 0
            self.moveY = -self.imageSize
        elif dir == 'down':
            self.moveX = 0 
            self.moveY = self.imageSize
        else:
            print("Error: Movement command was given an invalid direction")
            sys.exit(1)
            
        for i in range(len(bodyParts) - 1):
            
            c1 = self.coords(bodyParts[i])
            c2 = self.coords(bodyParts[i+1])
            self.move(bodyParts[i], c2[0]-c1[0], c2[1]-c1[1])
            
        self.move(head, self.moveX, self.moveY) 
        
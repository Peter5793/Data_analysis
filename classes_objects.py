# -*- coding: utf-8 -*-
"""
Created on Sat May 28 11:17:47 2022

@author: hp
"""
#import pandas as pd
import matplotlib.pyplot as plt

class Circle():
    # Constrcutor
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
        
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return (self.radius)
     
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0,0), radius = self.radius, fc = self.color))
        plt.axis('scaled')
        plt.show()
        
   
        

# create an object
RedCirlce = Circle(4, 'red')
dir(RedCirlce) # list of all the methods
#print the radius 
RedCirlce.radius
#print color
RedCirlce.color
# draw the red cirlce
RedCirlce.drawCircle()


# intitating the blue circle
BlueCircle = Circle(10, 'blue')
BlueCircle.color
BlueCircle.radius

BlueCircle.drawCircle()

# creating a rectangle
class Rectangle():
    #initialze the constructor
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
    
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0,0), self.width, self.height, fc = self.color))
        plt.axis('scaled')
        plt.show()
        
# rectangle intialization
bluerectangle = Rectangle(56, 12, 'blue')
bluerectangle.color

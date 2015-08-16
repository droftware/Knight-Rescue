import pygame
import constants
import graphics
import landforms
import coin
import ladder
import item

class Person(item.Item):

	def __init__(self,x,y,width,height,image_path):

		super(Person,self).__init__(x,y,width,height,image_path)


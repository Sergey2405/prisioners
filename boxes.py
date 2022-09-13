#!/usr/bin/python3

import json

class Boxes:
# class Boxes(__int_):
  """docstring for Boxes"""

  __number = 0
  __boxes ={0:0}

  def __init__(self):
    __number = 0
    __boxes = {0: 0}

  def __init__(self, N):
    self.__number = N
    # {0: 0}
    for i in range(0, self.__number):
      self.__boxes[i] = i
      i += 1

  def __repr__(self):
    return repr(vars(self))

  def get_box(self, number):
    return self.__boxes[number]

  def get_boxes(self):
    return self.__boxes

  def swap(self, i, j):
    temp = self.__boxes[i]
    self.__boxes[i] = self.__boxes[j]
    self.__boxes[j] = temp
    return


#!/usr/bin/python3

import json

class Boxes:
# class Boxes(__int_):
  """docstring for Boxes"""

  number = 0
  boxes ={0:0}

  def __init__(self):
    number = 1
    boxes = {0: 0}

  def __init__(self, N):
    self.number = N
    # {0: 0}
    for i in range(0, self.number):
      self.boxes[i] = i
      i += 1

  def __repr__(self):
    return repr(vars(self))

  def get_box(self, number):
    return self.boxes[number]

  def get_boxes(self):
    return self.boxes

  def swap(self, i, j):
    temp = self.boxes[i]
    self.boxes[i] = self.boxes[j]
    self.boxes[j] = temp
    return


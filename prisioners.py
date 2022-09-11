#!/usr/bin/python3

from boxes import Boxes
import random

class Prisioners(Boxes):
  """docstring for Prisioners"""

  def __init__(self, number):
    self.number = number
    self.boxes = Boxes(number)
    self.prisioners = range(0, number)

  def __repr__(self):
    return repr(vars(self))		

  def __do_open_sequence_of_boxes(self, history,
                                  token_number, current_number,
                                  depth, offset):
    current_number = (current_number + offset) % self.number
    if token_number == self.get_box(current_number):
      return (self.open_one_box(current_number), history + self.open_one_box(current_number))
    elif depth <= 0:
      return ('depth', history)
    elif history != []:
      if history[-1] in history[:-1]:
        used_boxes = [used_box[1] for used_box in history]
        unused_boxes = [item for item in self.prisioners if item not in used_boxes]
        current_number = random.choice(unused_boxes)
      return self.__do_open_sequence_of_boxes(history + self.open_one_box(current_number),
                                              token_number,
                                              self.get_box(current_number),
                                              depth - 1, offset)
    else:
      return self.__do_open_sequence_of_boxes(history + self.open_one_box(current_number),
                                              token_number,
                                              self.get_box(current_number),
                                              depth - 1, offset)

  def get_box(self, number):
    return self.boxes.get_box(number)

  def open_one_box(self, number):
    return [(number, self.boxes.get_box(number))]

  # @overload
  # def open_sequence_of_boxes(self, start):
  #   return open_sequence_of_boxes(start, 0)

  # @overload
  def open_sequence_of_boxes(self, start, offset):
    return self.__do_open_sequence_of_boxes([], start, start, self.number // 2, offset)

  def open_sequence_of_boxes_by_all_the_prisioners(self, offset):
    results = {}
    for prisioner in self.prisioners:
      results[prisioner] = self.open_sequence_of_boxes(prisioner, offset)
    return results

  def statistics(self):
    statistics = {}
    for offset in range(0, self.number):
      statistics[offset] = self.open_sequence_of_boxes_by_all_the_prisioners(offset)
    return statistics

  def trim_statistics(self):
    statistics = self.statistics()
    print("statistics=",statistics)
    for token_offset in statistics:
      # print("token_stat", token_stat)# int
      # print("statistics[token_stat]=", statistics[token_stat]) # statistics[token_stat]= {0: ([(6, 0)], [(5, 6), (1, 1), (6, 0)]), 1: ([(1, 1)], [(6, 0), (5, 6), (1, 1)]), 2: ([(7, 2)], [(7, 2)]), 3: ([(0, 3)], [(8, 7), (2, 8), (3, 5), (0, 3)]), 4: ([(4, 4)], [(9, 9), (4, 4)]), 5: ([(3, 5)], [(0, 3), (8, 7), (2, 8), (3, 5)]), 6: ([(5, 6)], [(1, 1), (6, 0), (5, 6)]), 7: ([(8, 7)], [(2, 8), (3, 5), (0, 3), (8, 7)]), 8: ([(2, 8)], [(3, 5), (0, 3), (8, 7), (2, 8)]), 9: ([(9, 9)], [(4, 4), (9, 9)])}
      token_stat = statistics[token_offset]
      token_stat['unreleased'] = 0
      token_stat['released'] = self.number
      print("token_stat=", token_stat)
      for token_prisioner in token_stat:
        opened_boxes = token_stat[token_prisioner]
        print("opened_boxes=",opened_boxes)
        if token_prisioner == 'unreleased' or token_prisioner == 'released':
          continue
        if opened_boxes[0] == 'depth':
          token_stat['unreleased'] += 1
          token_stat['released'] -= 1
      statistics[token_offset] = token_stat
    return statistics

  def shuffle_up_boxes(self, sequence):
    for token in sequence:
      self.boxes.swap(token[0], token[1])


prisioners10 = Prisioners(10)
print("prisioners10",prisioners10)
print('prisioners10.open_one_box',prisioners10.open_one_box(6))
prisioners10.shuffle_up_boxes([(3,6), (0,9), (3,5), (6,9), (7,8), (9,0), (7,2)])
print("After shuffling up boxex. prisioners10.get_boxes",prisioners10.get_boxes())
print("After shuffling up boxex. prisioners10.get_boxes",prisioners10.boxes.boxes)
print("prisioners10.boxes.get_box(5)=",prisioners10.boxes.get_box(5))
print("prisioners10.get_box(5)=",prisioners10.get_box(5))
print("prisioners10.open_sequence_of_boxes(5, 8)",prisioners10.open_sequence_of_boxes(5, 8))
print("prisioners10.trim_statistics()=", prisioners10.trim_statistics())

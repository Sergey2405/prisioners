#!/usr/bin/python3

from boxes import Boxes
import random

class Prisioners(Boxes):
  """docstring for Prisioners"""

  def __init__(self, number):
    self.__number = number
    self.__boxes = Boxes(number)
    self.__prisioners = range(0, number)

  def __repr__(self):
    return repr(vars(self))		

  def __do_open_sequence_of_boxes(self, history,
                                  token_number, current_number,
                                  depth, offset):
    current_number = (current_number + offset) % self.__number
    if token_number == self.get_box(current_number):
      return (self.open_one_box(current_number), history + self.open_one_box(current_number))
    elif depth <= 0:
      return ('depth', history)
    elif history != []:
      if history[-1] in history[:-1]:
        used_boxes = [used_box[1] for used_box in history]
        unused_boxes = [item for item in self.__prisioners if item not in used_boxes]
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
    return self.__boxes.get_box(number)

  def open_one_box(self, number):
    return [(number, self.__boxes.get_box(number))]

  # @overload
  # def open_sequence_of_boxes(self, start):
  #   return open_sequence_of_boxes(start, 0)

  # @overload
  def open_sequence_of_boxes(self, start, offset):
    return self.__do_open_sequence_of_boxes([], start, start, self.__number // 2, offset)

  def open_sequence_of_boxes_by_all_the_prisioners(self, offset):
    results = {}
    for prisioner in self.__prisioners:
      results[prisioner] = self.open_sequence_of_boxes(prisioner, offset)
    return results

  def statistics(self):
    statistics = {}
    for offset in range(0, self.__number):
      statistics[offset] = self.open_sequence_of_boxes_by_all_the_prisioners(offset)
    return statistics

  def analyze_statistics(self):
    statistics = self.statistics()
    for token_offset in statistics:
      token_stat = statistics[token_offset]
      token_stat['unreleased'] = 0
      token_stat['released'] = self.__number
      for token_prisioner in token_stat:
        opened_boxes = token_stat[token_prisioner]
        if token_prisioner == 'unreleased' or token_prisioner == 'released':
          continue
        if opened_boxes[0] == 'depth':
          token_stat['unreleased'] += 1
          token_stat['released'] -= 1
      statistics[token_offset] = token_stat
    return statistics

  def trim_statistics(self):
    all_statistics = self.analyze_statistics()
    trimmed_statistics = {}
    trimmed_statistics['total_released'] = 0
    trimmed_statistics['total_unreleased'] = 0
    for token_offset in all_statistics:
      trimmed_statistics[token_offset] = {}
      trimmed_statistics[token_offset]['unreleased'] = all_statistics[token_offset]['unreleased']
      trimmed_statistics[token_offset]['released'] = all_statistics[token_offset]['released']
      if trimmed_statistics[token_offset]['unreleased'] == 0 and trimmed_statistics[token_offset]['released'] == self.__number:
        trimmed_statistics['total_released'] += 1
      else:
        trimmed_statistics['total_unreleased'] += 1
    return trimmed_statistics


  def shuffle_up_boxes(self, sequence):
    for token in sequence:
      self.__boxes.swap(token[0], token[1])

  def shuffle_up_boxes_randomly(self):
    boxes = self.__boxes.get_boxes()
    for token_box in boxes:
      self.__boxes.swap(token_box, random.choice(list(boxes.keys())))

number = 300
prisioners10 = Prisioners(number)
# print("prisioners10",prisioners10)
# print('prisioners10.open_one_box',prisioners10.open_one_box(6))
# prisioners10.shuffle_up_boxes([(3,6), (0,9), (3,5), (6,9), (7,8), (9,0), (7,2)])
prisioners10.shuffle_up_boxes_randomly()
# print("After shuffling up boxex. prisioners10.get_boxes",prisioners10.get_boxes())
# print("After shuffling up boxex. prisioners10.get_boxes",prisioners10.boxes.boxes)
# print("prisioners10.boxes.get_box(5)=",prisioners10.boxes.get_box(5))
# print("prisioners10.get_box(5)=",prisioners10.get_box(5))
# print("prisioners10.open_sequence_of_boxes(5, 8)",prisioners10.open_sequence_of_boxes(5, 8))
# print("prisioners10.analyze_statistics()=", prisioners10.analyze_statistics())
trimmed_statistics = prisioners10.trim_statistics()
print("trimmed_statistics=", trimmed_statistics)
print("trimmed_statistics['total_released']=", trimmed_statistics['total_released'])
print("trimmed_statistics['total_unreleased']=", trimmed_statistics['total_unreleased'])

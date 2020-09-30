#!/usr/bin/env python
import shutil as sh
import sys
from collections import namedtuple
from glob import glob
import re
import os

class WrongInputs(Exception):
        pass

class Movement:
        def __init__(self, pattern, to, from_):        
                self.to = to
                self.pattern = pattern
                self.from_ = from_
        
        def memory_size(self, place='to'):
                '''
                Returning the disk usage of the current directory
                '''
                try:
                        if place.startswith('t'):
                                return sh.disk_usage(self.to)
                        elif place.startswith('f'):
                                return sh.disk_usage('.')
                except:
                        print('The parameter is not well placed')

                        
        def memo_in_percent(self):
                '''
                Converting the used and free space to the overall percentage
                
                '''
                print("Size of which location? ['from' | 'to']\n>>>>", end=' ')
                place = input().lower()
                space = self.memory_size(place)
                total = 100
                free = round(space.free/space.total*total, 2)
                used = round(space.used/space.total*total, 2)
                memory = namedtuple('Memory', ['Free', 'Used', 'Total'])
                return memory(free, used, total)

        
        def move(self):
                '''
                Moving the capture pattern to the specified location
                '''
                try:
                        data = glob(os.path.join(self.from_, self.pattern))
                        for i in data:
                                sh.move(i, self.to)
                except Exception as e:
                        print(f'The process cannot be done because {e}')

def main():
        try:
                print('From which location?\n. --> current directory\nSpecify the path e.g C:\\user\\.')
                path0 = input()
                path1 = input('Input the pattern to use: ')
                path2 = input('The location to move-to: ')
                mov = Movement(path1, path2, path0)
                print('Do you want to move the data to the specified location?\n[Y|N]>>>', end=' ')
                ask = input().capitalize()
                if ask.startswith('Y'):
                        mov.move()
                print('Do you want to check the memory usage?\n[Y|N]>>>', end=' ')
                ask = input().capitalize()
                if ask.startswith('Y'):
                        print(mov.memo_in_percent())
                else:
                        pass
                sys.exit(0)
        except Exception as e:
                raise WrongInputs('Invalid pattern or location')
                sys.exit(1)
                
if __name__ == '__main__':
        main()

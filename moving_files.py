#!/usr/bin/env python
import shutil as sh
import sys
from collections import namedtuple
from glob import glob
import os
from dataclasses import dataclass


class WrongInputs(Exception):
    pass


@dataclass
class Movement:
    """
    Movement(from_, pattern, to)

    Moving files through pattern from one location to the other
    And viewing the size through the location specify has taken in the memory
    """
    from_: str
    pattern: str
    to: str

    def memory_size(self, place='to'):
        """
        Returning the disk usage of the current directory
        """
        try:
            if place.startswith('t'):
                return sh.disk_usage(self.to)
            elif place.startswith('f'):
                return sh.disk_usage('.')
        except Exception as e:
            WrongInputs(f'The parameter is not well placed\n{e}')

    def memo_in_percent(self):
        """
        Converting the used and free space to the overall percentage
        """
        print("Size of which location? ['from' | 'to']\n>>>>", end=' ')
        place = input().lower()
        space = self.memory_size(place)
        total = 100
        free = round(space.free/space.total*total, 2)
        used = round(space.used/space.total*total, 2)
        memory = namedtuple('Memory', ['Free', 'Used', 'Total'])
        return memory(free, used, total)

    def move(self):
        """
        Moving the capture pattern to the specified location
        """
        try:
            data = glob(os.path.join(self.from_, self.pattern))
            for i in data:
                sh.move(i, self.to)
        except Exception as e:
            print(f'{e}')


def main():
    try:
        print('From which location?\n [.] --> Current directory\n[..] --> Parent directory\nSpecify the path e.g C:\\user\\.')
        path0 = input('>>> ')
        path1 = input('Input the pattern to use: ')
        path2 = input('The location to move-to: ')
        mov = Movement(path0, path1, path2)
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
        raise WrongInputs(f'Invalid pattern or location')
        sys.exit(1)


if __name__ == '__main__':
    main()

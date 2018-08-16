import sys
import termios
import tty
import os
import time
from config import FRAME_RATE


def keyAction(key=None, player=None, scene=None):
    if key is None:
        scene._grid[player.pos['y']][player.pos['x']] = 0
        player.move(action=None, scene=scene)
    else:
        if key == 'q':
            time.sleep(1/FRAME_RATE)
            return False
        elif key == 'a':
            if player is None:
                return
            if scene is None:
                return
            scene._grid[player.pos['y']][player.pos['x']] = 0
            player.move('LEFT', scene=scene)
            time.sleep(1/FRAME_RATE)
            # MOVE LEFT
        elif key == 'd':
            if player is None:
                return
            if scene is None:
                return
            scene._grid[player.pos['y']][player.pos['x']] = 0
            player.move('RIGHT', scene=scene)
            time.sleep(1/FRAME_RATE)
            # MOVE RIGHT
        elif key == 'w':
            if player is None:
                return
            if scene is None:
                return
            scene._grid[player.pos['y']][player.pos['x']] = 0
            player.move('JUMP', scene=scene)
            time.sleep(1/FRAME_RATE)
            # JUMP
        elif key == 'i':
            print("INSTRUCTIONS")
            time.sleep(1/FRAME_RATE)
            # INSTRUCTIONS
        elif key == 'p':
            print("PAUSE")
            time.sleep(1/FRAME_RATE)
        else:
            pass
            time.sleep(1/FRAME_RATE)
            # PAUSE
    return True
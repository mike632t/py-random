#!/usr/bin/python3
#
#   py-random-draw.py
#
#   Displays points generated using a pseudo-random number generator.
#
#   The latest point is shown in RED with the most recent 1000 points shown
#   in BLUE, older points are shown in GREY.
#
#   While the points are being plotted the followign keys can be used:
#
#   `Space` pauses the updates and allows points to be drawn one at a time.
#
#   `Enter` continues plotting.
#
#   `Escape` quits.
#
#   `Cursor Up`  and  `Cursor Down` decrease of increase the delay  between
#   iterations.
#
#   This program is free software: you can redistribute it and/or modify it
#   under  the terms of the GNU General Public License as published by  the
#   Free Software Foundation, either version 3 of the License, or (at  your
#   option) any later version.
#
#   This  program is distributed in the hope that it will  be  useful,  but
#   WITHOUT   ANY   WARRANTY;   without even  the   implied   warranty   of
#   MERCHANTABILITY  or  FITNESS  FOR A PARTICULAR  PURPOSE.  See  the  GNU
#   General Public License for more details.
#
#   You should have received a copy of the GNU General Public License along
#   with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#   24 Oct 26   0.1   - Initial version - MT
#   25 Oct 26   0.2   - Modified to display number of iterations - MT
#                     - Moved  random number generator to a separate  class
#                       with a subset of the python random number generator
#                       properties and methods.  Allowing either to be used
#                       simply by selecting which class is imported - MT
#

import os, sys, math, time, pygame
import random

NAME = "Random Number Scatter Plot"
VERSION = "0.2"

COLUMNS = 8  # Number of columns of coordinates to print on a line (1 - 8).

WIDTH = 900  # Width of window.
HEIGHT = 900  # Height of window.
MARGIN = 50  # Margin around edge of plot area.

POINTS = 1000  # Number of point to highlight (in BLUE).
INTERVAL = 0.05  #  Delay (is seconds) between each iteration.

SIZE = 2  # Size of point

WHITE = (255, 255, 255)  # Define colours
BLACK = (0, 0, 0)
RED = (192, 0, 0)
BLUE = (30, 100, 220)
GREY = (210, 210, 210)

def _update():  # Update display.

  global _count, _seed, _points, _x_pos, _y_pos

  _count += 1
  _x = random.random()  # Coordinates use floats.
  _y = random.random()

  if _print:  # Print coordinates if required.
    sys.stdout.write(format(_x, ".4f") + ", " + format(_y, ".4f"))  # Don't use print(), format() returns a string so no need to use str().
    if _count % _columns == 0:
      sys.stdout.write("\n")
    else:
      sys.stdout.write("  ")

  if len(_points) > 0:  # If there is more than one point redraw the last one in BLUE.
    pygame.draw.circle(_screen, BLUE, (_x_pos, _y_pos), SIZE)

  _x_pos = int(_left + SIZE + _x * (_width - 2 * SIZE))  # Points are scaled to plot inside the axis (not strictly correct but it looks better).
  _y_pos = int(_top + SIZE + (1 - _y) * (_height - 2 * SIZE))

  _points.append((_x_pos, _y_pos))

  if len(_points) > POINTS:
    pygame.draw.circle(_screen, GREY, _points[0], SIZE)  # Redraw the oldest point in GREY.
    _points.pop(0)  # and remove from the list.

  pygame.draw.circle(_screen, RED, (_x_pos, _y_pos), SIZE)  # Draw the latest point in RED.
  pygame.display.flip()

def _format(_int):
    if abs(_int) >= 1_000_000:
        return format(_int / 1000000, ".1f") + " M"
    if abs(_int) >= 1_000:
        return format(_int / 1_000, ".0f") + " K"
    return format(_int, "d")


def _about():
  sys.stdout.write(
    "Usage: " + sys.argv[0] + " [OPTION]...\n" +
    "Plots pains of random number values (between 0 and 1) .\n" + "\n" +
    "      --print              print each pair of numbers \n" +
    "  -?, --help               display this help and exit\n" +
    "      --version            output version information and exit\n" +
    "\n")
  raise SystemExit

def _version():
  sys.stdout.write(os.path.basename(sys.argv[0]) + " " + str(VERSION) +"\n"
    "License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>.\n"
    "This is free software: you are free to change and redistribute it.\n"
    "There is NO WARRANTY, to the extent permitted by law.\n")
  raise SystemExit

def _error(_error):
  sys.stderr.write(os.path.basename(sys.argv[0]) + ": " + _error + "\n")
  raise SystemExit


_left = MARGIN
_top = MARGIN
_width = WIDTH - 2 * MARGIN
_height = HEIGHT - 2 * MARGIN

_wait = INTERVAL

#
#  Parse command line.
#
_verbose = 0
_debug = False
_print = False
_count = 0
while _count < len(sys.argv):
  _arg = sys.argv [_count]
  if _arg[:1] == "-" and len(_arg) > 1:
    if _arg in ["-?", "--help"]:
      _about()
    elif _arg in ["-v", "--version"]:
      _version()
    elif _arg in ["--print"]:
      _print = True
      _wait = 0.05
    elif _arg in "--delay":
      if _count < len(sys.argv):
        if sys.argv[_count + 1][:1] != "-":
          try:
            _wait = float(sys.argv[_count + 1])
            if not math.isfinite(_wait) or _wait > 0.5:
                raise ValueError
            _wait = max(0.00005, _wait)
          except ValueError:
            error("invalid delay")
          _count += 1
    else:
      if _arg[:2] == "--":
        _error ("unrecognized option -- '" + (_arg[2:] + "'"))
      else:
        _error ("invalid option -- '" + (_arg[1:] + "'"))
  else:
    if _count > 0:
      _error ("extra operand '" + (_arg + "'"))
  _count += 1

_columns = max( 1 , COLUMNS)  # Must be at least one column
_columns = min( 8 , _columns)  # but not more than eight.

pygame.init()
_screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Random Number Scatter Plot")

_font = pygame.font.SysFont("Arial", min(16, MARGIN // 2), bold=False)

#
#   Draw Axis.
#

_screen.fill(WHITE)
pygame.draw.rect(_screen, BLACK,(_left, _top, _width, _height), 2)

#
#   Draw grid lines and centred labels.
#

for _count in range(11):
    _x = _left + _count * _width / 10
    _y = _top + _count * _height / 10

    pygame.draw.line(_screen, GREY, (_x, _top), (_x, _top + _height))
    pygame.draw.line(_screen, GREY, (_left, _y), (_left + _width, _y))

    # X-axis label: horizontally centred under the tick.

    _label = _font.render(format(_count / 10, ".1f"), True, BLACK)
    _label_rect = _label.get_rect()
    _label_rect.centerx = round(_x)
    _label_rect.top = _top + _height + (MARGIN - _label_rect.height) // 2
    _screen.blit(_label, _label_rect)

    # Y-axis label: vertically centred beside the tick

    _label = _font.render(format(1 - _count / 10, ".1f"), True, BLACK)
    _label_rect = _label.get_rect()
    _label_rect.left = (MARGIN - _label_rect.width) // 2
    _label_rect.centery = round(_y)
    _screen.blit(_label, _label_rect)

#
#   Plot points until window is closed.
#

_count = 0
_points = []
_running = True
_paused = False

random.seed("0.5284163")

while _running:

  # Update counter

  if _count % 1000 == 0:
    if _label_rect:_screen.fill(WHITE, _label_rect)
    _label = _font.render("n > " + _format(_count), True, BLACK)
    _label_rect = _label.get_rect()
    _label_rect.right = _left + _width
    _label_rect.centery = _top // 2
    _screen.blit(_label, _label_rect)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      _running = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        if _paused: _update()  # Space single steps updates.
        _paused = True
      elif event.key == pygame.K_RETURN:
        if _paused: _paused = False
      elif event.key == pygame.K_ESCAPE:
        _running = False
      elif event.key == pygame.K_UP:
        _wait = max(0.00005, _wait / 2)
      elif event.key == pygame.K_DOWN:
        _wait = min(0.1, _wait * 2)

  if not _paused:
    _update()
    time.sleep(_wait)

if _print and (_count % _columns != 0): sys.stdout.write("\n")
sys.stdout.flush()

pygame.quit()
sys.exit()

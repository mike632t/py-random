#!/usr/bin/python3
#
#   py-random-test.py
#
#   A simplified test harness that generate 16 pairs of random numbers.
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
#   25 Oct 26   0.1   - Initial version - MT
#

import sys
import class_random as random  # Use custom generator class.

_columns = 8
_count = 0
while _count < 16:
  _count += 1
  _x = random.random()
  _y = random.random()

  sys.stdout.write(
    format(_x, ".4f") + ", " + format(_y, ".4f")
  )

  if _count % _columns == 0:
    sys.stdout.write("\n")
  else:
    sys.stdout.write("  ")

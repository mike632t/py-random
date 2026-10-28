#!/usr/bin/python3
#
#   class_random.py
#
#   A pseudo-random number generator class that implements a subset of  the
#   standard module.
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
#   27 Oct 26         - Return the initial seed on first use - MT                  -
#

import decimal

# HP67 - Period length 5,000,000

SEED = "0.5284163"

_a = decimal.Decimal("997")
_c = decimal.Decimal("0")
_m = decimal.Decimal("1")

def _rand(_r):  # r_{n+1}=(9821 * r_{n} + 0.211327) \mod 1
  _r = (_a * _r + _c) % _m
  return _r


class random:
  def __init__(self, _seed=None):
    decimal.getcontext().prec = 12
    self.seed(_seed)

  def seed(self, _seed=None, _version=2):  # Version is ignored.
    if _seed is None:
      _seed = SEED
    self._seed = decimal.Decimal(str(_seed))
    self._init = True

  def random(self):
    if self._init:  # Return initial seed.
      self._seed = self._seed
      self._init = False
    else:
      self._seed = _rand(self._seed)
    return float(self._seed)

  def randrange(self, _start, _stop=None, _step=1):
    if _stop is None:
      _start, _stop = 0, _start
    _count = len(range(_start, _stop, _step))
    if _count <= 0:
      raise ValueError("empty range for randrange()")
    return _start + _step * int(self.random() * _count)

  def randint(self, _start, _stop):
    return self.randrange(_start, _stop + 1)

  def uniform(self, _start, _stop):
    return _start + (_stop - _start) * self.random()

  def choice(self, _sequence):
    if not _sequence:
      raise IndexError("Cannot choose from an empty sequence")
    return _sequence[self.randrange(len(_sequence))]

  def shuffle(self, _list):
    for _count in range(len(_list) - 1, 0, -1):
      _index = self.randrange(_count + 1)  # Pick a random index.
      _list[_count], _list[_index] = _list[_index], _list[_count]  # Swap elements.

_instance = random(SEED)  # Create a single reusable instance of the class.

def seed(_seed=None, _version=2):
  _instance.seed(_seed, _version)

def random():
  return _instance.random()

def randrange(_start, _stop=None, _step=1):
  return _instance.randrange(_start, _stop, _step)

def randint(_start, _stop):
  return _instance.randint(_start, _stop)

def uniform(_start, _stop):
  return _instance.uniform(_start, _stop)

def choice(_sequence):
  return _instance.choice(_sequence)

def shuffle(_list):
  return _instance.shuffle(_list)


if __name__ == "__main__":

  import sys

  _columns = 8
  for _count in range(1, 17):
    _x = random()
    _y = random()

    sys.stdout.write(
      format(_x, ".4f") + ", " + format(_y, ".4f")
    )

    if _count % _columns == 0:
      sys.stdout.write("\n")
    else:
      sys.stdout.write("  ")

# Random Number Scatter Plot

Allows pseudo-random number sequences to be visualized in two dimensions.

While distribution can appear uniform the visualisation is not a substitute
for formal statistical testing.  However, a scatter plot can reveal visible
patterns,  clustering, or other irregularities that might otherwise not  be
noticed

Using a separate class that provides a replacement the python random number
generator  with a subset of the standard interface interface allows for the
behaviour of different algorithms to be compared.

To make it easier to see the how the points are distributed the most recent
1,000 points are shown in blue, with any older points shown in grey.


## Usage

```
Usage: ./py-random-plot.py [OPTION]...
Plots pairs of random number values (between 0 and 1) .

      --delay  <seconds>   wait for <seconds> between points
      --print              print each pair of numbers
      --skip               skip the initial seed value
  -?, --help               display this help and exit
      --version            output version information and exit
```

- `--delay <seconds>` Sets the delay between plotted points in seconds.

- `--limit <number>` Pauses plotting after <number> points. (Press **Enter** to continue).

- `--print` Prints the coordinate pairs on standard output (formatted to four decimal places).

- `--skip` Skips the initial seed value.


## Controls

| Key            | Action  |
|----------------|---------|
| **Space**      | Pause plotting. While paused, each press advances the plot by one point. |
| **Enter**      | Resume continuous plotting. |
| **Escape**     | Quit the application. |
| **Up arrow**   | Halve the delay between points, down to the minimum delay. |
| **Down arrow** | Double the delay between points, up to 0.1 seconds. |


## A replacement random number class

A replacement for python's standard random number generator that implements
a subset of the usual interface provides an easy way to modify the way that
the random numbers are generated.

The available methods and functions are:

| Method | Description |
|--------|-------------|
| `seed(a=None)`       | Initialise or reset the seed. If `a` is `None` the default seed is used. |
| `random()`           | Return the next value as a float. |
| `randrange(start, stop=None, step=1)` | Select an integer from a specified range. |
| `randint(a, b)`      | Select an integer between `a` and `b`, inclusive. |
| `uniform(a, b)`      | Return a floating-point value between the specified endpoints. |
| `choice(sequence)`   | Select an element from a non-empty sequence. |
| `shuffle(list)`      | Shuffle a list in place. |

The first call to `random()` returns the initial seed.

To avoid rounding errors it uses decimal arithmetic internally and converts
the generated values to floats.  To modify the random number generator  you
just need to replace the rand() function.

The class module should be in the same folder as the python script.


## Prerequisites

- Python 3
- Pygame

Install Pygame using pip:
```
python3 -m pip install pygame
```


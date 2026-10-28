# Random Number Scatter Plot

Allows pseudo-random number sequences to be visualized in two dimensions.

While distribution can appear uniform the visualisation is not a substitute
for formal statistical testing.  However, a scatter plot can reveal visible
patterns,  clustering, or other irregularities that might otherwise not  be
noticed

Using a seperate class that provides a replacement the python random number
generator  with a subset of the standard interface interface allows for the
behaviour of different algorythms to be compaired.

To make it easier to see the how the points are distributed the most recent
1,000 points are shown in blue, with any older points shown in grey.


## Usage

```
   Usage: py-random-draw.py [OPTION]...

     --delay <seconds>   Wait for <seconds> between points
     --limit <number>    Pause after plotting <number> of points
     --print             Print each pair of coordinates
     --skip              Skip the initial seed value
     -?, --help          Display help and exit
     -v, --version       Display version information and exit
```

- `--delay <seconds>` Sets the delay between plotted points in seconds.

- `--limit <number>` Pauses plotting after <number> points. (Press **Enter** to continue).

- `--print` Prints the coordinate pairs on standard output (formatted to four decimal places).

- `--skip` Skips the initial seed value.


## Controls

| Key | Action |
|---|---|
| **Space** | Pause plotting. While paused, each press advances the plot by one point. |
| **Enter** | Resume continuous plotting. |
| **Escape** | Quit the application. |
| **Up arrow** | Halve the delay between points, down to the minimum delay. |
| **Down arrow** | Double the delay between points, up to 0.1 seconds. |


## Replacement random number class

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


## Files

| File | Description |
|---|---|
| `py-random-draw.py` | Main application. Generates and plots coordinate pairs using Pygame. |
| `class_random.py` | Custom pseudo-random number generator and a subset of the Python `random` module interface. |

Keep both files in the same directory.


## Prerequsites

- Python 3
- Pygame

Install Pygame using pip:

```
python3 -m pip install pygame
```


# rgbxmastree

Code library, CLI, and examples for the RGB Xmas Tree produced by PiHut.

This fork from the [original PiHut code](https://github.com/ThePiHut/rgbxmastree) is totally independent and very grateful to [@bennuttal](https://github.com/bennuttall) for the initial work! Any bugs and mistakes herein are my own.

## Getting started

Install via [pipx](https://pipx.pypa.io/stable/) for easy access to the commandline interface:

```bash
pipx install rgbxmastree
```

You can now use the `rgbxmastree` command and subcommands to run your tree!

To use the API in your own scripts and applications install via plain pip or your favourite project management tool:

```bash
pip install rgbxmastree
poetry add rgbxmastree
uv add rgbxmastree
```

## Initialising a tree instance

Open a Python shell or IDE, import `RGBXmasTree` and initialise your tree:

```python
from rgbxmastree.tree import RGBXmasTree

tree = RGBXmasTree()
```

## Change the colour

You can set the colour of all the LEDs together using RGB values (all 0-1):

```python
from rgbxmastree.tree import RGBXmasTree

tree = RGBXmasTree()

tree.color = (1, 0, 0)
```

Alternatively you can use the `colorzero` library:

```python
from rgbxmastree.tree import RGBXmasTree
from colorzero import Color

tree = RGBXmasTree()

tree.color = Color('red')
```

You can write a loop to repeatedly cycle through red, green and blue:

```python
from rgbxmastree.tree import RGBXmasTree
from time import sleep

tree = RGBXmasTree()

colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

for color in colors:
    tree.color = color
    sleep(1)
```

## Individual control

You can also control each LED individually, for example turn each one red, one
at a time:

```python
from rgbxmastree.tree import RGBXmasTree
from time import sleep

tree = RGBXmasTree()

for pixel in tree:
    pixel.color = (1, 0, 0)
    sleep(1)
```

To control a specific pixel, you can access it by its index number (0-24):

```python
tree[0].color = (0, 1, 0)
```

## Change the brightness

You can change the brightness from 0 to 1 - the default is 0.5. You can set this
when initialising your tree:

```python
from rgbxmastree.tree import RGBXmasTree

tree = RGBXmasTree(brightness=0.1)
```

Alternatively, you can change it after initialisation:

```python
from rgbxmastree.tree import RGBXmasTree

tree = RGBXmasTree()

tree.brightness = 0.1
```

You'll find that 1 is _extremely bright_ and even 0.1 is plenty bright enough if
the tree is on your desk :)

## Examples

## RGB cycle

Cycle through red, green and blue, changing all pixels together

- [rgb.py](examples/rgb.py)

### One-by-one

Cycle through red, green and blue, changing pixel-by-pixel

- [onebyone.py](examples/onebyone.py)

### Hue cycle

Cycle through hues forever

- [huecycle.py](examples/huecycle.py)

### Random sparkles

Randomly sparkle all the pixels

- [randomsparkles.py](examples/randomsparkles.py)

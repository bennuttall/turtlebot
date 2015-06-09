# turtlebot

An extension of the Python `turtle` module for use with Raspberry Pi robots driven by motor boards such as [Ryanteck RTK](https://www.ryanteck.ltd.uk/store/index.php?id_product=8&controller=product)

## Usage

```python
from turtlebot import TurtleBot

bot = TurtleBot(17, 18, 22, 23, 90)  # configure for RTK motor board pins, with turn speed 90

bot.forward(2)  # drive forwards for 2 seconds
bot.left(90)  # turn left 90 degrees
bot.backward(1)  # drive backwards for 1 second
bot.right(180)  # turn 180 degrees
```

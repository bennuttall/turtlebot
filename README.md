**This project has been superceded by [GPIO Zero](https://github.com/RPi-Distro/python-gpiozero)**

# turtlebot

Drive your Raspberry Pi robot like you're using the Python Turtle module

## Usage

```python
from turtlebot import TurtleBot

bot = TurtleBot(17, 18, 22, 23, 90)  # configure for RTK motor board pins, with turn speed 90

bot.forward(2)  # drive forwards for 2 seconds
bot.left(90)  # turn left 90 degrees
bot.backward(1)  # drive backwards for 1 second
bot.right(180)  # turn 180 degrees
```

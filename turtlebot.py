from __future__ import division
from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class TurtleBot(object):
    def __init__(right_forward, right_backward,
            left_forward, left_backward, speed):
        self.right_forward = right_forward
        self.right_backward = right_backward
        self.left_forward = left_forward
        self.left_backward = left_backward
        self.speed = speed
        self._setup_gpio()

    def _setup_gpio(self):
        """
        Setup motor pins as GPIO outputs
        """

        GPIO.setup(self.right_forward, GPIO.OUT)
        GPIO.setup(self.right_backward, GPIO.OUT)
        GPIO.setup(self.left_forward, GPIO.OUT)
        GPIO.setup(self.left_backward, GPIO.OUT)

    def _motor_on(motor):
        """
        Turn a given motor on
        """

        GPIO.output(motor, True)

    def _motor_off(motor):
        """
        Turn a given motor off
        """

        GPIO.output(motor, False)

    def forward(seconds):
        """
        Move the robot forwards for a given number of seconds
        """

        _motor_on(self.left_forward)
        _motor_on(self.right_forward)
        sleep(seconds)
        _motor_off(self.left_forward)
        _motor_off(self.right_forward)

    def backward(seconds):
        """
        Move the robot backwards for a given number of seconds
        """

        _motor_on(self.left_backward)
        _motor_on(self.right_backward)
        sleep(seconds)
        _motor_off(self.left_backward)
        _motor_off(self.right_backward)

    def left(angle):
        """
        Turn the robot left a given number of degrees (based on a number of
        seconds calculated by the object's speed property)
        """

        _motor_on(self.right_forward)
        _motor_on(self.left_backward)
        sleep(angle / self.speed)
        _motor_off(self.right_forward)
        _motor_off(self.left_backward)

    def right(angle):
        """
        Turn the robot right a given number of degrees (based on a number of
        seconds calculated by the object's speed property)
        """

        _motor_on(self.left_forward)
        _motor_on(self.right_backward)
        sleep(angle / self.speed)
        _motor_off(self.left_forward)
        _motor_off(self.right_backward)

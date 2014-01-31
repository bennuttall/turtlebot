import RPi.GPIO as GPIO
from time import sleep
import turtle

GPIO.setmode(GPIO.BCM)

RIGHT_FORWARD = 17
RIGHT_BACKWARD = 18
LEFT_FORWARD = 22
LEFT_BACKWARD = 23

GPIO.setup(RIGHT_FORWARD, GPIO.OUT)
GPIO.setup(RIGHT_BACKWARD, GPIO.OUT)

GPIO.setup(LEFT_FORWARD, GPIO.OUT)
GPIO.setup(LEFT_BACKWARD, GPIO.OUT)


def motor_on(motor):
    GPIO.output(motor, 1)


def motor_off(motor):
    GPIO.output(motor, 0)


def forward(seconds):
    turtle.forward(seconds * 100)
    motor_on(LEFT_FORWARD)
    motor_on(RIGHT_FORWARD)
    sleep(seconds)
    motor_off(LEFT_FORWARD)
    motor_off(RIGHT_FORWARD)


def backward(seconds):
    turtle.backward(seconds * 100)
    motor_on(LEFT_BACKWARD)
    motor_on(RIGHT_BACKWARD)
    sleep(seconds)
    motor_off(LEFT_BACKWARD)
    motor_off(RIGHT_BACKWARD)


def left(angle):
    motor_on(RIGHT_FORWARD)
    motor_on(LEFT_BACKWARD)
    sleep(angle / 90)
    motor_off(RIGHT_FORWARD)
    motor_off(LEFT_BACKWARD)


def right(angle):
    motor_on(LEFT_FORWARD)
    motor_on(RIGHT_BACKWARD)
    sleep(angle / 90)
    motor_off(LEFT_FORWARD)
    motor_off(RIGHT_BACKWARD)

import time
import ssd1306
from machine import Pin, I2C


i2c = I2C(-1, scl=Pin(5), sda=Pin(4))
oled_width = 64
oled_height = 48
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


def let_it_snow(x, speed=0.5):
    """Let it snow! This function is drawing one snowflake."""
    oled.pixel(x, 1, 1)
    oled.pixel(x, 2, 1)
    oled.pixel(x, 3, 1)
    oled.pixel(x, 4, 1)
    oled.pixel(x, 5, 1)
    oled.pixel(x, 6, 1)
    oled.pixel(x, 7, 1)
    oled.pixel(x+3, 4, 1)
    oled.pixel(x+2, 4, 1)
    oled.pixel(x+1, 4, 1)
    oled.pixel(x-1, 4, 1)
    oled.pixel(x-2, 4, 1)
    oled.pixel(x-3, 4, 1)
    oled.pixel(x-1, 3, 1)
    oled.pixel(x-2, 2, 1)
    oled.pixel(x-1, 5, 1)
    oled.pixel(x-2, 6, 1)
    oled.pixel(x+1, 3, 1)
    oled.pixel(x+2, 2, 1)
    oled.pixel(x+1, 5, 1)
    oled.pixel(x+2, 6, 1)
    for i in range(8):
        oled.scroll(0, 1)
        oled.show()
        time.sleep(speed)

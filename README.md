# let_it_snow
Making a lot of snowflakes on OLED display 64x48 pixel with WEMOS D1 mini board
1. For OLED display I use driver [ssd1306](https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py) and put ssd1306 pyhon file on my board. For example:
`ampy -p COM3 put ssd1306.py`

2. Function let_it_snow is drawing one snowflake. Put let_it_snow.py on your board:
`ampy -p COM3 put let_it_snow.py`

3. Snowflakes should appear in random places on the display, we need [random](https://github.com/micropython/micropython-lib/tree/master/random) lib! Download it and put it on your board:
`ampy -p COM3 put random.py`

4. Please see an example py for example usage. Put example python file on your board or just run:
`ampy -p COM3 run example.py`

* COM3 is the serial port on my computer. COM port on your computer may be different.
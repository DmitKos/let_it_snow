# Let it snow!
Making a lot of snowflakes on OLED display 64x48 pixel with WEMOS D1 mini board.  

[![Snowflakes on OLED](https://media.giphy.com/media/NDX2VlA1EzItu9v0qD/giphy.gif)](https://www.youtube.com/watch?v=dPt2NKRdVaU)

![OLED](https://github.com/DmitKos/let_it_snow/blob/main/oled_let_it_snow_bb.png)  

## Components:  
1 × Wemos D1 mini on esp8266 board  
1 × OLED Display 64x48 pixel or 128x64 pixel  
1 × Breadboard  

## Details:
1. For OLED display I use driver [ssd1306](https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py) and put ssd1306 pyhon file on my board. For example:  
`ampy -p COM3 put ssd1306.py`

2. Function let_it_snow is drawing one snowflake. Put let_it_snow.py on your board:  
`ampy -p COM3 put let_it_snow.py`

3. Snowflakes should appear in random places on the display, we need [random](https://github.com/micropython/micropython-lib/tree/master/random) lib! Download it and put it on your board:  
`ampy -p COM3 put random.py`

4. Please see an example py for example usage. Put example python file on your board or just run:  
`ampy -p COM3 run example.py`

_COM3 is the serial port on my computer. COM port on your computer may be different._
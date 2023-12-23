
import busio
import gc
import board

import adafruit_displayio_ssd1306
import displayio
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label
import terminalio

from kmk.extensions import Extension


class OledDisplayMode:
    TXT = 0
    IMG = 1


class OledReactionType:
    STATIC = 0
    LAYER = 1


class OledData:
    def __init__(
        self,
        image=None,
        corner_one=None,
        corner_two=None,
        corner_three=None,
        corner_four=None,
        macros = None,
    ):
        self.macros = macros if macros is not None else []
        if image:
            self.data = [image]
        elif corner_one and corner_two and corner_three and corner_four:
            self.data = [corner_one, corner_two, corner_three, corner_four]
        


class Oled(Extension):
    def __init__(
        self,
        views,
        toDisplay=OledDisplayMode.TXT,
        oWidth=128,
        oHeight=32,
        flip: bool = False,
    ):
        displayio.release_displays()
        self.rotation = 180 if flip else 0
        self._views = views.data
        self._macros = views.macros
        self._toDisplay = toDisplay
        self._width = oWidth
        self._height = oHeight
        self._prevLayers = 0
## Modificated Code for Displaying Macro Labeling
        self._layerString = [
            [self.to_row_format(0, 0 , 0), self.to_row_format(0, 4 , 1), self.to_row_format(0, 8, 2)],
            [self.to_row_format(1, 0, 0), self.to_row_format(1, 4, 1), self.to_row_format(1, 8, 2)],
            [self.to_row_format(2, 0, 0), self.to_row_format(2, 4, 1), self.to_row_format(2, 8, 2)],
            [self.to_row_format(3, 0, 0), self.to_row_format(3, 4, 1), self.to_row_format(3, 8, 2)],
            [self.to_row_format(4, 0, 0), self.to_row_format(4, 4, 1), self.to_row_format(4, 8, 2)],
            [self.to_row_format(5, 0, 0), self.to_row_format(5, 4, 1), self.to_row_format(5, 8 , 2)]
        ]
            
                            
        
        gc.collect()

    def to_row_format(self, layer,index,row):
        # Funktion zum Formatieren der Strings für jede Row
        row_label = f"R{row + 1}:"
        return row_label + self._macros[layer][index + 0] +"| " + self._macros[layer][index + 1] +"| "+self._macros[layer][index + 2] +"| "+ self._macros[layer][index + 3]
    

    def returnCurrectRenderText(self, layer, singleView):
        # for now we only have static things and react to layers. But when we react to battery % and wpm we can handle the logic here
        if singleView[0] == OledReactionType.STATIC:
            return singleView[1][0]
        if singleView[0] == OledReactionType.LAYER:
            return singleView[1][layer]
    def to_text(self,layer, row):
        return self._layerString[layer][row]
                
            
    def renderOledTextLayer(self, layer):
        splash = displayio.Group()
        splash.append(
            label.Label(
                terminalio.FONT,
                text= self.returnCurrectRenderText(layer, self._views[2]) + ":"+ str(layer),
                color=0xFFFFFF,
                x=5,
                y=12,
            )
        )
        
        splash.append(
            label.Label(
                terminalio.FONT,
                text= self.to_text(layer,0),
                color=0xFFFFFF,
                x=0,
                y=24,
            )
        )
        splash.append(
            label.Label(
                terminalio.FONT,
                text=self.to_text(layer,1),
                color=0xFFFFFF,
                x=0,
                y=36,
            )
        )
        splash.append(
            label.Label(
                terminalio.FONT,
                text=self.to_text(layer,2),
                color=0xFFFFFF,
                x=0,
                y=48,
            )
        )
        self._display.show(splash)
        gc.collect()
##
    def renderOledImgLayer(self, layer):
        splash = displayio.Group()
        odb = displayio.OnDiskBitmap(
            '/' + self.returnCurrectRenderText(layer, self._views[0])
        )
        image = displayio.TileGrid(odb, pixel_shader=odb.pixel_shader)
        splash.append(image)
        self._display.show(splash)
        gc.collect()

    def updateOLED(self, sandbox):
        print(sandbox.active_layers)
        if self._toDisplay == OledDisplayMode.TXT:
            self.renderOledTextLayer(sandbox.active_layers[0])
        if self._toDisplay == OledDisplayMode.IMG:
            self.renderOledImgLayer(sandbox.active_layers[0])
        gc.collect()

    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, keyboard):
        displayio.release_displays()
        i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
        display_bus = displayio.I2CDisplay(i2c, device_address=0x3D)
        self._display = adafruit_displayio_ssd1306.SSD1306(display_bus, width =128, height=64)
        if self._toDisplay == OledDisplayMode.TXT:
            self.renderOledTextLayer(0)
        return

    def before_matrix_scan(self, sandbox):
        if sandbox.active_layers[0] != self._prevLayers:
            self._prevLayers = sandbox.active_layers[0]
            self.updateOLED(sandbox)
        return

    def after_matrix_scan(self, sandbox):

        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        return

    def on_powersave_enable(self, sandbox):
        return

    def on_powersave_disable(self, sandbox):
        return



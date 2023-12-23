
import board
import customKeys
from kmk.extensions.peg_oled_Display import Oled,OledDisplayMode,OledReactionType,OledData
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.tapdance import TapDance
from kmk.modules.mouse_keys import MouseKeys


# Keyboard-Setup
layers = Layers()
keyboard = KMKKeyboard()
encoders = EncoderHandler()
tapdance = TapDance()
tapdance.tap_time = 400
keyboard.modules = [Layers(), encoders, tapdance,MouseKeys()]
keyboard.extensions.append(MediaKeys())

keyboard.col_pins = (board.D3, board.D4, board.D5, board.D6)
keyboard.row_pins = (board.D7, board.D8, board.D9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
encoders.pins = ((board.A2, board.A1, board.A0, False), (board.SCK, board.MISO, board.MOSI, False),)
keyboard_dict = {}




POWERSHELL= simple_key_sequence([KC.LWIN(KC.X),KC.MACRO_SLEEP_MS(400),KC.I,KC.MACRO_SLEEP_MS(600)])
EXE = simple_key_sequence([KC.LWIN(KC.R),KC.MACRO_SLEEP_MS(100),KC.LWIN(KC.SPACE)])



AUSGABEHP = KC.TD(simple_key_sequence([KC.LCTRL(KC.LWIN(KC.V)),KC.MACRO_SLEEP_MS(1000),KC.DOWN,KC.DOWN,KC.ENTER,KC.ESC]),
                  simple_key_sequence([KC.LCTRL(KC.LWIN(KC.V)),KC.MACRO_SLEEP_MS(1000),KC.DOWN,KC.DOWN,KC.DOWN,KC.ENTER,KC.ESC,]),
                  simple_key_sequence([KC.LCTRL(KC.LWIN(KC.V)),KC.MACRO_SLEEP_MS(1000),KC.PGDOWN,KC.PGDOWN,KC.PGDOWN])
                  )
#Windows
keyboard_dict['WhATsapp'] = simple_key_sequence([EXE,send_string(r"C:\Users\mrlnl\Desktop\WhatsApp.lnk"),KC.ENTER,KC.LWIN(KC.SPACE)])
keyboard_dict['WOrkUpload'] = simple_key_sequence([POWERSHELL,send_string("start firefox @workupload.com@ < exit"),KC.ENTER,])
keyboard_dict['DIsCord'] = simple_key_sequence([EXE,send_string(r"C:\Users\mrlnl\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk"),KC.ENTER,KC.MACRO_SLEEP_MS(500),KC.LWIN(KC.SPACE)])
keyboard_dict['YOUtube'] = simple_key_sequence([POWERSHELL,send_string("start firefox @zoutube.com@ < exit"),KC.ENTER,])
keyboard_dict['CHAgpt'] = simple_key_sequence([POWERSHELL,send_string("start firefox @chat.openai.com@ < exit"),KC.ENTER,])
keyboard_dict['VALorant'] = simple_key_sequence([EXE,send_string(r"C:\Riot Games\Riot Client\RiotClientServices.exe"),KC.ENTER,KC.LWIN(KC.SPACE)])
keyboard_dict['SPOtify'] = KC.TD(simple_key_sequence([POWERSHELL,KC.MACRO_SLEEP_MS(1000),send_string("start spotifz < exit"),KC.ENTER]),
                simple_key_sequence([POWERSHELL,send_string("start spotifz < exit"),KC.ENTER,KC.MACRO_SLEEP_MS(4000),KC.LCTRL(KC.L),KC.MACRO_SLEEP_MS(2000),send_string("Weinachts Stimmung"),KC.MACRO_SLEEP_MS(2000),KC.TAB,KC.TAB,KC.TAB,KC.TAB,KC.TAB,KC.TAB,KC.TAB,KC.ENTER]))
keyboard_dict['GAMing'] = KC.TD(simple_key_sequence([EXE,send_string(r"C:\Users\mrlnl\Desktop\Games"),KC.LWIN(KC.SPACE),KC.ENTER]),
                                simple_key_sequence([EXE,send_string(r"C:\Users\mrlnl\Desktop\Games\RocketLeague.url"),KC.LWIN(KC.SPACE),KC.ENTER]))
keyboard_dict['MIcrosoftApps'] = KC.TD(simple_key_sequence([EXE,send_string(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"),KC.LWIN(KC.SPACE),KC.ENTER]),
                      simple_key_sequence([EXE,send_string(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"),KC.LWIN(KC.SPACE),KC.ENTER]),
                      simple_key_sequence([EXE,send_string(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk"),KC.LWIN(KC.SPACE),KC.ENTER])
                      )
keyboard_dict['OpenSCript'] = simple_key_sequence([KC.LWIN(),KC.MACRO_SLEEP_MS(1000),send_string("cmd"),KC.MACRO_SLEEP_MS(1000),KC.ENTER,KC.MACRO_SLEEP_MS(2000),KC.LWIN(KC.SPACE),send_string(r"cd C:\Users\mrlnl\Downloads"), KC.ENTER, send_string("python a.py"),KC.MACRO_SLEEP_MS(400),KC.ENTER,KC.LALT(KC.SPACE),KC.DOWN,KC.DOWN,KC.DOWN,KC.DOWN,KC.ENTER,KC.MACRO_SLEEP_MS(500),KC.LWIN(KC.SPACE)])

keyboard_dict['OFF'] = simple_key_sequence([KC.LWIN(KC.X),KC.MACRO_SLEEP_MS(500),KC.R,KC.DOWN,KC.DOWN,KC.ENTER])

keyboard_dict['HalfWIndow'] = KC.TD(simple_key_sequence([KC.LWIN(KC.RIGHT)]),
                   simple_key_sequence([KC.LWIN(KC.RIGHT),KC.MACRO_SLEEP_MS(400)
                                        ,KC.RIGHT,KC.ENTER]),
                   simple_key_sequence([KC.LWIN(KC.X),KC.MACRO_SLEEP_MS(300),KC.D]),
                   )
#Illustrator
keyboard_dict['ill_PIPette'] = simple_key_sequence([KC.I, KC.MB_LMB,KC.V])
keyboard_dict['ill_VorRGround'] = KC.TD(
                                         KC.LALT(KC.LCTRL(KC.LSHIFT(KC.V))),
                                         KC.LALT(KC.LCTRL(KC.LSHIFT(KC.R))),
                                         )
keyboard_dict['ill_ShriftToPfad'] = KC.LSHIFT(KC.LCTRL(KC.O))
keyboard_dict['ill_EXPort'] = KC.TD( simple_key_sequence([KC.MB_RMB, KC.UP,KC.ENTER]),
                    simple_key_sequence([KC.MB_RMB, KC.UP,KC.ENTER,KC.MACRO_SLEEP_MS(200),KC.ENTER]),)
#VisualStudio
keyboard_dict['git_ADD'] = simple_key_sequence([KC.LCTRL(KC.LSHIFT(KC.LALT(KC.C))),KC.MACRO_SLEEP_MS(1000),send_string("git add ."),KC.ENTER])
keyboard_dict['git_PUSh'] = simple_key_sequence([KC.LCTRL(KC.LSHIFT(KC.LALT(KC.C))),KC.MACRO_SLEEP_MS(1000),send_string("git push"),KC.ENTER])
keyboard_dict['git_PULl'] = simple_key_sequence([KC.LCTRL(KC.LSHIFT(KC.LALT(KC.C))),KC.MACRO_SLEEP_MS(1000),send_string("git pull"),KC.ENTER])
keyboard_dict['git_COMmit'] = simple_key_sequence([KC.LCTRL(KC.LSHIFT(KC.LALT(KC.C))),KC.MACRO_SLEEP_MS(1000),send_string("git commit -m @")])
keyboard_dict['CChAt'] = simple_key_sequence([KC.LCTRL(KC.C),POWERSHELL ,KC.MACRO_SLEEP_MS(300),send_string("start firefox @chat.openai.com@ < exit"),KC.ENTER,KC.MACRO_SLEEP_MS(6000),KC.LCTRL(KC.V)])
keyboard_dict['SPLitleft'] = simple_key_sequence([KC.LCTRL(KC.LSHIFT(KC.LALT(KC.G)))])
keyboard_dict['CloseALl'] = simple_key_sequence([KC.LCTRL(KC.LSHIFT(KC.LALT(KC.Q)))])
keyboard_dict['ENDpräsentation'] = simple_key_sequence([KC.LWIN(KC.R),KC.MACRO_SLEEP_MS(700),KC.LWIN(KC.SPACE),KC.MACRO_SLEEP_MS(700),send_string(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"),KC.ENTER,KC.MACRO_SLEEP_MS(5000),KC.ENTER,KC.LCTRL(KC.LALT(KC.C)),KC.LCTRL(KC.E),send_string("Danke fuer eure Aufmerksamkeit"),KC.ENTER,KC.MACRO_SLEEP_MS(1000),KC.LWIN(KC.SPACE),KC.MACRO_SLEEP_MS(800),KC.ENTER,KC.LCTRL(KC.V)])
#Fl-Studio
keyboard_dict['MIxer_On'] = KC.F9
keyboard_dict['StOpp_Sound'] = simple_key_sequence([KC.LCTRL(KC.H)])
keyboard_dict['EXPortiern'] = KC.TD(KC.LCTRL(KC.R), KC.LCTRL(KC.LSHIFT(KC.R)),KC.LCTRL(KC.LSHIFT(KC.M)))
keyboard_dict['NOTes'] = simple_key_sequence([KC.LWIN,KC.MACRO_SLEEP_MS(1000), send_string("kury"),KC.MACRO_SLEEP_MS(500),KC.ENTER])
keyboard_dict['METronom'] = KC.CTRL(KC.M)
keyboard_dict['SOLo'] = KC.S
keyboard_dict['CLOse'] = KC.F12
keyboard_dict['SWItch'] = KC.L

                                    
#Adobe Audition 
keyboard_dict['neueMUltiTracksession'] = KC.LCTRL(KC.N)
keyboard_dict['KanäleON'] = KC.LCTRL(KC.B)
keyboard_dict['AlleMarkerLöschen'] = simple_key_sequence([KC.LCTRL(KC.LALT(KC.N0))])



#Layer Steuerung
keyboard_dict['EXMatrikulation'] = simple_key_sequence([POWERSHELL,send_string("start firefox https>&&www.fh/kiel.de&fileadmin&data&multimedia&pruefungsangelegenheiten&exmatrikulation?antrag.pdf < exit"), KC.ENTER])
keyboard_dict['LayerSWitch1'] = KC.TO(1)
keyboard_dict['LayerSWitch2'] = KC.TO(2)
keyboard_dict['LayerSWitch3'] = KC.TO(3)
keyboard_dict['LayerSWitch4'] = KC.TO(4)
keyboard_dict['LayerSWitch5'] = KC.TO(5)
keyboard_dict['LayerSWitch0'] = KC.TO(0)


keyboard_dict['___'] = KC.NONE


keyboard.keymap = [
    #Windows               
    [
        keyboard_dict['GAMing'], keyboard_dict['HalfWIndow'], keyboard_dict['OFF'], keyboard_dict['LayerSWitch1'],
        keyboard_dict["WOrkUpload"], keyboard_dict['YOUtube'],keyboard_dict['WhATsapp'] , keyboard_dict['CHAgpt'],
        keyboard_dict['DIsCord'], keyboard_dict['MIcrosoftApps'], keyboard_dict['SPOtify'], keyboard_dict['OpenSCript'],
    ],
    #Illustrator
    [
        keyboard_dict['ill_PIPette'], keyboard_dict['ill_VorRGround'], keyboard_dict['ill_ShriftToPfad'], keyboard_dict['LayerSWitch2'],
        keyboard_dict['ill_EXPort'], keyboard_dict['YOUtube'], keyboard_dict['CHAgpt'], keyboard_dict['SPOtify'],
        keyboard_dict['___'], keyboard_dict['___'], keyboard_dict['___'], keyboard_dict['___'],
    ],
    #Visual Studion Code
    [
        keyboard_dict['git_ADD'], keyboard_dict['git_PUSh'], keyboard_dict['git_COMmit'], keyboard_dict['LayerSWitch3'],
        keyboard_dict['git_PULl'], keyboard_dict['CChAt'], keyboard_dict['CHAgpt'], keyboard_dict['SPOtify'],
        keyboard_dict['SPLitleft'], keyboard_dict['CloseALl'], keyboard_dict['___'], keyboard_dict['___'],
    ],
    #Photoshop
    [
       keyboard_dict['___'], keyboard_dict['___'], keyboard_dict['___'], keyboard_dict['LayerSWitch4'],
       keyboard_dict['___'], keyboard_dict['___'], keyboard_dict['___'], keyboard_dict['___'],
       keyboard_dict['___'], keyboard_dict['___'], keyboard_dict['___'], keyboard_dict['___'],
    ],
    #Fl Studio
    [
        keyboard_dict['SOLo'], keyboard_dict['METronom'], keyboard_dict['SWItch'], keyboard_dict['LayerSWitch5'],
        keyboard_dict['CLOse'],keyboard_dict['___'], keyboard_dict['___'], keyboard_dict['___'],
        keyboard_dict['EXPortiern'], keyboard_dict['NOTes'], keyboard_dict['___'], keyboard_dict['___'],
    ],
    #Adobe Audition
    [
        keyboard_dict['neueMUltiTracksession'], keyboard_dict['KanäleON'], keyboard_dict['AlleMarkerLöschen'], keyboard_dict['LayerSWitch0'],
        keyboard_dict['___'], keyboard_dict['___'], keyboard_dict['___'], keyboard_dict['___'],
        keyboard_dict['___'], keyboard_dict['NOTes'], keyboard_dict['___'], keyboard_dict['___'],   
    ],

]
encoders.map = [
    ((KC.VOLD, KC.VOLU, KC.MUTE), (KC.VOLD, KC.VOLU, AUSGABEHP)),
    ((KC.LALT(KC.MW_DOWN), KC.LALT(KC.MW_UP), KC.MUTE), (KC.LCTRL(KC.LSHIFT(KC.Y)), KC.LCTRL(KC.Y), AUSGABEHP)),
    ((KC.LALT(KC.MW_DOWN), KC.LALT(KC.MW_UP), KC.MUTE), (KC.LCTRL(KC.LSHIFT(KC.Y)), KC.LCTRL(KC.Y), AUSGABEHP)),
    ((KC.VOLD, KC.VOLU, KC.MUTE), (KC.LEFT, KC.RIGHT, AUSGABEHP )),
    ((KC.MW_UP,KC.MW_DOWN,KC.LCTRL(KC.L)), (KC.LEFT, KC.RIGHT, KC.F9)),
]

def extract_uppercase(text):
    if("___"in text):
        return text
    else:
        uppercase_letters = ''.join(filter(str.isupper, text))
        return uppercase_letters

def find_key_by_value(dictionary, search_value):
    for key, value in dictionary.items():
        if value == search_value:
            return key
    return None


def create_string_map():
    string_map = []
    
    for layer_idx, layer in enumerate(keyboard.keymap):
        layer_strings = []
        for key in layer:
            macro = find_key_by_value(keyboard_dict, key)
            if macro:
                layer_strings.append(extract_uppercase(macro))
            else:
                layer_strings.append(None)  
        string_map.append(layer_strings)
    
    return string_map

# Die String-Map erstellen
string_map = create_string_map()   


oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["layer"]},
        corner_two={0:OledReactionType.LAYER,1:["1","2","3","4"]},
        corner_three={0:OledReactionType.LAYER,1:["Windows","Illustrator","Visual Studio","Photoshop","Fl-Studio","Audition"]},
        corner_four={0:OledReactionType.LAYER,1:["qwerty","nums","shifted","leds"]},
        macros = string_map
        ),
        toDisplay=OledDisplayMode.TXT,flip=False)
keyboard.extensions.append(oled_ext) 
        


# Hauptloop
if __name__ == '__main__':
    value = string_map[1][4]  # Wert von keyboard.keymap[0][4]
    print(value)
    keyboard.go()

    


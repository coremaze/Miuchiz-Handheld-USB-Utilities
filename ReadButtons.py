from HandheldCore import Handheld
import struct
def main():
    handheld = Handheld.FindHandhelds()[0]

    buttons = ['Mute', 'Action', 'Screen Bottom Right', 'Screen Bottom Left', 'Screen Top Right',
               'Screen Top Left', 'Upside-Down', 'Upside-Up', 'Menu', 'Power', 'Right', 'Left', 'Down', 'Up' ]
    while True:
        data = handheld.ReadRamLeak()[0x3FFF: 0x4001]
        mask, = struct.unpack('<H', data)
        #print(bin(mask))
        
        print(', '.join([x for i,x in enumerate(buttons) if (not (1<<(len(buttons)-1-i)) & mask) and x]))


if __name__ == '__main__':
    main()

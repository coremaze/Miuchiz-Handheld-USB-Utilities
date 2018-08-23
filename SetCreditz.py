from HandheldCore import Handheld
import sys
import struct

def HexCodedDecimal(i):
    #Converts, for example, 2500 to 0x2500, and returns as bytes
    return struct.pack('<I', int(str(i), base=16) )
    

def main():
    if len(sys.argv) > 2:
        print('USAGE: %s <creditz>' % sys.argv[0])
        return

    handhelds = Handheld.FindHandhelds()

    if len(handhelds) == 0:
        print('No handhelds are connected.')
        return

    #Allow user to provide creditz during execution
    if len(sys.argv) == 2:
        creditz = sys.argv[1]
    else:
        creditz = input('New creditz value: ')

    #Ensure that the creditz value is a number
    try:
        creditz = int(creditz)
    except:
        print('Number of creditz needs to be an integer.')
        return

    #Operate on the first connected handheld
    handheld = handhelds[0]
    
    data = handheld.ReadPage(1, 0xFF)
    
    creditzhcd = HexCodedDecimal(creditz)
    data = list(data)
    data[0x9AA : 0x9AE] = list(creditzhcd)
    data = bytes(data)
    
    handheld.WritePage(data, 1, 0xFF)

if __name__ == '__main__':
    main()

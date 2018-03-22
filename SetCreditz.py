from HandheldCore import Handheld
import sys

def HexCodedDecimal(i, size):
    hexlist = ""
    while i > 0:
        hexlist += "%02d " % (i % 100)
        i = i//100
    hexlist = [int(x, base=16) for x in hexlist[:-1].split(" ")]
    hexlist = hexlist + ([0]*(size-len(hexlist)))
    return bytes(hexlist)

def main():
    if len(sys.argv) != 2:
        print('USAGE: %s <creditz>' % sys.argv[0])
        return
    handheld = Handheld.FindHandhelds()[0]
    data = handheld.ReadPage(1, 0xFF)
    
    creditz = int(sys.argv[1])
    creditzhcd = HexCodedDecimal(creditz, 4)
    data = list(data)
    data[0x9AA : 0x9AE] = list(creditzhcd)
    data = bytes(data)
    
    handheld.WritePage(data, 1, 0xFF)

if __name__ == '__main__':
    main()


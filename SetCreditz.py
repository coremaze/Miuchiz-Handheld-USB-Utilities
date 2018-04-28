from HandheldCore import Handheld
import sys

def HexCodedDecimal(i, size):
    hexlist = ""
    while True:
        hexlist += "%02d " % (i % 100)
        i = i//100
        if not i > 0:
            break
    hexlist = [int(x, base=16) for x in hexlist[:-1].split(" ")]
    hexlist = hexlist + ([0]*(size-len(hexlist)))
    return bytes(hexlist)

def main():
    if len(sys.argv) > 2:
        print('USAGE: %s <creditz>' % sys.argv[0])
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

        
    handhelds = Handheld.FindHandhelds()

    if len(handhelds) == 0:
        print('No handhelds are connected.')
        return

    #Operate on the first connected handheld
    handheld = handhelds[0]
    
    data = handheld.ReadPage(1, 0xFF)
    
    creditzhcd = HexCodedDecimal(creditz, 4)
    data = list(data)
    data[0x9AA : 0x9AE] = list(creditzhcd)
    data = bytes(data)
    
    handheld.WritePage(data, 1, 0xFF)

if __name__ == '__main__':
    main()


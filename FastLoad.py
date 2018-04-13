from HandheldCore import Handheld
import sys
def main():
    if len(sys.argv) != 3:
        print('USAGE: %s <Flash clone file> <Flash load file>' % sys.argv[0])
        return
    handheld = Handheld.FindHandhelds()[0]
    clone, load = sys.argv[1:3]
    
    while True:
        try:
            with open(clone, 'rb') as f:
                cloneData = f.read()
            break
        except FileNotFoundError:
            handheld.DumpFull(clone)

    with open(load, 'rb') as f:
        loadData = f.read()

    BANK_LENGTH = 1048576
    PAGE_LENGTH = 0x1000

    if len(loadData) != BANK_LENGTH * 2 and len(cloneData) != BANK_LENGTH * 2:
            raise Exception('Full handheld data should be 2097152 bytes.')

    for bank in range(2):
        for page in range(256):
            bankstart = bank * BANK_LENGTH
            pagestart = bankstart + page * PAGE_LENGTH
            pageend = bankstart + (page+1) * PAGE_LENGTH

            thisLoadData = loadData[pagestart : pageend]
            thisCloneData = cloneData[pagestart : pageend]

            if thisLoadData == thisCloneData:
                continue

            print('Writing bank %d, page %d.' % (bank, page))
            
            handheld.WritePage(thisLoadData, bank, page)

    with open(clone, 'wb') as f:
        print('Updating clone file.')
        f.write(loadData)
    
    handheld.Eject()

if __name__ == '__main__':
    main()

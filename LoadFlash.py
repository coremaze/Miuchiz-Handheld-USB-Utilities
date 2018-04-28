from HandheldCore import Handheld
import sys
import os
def main():
    if len(sys.argv) > 2:
        print('USAGE: %s <file>' % sys.argv[0])
        return

    #Allow user to provide filename during execution
    if len(sys.argv) == 2:
        inFile = sys.argv[1]
    else:
        inFile = input('Name of file to load from: ')


    if not os.path.isfile(inFile):
        print('"%s" does not exist, so it cannot be loaded.' % inFile)
        return


    handhelds = Handheld.FindHandhelds()

    if len(handhelds) == 0:
        print('No handhelds are connected.')
        return

    #Get and load to the first connected handheld
    handheld = handhelds[0]
    handheld.WriteFull(inFile)
    handheld.Eject()

if __name__ == '__main__':
    main()

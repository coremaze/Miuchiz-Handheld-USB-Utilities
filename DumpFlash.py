from HandheldCore import Handheld
import sys
def main():
    if len(sys.argv) > 2:
        print('USAGE: %s <file>' % sys.argv[0])
        return

    #Allow user to provide filename during execution
    if len(sys.argv) == 2:
        outFile = sys.argv[1]
    else:
        outFile = input('Name of file to write: ')


    handhelds = Handheld.FindHandhelds()

    if len(handhelds) == 0:
        print('No handhelds are connected.')
        return

    #Get and dump the first connected handheld
    handheld = handhelds[0]
    handheld.DumpFull(outFile)

if __name__ == '__main__':
    main()

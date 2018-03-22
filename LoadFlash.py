from HandheldCore import Handheld
import sys
def main():
    if len(sys.argv) != 2:
        print('USAGE: %s <file>' % sys.argv[0])
        return
    handheld = Handheld.FindHandhelds()[0]
    handheld.WriteFull(sys.argv[1])
    handheld.Eject()

if __name__ == '__main__':
    main()

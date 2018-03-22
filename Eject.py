from HandheldCore import Handheld

def main():
    handheld = Handheld.FindHandhelds()[0]
    handheld.Eject()

if __name__ == '__main__':
    main()

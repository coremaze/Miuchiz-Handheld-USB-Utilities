from HandheldCore import Handheld

def UndoHCD(b):
    return sum( [int(hex(e)[2:]) * 100**i for i, e in enumerate(b)])

def main():
    handheld = Handheld.FindHandhelds()[0]
    data = handheld.ReadPage(1, 0xFF)
    creditz = UndoHCD(data[0x9AA : 0x9AE])
    print(creditz)

if __name__ == '__main__':
    main()

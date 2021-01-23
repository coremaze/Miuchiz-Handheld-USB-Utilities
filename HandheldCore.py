import win32api
import math
import struct
import win32file

class Handheld():
    def __init__(self, drive):
        self.drive = drive
        if not self.IsHandheld():
            self.drive = None
        else:
            self._OpenDrive()

    @classmethod
    def FindHandhelds(self):
        #Retrieve all drives
        mask = win32api.GetLogicalDrives()

        #Convert drive mask to letters/drives
        drives = []
        for i in range(int(math.log(mask, 2))+1):
            driveExists = bool(mask & 1<<i)
            if driveExists:
                letter = chr(ord('A') + i)
                drives.append(r'\\.\%s:' % letter)

        #Make each drive into a potential handheld
        handheldCandidates = [Handheld(x) for x in drives]

        #Only get the drives which are actual handhelds
        validHandhelds = [x for x in handheldCandidates if x.IsHandheld()]

        return validHandhelds
        
            
        

    def _OpenDrive(self): #Allows for writing to the Miuchiz Device
        self.handle = win32file.CreateFile(self.drive,
                              win32file.GENERIC_READ, #dwDesiredAccess
                              win32file.FILE_SHARE_READ | win32file.FILE_SHARE_WRITE, #dwShareMode
                              None, #lpSecurityAttributes
                              win32file.OPEN_EXISTING, #dwCreationDisposition
                              win32file.FILE_FLAG_NO_BUFFERING | win32file.FILE_ATTRIBUTE_NORMAL, #dwFlagsAndAttributes
                              None) #hTemplateFile

    def _ReadSectors(self, sector, numSectors):
        sector_size = 512
        with open(self.drive, 'rb') as disk:
            disk.seek( sector * sector_size )
            data = disk.read( numSectors * sector_size )
        return data

    def _WriteSectors(self, sector, numSectors, data):
        sector_size = 512
        
        if len(data) > numSectors * sector_size:
            raise Exception('Data is too large.')
        
        with open(self.drive, 'r+b') as disk:
            disk.seek( sector * sector_size )
            data = disk.write(data)

    def _SendCodeToDrive(self, code):
        buffer = (code + [0] * 512)[:512]
        buffer = bytes(buffer)
        self._WriteSectors(0x31, 1, buffer)

    def IsHandheld(self):
        if self.drive == None:
            return False
        
        try:
            with open(self.drive, 'rb') as d:
                data = d.read(53)
        except:
            return False
        
        return data[43:53] == b'SITRONIXTM'

    def ReadPage(self, bank, page):
        self._SendCodeToDrive([0x80, 0, 0, 0, 0])
        self._SendCodeToDrive([0x28, 0, 0, bank, page])
        data = self._ReadSectors(0x58, 0x80)
        self._SendCodeToDrive([0x81, 0, 0, 0, 0])
        length, = struct.unpack('>I', data[0:4])
        data = data[4:length]
        return data

    def WritePage(self, data, bank, page):
        if len(data) != 0x1000:
            print('Data should be 0x1000 bytes long.')
            return
        self._SendCodeToDrive([0x80, 0, 0, 0, 0])
        self._SendCodeToDrive([0x2a, 0, 0, bank, page, 0, 0, 0x10, 0x00])
        self._WriteSectors(0x33, 16, data+data)
        self._SendCodeToDrive([0x81, 0, 0, 0, 0])

    def WriteFull(self, d, output=True):
        BANK_LENGTH = 1048576
        PAGE_LENGTH = 0x1000
        if type(d) == str:
            with open(d, 'rb') as f:
                d = f.read()
        elif type(d) != bytes:
            raise Exception('WriteFull takes a filename or bytes data.')

        if len(d) != BANK_LENGTH * 2:
            raise Exception('Full handheld data should be 2097152 bytes.')

        for bank in range(2):
            for page in range(256):
                bankstart = bank * BANK_LENGTH
                pagestart = bankstart + page * PAGE_LENGTH
                pageend = bankstart + (page+1) * PAGE_LENGTH
                thisData = d[pagestart : pageend]
                if output:
                    print('Writing bank %d, page %d.' % (bank, page))
                self.WritePage(thisData, bank, page)

    def DumpFull(self, filename, output=True):
        BANK_LENGTH = 1048576
        PAGE_LENGTH = 0x1000
        data = b''
        for bank in range(2):
            for page in range(256):
                if output:
                    print('Reading bank %d, page %d.' % (bank, page))
                data += self.ReadPage(bank, page)
        with open(filename, 'wb') as f:
            f.write(data)

    def Eject(self):
        try:
            self._SendCodeToDrive([0x28, 0, 0, 2, 0])
        except FileNotFoundError:
            pass

    def ReadRamLeak(self):
        #The device seems to be unintentionally leaking the contents of its RAM.
        #There may be a real way to access its RAM.
        self._SendCodeToDrive([0x80, 0, 0, 0, 0])
        self._SendCodeToDrive([0x28, 0, 0, 0, 0])
        data = self._ReadSectors(0x58, 0x80)
        self._SendCodeToDrive([0x81, 0, 0, 0, 0])
        data = data[0x2005 : 0x8000]
        return data

    def ReadOTP(self):
        #When you read from sector 0, it exposes the OTP, repeating, and
        #beginning at offset 0xBDC in the OTP.
        OTP_STARTING_OFFSET = 0xBDC

        #OTP is 16KiB, and with 512 bytes per sector, we need 32 sectors.
        data = self._ReadSectors(0, 32)

        #Put the last 0xBDC bytes at the start to correct OTP
        data = data[-OTP_STARTING_OFFSET:] + data[:-OTP_STARTING_OFFSET]

        return data

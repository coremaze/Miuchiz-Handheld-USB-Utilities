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

    #Get and dump the OTP for the first connected handheld
    handheld = handhelds[0]

    otp = handheld.ReadOTP()
    
    with open(outFile, 'wb') as f:
        f.write(otp)

    checksumLong = '%06X' % sum(otp)
    checksumShort = checksumLong[-4:]

    print('OTP checksum is %s (displayed as %s on 1.0 firmware)' % (checksumLong, checksumShort))

if __name__ == '__main__':
    main()

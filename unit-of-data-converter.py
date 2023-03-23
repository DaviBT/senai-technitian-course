

## byte to bit converter
byteQuantidy = 2
byteQuantidy = float(byteQuantidy)
BYTE_TO_BIT_MULTIPLIER = 8

def convertByteToBit(byteQuantidy , BYTE_TO_BIT_MULTIPLIER):
    bitQuantidy = byteQuantidy * BYTE_TO_BIT_MULTIPLIER
    bitQuantidy = float(bitQuantidy)
    strByteQuantidy = str(byteQuantidy)
    strBitQuantidy = str(bitQuantidy)
    return print(strByteQuantidy + " bytes " + "is equal to " + strBitQuantidy + " bites")

convertByteToBit(byteQuantidy , BYTE_TO_BIT_MULTIPLIER) ## result: 2.0 bytes is equal to 16.0 bits


## bit to byte converter
bitQuantidy = 16
bitQuantidy = float(bitQuantidy)
BIT_TO_BYTE_DIVIDER = 8

def convertBitToByte(bitQuantidy, BIT_TO_BYTE_DIVIDER):
    byteQuantidy = bitQuantidy / BIT_TO_BYTE_DIVIDER
    byteQuantidy = float(byteQuantidy)
    strBitQuantidy = str(bitQuantidy)
    strByteQuantidy = str(byteQuantidy)
    return print(strBitQuantidy + " bits " + "is equal to " + strByteQuantidy + " bytes")

convertBitToByte(bitQuantidy, BIT_TO_BYTE_DIVIDER) ## result: 16.0 bits is equal to 2.0 bytes


## byte to Kilobyte
byteQuantidy = 1024
byteQuantidy = float(byteQuantidy)
BYTE_TO_KB_DIVIDER = 1024

def convertByteToKb(byteQuantidy, BYTE_TO_KB_DIVIDER):
    KbQuantidy = byteQuantidy / BYTE_TO_KB_DIVIDER
    KbQuantidy = float(KbQuantidy)
    strByteQuantidy = str(byteQuantidy)
    strKbQuantidy = str(KbQuantidy)
    return print(strByteQuantidy + " bytes " + "is equal to " + strKbQuantidy + " Kilobytes")

convertByteToKb(byteQuantidy, BYTE_TO_KB_DIVIDER) ## result: 1024.0 bytes is equal to 1.0 Kilobytes

## Kilobyte to byte
kbQuantidy = 1
kbQuantidy = float(kbQuantidy)
KB_TO_BYTE_MULTIPLIER = 1024

def convertKbToByte(kbQuantidy, KB_TO_BYTE_MULTIPLIER):
    byteQuantidy = kbQuantidy * KB_TO_BYTE_MULTIPLIER
    byteQuantidy = float(byteQuantidy)
    strbyteQuantidy = str(byteQuantidy)
    strKbQuantidy = str(kbQuantidy)
    return print(strKbQuantidy + " Kilobyte " + "is equal to " + strbyteQuantidy + " bytes")

convertKbToByte(kbQuantidy, KB_TO_BYTE_MULTIPLIER) ## result: 1.0 Kilobyte is equal to 1024.0 bytes



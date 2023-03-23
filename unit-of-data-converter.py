

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

convertByteToBit(byteQuantidy , BYTE_TO_BIT_MULTIPLIER) ## result: 16.0 bits is equal to 2.0 bytes


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



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


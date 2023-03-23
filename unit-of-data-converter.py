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


## Kilobyte to Megabyte
kbQuantidy = 1024
kbQuantidy = float(kbQuantidy)
KB_TO_MB_DIVIDER = 1024

def convertKbToMb(kbQuantidy, KB_TO_MB_DIVIDER):
    mbQuantidy = kbQuantidy / KB_TO_MB_DIVIDER
    mbQuantidy = float(mbQuantidy)
    strMbQuantidy = str(mbQuantidy)
    strKbQuantidy = str(kbQuantidy)
    return print(strKbQuantidy + " Kilobytes " + "is equal to " + strMbQuantidy + " Megabytes")

convertKbToMb(kbQuantidy, KB_TO_MB_DIVIDER) ## result: 1024.0 Kilobytes is equal to 1.0 Megabytes


## Megabyte to Kilobyte
mbQuantidy = 1
mbQuantidy = float(mbQuantidy)
MB_TO_KB_MULTIPLIER = 1024

def convertKbToMb(mbQuantidy, MB_TO_KB_MULTIPLIER):
    kbQuantidy = mbQuantidy * MB_TO_KB_MULTIPLIER
    kbQuantidy = float(kbQuantidy)
    strKbQuantidy = str(kbQuantidy)
    strMbQuantidy = str(mbQuantidy)
    return print(strMbQuantidy + " Megabytes " + "is equal to " + strKbQuantidy + " Kilobytes")

convertKbToMb(mbQuantidy, MB_TO_KB_MULTIPLIER) ## result: 1.0 Megabytes is equal to 1024.0 Kilobytes


## Megabyte to Gigabyte
megabyteQuantidy = 1024
megabyteQuantidy = float(megabyteQuantidy)
MB_TO_GB_DIVIDER = 1024

def convertMbToGb(megabyteQuantidy, MB_TO_GB_DIVIDER):
    gigabyteQuantidy = megabyteQuantidy / MB_TO_GB_DIVIDER
    gigabyteQuantidy = float(gigabyteQuantidy)
    strGigabyteQuantidy = str(gigabyteQuantidy)
    strMegabyteQuantidy = str(megabyteQuantidy)
    return print(strMegabyteQuantidy + " Megabytes " + "is equal to " + strGigabyteQuantidy + " Gigabytes")

convertMbToGb(megabyteQuantidy, MB_TO_GB_DIVIDER) ## result: 1024.0 Megabytes is equal to 1.0 Gigabytes


## Gigabyte to Megabyte
gbQuantidy = 1
gbQuantidy = float(gbQuantidy)
GB_TO_MB_MULTIPLIER = 1024

def convertGbToMb(gbQuantidy, GB_TO_MB_MULTIPLIER):
    mbQuantidy = gbQuantidy * GB_TO_MB_MULTIPLIER
    mbQuantidy = float(mbQuantidy)
    strMbQuantidy = str(mbQuantidy)
    strGbQuantidy = str(gbQuantidy)
    return print(strGbQuantidy + " Gigabytes " + "is equal to " + strMbQuantidy + " Megabytes")

convertGbToMb(gbQuantidy, GB_TO_MB_MULTIPLIER) ## result: 1.0 Gigabytes is equal to 1024.0 Megabytes
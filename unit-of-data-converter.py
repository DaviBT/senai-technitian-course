## byte to bit converter
byteQuantidy = int(input("Enter byte: "))
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
bitQuantidy = int(input("Enter bit: "))
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
byteQuantidy = int(input("Enter byte: "))
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
kbQuantidy = int(input("Enter kilobyte: "))
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
kbQuantidy = int(input("Enter kilobyte: "))
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
mbQuantidy = int(input("Enter megabyte: "))
mbQuantidy = float(mbQuantidy)
MB_TO_KB_MULTIPLIER = 1024

def convertMbToKb(mbQuantidy, MB_TO_KB_MULTIPLIER):
    kbQuantidy = mbQuantidy * MB_TO_KB_MULTIPLIER
    kbQuantidy = float(kbQuantidy)
    strKbQuantidy = str(kbQuantidy)
    strMbQuantidy = str(mbQuantidy)
    return print(strMbQuantidy + " Megabytes " + "is equal to " + strKbQuantidy + " Kilobytes")

convertMbToKb(mbQuantidy, MB_TO_KB_MULTIPLIER) ## result: 1.0 Megabytes is equal to 1024.0 Kilobytes


## Megabyte to Gigabyte
megabyteQuantidy = int(input("Enter megabyte: "))
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
gbQuantidy = int(input("Enter gigabyte: "))
gbQuantidy = float(gbQuantidy)
GB_TO_MB_MULTIPLIER = 1024

def convertGbToMb(gbQuantidy, GB_TO_MB_MULTIPLIER):
    mbQuantidy = gbQuantidy * GB_TO_MB_MULTIPLIER
    mbQuantidy = float(mbQuantidy)
    strMbQuantidy = str(mbQuantidy)
    strGbQuantidy = str(gbQuantidy)
    return print(strGbQuantidy + " Gigabytes " + "is equal to " + strMbQuantidy + " Megabytes")

convertGbToMb(gbQuantidy, GB_TO_MB_MULTIPLIER) ## result: 1.0 Gigabytes is equal to 1024.0 Megabytes


## Gigabyte to Terabyte
gbQuantidy = int(input("Enter gigabyte: "))
gbQuantidy = float(gbQuantidy)
GB_TO_TB_DIVIDER = 1024

def convertGbToTb(gbQuantidy, GB_TO_TB_DIVIDER):
    tbQuantidy = gbQuantidy / GB_TO_TB_DIVIDER
    tbQuantidy = float(tbQuantidy)
    strTbQuantidy = str(tbQuantidy)
    strGbQuantidy = str(gbQuantidy)
    return print(strGbQuantidy + " Gigabytes " + "is equal to " + strTbQuantidy + " Terabytes")

convertGbToTb(gbQuantidy, GB_TO_TB_MULTIPLIER) ## result: 1024.0 Gigabytes is equal to 1.0 Terabytes


## Terabyte to Gigabyte
tbQuantidy = int(input("Enter terabyte: "))
tbQuantidy = float(tbQuantidy)
TB_TO_GB_MULTIPLIER = 1024

def convertTbToGb(tbQuantidy, TB_TO_GB_MULTIPLIER):
    gigabyteQuantidy = tbQuantidy * TB_TO_GB_MULTIPLIER
    gigabyteQuantidy = float(gigabyteQuantidy)
    strGigabyteQuantidy = str(gigabyteQuantidy)
    strTbQuantidy = str(tbQuantidy)
    return print(strTbQuantidy + " Terabytes " + "is equal to " + strGigabyteQuantidy + " Gigabytes")

convertTbToGb(tbQuantidy, TB_TO_GB_MULTIPLIER) ## result: 1.0 Terabytes is equal to 1024.0 Gigabytes


## Terabyte to Petabyte
tbQuantidy = int(input("Enter terabyte: "))
tbQuantidy = float(tbQuantidy)
TB_TO_PB_DIVIDER = 1024

def convertTbToPb(tbQuantidy, TB_TO_PB_DIVIDER):
    pbQuantidy = tbQuantidy / TB_TO_PB_DIVIDER
    pbQuantidy = float(pbQuantidy)
    strPbQuantidy = str(pbQuantidy)
    strTbQuantidy = str(tbQuantidy)
    return print(strTbQuantidy + " Terabytes " + "is equal to " + strPbQuantidy + " Petabytes")

convertTbToPb(tbQuantidy, TB_TO_PB_DIVIDER) ## result: 1024.0 Terabytes is equal to 1.0 Petabytes


## Petabyte to Terabyte
PbQuantidy = int(input("Enter petabyte: "))
PbQuantidy = float(PbQuantidy)
PB_TO_TB_MULTIPLIER = 1024

def convertPbToTb(PbQuantidy, PB_TO_TB_MULTIPLIER):
    tbQuantidy = PbQuantidy * PB_TO_TB_MULTIPLIER
    tbQuantidy = float(tbQuantidy)
    strTbQuantidy = str(tbQuantidy)
    strPbQuantidy = str(PbQuantidy)
    return print(strPbQuantidy + " Petabytes " + "is equal to " + strTbQuantidy + " Terabytes")

convertPbToTb(PbQuantidy, PB_TO_TB_MULTIPLIER) ## result: 1.0 Petabytes is equal to 1024.0 Terabytes
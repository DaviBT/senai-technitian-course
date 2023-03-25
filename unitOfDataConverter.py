BYTE_SIZE = 8
BYTE_FACTOR = 1024

def convertByteToBit(byte):
    print('Byte to Bit calculated')
    bit = byte * BYTE_SIZE
    return bit

def convertBitToByte(bit):
    print('Bit to Byte calculated')
    byte = bit / BYTE_SIZE
    return byte

def convertByteToKb(byte):
    print('Byte to Kb calculated')
    kb = byte / BYTE_FACTOR
    return kb

def convertKbToByte(kb):
    print('Kb to Byte calculated')
    byte = kb * BYTE_FACTOR
    return byte

def convertKbToMb(kb):
    print('Kb to mb calculated')
    mb = kb / BYTE_FACTOR
    return mb

def convertMbToKb(mb):
    print('mb to kb calculated')
    kb = mb * BYTE_FACTOR
    return kb

def convertMbToGb(mb):
    print('mb to gb calculated')
    gb = mb / BYTE_FACTOR
    return gb

def convertGbToMb(gb):
    print('gb to mb calculated')
    mb = gb * BYTE_FACTOR
    return mb 

def convertGbToTb(gb):
    print('gb to tb calculated')
    tb = gb / BYTE_FACTOR
    return tb

def convertTbToGb(tb):
    print('tb to gb calculated')
    gb = tb * BYTE_FACTOR
    return gb

def convertTbToPb(tb):
    print('tb to pb calculated')
    pb = tb / BYTE_FACTOR
    return pb

def convertPbToTb(pb):
    print('pb to tb calculated')
    tb = pb * BYTE_FACTOR
    return tb

#######################

def convertStringToFloat(value):
    print('Value converted from string to float.')
    return float(value)

print('Enter the value you want to convert: ')
inputValueToBeConverted  = convertStringToFloat(input())
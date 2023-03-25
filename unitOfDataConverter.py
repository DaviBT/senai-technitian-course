BYTE_SIZE = 8
BYTE_FACTOR = 1024

def convertByteToBit(byte):
    return byte * BYTE_SIZE

def convertBitToByte(bit):
    return bit / BYTE_SIZE

def convertByteToKb(byte):
    return byte / BYTE_FACTOR

def convertKbToByte(kb):
    return kb * BYTE_FACTOR

def convertKbToMb(kb):
    return kb / BYTE_FACTOR

def convertMbToKb(mb):
    return mb * BYTE_FACTOR

def convertMbToGb(mb):
    return mb / BYTE_FACTOR

def convertGbToMb(gb):
    return gb * BYTE_FACTOR

def convertGbToTb(gb):
    return gb / BYTE_FACTOR

def convertTbToGb(tb):
    return tb * BYTE_FACTOR

def convertTbToPb(tb):
    return tb / BYTE_FACTOR

def convertPbToTb(pb):
    return pb * BYTE_FACTOR
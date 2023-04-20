units = ["bit", "byte", "KB", "MB", "GB", "TB", "PB"]

origin = input("Enter the unit of data you want to convert (example: bit, KB, GB): ")
quantidy = input("Enter the quantity you want to convert: ")
quantidyNum = float(quantidy)
end = input("Enter the unit of data you want to get (example: byte, MB, TB): ")

BIT_FACTOR = 1024

def converterFunction(quantidyNum, origin, end):
    originNum = units.index(origin)
    endNum = units.index(end)
    factor = 1
    
    if originNum > endNum:
        factor = 1 / (BIT_FACTOR ** (originNum - endNum))
    elif originNum < endNum:
        factor = BIT_FACTOR ** (endNum - originNum)

    byteValue = quantidyNum * factor
    
    if endNum == 0:
        return byteValue * 8
    
    return byteValue / (BIT_FACTOR ** (endNum * 10))

print(converterFunction(quantidyNum, origin, end))

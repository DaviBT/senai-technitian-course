units = ["bit", "byte", "KB", "MB", "GB", "TB", "PB"]

origin = input("Enter the unit of data you want to convert (example: bit, KB, GB): ")
while origin not in units:
    origin = input("Enter a valid unit of data you want to convert (example: bit, KB, GB): ")

quantidy = input("Enter the quantidy you want to convert: ")
quantidyNum = float(quantidy)

end = input("Enter the unit of data you want to get (example: byte, MB, TB): ")
while end not in units:
    end = input("Enter a valid unit of data you want to get (example: byte, MB, TB): ")

CONVERSION_FACTOR = 1024

def converterFunction(quantidyNum, origin, end):
    for i in units:
        if i == origin:
            originNum = units.index(i)
        if i == end:
            endNum = units.index(i)

    displacement = endNum - originNum
    positiveDisplacement = abs(displacement)

    # transforming bit to byte
    if originNum == 0 and endNum == 1:
        finalQuantidy = quantidyNum / 8
        return finalQuantidy
    
    # transforming byte to bit
    if originNum == 1 and endNum == 0:
        finalQuantidy = quantidyNum * 8
        return finalQuantidy

    # transforming bit to byte to transform a bit value to any other unit
    if originNum == 0:
        byteValue = quantidyNum / 8
        for conversion in range(positiveDisplacement):
            finalQuantidy = byteValue / CONVERSION_FACTOR
        return finalQuantidy    

    ## converting any value to bit
    if endNum == 0:
        for conversion in range(positiveDisplacement):
            finalQuantidy = quantidyNum * CONVERSION_FACTOR
            finalBitQuantidy = finalQuantidy * 8
        return finalBitQuantidy    
    
    ## multiply or divide
    if displacement < 0: ## it will multiply
        for conversion in range(positiveDisplacement):
            finalQuantidy = quantidyNum * CONVERSION_FACTOR
        return finalQuantidy    
    
    elif displacement > 0: # it will divide
        for conversion in range(positiveDisplacement):
            finalQuantidy = quantidyNum / CONVERSION_FACTOR
        return finalQuantidy    
    
print(converterFunction(quantidyNum, origin, end))
units = ["bit", "byte", "KB", "MB", "GB", "TB", "PB"]

origin = input("Enter the unit of data you want to convert (example: bit, KB, GB): ")
quantidy = input("Enter the quantidy you want to convert: ")
quantidyNum = float(quantidy)
end = input("Enter the unit of data you want to get (example: byte, MB, TB): ")

BIT_FACTOR = 1024

def converterFunction(quantidyNum, origin, end):
    for u in units:
        if origin not in units:
            print('This is not a valid data!')
        if end not in units:
            print('This is not a valid data!')

    for i in units:
        if i == origin:
            originNum = units.index(i)
        if i == end:
            endNum = units.index(i)

    displacement = endNum - originNum
    positiveDisplacement = abs(displacement)

    # transforming bit to byte to transform a bit value to any other unit
    if originNum == 0:
        byteValue = quantidyNum / 8 
        finalQuantidy = byteValue / (BIT_FACTOR ** displacement)
        return finalQuantidy

    ## conveting any value to bit
    if endNum == 0:
        finalQuantidy = quantidyNum * (BIT_FACTOR ** positiveDisplacement)
        finalBitQuantidy = finalQuantidy * 8
        return finalBitQuantidy
    
    ## multiply or divide
    if displacement < 0: ## it will multiply
        for conversion in range(positiveDisplacement):
            finalQuantidy = quantidyNum * BIT_FACTOR
            return finalQuantidy
    
    elif displacement > 0: # it will divide
        for conversion in range(positiveDisplacement):
            finalQuantidy = quantidyNum / BIT_FACTOR
            return finalQuantidy
    
print(converterFunction(quantidyNum, origin, end))
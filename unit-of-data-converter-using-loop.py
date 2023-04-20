units = ["bit", "byte", "KB", "MB", "GB", "TB", "PB"]

origin = input("Enter the unit of data you want to convert (example: bit, KB, GB): ")
quantidy = input("Enter the quantidy you want to convert: ")
quantidyNum = float(quantidy)
end = input("Enter the unit of data you want to get (example: byte, MB, TB): ")

BIT_FACTOR = 1024

def converterFunction(quantidyNum, origin, end):
    for i in units:
        if i == origin:
            originNum = units.index(i)
        if i == end:
            endNum = units.index(i)

    displacement = endNum - originNum
    positiveDisplacement = abs(displacement)

    # transforming bit to byte
    if originNum == 0:
        byteValue = quantidyNum / 8 
        finalQuantidy = byteValue / (BIT_FACTOR ** displacement)
        return finalQuantidy

    ## multiply or divide
    if displacement < 0: ## it will multiply
        finalQuantidy = quantidyNum * (BIT_FACTOR ** positiveDisplacement)
        return finalQuantidy
    
    elif displacement > 0: # it will divide
        finalQuantidy = quantidyNum / (BIT_FACTOR ** displacement)
        return finalQuantidy

print(converterFunction(quantidyNum, origin, end))
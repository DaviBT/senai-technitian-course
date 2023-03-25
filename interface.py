from unitOfDataConverter import *

print('Type 1 to convert from byte to bit \n Type 2 to convert from bit to byte \n Type 3 to convert from byte to Kb \n Type 4 to convert from Kb to byte \n Type 5 to convert from Kb to Mb \n Type 6 to convert from Mb to Kb \n Type 7 to convert from Mb to Gb \n Type 8 to convert from Gb to Mb \n Type 9 to convert from Gb to Tb \n Type 10 to convert from Tb to Gb \n Type 11 to convert from Tb to Pb \n Type 12 to convert from Pb to Tb \n')

choise = input()

if (choise == '1'):
    ConvertedValue = convertByteToBit (inputValueToBeConverted)
    print (ConvertedValue)

elif (choise == '2'):
    ConvertedValue = convertBitToByte(inputValueToBeConverted)
    print (ConvertedValue)

elif (choise == '3'):
    ConvertedValue = convertByteToKb (inputValueToBeConverted)
    print (ConvertedValue)

elif (choise == '4'):
    ConvertedValue = convertKbToByte (inputValueToBeConverted)
    print (ConvertedValue)

elif (choise == '5'):
    ConvertedValue = convertKbToMb (inputValueToBeConverted)
    print (ConvertedValue)

elif (choise == '6'):
    ConvertedValue = convertMbToKb (inputValueToBeConverted)
    print (ConvertedValue)

elif (choise == '7'):
    ConvertedValue = convertMbToGb (inputValueToBeConverted)
    print (ConvertedValue)

elif (choise == '8'):
    ConvertedValue = convertGbToMb (inputValueToBeConverted)
    print (ConvertedValue)

elif (choise == '9'):
    ConvertedValue = convertGbToTb (inputValueToBeConverted)
    print (ConvertedValue)

elif (choise == '10'):
    ConvertedValue = convertTbToGb (inputValueToBeConverted)
    print (ConvertedValue)

elif (choise == '11'):
    ConvertedValue = convertTbToPb (inputValueToBeConverted)
    print (ConvertedValue)

elif (choise == '12'):
    ConvertedValue = convertPbToTb (inputValueToBeConverted)
    print (ConvertedValue)

else:
    print('Enter a value between 1 and 12!')
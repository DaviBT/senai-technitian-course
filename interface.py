from unitOfDataConverter import convertByteToBit, convertBitToByte, convertByteToKb, convertKbToByte, convertKbToMb, convertMbToKb, convertMbToGb, convertGbToMb, convertGbToTb, convertTbToGb, convertTbToPb, convertPbToTb

print(" - Write 1 for byte to bit \n - Write 2 for bit to byte - \n - write 3 for Byte to Kilobyte - \n - write 4 for Kilobyte to Byte - \n - write 5 for Kilobyte to Megabyte - \n - write 6 for Megabyte to Kilobyte - \n - write 7 for Megabyte to Gigabyte - \n - write 8 for Gigabyte to Megabyte - \n - write 9 for Gigabyte to Terabyte - \n - write 10 for Terabyte to Gigabyte - \n - write 11 for Terabyte to Petabyte - \n - write 12 for Petabyte to Terabyte -")
choise = input()
if (choise == '1'):
    convertByteToBit(byteQuantidy , BYTE_TO_BIT_MULTIPLIER)
elif (choise == '2'):
    convertBitToByte(bitQuantidy, BIT_TO_BYTE_DIVIDER)
elif (choise == '3'):
    convertByteToKb(byteQuantidy, BYTE_TO_KB_DIVIDER)
elif (choise == '4'):
    convertKbToByte(kbQuantidy, KB_TO_BYTE_MULTIPLIER)
elif (choise == '5'):
    convertKbToMb(kbQuantidy, KB_TO_MB_DIVIDER)
elif (choise == '6'):
    convertMbToKb(mbQuantidy, MB_TO_KB_MULTIPLIER)
elif (choise == '7'):
    convertMbToGb(megabyteQuantidy, MB_TO_GB_DIVIDER)
elif (choise == '8'):
    convertGbToMb(gbQuantidy, GB_TO_MB_MULTIPLIER)
elif (choise == '9'):
    convertGbToTb(gbQuantidy, GB_TO_TB_DIVIDER)
elif (choise == '10'):
    convertTbToGb(tbQuantidy, TB_TO_GB_MULTIPLIER)
elif (choise == '11'):
    convertTbToPb(tbQuantidy, TB_TO_PB_DIVIDER)
elif (choise == '11'):
    convertPbToTb(PbQuantidy, PB_TO_TB_MULTIPLIER)
else:
    print("write a number between 1 and 12!")
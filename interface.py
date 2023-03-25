from unitOfDataConverter import *

input_string = input("Enter a acronym for a unit of data: ")
def get_conversion(input_string):
    """
    Checks if string contains valid data unit conversions and returns the appropriate conversion function
    """
    # Check if the input string contains a valid conversion string
    if 'b' in input_string and 'B' in input_string:
        raise ValueError("Invalid input string. Cannot convert between bits and bytes.")
    elif 'b' in input_string:
        if 'kb' in input_string:
            return convertBitToByte, convertByteToKb
        elif 'mb' in input_string:
            return convertBitToByte, convertKbToMb
        elif 'gb' in input_string:
            return convertBitToByte, convertMbToGb
        elif 'tb' in input_string:
            return convertBitToByte, convertGbToTb
        elif 'pb' in input_string:
            return convertBitToByte, convertTbToPb
        else:
            raise ValueError("Invalid input string. Cannot determine conversion function.")
    elif 'B' in input_string:
        if 'kb' in input_string:
            return convertByteToBit, convertByteToKb
        elif 'mb' in input_string:
            return convertByteToBit, convertKbToMb
        elif 'gb' in input_string:
            return convertByteToBit, convertMbToGb
        elif 'tb' in input_string:
            return convertByteToBit, convertGbToTb
        elif 'pb' in input_string:
            return convertByteToBit, convertTbToPb
        else:
            raise ValueError("Invalid input string. Cannot determine conversion function.")
    else:
        raise ValueError("Invalid input string. Cannot determine conversion function.")
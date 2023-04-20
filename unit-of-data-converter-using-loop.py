units = ["bit", "byte", "KB","MB", "GB", "TB", "PB"]

origin = input("Enter the unit of data you want to convert (example: bit, KB, GB): ")
quantidy = input("Enter the quantidy you want to convert: ")
quantidyNum = float(quantidy)
end = input("Enter the unit of data you want to get (example: byte, MB, TB): ")

def converterFunction(quantidy, origin, end):
    origin = units.index(origin)
    end = units.index(end)
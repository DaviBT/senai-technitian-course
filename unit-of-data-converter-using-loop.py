units = ["bit", "byte", "KB", "MB", "GB", "TB", "PB"]

origin = input("Enter the unit of data you want to convert (example: bit, KB, GB): ")
quantity = input("Enter the quantity you want to convert: ")
quantityNum = float(quantity)
end = input("Enter the unit of data you want to get (example: byte, MB, TB): ")

BIT_FACTOR = 1024


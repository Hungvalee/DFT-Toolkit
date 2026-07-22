from python.parsers import OUTCARParser

parser = OUTCARParser().read("OUTCAR")
data = parser.parse()

print(data)

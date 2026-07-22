from python.parsers import DOSCARParser

dos = DOSCARParser().read("DOSCAR").parse()

print(dos)

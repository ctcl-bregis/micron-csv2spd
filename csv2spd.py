# Micron CSV to SPD
# Version 0.1.0
# Date: March 11, 2023 - March 12, 2023
# CTCL 2023

from itertools import cycle, islice
import os, csv, sys, re

def ljust(s1, s2, n):
    return f'{s1}{"".join(islice(cycle(s2), 0, n-len(s1)))}'

def printhelp():
    print("Usage: python3 csv2spd <input csv> <output bin> <memory type>")
    print("""<memory type> accepted values, not case sensitive:
- SDRAM
- DDR
- DDR2
- DDR3
- DDR4""")

def csv2spd(inpfile, outfile, memtype):
    with open(inpfile, "r") as f:
        incsv = list(csv.DictReader(f))

    # SPD sizes:
    # SDRAM - 128 Bytes
    # DDR - 128 Bytes
    # DDR2 - 256 Bytes
    # DDR3 - 256 Bytes
    # DDR4 - 512 Bytes

    # Not going to use match..case since it is a realitively new feature in Python and older versions (<3.10) do not support it. 
    memtype = memtype.lower()
    if memtype == "sdram":
        spdsize = 128
    elif memtype == "ddr":
        spdsize = 128
    elif memtype == "ddr2":
        spdsize = 256
    elif memtype == "ddr3":
        spdsize = 256
    elif memtype == "ddr4":
        spdsize = 512
    elif memtype == "ddr5":
        return "DDR5 support not implemented yet"
    else:
        return f"Invalid option: {memtype}"
    
    tmplst = []
    for i in incsv:
        # Model number is the only value in plaintext and not hexadecimal
        if memtype == "ddr4":
            if i["Byte Number"] == "329-348":
                i["Byte Value"] = i["Byte Value"].ljust(20).encode("utf-8").hex()
            elif i["Byte Number"] == "384-511":
                i["Byte Value"] = i["Byte Value"].ljust(256, "0")
        elif memtype == "ddr3" and i["Byte Number"] == "128-145":
            i["Byte Value"] = i["Byte Value"].ljust(18).encode("utf-8").hex()
        elif memtype == "ddr2" and i["Byte Number"] == "128-145":
            i["Byte Value"] = i["Byte Value"].ljust(18).encode("utf-8").hex()
        elif memtype == "ddr" and i["Byte Number"] == "73-90":
            i["Byte Value"] = i["Byte Value"].ljust(18).encode("utf-8").hex()
        elif memtype == "sdram" and i["Byte Number"] == "73-90": 
            i["Byte Value"] = i["Byte Value"].ljust(18).encode("utf-8").hex()
        tmplst.append(i)
       
    incsv = tmplst

    with open(outfile, "wb") as f:
        spdbytes = "".join([i["Byte Value"] for i in incsv])
        f.write(bytes.fromhex(spdbytes))

    return True
    
if __name__ == "__main__":
    if len(sys.argv) > 4:
        print("Too many arguments")
        printhelp()
    elif len(sys.argv) < 4:
        print("Too little arguments")
        printhelp()
    else:
        inpfile = sys.argv[1]
        outfile = sys.argv[2]
        memtype = sys.argv[3]
        
        res = csv2spd(inpfile, outfile, memtype) 
        if res != True:
            print(f"csv2spd error: {res}")
        else:
            print(f"Binary exported to {outfile}. Serial number, manufacture date, manufacture location may have to be programmed manually.")
        
        

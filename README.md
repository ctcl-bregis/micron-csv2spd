# micron-csv2spd
Converts exported CSV files from micron.com to an usable SPD binary dump for Micron Technology memory modules.

Example applications:

- Repair of corrupted SPD data
- Hardware experimentation
- Education

## Use
micron-csv2spd is a command-line utility, it is used like this:
`python3 csv2spd.py <input file> <output file> <memory type>`

The memory type field is not case sensitive. 

Examples: 

- `python3 csv2spd.py SPDDetails.csv output.bin ddr4`
- `python3 csv2spd.py SPDDetails.csv output.bin DDR3`

## Requirements
This utility has been developed on a Linux environment (Debian 11/Linux Mint 21.1, x86-64). 

Built-in packages used: csv, sys, itertools

It should run as intended on Windows, Mac, FreeBSD operating systems though untested on such platforms. 

## Licensing and Legal Info
This software is licensed under the Creative Commons Zero 1.0 Universal license.

All product names, logos, brands, trademarks and registered trademarks are property of their respective owners. All company, product and service names used are for identification purposes only. Use of these names, trademarks and brands does not imply endorsement.

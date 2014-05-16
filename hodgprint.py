# import printer
import textwrap
import linecache

hobonumber = raw_input("Please enter hobo # > ")
hobonumber = hobonumber.upper()
hoboinfo = ""

if hobonumber == "ALL":
	hoboinfo = open("hobocleaned.txt", "r")
	print hoboinfo.read()
	hoboinfo.close()
elif int(hobonumber) < 701 :
	hoboinfo = linecache.getline("hobocleaned.txt", int(hobonumber))
	print hoboinfo
else:
	print "INVALID HOBO!"

# p = printer.ThermalPrinter(serialport="/dev/ttyAMA0")

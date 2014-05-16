import printer
import textwrap
import linecache

hobonumber = raw_input("Please enter hobo # > ")
hobonumber = hobonumber.upper()
hoboinfo = ""
wrapped_text = ""
yn = ""

if hobonumber == "ALL":
	hoboinfo = open("hobocleaned.txt", "r")
	p = printer.ThermalPrinter(serialport="/dev/ttyAMA0")
	print hoboinfo.read()
	yn = raw_input("Are you sure you want a hard copy of all 700 hobo names y/n? > ")
	if yn.upper() == "Y":
		for line in hoboinfo:		
			p = printer.ThermalPrinter(serialport="/dev/ttyAMA0")
			wrapped_text = textwrap.fill(line, 32)
			p.print_text(wrapped_text)
		p.linefeed() 
		p.linefeed() 
		p.linefeed()
	else:
		print "OPERATION TERMINATED AT USER REQUEST THAT IS ALL"
elif int(hobonumber) < 701 :
	hoboinfo = linecache.getline("hobocleaned.txt", int(hobonumber))
	print hoboinfo
	p = printer.ThermalPrinter(serialport="/dev/ttyAMA0")
	wrapped_text = textwrap.fill(hoboinfo, 32)
	p.print_text(wrapped_text)
	p.linefeed() 
	p.linefeed() 
	p.linefeed()
	hoboinfo.close()
else:
	print "INVALID HOBO!"
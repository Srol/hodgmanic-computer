# This was the script I wrote to take the list of hobos from e-hobo.com 
# and clean it up. It really serves no purpose anymore, but here it 
# is anyway in all its inefficient glory

hobo = open("hobos.txt", "r")
broken = []
named = ""
hoboclean = open("hobocleaned.txt", "w")

for line in hobo:
	broken = line.split(" ")
	broken = broken[:-2]
	broken = broken[1:]
	for word in broken:
		named += word + " "
	named = named[:-1]
	hoboclean.write(str(named) + "\n")
	named = ""
	broken = []
	
hobo.close
hoboclean.close
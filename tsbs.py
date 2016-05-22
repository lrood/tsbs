import os
os.system ('clear')
all_three_empty = False
make = input("Enter a make: ")
model = input("Enter a model: ")	
year = input("Enter a year: ")

make = make.upper()
model = model.upper()


file = open("FLAT_TSBS.txt", "r", errors = "ignore")
if make == '':
	if model == '':
		if year == '':
			all_three_empty = True
			print ('Please enter some more search criteria')			
if make == '' and all_three_empty == False:
	if year == '':
		print ('Please enter some more search criteria')

if model == '' and all_three_empty == False:
	if year == '':
		print ('Please enter some more search criteria')

if make == '' and all_three_empty == False:
	if model == '':
		print ('Please enter some more search criteria')
				 
if make == "":
	for line in file:
        	x = line.split("\t")
        	if x[6] == model and x[7] == year :
            		print (x[5], x[6], x[7], x[9])

if model == "":
	for line in file:
        	x = line.split("\t")
        	if x[5] == make and x[7] == year :
            		print (x[5], x[6], x[7], x[9])

if year == "":
    	for line in file:
        	x = line.split("\t")
        	if x[5] == make and x[6] == model:
            		print (x[5], x[6], x[7], x[9])

if make != "":
	if model != "":
		if year != "":    
			for line in file:
				x = line.split("\t")
				if x[5] == make and x[6] == model and x[7] == year:
					print (x[5], x[6], x[7], x[9])
			
file.close()

__author__ = 'Finn'
#person 3 counter
seasons = [0,0,0,0]
no_of_bdays = {}
birthdayfile = open("xyz.csv").readlines()
del birthdayfile[0]
for entry in birthdayfile:
    entry = (entry[:-1])
    entry = entry.split(',')
    if int(entry[2]) not in no_of_bdays:
        no_of_bdays[int(entry[2])] = 1
    else:
        no_of_bdays[int(entry[2])] +=1
months=[(month,number) for month,number in no_of_bdays.items()]
months.sort()
months=[(month,number) for month,number in months]
print(months)
for pair in months:
	if (pair[0] < 3 or pair[0] > 11):
		seasons[0] += pair[1]
	elif (pair[0] < 6 and pair[0] >= 3):
		seasons[1] += pair[1]
	elif (pair[0] < 9 and pair[0] >= 6):
		seasons[2] += pair[1]
	elif (pair[0] <= 11 and pair[0] >= 9):
		seasons[3] += pair[1]
		
print(list(zip(["summer: ","autumn: ","winter: ","spring: "], seasons)))


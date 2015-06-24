
#person 2 chrono
months_number = {1 : 'January',
          2: 'Feburary',
          3: 'March',
          4: 'April',
          5: 'May',
          6: 'June',
          7: 'July',
          8 : 'August',
          9 : 'September',
          10: 'October',
          11: 'November',
          12: 'December'}
          
def order_birthdays(input_csv_name):
    
#    name_of_csv = input('Name of output CSV file: ')
#    if '.csv' not in name_of_csv:
#        name_of_csv += '.csv'
    birthdays = open(input_csv_name).readlines()
    birthday_name_date_month = []
    month = {'Jan': 1,
             'Feb': 2,
             'Mar': 3,
             'Apr': 4,
             'May': 5,
             'Jun': 6,
             'Jul': 7,
             'Aug': 8,
             'Sep': 9,
             'Oct': 10,
             'Nov': 11,
             'Dec': 12}
    del birthdays[0]
    for entry in birthdays:
        entry = entry.strip()
        entry = entry.split(',')
        birthday = entry[1]
        birthday_month_and_date = birthday.split('-')
        everything = (list([entry[0]]+birthday_month_and_date))
        month_int = month[everything[2]]
        everything[2] = month_int
        date = int(everything[1])
        everything[1] = date
        everything2 = list(everything)
        everything2[0] = everything[2]
        everything2[2] = everything[0]
        birthday_name_date_month.append(everything2)
    birthday_name_date_month.sort()
#    c = open(name_of_csv, 'w')
#    c.write('First Name,Day,Month\n')
    for entry in birthday_name_date_month:
        print(str(entry[2])+','+str(entry[1])+','+str(entry[0])+'\n')
 #   print(name_of_csv+' has been written.')
order_birthdays('birthdays.csv')


#person 2 end

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
months_for_next=[(month,number) for month,number in months]
months=[(months_number[month],number) for month,number in months]
for pair in months_for_next:
	if (pair[0] < 3 or pair[0] > 11):
		seasons[0] += pair[1]
	elif (pair[0] < 6 and pair[0] >= 3):
		seasons[1] += pair[1]
	elif (pair[0] < 9 and pair[0] >= 6):
		seasons[2] += pair[1]
	elif (pair[0] <= 11 and pair[0] >= 9):
		seasons[3] += pair[1]
highest = ('abc',0)
for pair in months:
    if pair[1]>highest[1]:
        highest = (pair[0],pair[1])
print('HIGHEST MONTH: ',highest[0],': ',highest[1],"people.")

seasons_list = list(zip(["summer: ","autumn: ","winter: ","spring: "], seasons))


highest_season = ('def',0)

for happy_days in seasons_list:
    if happy_days[1] > highest_season[1]:
        highest_season = happy_days
print("Highest season: ",highest_season[0],highest_season[1], "people.")
    
#end of person 3

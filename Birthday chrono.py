__author__ = 'Deep'


def order_birthdays(input_csv_name):
    print('Instructions: Place a file named birthdays.csv \ncontaining names without commas in one column\n'
          'and birthday dates in the format 01-Jan in the other.')
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
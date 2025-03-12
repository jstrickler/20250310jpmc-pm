import csv

whigs = []
with open('DATA/presidents.txt') as pres_in:
    with open('whigs.csv', 'w') as whigs_out:
        wtr = csv.writer(whigs_out, lineterminator='\n')
        for raw_line in pres_in:
            line = raw_line.rstrip()
            all_fields = line.split(':')
            if 'Whig' in raw_line:
                wtr.writerow([all_fields[2], all_fields[1], all_fields[7]])

for whig in whigs:
    print(whig)

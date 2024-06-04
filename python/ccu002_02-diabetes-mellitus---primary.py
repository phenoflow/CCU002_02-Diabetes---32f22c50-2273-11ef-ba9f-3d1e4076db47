# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"530558861000132104","system":"snomedct"},{"code":"5368009","system":"snomedct"},{"code":"735200002","system":"snomedct"},{"code":"237616002","system":"snomedct"},{"code":"81531005","system":"snomedct"},{"code":"73211009","system":"snomedct"},{"code":"44054006","system":"snomedct"},{"code":"197605007","system":"snomedct"},{"code":"267467004","system":"snomedct"},{"code":"33559001","system":"snomedct"},{"code":"335621000000101","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-diabetes-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu002_02-diabetes-mellitus---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu002_02-diabetes-mellitus---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu002_02-diabetes-mellitus---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

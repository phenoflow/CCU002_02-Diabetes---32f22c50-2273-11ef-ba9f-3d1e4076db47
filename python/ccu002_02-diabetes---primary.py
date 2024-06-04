# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"230579006","system":"snomedct"},{"code":"238983004","system":"snomedct"},{"code":"193489006","system":"snomedct"},{"code":"308106006","system":"snomedct"},{"code":"238982009","system":"snomedct"},{"code":"707221002","system":"snomedct"},{"code":"724136006","system":"snomedct"},{"code":"201723002","system":"snomedct"},{"code":"62260007","system":"snomedct"},{"code":"309426007","system":"snomedct"},{"code":"200687002","system":"snomedct"},{"code":"48951005","system":"snomedct"},{"code":"280137006","system":"snomedct"},{"code":"398140007","system":"snomedct"},{"code":"238984005","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-diabetes-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["ccu002_02-diabetes---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["ccu002_02-diabetes---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["ccu002_02-diabetes---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

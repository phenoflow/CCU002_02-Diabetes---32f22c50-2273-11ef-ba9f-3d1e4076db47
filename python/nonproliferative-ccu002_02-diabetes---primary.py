# CVD-COVID-UK consortium, William N Whiteley, et al., 2024.

import sys, csv, re

codes = [{"code":"312908007","system":"snomedct"},{"code":"408413000","system":"snomedct"},{"code":"59276001","system":"snomedct"},{"code":"193349004","system":"snomedct"},{"code":"769183005","system":"snomedct"},{"code":"769181007","system":"snomedct"},{"code":"769184004","system":"snomedct"},{"code":"769182000","system":"snomedct"},{"code":"312907002","system":"snomedct"},{"code":"408411003","system":"snomedct"},{"code":"408414006","system":"snomedct"},{"code":"408412005","system":"snomedct"},{"code":"312909004","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('ccu002_02-diabetes-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["nonproliferative-ccu002_02-diabetes---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["nonproliferative-ccu002_02-diabetes---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["nonproliferative-ccu002_02-diabetes---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

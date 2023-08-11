# Anthony Mathews, Emily Herret, Antonio Gassparrini, Tjeerd Van Staa, Ben Goldacre, Liam Smeeth, Krishnan Bhaskaran, 2023.

import sys, csv, re

codes = [{"code":"7A41400","system":"readv2"},{"code":"7A41600","system":"readv2"},{"code":"7A41900","system":"readv2"},{"code":"7A41B00","system":"readv2"},{"code":"G360.00","system":"readv2"},{"code":"G361.00","system":"readv2"},{"code":"G362.00","system":"readv2"},{"code":"G363.00","system":"readv2"},{"code":"G364.00","system":"readv2"},{"code":"G365.00","system":"readv2"},{"code":"G366.00","system":"readv2"},{"code":"G769.00","system":"readv2"},{"code":"N111.11","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cardiovascular-event-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cardiovascular-event-compression---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cardiovascular-event-compression---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cardiovascular-event-compression---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

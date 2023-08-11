# Anthony Mathews, Emily Herret, Antonio Gassparrini, Tjeerd Van Staa, Ben Goldacre, Liam Smeeth, Krishnan Bhaskaran, 2023.

import sys, csv, re

codes = [{"code":"7A42.11","system":"readv2"},{"code":"7A42011","system":"readv2"},{"code":"7A42111","system":"readv2"},{"code":"7A43.11","system":"readv2"},{"code":"7A43011","system":"readv2"},{"code":"7A43111","system":"readv2"},{"code":"7A44.11","system":"readv2"},{"code":"7A48.12","system":"readv2"},{"code":"7A49.11","system":"readv2"},{"code":"7A4A.11","system":"readv2"},{"code":"7N44500","system":"readv2"},{"code":"7NB6500","system":"readv2"},{"code":"G72y000","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cardiovascular-event-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cardiovascular-event-socommon---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cardiovascular-event-socommon---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cardiovascular-event-socommon---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

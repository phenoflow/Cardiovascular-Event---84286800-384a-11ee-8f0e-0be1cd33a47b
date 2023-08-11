# Anthony Mathews, Emily Herret, Antonio Gassparrini, Tjeerd Van Staa, Ben Goldacre, Liam Smeeth, Krishnan Bhaskaran, 2023.

import sys, csv, re

codes = [{"code":"1477","system":"readv2"},{"code":"1JA1.00","system":"readv2"},{"code":"F14..11","system":"readv2"},{"code":"G6...00","system":"readv2"},{"code":"G61..00","system":"readv2"},{"code":"G61..11","system":"readv2"},{"code":"G61..12","system":"readv2"},{"code":"G613.00","system":"readv2"},{"code":"G617.00","system":"readv2"},{"code":"G618.00","system":"readv2"},{"code":"G61z.00","system":"readv2"},{"code":"G641.00","system":"readv2"},{"code":"G641.11","system":"readv2"},{"code":"G660.00","system":"readv2"},{"code":"G661.00","system":"readv2"},{"code":"G662.00","system":"readv2"},{"code":"G664.00","system":"readv2"},{"code":"G67..00","system":"readv2"},{"code":"G671000","system":"readv2"},{"code":"G679.00","system":"readv2"},{"code":"G67y.00","system":"readv2"},{"code":"G67z.00","system":"readv2"},{"code":"G681.00","system":"readv2"},{"code":"G6y..00","system":"readv2"},{"code":"G6z..00","system":"readv2"},{"code":"Gyu6.00","system":"readv2"},{"code":"Gyu6200","system":"readv2"},{"code":"S62..00","system":"readv2"},{"code":"S62..14","system":"readv2"},{"code":"S62z.00","system":"readv2"},{"code":"S63..00","system":"readv2"},{"code":"S63z.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cardiovascular-event-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cardiovascular-event-cereb---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cardiovascular-event-cereb---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cardiovascular-event-cereb---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

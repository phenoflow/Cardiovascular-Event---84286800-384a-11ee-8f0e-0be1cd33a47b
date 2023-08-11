# Anthony Mathews, Emily Herret, Antonio Gassparrini, Tjeerd Van Staa, Ben Goldacre, Liam Smeeth, Krishnan Bhaskaran, 2023.

import sys, csv, re

codes = [{"code":"5513","system":"readv2"},{"code":"5C10.00","system":"readv2"},{"code":"7A2..00","system":"readv2"},{"code":"7A20.00","system":"readv2"},{"code":"7A20000","system":"readv2"},{"code":"7A20100","system":"readv2"},{"code":"7A20200","system":"readv2"},{"code":"7A20300","system":"readv2"},{"code":"7A20311","system":"readv2"},{"code":"7A20400","system":"readv2"},{"code":"7A20700","system":"readv2"},{"code":"7A20y00","system":"readv2"},{"code":"7A20z00","system":"readv2"},{"code":"7A21.00","system":"readv2"},{"code":"7A21000","system":"readv2"},{"code":"7A21200","system":"readv2"},{"code":"7A21y00","system":"readv2"},{"code":"7A21z00","system":"readv2"},{"code":"7A22.00","system":"readv2"},{"code":"7A22000","system":"readv2"},{"code":"7A22200","system":"readv2"},{"code":"7A22300","system":"readv2"},{"code":"7A22y00","system":"readv2"},{"code":"7A22z00","system":"readv2"},{"code":"7N44000","system":"readv2"},{"code":"7N44L00","system":"readv2"},{"code":"7N48200","system":"readv2"},{"code":"7NB6400","system":"readv2"},{"code":"7NBC.00","system":"readv2"},{"code":"G601.00","system":"readv2"},{"code":"G631.12","system":"readv2"},{"code":"G673200","system":"readv2"},{"code":"G70y011","system":"readv2"},{"code":"G72y100","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cardiovascular-event-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cardiovascular-event-carot---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cardiovascular-event-carot---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cardiovascular-event-carot---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

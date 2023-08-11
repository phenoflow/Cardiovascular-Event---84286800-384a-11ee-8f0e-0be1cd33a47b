# Anthony Mathews, Emily Herret, Antonio Gassparrini, Tjeerd Van Staa, Ben Goldacre, Liam Smeeth, Krishnan Bhaskaran, 2023.

import sys, csv, re

codes = [{"code":"7A12000","system":"readv2"},{"code":"7A12100","system":"readv2"},{"code":"7A4..00","system":"readv2"},{"code":"7A41100","system":"readv2"},{"code":"7A41211","system":"readv2"},{"code":"7A41311","system":"readv2"},{"code":"7A47.00","system":"readv2"},{"code":"7A47.13","system":"readv2"},{"code":"7A47.15","system":"readv2"},{"code":"7A47.16","system":"readv2"},{"code":"7A47y00","system":"readv2"},{"code":"7A47z00","system":"readv2"},{"code":"7A48.00","system":"readv2"},{"code":"7A48.11","system":"readv2"},{"code":"7A48.14","system":"readv2"},{"code":"7A48.16","system":"readv2"},{"code":"7A48800","system":"readv2"},{"code":"7A48A00","system":"readv2"},{"code":"7A48D00","system":"readv2"},{"code":"7A48E00","system":"readv2"},{"code":"7A48y00","system":"readv2"},{"code":"7A48z00","system":"readv2"},{"code":"7A49.00","system":"readv2"},{"code":"7A49.13","system":"readv2"},{"code":"7A49.15","system":"readv2"},{"code":"7A49000","system":"readv2"},{"code":"7A49200","system":"readv2"},{"code":"7A49400","system":"readv2"},{"code":"7A49600","system":"readv2"},{"code":"7A49800","system":"readv2"},{"code":"7A49y00","system":"readv2"},{"code":"7A49z00","system":"readv2"},{"code":"7A4A.00","system":"readv2"},{"code":"7A4A.14","system":"readv2"},{"code":"7A4A000","system":"readv2"},{"code":"7A4A200","system":"readv2"},{"code":"7A4A212","system":"readv2"},{"code":"7A4Ay00","system":"readv2"},{"code":"7A4Az00","system":"readv2"},{"code":"7A4B.00","system":"readv2"},{"code":"7A4B.13","system":"readv2"},{"code":"7A4B.15","system":"readv2"},{"code":"7A4By00","system":"readv2"},{"code":"7A4Bz00","system":"readv2"},{"code":"7A4y.00","system":"readv2"},{"code":"7A4z.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cardiovascular-event-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["femorofemoral-cardiovascular-event---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["femorofemoral-cardiovascular-event---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["femorofemoral-cardiovascular-event---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

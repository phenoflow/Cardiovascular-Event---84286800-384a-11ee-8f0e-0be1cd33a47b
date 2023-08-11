# Anthony Mathews, Emily Herret, Antonio Gassparrini, Tjeerd Van Staa, Ben Goldacre, Liam Smeeth, Krishnan Bhaskaran, 2023.

import sys, csv, re

codes = [{"code":"7A12300","system":"readv2"},{"code":"7A41.00","system":"readv2"},{"code":"7A41y00","system":"readv2"},{"code":"7A41z00","system":"readv2"},{"code":"7A42.00","system":"readv2"},{"code":"7A42000","system":"readv2"},{"code":"7A42012","system":"readv2"},{"code":"7A42100","system":"readv2"},{"code":"7A42y00","system":"readv2"},{"code":"7A42z00","system":"readv2"},{"code":"7A43.00","system":"readv2"},{"code":"7A43000","system":"readv2"},{"code":"7A43100","system":"readv2"},{"code":"7A43y00","system":"readv2"},{"code":"7A43z00","system":"readv2"},{"code":"7A44.00","system":"readv2"},{"code":"7A44y00","system":"readv2"},{"code":"7A44z00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cardiovascular-event-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cardiovascular-event-aortouniiliac---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cardiovascular-event-aortouniiliac---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cardiovascular-event-aortouniiliac---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

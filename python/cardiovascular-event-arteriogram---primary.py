# Anthony Mathews, Emily Herret, Antonio Gassparrini, Tjeerd Van Staa, Ben Goldacre, Liam Smeeth, Krishnan Bhaskaran, 2023.

import sys, csv, re

codes = [{"code":"5593","system":"readv2"},{"code":"55A2.00","system":"readv2"},{"code":"7A41000","system":"readv2"},{"code":"7A41200","system":"readv2"},{"code":"7A41300","system":"readv2"},{"code":"7A41C00","system":"readv2"},{"code":"7A47.11","system":"readv2"},{"code":"7A47000","system":"readv2"},{"code":"7A47100","system":"readv2"},{"code":"7A47200","system":"readv2"},{"code":"7A47300","system":"readv2"},{"code":"7A47400","system":"readv2"},{"code":"7A47600","system":"readv2"},{"code":"7A47700","system":"readv2"},{"code":"7A47B00","system":"readv2"},{"code":"7A47C00","system":"readv2"},{"code":"7A47D00","system":"readv2"},{"code":"7A48000","system":"readv2"},{"code":"7A48200","system":"readv2"},{"code":"7A48400","system":"readv2"},{"code":"7A48600","system":"readv2"},{"code":"7A48B00","system":"readv2"},{"code":"7A48C00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cardiovascular-event-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cardiovascular-event-arteriogram---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cardiovascular-event-arteriogram---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cardiovascular-event-arteriogram---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

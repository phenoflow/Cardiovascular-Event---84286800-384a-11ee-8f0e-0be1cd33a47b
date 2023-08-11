# Anthony Mathews, Emily Herret, Antonio Gassparrini, Tjeerd Van Staa, Ben Goldacre, Liam Smeeth, Krishnan Bhaskaran, 2023.

import sys, csv, re

codes = [{"code":"3233","system":"readv2"},{"code":"3234","system":"readv2"},{"code":"3235","system":"readv2"},{"code":"G300.00","system":"readv2"},{"code":"G301000","system":"readv2"},{"code":"G301100","system":"readv2"},{"code":"G302.00","system":"readv2"},{"code":"G303.00","system":"readv2"},{"code":"G307.00","system":"readv2"},{"code":"G307000","system":"readv2"},{"code":"G309.00","system":"readv2"},{"code":"G30y000","system":"readv2"},{"code":"G30y100","system":"readv2"},{"code":"G30y200","system":"readv2"},{"code":"G311.00","system":"readv2"},{"code":"G311.12","system":"readv2"},{"code":"G311z00","system":"readv2"},{"code":"G33z500","system":"readv2"},{"code":"G501.00","system":"readv2"},{"code":"G64..12","system":"readv2"},{"code":"G640000","system":"readv2"},{"code":"G641000","system":"readv2"},{"code":"G64z.00","system":"readv2"},{"code":"G64z.12","system":"readv2"},{"code":"G64z200","system":"readv2"},{"code":"G64z300","system":"readv2"},{"code":"G683.00","system":"readv2"},{"code":"G68X.00","system":"readv2"},{"code":"Gyu6400","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cardiovascular-event-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cardiovascular-event-preinfarction---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cardiovascular-event-preinfarction---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cardiovascular-event-preinfarction---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

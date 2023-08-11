# Anthony Mathews, Emily Herret, Antonio Gassparrini, Tjeerd Van Staa, Ben Goldacre, Liam Smeeth, Krishnan Bhaskaran, 2023.

import sys, csv, re

codes = [{"code":"5562","system":"readv2"},{"code":"7A11211","system":"readv2"},{"code":"7A11311","system":"readv2"},{"code":"7A13400","system":"readv2"},{"code":"7A13411","system":"readv2"},{"code":"7A14400","system":"readv2"},{"code":"7A14411","system":"readv2"},{"code":"7A1B000","system":"readv2"},{"code":"7A1B800","system":"readv2"},{"code":"7A1C000","system":"readv2"},{"code":"G713.00","system":"readv2"},{"code":"G713.11","system":"readv2"},{"code":"G714.00","system":"readv2"},{"code":"G714.11","system":"readv2"},{"code":"G715000","system":"readv2"},{"code":"G716000","system":"readv2"},{"code":"G718.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cardiovascular-event-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["thoracoabdominal-cardiovascular-event---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["thoracoabdominal-cardiovascular-event---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["thoracoabdominal-cardiovascular-event---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

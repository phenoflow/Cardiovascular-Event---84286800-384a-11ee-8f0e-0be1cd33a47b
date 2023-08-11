# Anthony Mathews, Emily Herret, Antonio Gassparrini, Tjeerd Van Staa, Ben Goldacre, Liam Smeeth, Krishnan Bhaskaran, 2023.

import sys, csv, re

codes = [{"code":"14AE.00","system":"readv2"},{"code":"7A11.00","system":"readv2"},{"code":"7A11000","system":"readv2"},{"code":"7A11100","system":"readv2"},{"code":"7A11200","system":"readv2"},{"code":"7A11300","system":"readv2"},{"code":"7A11y00","system":"readv2"},{"code":"7A11z00","system":"readv2"},{"code":"7A13.00","system":"readv2"},{"code":"7A13.11","system":"readv2"},{"code":"7A13300","system":"readv2"},{"code":"7A13y00","system":"readv2"},{"code":"7A13z00","system":"readv2"},{"code":"7A14.00","system":"readv2"},{"code":"7A14.11","system":"readv2"},{"code":"7A14200","system":"readv2"},{"code":"7A14300","system":"readv2"},{"code":"7A14y00","system":"readv2"},{"code":"7A14z00","system":"readv2"},{"code":"7A19400","system":"readv2"},{"code":"7A1B.00","system":"readv2"},{"code":"7A1B100","system":"readv2"},{"code":"7A1B500","system":"readv2"},{"code":"7A1B700","system":"readv2"},{"code":"7A1BD00","system":"readv2"},{"code":"7A1Bz00","system":"readv2"},{"code":"7A1C.00","system":"readv2"},{"code":"7A1C100","system":"readv2"},{"code":"7A40.00","system":"readv2"},{"code":"7A40000","system":"readv2"},{"code":"7A40z00","system":"readv2"},{"code":"7A43200","system":"readv2"},{"code":"7A45.00","system":"readv2"},{"code":"7A45.14","system":"readv2"},{"code":"7A45.15","system":"readv2"},{"code":"7A45000","system":"readv2"},{"code":"7A45200","system":"readv2"},{"code":"7A45700","system":"readv2"},{"code":"7A45D00","system":"readv2"},{"code":"7A46.00","system":"readv2"},{"code":"7A46.11","system":"readv2"},{"code":"7A46.14","system":"readv2"},{"code":"7A46000","system":"readv2"},{"code":"7A46100","system":"readv2"},{"code":"7A46300","system":"readv2"},{"code":"7A46C00","system":"readv2"},{"code":"7A46D00","system":"readv2"},{"code":"7A46y00","system":"readv2"},{"code":"7A46z00","system":"readv2"},{"code":"7A4A400","system":"readv2"},{"code":"7A4A500","system":"readv2"},{"code":"G71..00","system":"readv2"},{"code":"G714000","system":"readv2"},{"code":"G71z.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('cardiovascular-event-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["cardiovascular-event-aneury---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["cardiovascular-event-aneury---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["cardiovascular-event-aneury---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

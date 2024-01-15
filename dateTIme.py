import csv
from datetime import datetime, timezone, timedelta

import csv
from datetime import datetime, timezone

def convert_datetime(input_str):
    input_datetime = datetime.strptime(input_str, '%Y-%m-%dT%H:%M:%S.%fZ')

    output_str = input_datetime.replace(tzinfo=timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

    return output_str

# Read CSV file
input_file = 'CSV-ji/TCX/datotekeTCX.csv'
output_file = 'CSV-ji/TCX/datotekeTCX_real.csv'

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames


    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    # Convert datetime format and write rows
    for row in reader:
        for row in reader:
            row['zacetekAktivnosti'] = convert_datetime(row['zacetekAktivnosti'])
            writer.writerow(row)
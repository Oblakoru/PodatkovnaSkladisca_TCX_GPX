import csv
from datetime import datetime, timezone, timedelta


# def parse_custom_datetime(datetime_str):
#     # Custom function to parse datetime strings with time zone information
#     parts = datetime_str.split("(")[1].split(")")[0].split(", ")
#
#     # Extract the time zone offset string
#     tz_offset_str = parts[-1]
#
#     # Handle the case where the time zone offset includes non-numeric characters
#     try:
#         hours_offset = int(tz_offset_str[-5:-3]) * int(tz_offset_str[-3] + '1')
#     except ValueError:
#         hours_offset = 0
#
#     return datetime(*map(int, parts[:-1]), tzinfo=timezone(timedelta(hours=hours_offset)))
#
#
# input_file = 'CSV-ji/GPX/combined_file_GPX.csv'
# output_file = 'CSV-ji/GPX/datotekeGPX.csv'
#
# with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
#     reader = csv.DictReader(infile)
#     fieldnames = reader.fieldnames
#
#     # Write header
#     writer = csv.DictWriter(outfile, fieldnames=fieldnames)
#     writer.writeheader()
#
#     # Convert datetime format and write rows
#     for row in reader:
#         row['zacetekAktivnosti'] = parse_custom_datetime(row['zacetekAktivnosti']).strftime('%Y-%m-%d %H:%M:%S %Z')
#         writer.writerow(row)
#
# print(f'Datetime format conversion completed. Output saved to {output_file}')


import csv
from datetime import datetime, timezone

def convert_datetime(input_str):
    # Convert the input string to a datetime object
    input_datetime = datetime.strptime(input_str, '%Y-%m-%dT%H:%M:%S.%fZ')

    # Convert the datetime object to the desired format
    output_str = input_datetime.replace(tzinfo=timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

    return output_str

# Read CSV file
input_file = 'CSV-ji/TCX/datotekeTCX.csv'
output_file = 'CSV-ji/TCX/datotekeTCX_real.csv'

with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    # Write header
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    # Convert datetime format and write rows
    for row in reader:
        for row in reader:
            row['zacetekAktivnosti'] = convert_datetime(row['zacetekAktivnosti'])
            writer.writerow(row)
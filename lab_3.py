# CIS-117 LAB3
# Robinson Garcia
'''
The purpose of this lab is to write a Python script that reads the data from a CSV file containing information on countries
and then split the countries by region generating one file per region. In addition, incorporate exception handling (try/except) to the script. 
'''



import csv #import csv module


def split_countries_by_region(csv_filename):
    regions_data = {}
    try:
        with open('country_full.csv', newline='') as csv_file: # open and read data from country_full.csv
            reader = csv.reader(csv_file)
            next(reader)  # Skip the header row
            for row in reader:
                
                if len(row) >= 2:
                    country_name = row[0]
                    region = row[5]
                    if region not in regions_data:
                        regions_data[region] = []
                    regions_data[region].append([country_name, region])
    except (IOError, FileNotFoundError, PermissionError) as e:
        print(f"An error occurred while reading the input file: {e}")
        return
    #print(regions_data) # print test for region_data if country and region are stored

    for region, countries in regions_data.items():
        output_filename = f"{region.replace(' ', '_')}.csv"
        try:
            with open(output_filename, mode='w', newline='') as outfile: # write data
                writer = csv.writer(outfile)
                writer.writerow(['Country', 'Region'])
                writer.writerows(countries)
            print(f"Successfully created file: {output_filename}")
        except (IOError, PermissionError) as e:
            print(f"An error occurred while writing to file {output_filename}: {e}")


split_countries_by_region('country_full.csv')
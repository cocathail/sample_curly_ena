#!/usr/bin/python

import requests
import argparse

parser = argparse.ArgumentParser(description='ENA portal api curl query tool')

parser.add_argument('-i',
                    '--input_file',
                    help="Line separated list of input accessions",
                    type=str,
                    required=True)

parser.add_argument('-it',
                    '--input_type',
                    help="Accession type of inputs e.g. sample or run",
                    type=str,
                    required=True)

parser.add_argument('-qt',
                    '--query_type',
                    help="Accession type of query e.g. sample or run. This should be different to your input type",
                    type=str,
                    required=True)

args = parser.parse_args()

def query_api(infile, input_t, query_t):
    with open(infile, 'r') as in_file:
        sample_list = []
        for line in in_file:
            line = line.strip('\n')
            sample_list.append(line)
        string1 = "%2C"
        new_sample_list = [x + string1 for x in sample_list]
        full_query = ''.join(new_sample_list)
        size = len(full_query)
        final_query = full_query[:size - 3]
    
        print("Querying....")

        url = "https://www.ebi.ac.uk/ena/portal/api/search"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'result': f'{query_t}', 'includeAccessionType': f'{input_t}', 'includeAccessions':str(final_query), 'fields': 'description%2Ccountry', 'format': 'tsv'}

        r = requests.post(url, data=payload, headers=headers)
        results = r.text
        return results

if __name__ == '__main__':
    for_writing = query_api(args.input_file, args.input_type, args.query_type)
    with open('output.txt', 'w', encoding="utf-8") as out_file:
        out_file.write(for_writing)
    print("Done")
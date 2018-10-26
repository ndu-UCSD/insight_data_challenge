#!/usr/bin/env python

__author__ = "Niu Du"
__email__ = "jiyin.dna@gmail.com"


import argparse,csv

def correct_name(name,name_list):
    # Correct item name if no match found
    return [x for x in name_list if name in x][0]

def top_counter(inputfile,item_name,count_n = 10):
    # This function take input file and count top n of selected item
    with open(inputfile,'r') as f:
        spamreader = csv.reader(f, delimiter=';')
        # Read header and get index number of traget parameters
        header = next(spamreader, None)
        try:
            idx_decision = header.index('STATUS')
        except ValueError:
            idx_decision = header.index(correct_name('STATUS',header))
        try:
            idx_item = header.index(item_name)
        except ValueError:
            idx_item =header.index(correct_name(item_name,header))
        # Extract data for traget parameters from the csv file
        # Getting data for only certified cases
        item_list = [row[idx_item] for row in spamreader if row[idx_decision]=='CERTIFIED']
        item_set = list(set(item_list))

        # Create and sort count dictonaries for occupations and states that are successful cases
        dict_item = dict(zip(item_set,[item_list.count(occupation) for occupation in item_set]))
        dict_item = dict(sorted(dict_item.items(), key=lambda x: x[0],reverse = False))
        dict_item = dict(sorted(dict_item.items(), key=lambda x: x[1],reverse = True))

        # Get top n counts and compute percentile
        item_top_counts = list(dict_item.values())[:int(count_n)]
        item_top_names = list(dict_item.keys())[:int(count_n)]
        item_top_percentile = ['%.1f%%'%(dict_item[x]*100/len(item_list)) for x in item_top_names]

    return item_top_names,item_top_counts,item_top_percentile


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputfile', type=str)
    parser.add_argument('-n', '--top_n_counts', type=str, default = 10, help = 'Top_n_values_to_count')
    parser.add_argument('-o', '--outputfile',nargs='*', type=str)
    opts = parser.parse_args()

    input_file = opts.inputfile
    count_n = opts.top_n_counts
    dict_new_name = dict(zip(['SOC_NAME','WORKSITE_STATE'],['TOP_OCCUPATIONS','TOP_STATES']))
    output_files = opts.outputfile

    for item_name,output_file in zip(['SOC_NAME','WORKSITE_STATE'],output_files):
        item_top_names,item_top_counts,item_top_percentile = top_counter(input_file,item_name,count_n = count_n)

        with open(output_file,'w', newline='') as output_csv:
            spamwriter = csv.writer(output_csv,delimiter = ';')
            spamwriter.writerow([str(dict_new_name[item_name]),'NUMBER_CERTIFIED_APPLICATIONS','PERCENTAGE'])
            for line,item in enumerate(item_top_names):
                spamwriter.writerow([item,item_top_counts[line],item_top_percentile[line]])

if __name__ == "__main__":
    main()

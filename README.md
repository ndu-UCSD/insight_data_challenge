# insight_data_challenge
# Table of Contents
1. [Problem](README.md#Problem)
2. [Approach](README.md#approach)
3. [Instructions](README.md#instructions)
 

# Problem
Load in H1B immigration data in a semicolon-separated csv file and calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications. Export results into two semicolon- separated txt files.

# Approach
Open csv file. For each feature (occupation or state), compute top 10 counts and get 'TOP\_FEATURE', 'NUMBER_CERTIFIED\_APPLICATIONS' and 'PERCENTAGE' values via function ***top\_counter***, and write results into coresponding txt files. 

### Function ***top_counter***: 
Read first row (header line) as list, find index number for target feature, then iterate the rows below and append coresponding data to a list based on the index number. Once finished, count the number of each unique element in the list, and create a dictionary combining element name and its frequency counts. The generated dictionary is then sorted from high counts to low counts, and the name, counts and count percentage of the top n elements are returned.

# Instruction
To run the script, type in command line

```
usr$ python h1b_counting.py -i <input_file_path_and_name> -n top_n_element_to_export -o <output_file1> <output_file2> 
```

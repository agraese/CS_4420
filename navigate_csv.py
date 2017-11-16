import csv
import os, sys
import argparse


def main():

    in_file = 'Lost__found__adoptable_pets.csv'
    csvfile = open(in_file)
    lines = csvfile.readlines()

    clean_rows = []
    for row in lines:
        if row[0] == '"':
            continue
        clean_row = row.strip()
        fields = clean_row.split(',')
        if len(fields) < 15:
            continue
        clean_rows += [fields]

    for row in clean_rows:
        print(row)

    in_file2 = 'Animal_Breed_Index.csv'
    breedfile = open(in_file2)
    breed_file_lines = breedfile.readlines()

    breed_index = 0
    for i in range(len(clean_rows[0])):
        if clean_rows[0][i] == "Animal_Breed":
            breed_index = i
            print("found breed index")
    
    for row in clean_rows:
        breed = row[breed_index]
        for breed in breed_file_lines:
            breed_string = breed.split(',')[1]
            index = breed.split(',')[0]
            if breed_string == breed:
                row[breed_index] = index

    print(clean_rows)
    


if __name__ == "__main__":
    main()
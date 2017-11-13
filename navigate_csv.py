import csv
import os, sys
import argparse


def main():

    in_file = 'Lost__found__adoptable_pets.csv'
    csvfile = open(in_file)
    lines = csvfile.readlines()

    for row in lines:
        fields = row.split(',')
        print(fields)

if __name__ == "__main__":
    main()
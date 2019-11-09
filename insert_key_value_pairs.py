import binary_tree as bt
import sys

sys.path.insert(1,"hash-tables-ocmadin")
sys.path.insert(1,"avl_tree")
import hash_functions
import hash_tables
import avl
import time
import argparse
import numpy as np

def import_data(sorted_data_file,unsorted_data_file):
    with open(sorted_data_file) as f:
        sorted_data = f.readlines()
        sorted_data = [x.strip() for x in sorted_data]
    with open(unsorted_data_file) as f:
        unsorted_data = f.readlines()
        unsorted_data = [x.strip() for x in unsorted_data]
    return sorted_data, unsorted_data

def parse_args():
    parser = argparse.ArgumentParser(description = 'Data structure to use')
    parser.add_argument('--data_structure', type = str, help = " 'hash','avl','tree',", required = True)
    arg = parser.parse_args()
    return arg

def time_insert_sorted(arg,sorted_data):
    if arg == 'hash':
        table = hash_tables.LinearProbe(100000,hash_functions.h_rolling)
        t0=time.time()
        
        for i in range(len(sorted_data)):
            table.add(sorted_data[i][0],sorted_data[i][1])
        t1 = time.time()
        elapsed_sorted_insert = t1-t0
    
    if arg == 'tree':
        root = None
        t0=time.time()
        for i in range(len(sorted_data)):
            bt.insert(root,int(sorted_data[i][0]),sorted_data[i][1])
        t1=time.time()
        elapsed_sorted_insert = t1-t0
    return elapsed_sorted_insert,elapsed_sorted_search
    
def time_unsorted(arg,unsorted_data):
    if arg == 'hash':
        table = hash_tables.LinearProbe(100000,hash_functions.h_rolling)
        t0=time.time()
        for i in range(len(unsorted_data)):
            table.add(unsorted_data[i][0],unsorted_data[i][1])
        t1 = time.time()
        elapsed_unsorted_insert = t1-t0
    if arg == 'tree':
        root = None
        t0=time.time()
        for i in range(len(unsorted_data)):
            bt.insert(root,int(unsorted_data[i][0]),unsorted_data[i][1])
        t1=time.time()
        elapsed_unsorted_insert = t1-t0
    return elapsed_unsorted_insert

    


def main():
    sorted_data,unsorted_data=import_data('sorted_data.txt','unsorted_data.txt')

    arg = parse_args()
    elapsed_sorted_insert,elapsed_sorted_search = time_insert_sorted(arg.data_structure,sorted_data)
    elapsed_unsorted_insert = time_insert_sorted(arg.data_structure,unsorted_data)
    print('Sorted Insert: ', elapsed_sorted_insert)
    print('Unsorted Insert: ', elapsed_unsorted_insert)
    print('Sorted Search: ', elapsed_sorted_search)    
if __name__ == '__main__':
    main()
    

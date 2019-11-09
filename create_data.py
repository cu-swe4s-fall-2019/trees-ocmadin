#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 22:48:48 2019

@author: owenmadin
"""

import sys
import numpy as np
import string
import random

def create_rand_data(num_values,key_range=1000000):
    keys = np.random.choice(key_range,num_values,replace=False)
    random_vals = []
    for i in range(num_values):
        random_vals.append(''.join([random.choice(string.ascii_letters
                 + string.digits) for n in range(32)]))
    file = open('unsorted_data.txt','w')
    for i in range(num_values):
        file.write(str(keys[i])+', '+random_vals[i]+'\n')
    file.close()

def create_sorted_data(num_values,key_range=1000000):
    keys = np.random.choice(key_range,num_values,replace=False)
    random_vals = []
    for i in range(num_values):
        random_vals.append(''.join([random.choice(string.ascii_letters
                 + string.digits) for n in range(32)]))
    sorted_keys = sorted(keys)
    file = open('sorted_data.txt','w')
    for i in range(num_values):
        file.write(str(sorted_keys[i])+', '+random_vals[i]+'\n')
    file.close()


def main():
    create_rand_data(10000)
    create_sorted_data(10000)
    
if __name__ == '__main__':
    main()
    
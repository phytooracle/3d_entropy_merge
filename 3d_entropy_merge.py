#!/usr/bin/env python3
"""
Author : Emmanuel Gonzalez
Date   : 2021-12-05
Purpose: 3D features merge
"""

import argparse
import os
import sys
import glob
import pandas as pd


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='3D features merge',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i',
                        '--input_dir',
                        help='Directory containing individual plant subdirectories.',
                        metavar='str',
                        type=str,
                        default='individual_plants_out/combined_pointclouds')

    parser.add_argument('-o',
                        '--output_dir',
                        help='Output directory to save merged CSV.',
                        metavar='str',
                        type=str,
                        required=True)

    parser.add_argument('-f',
                        '--file_name',
                        help='CSV output filename.',
                        metavar='str',
                        type=str,
                        required=True)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    df = pd.concat([pd.read_csv(csv) for csv in glob.glob(os.path.join(args.input_dir, '*', '*_hull_volumes.csv'))])

    if not os.path.isdir(args.output_dir): 
        os.makedirs(args.output_dir) 

    df.to_csv(os.path.join(args.output_dir, ''.join([args.file_name, '.csv'])), index=False)
    
        
    
    


# --------------------------------------------------
if __name__ == '__main__':
    main()

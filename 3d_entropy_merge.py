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

    parser.add_argument('-ie',
                        '--input_dir_entropy',
                        help='Directory containing individual plant subdirectories.',
                        metavar='str',
                        type=str,
                        default='individual_plants_out/combined_pointclouds')

    parser.add_argument('-is',
                        '--input_dir_stats',
                        help='Directory containing individual plant subdirectories.',
                        metavar='str',
                        type=str,
                        default='individual_plants_out/plant_reports')

    parser.add_argument('-d',
                        '--date',
                        help='Collection date for the scan.',
                        metavar='str',
                        type=str,
                        required=True)

    return parser.parse_args()


# --------------------------------------------------
def generate_tda_csv(date, in_dir, out_dir):

    df = pd.concat([pd.read_csv(csv) for csv in glob.glob(os.path.join(in_dir, '*', '*_hull_volumes.csv'))])

    if not os.path.isdir(out_dir): 
        os.makedirs(out_dir) 

    df.to_csv(os.path.join(out_dir, ''.join([date, '_tda', '.csv'])), index=False)


# --------------------------------------------------
def generate_stats_csv(date, in_dir, out_dir):

    df_list = []

    if not os.path.isdir(out_dir): 
        os.makedirs(out_dir) 

    for csv in glob.glob(os.path.join(in_dir, '*', '*pointcloud_stats.csv')):
        plant_name = os.path.split(os.path.dirname(csv))[-1]
        temp_df = pd.read_csv(csv)
        temp_df['plant_name'] = plant_name
        temp_df = temp_df.set_index('plant_name')
        df_list.append(temp_df)
    df = pd.concat(df_list)

    try:
        df = df.drop('Unnamed: 0', axis=1)
    except:
        df = df

    df.to_csv(os.path.join(out_dir, ''.join([date, '_stats', '.csv'])), index=True)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    generate_tda_csv(args.date, args.input_dir_entropy, args.date)
    generate_stats_csv(args.date, args.input_dir_stats, args.date)


# --------------------------------------------------
if __name__ == '__main__':
    main()

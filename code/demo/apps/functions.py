# Functions to facilitate demo

import pandas as pd
import numpy as np
import pickle 

# Read in the pickle file of the feature space (columns names of X feature matrix)
with open('../../../data/data_subsets/X_cols.pkl', 'rb') as pickle_in:
    X_cols = pickle.load(pickle_in)

all_X_cols = X_cols    

top_notes_demo = ['top_0_amalfi_lemon',  'top_0_pink_grapefruit', 'top_1_watermelon',
                  'top_1_mint', 'top_1_earl_grey_tea', 'top_1_champagne', 'top_1_creme_brulee',
                  'top_1_pepper', 'top_1_nutmeg', 'top_1_teak_wood', 'top_1_pine_needles', 'top_1_mountain_air']


# Read in the mini dataframe including top notes listed in top_notes_demo and their corresponding middle and base notes
demo_df = pd.read_csv('../../../data/data_subsets/demo/demo_df.csv')

def get_mid_and_base_notes():

    top_note_sel_top = [col for col in demo_df.columns if ('top' in col) & ('none' not in col)]
    mid_note_sel_top = [col for col in all_X_cols if ('middle' in col) & ('none' not in col)]
    base_note_sel_top = [col for col in all_X_cols if ('base' in col) & ('none' not in col)]
    
    return mid_note_sel_top, base_note_sel_top

def make_a_fragrance(top):
    
   # Grab all columns in X feature space
    all_X_cols = X_cols
    
    # Create a dataframe with the same features as X, set all values to zero
    notes_df = pd.DataFrame(columns = all_X_cols)
    notes_df = notes_df.append([0]).fillna(0).drop(columns = 0)
        
    top = top
    
    """Though we'd normally set a seed for reproducibility, that's not the case here because randomly selected variables are part of the fun for the demo!"""
    # np.random.seed(42)

    # Select a middle and base note randomly
    middle_random = np.random.choice(get_mid_and_base_notes()[0])
    base_random = np.random.choice(get_mid_and_base_notes()[1])

    print(f'Random middle note: {middle_random}')
    print(f'Random base note: {base_random}')

    notes_df[top] = 1
    notes_df[middle_random] = 1
    notes_df[base_random] = 1
    
    # print(notes_df.sum().sum())           # should be 3

    # Sanitize notes names so they're presentable
    # return middle_random[12:].replace('_', ' ').capitalize()
    
    top_return = f'{top}'
    mid_return = f'{middle_random}'
    base_return = f'{base_random}'
    return top_return, mid_return, base_return
    # return f'{top[0]} (top note) + {middle_random} (middle note) + {base_random} (base note)'
    
    # Save the synthetic dataframe as a pickle file
    with open('../../../data/data_subsets/demo/synth_df.pkl', 'wb') as pickle_out:
        pickle_out = pickle.dump(notes_df, pickle_out)    
    
    # return notes_df
    

# Example
# make_a_fragrance('top_1_mountain_air')
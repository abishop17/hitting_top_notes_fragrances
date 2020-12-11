# README

# Capstone Project: Hitting the Top Notes

## Modeling on fragrance notes to classify ratings

## Problem statement: Are the scents in fragrances good predictors of average customer ratings?

**Data source:** [Fragrances - Notes and User Rating](https://www.kaggle.com/sagikeren88/fragrances-and-perfumes) | `notes_and_user_ratings.csv`
>An enhanced dataset with scent breakdown, user ranking and segmentation and many more<br>
>Perfume notes are divided into 3 main notes - Top, Middle (Heart) and Base.


**Project goal and evaluation:** The goal of the project is to use different supervised and unsupervised modeling techniques to make a determination about the problem statement, using accuracy scores and silhouette scores.

### Background: The interest area

Innovative combinations of diverse pieces / features are a natural point of interest for me. I am avidly interested in applications to create tangible / sense-stimulating products. An audiovisual example is multimedia art; a visual-tactile example is patchwork quilting that uses atypical fabric pairings (such as, say, a polyester holographic utility fabric and leather). 

Materializing meaningful business applications is the target of the creative product design experience. How do we use a data-supported framework to channel the mix 'n match mentality towards positive business outcomes (like high customer ratings)?

I will begin to explore this question through EDA and modeling.


## The data

### Data dimensions

The original raw dataset consisted of about 42,000 rows and 155 columns. After preprocessing, as detailed below, the column count ballooned to 6,753 columns (due to the multitude of unique notes with different prefixes).

### Background: The data source

## Methodology

**Handling of nulls**: The nulls in the dataset came in the form of the word "none" after the note name's prefix. After creating dummies, I imputed zero values to the "none"-nulls.

## Preprocessing

Tasks included:

**Extract top, middle and base notes from mixed columns**: The original dataset had four columns with a mix of top, middle and base notes and different prefixes (see variables below). I wrote a function to loop through the columns to extract the unique labels, which I broke out into new columns, grouped by the prefix variables.

![orig_cols_with_top_mid_base_notes](https://github.com/abishop17/fragrance_analysis_capstone/blob/figures/orig_cols_with_top_mid_base_notes.png)

top_cols = [`top_0`], [`top_1`], ['`top_2`'], ['`top_3`']

middle_cols = ['`middle_0`'], ['`middle_0_1`'], ['`middle_1`'], ['`middle_0_2`'], ['`middle_1_1`'], ['`middle_2`']

base_cols = ['`base_0`'], ['`base_0_1`'], ['`base_1`']


![extracted_cols_with_top_mid_base_notes](https://git.generalassemb.ly/abishop17/project_3/blob/figures/extracted_cols_with_top_mid_base_notes.png)


**Dummify top, middle and base notes**: The data included multiple top notes for many fragrances, which is consistent with fragrance formulation practices. There were significantly fewer datapoints on middle and base notes. This fact about the data profile immediately gave rise to a project focus around top notes.


![notes_counts_overall](https://git.generalassemb.ly/abishop17/project_3/blob/figures/notes_counts_overall.png)

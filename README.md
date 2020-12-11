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

Materializing meaningful business applications is the target of the creative product design experience. How do we use a data-supported framework to gear the mix 'n match mentality towards positive business outcomes (like high customer ratings)?

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

![orig_cols_with_top_mid_base_notes](https://github.com/abishop17/fragrance_analysis_capstone/blob/main/figures/orig_cols_with_top_mid_base_notes.png)

top_cols = [`top_0`], [`top_1`], ['`top_2`'], ['`top_3`']

middle_cols = ['`middle_0`'], ['`middle_0_1`'], ['`middle_1`'], ['`middle_0_2`'], ['`middle_1_1`'], ['`middle_2`']

base_cols = ['`base_0`'], ['`base_0_1`'], ['`base_1`']


![extracted_cols_with_top_mid_base_notes](https://github.com/abishop17/fragrance_analysis_capstone/blob/main/figures/extracted_cols_with_top_mid_base_notes.png)


**Dummify top, middle and base notes**: The data included multiple top notes for many fragrances, which is consistent with fragrance formulation practices. There were significantly fewer datapoints on middle and base notes. This fact about the data profile immediately gave rise to a project focus around top notes.

**Bin average ratings into ratings categories**: I binned the average ratings into 5 categories (for ratings 1 through 5) for simplicity. Before binning, I considered using the original two-decimal-point ratings in a regression task, but decided against it since ratings are not true continuous numbers. The volume of discrete values would have meant a many-multiclass classification task, and this seemed unnecessary.

![notes_counts_overall](https://github.com/abishop17/fragrance_analysis_capstone/blob/main/figures/notes_counts_overall.png)

## EDA

The distribution of average ratings approaches normal, with some left skew.
![distn_average_rating](https://github.com/abishop17/fragrance_analysis_capstone/blob/main/figures/distn_average_rating.png)

## Metrics

* 54% is the baseline accuracy percentage we compare with the model's accuracy.

* If the model does better than the baseline, then it is better than null model (predicting the majority class, fragrances with a binned average rating of 4).

* I chose accuracy because I did not prioritize one class over another.

## Modeling and Results

* The features I used consisted of the full set of top, middle and base notes. One reason I trained on all the notes was for demo purposes: I wanted to be able to predict the average rating with a complete set of notes, one from each of the three categories. However, given the class imbalance between top notes on the one hand and middle and base notes on the other, it would be worth it to use only the top notes as a feature set for modeling. 

* I chose to work with logistic regression with and without Principal Component Analysis (PCA) and Random Forest because I prioritized interpretability of results. With logistic regression, the ridge regularization selected (after GridSearch) took care of the correlation among features. With Random Forest, I hoped to reduce variance and decorrelate the notes features.

* Logistic regression used in a pipeline along with PCA, performed very poorly, with an accuracy score of 56.4% on test data (just a hair's width of improvement over the baseline). On this model, the feature set was reduced by PCA to just 80 out of the dummified 6k columns.

* The best performing model, Random Forest (with GridSearchCV in a pipeline), still didn't perform well, with an accuracy score on test data of 60%. It overfit to the training data a lot (score on train data was 92%). I still used train data for purposes of inference (see below).

## Conclusions

**Holding all else constant, the `woody` note category is a .06 times evidence that we can predict ratings classes accurately using a Random Forest model.**

The raw fragrance note data (dummified notes with prefixes and ungrouped into informative categories) are a weak predictor of customer ratings. See the "Next steps" section below for ways I plan to address this.

## Demo

Using the [Streamlit](https://github.com/streamlit/streamlit) web app framework, I deployed a minimally viable app to make a perfume on the spot. It is geared to be a crowdsourcing app to initiate the product development process. This is the mix 'n match mentality in action. See the app flow below (screenshots taken from the app launched from my desktop):

The header:

![demo_header](https://github.com/abishop17/fragrance_analysis_capstone/blob/main/figures/demo/demo_header.png)

The user makes a selection of a single top note from a static list taken directly from the dataset. A script randomly generates a middle and base note from those classes of features from within the dataset:

![demo_select_top_notes_and_make_a_fragrance](https://github.com/abishop17/fragrance_analysis_capstone/blob/main/figures/demo/demo_select_top_notes_and_make_a_fragrance.png)

The script generates a prediction and provides a user feedback field for whether the user would like to wear the fragrance if offered a sample.

![demo_prediction_and_user_feedback](https://github.com/abishop17/fragrance_analysis_capstone/blob/main/figures/demo/demo_prediction_and_user_feedback.png)


## Next steps

* **The demo**: I definitely plan to write the script to output middle and base notes that correspond better with the top note selected (it is completely random right now).

* **Bring in additional data sources to enrich the existing data**: The basis for the correspondence of middle and base notes with top notes will likely involve the use of an additional data or reference source with info about notes families and fragrance chemistry. I'd like to use the families as a way to group middle and base notes, and from those groups, randomly output a note as a pairing with the top note selected by the user.

With this I will address the raw notes data's weak predictor status of ratings, and thereby I hope to improve the models' performance.

* **Product development system**: I'd like to leverage decision tree modeling on training data to get insight on a potential product development routes.




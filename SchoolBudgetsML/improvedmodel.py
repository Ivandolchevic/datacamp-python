from multilabel import  multilabel_train_test_split
import pandas as pd
import numpy as np
import random
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

NUMERIC_COLUMNS = ['FTE', 'Total']
LABELS = ['Function',
     'Use',
     'Sharing',
     'Reporting',
     'Student_Type',
     'Position_Type',
     'Object_Type',
     'Pre_K',
     'Operating_Status']
EXTRAS = ['Unnamed: 0']

# Define combine_text_columns()
def combine_text_columns(data_frame, to_drop=NUMERIC_COLUMNS + LABELS):
    """ converts all text in each row of data_frame to single vector """

    # Drop non-text columns that are in the df
    to_drop = set(to_drop) & set(data_frame.columns.tolist())
    text_data = data_frame.drop(to_drop, axis=1)

    # Replace nans with blanks
    text_data.fillna('', inplace=True)

    # Join all text items in a row that have a space in between
    return text_data.apply(lambda x: " ".join(x), axis=1)

def getSampleDF():
    DF_SIZE = 1000

    text_values = ['', 'foo', 'bar', 'foo bar', 'bar foo', '']
    label_values = ['a', 'b']

    numerics = np.random.rand(DF_SIZE) * 70 - 35
    with_missings = [v if np.random.randint(0, 6) != 5 else np.nan for v in np.random.rand(DF_SIZE) * 7 - 6]
    texts = [text_values[index] for index in np.random.randint(0, 6, DF_SIZE)]
    labels = [label_values[index] for index in np.random.randint(0, 2, DF_SIZE)]
    df = pd.DataFrame({'numeric': numerics, 'text': texts, 'with_missing': with_missings, 'label': labels})
    return df

def getTrainingData():
    df = pd.read_csv("TrainingDataSample.csv")
    del df['Unnamed: 0']
    df.drop(df[df['FTE'] > 1.04].index, inplace=True)
    return df

def fnInstantiatePipeline():
    sample_df = getSampleDF()

    # Import Pipeline
    from sklearn.pipeline import Pipeline

    # Import other necessary modules
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.multiclass import OneVsRestClassifier

    # Split and select numeric data only, no nans
    X_train, X_test, y_train, y_test = train_test_split(sample_df[['numeric']],
                                                        pd.get_dummies(sample_df['label']),
                                                        random_state=22)

    # Instantiate Pipeline object: pl
    pl = Pipeline([
        ('clf', OneVsRestClassifier(LogisticRegression()))
    ])

    # Fit the pipeline to the training data
    pl.fit(X_train, y_train)

    # Compute and print accuracy
    accuracy = pl.score(X_test, y_test)
    print("\nAccuracy on sample data - numeric, no nans: ", accuracy)

def fnPreprocessingNumericFeatures():
    sample_df = getSampleDF()

    # Import the Imputer object
    from sklearn.preprocessing import Imputer

    # Create training and test sets using only numeric data
    X_train, X_test, y_train, y_test = train_test_split(sample_df[['numeric', 'with_missing']],
                                                        pd.get_dummies(sample_df['label']),
                                                        random_state=456)

    # Insantiate Pipeline object: pl
    pl = Pipeline([
        ('imp', Imputer()),
        ('clf', OneVsRestClassifier(LogisticRegression()))
    ])

    # Fit the pipeline to the training data
    pl.fit(X_train, y_train)

    # Compute and print accuracy
    accuracy = pl.score(X_test, y_test)
    print("\nAccuracy on sample data - all numeric, incl nans: ", accuracy)

def fnProcessingTextFeatures():
    sample_df = getSampleDF()

    # Import the CountVectorizer
    from sklearn.feature_extraction.text import CountVectorizer

    # Split out only the text data
    X_train, X_test, y_train, y_test = train_test_split(sample_df['text'],
                                                        pd.get_dummies(sample_df['label']),
                                                        random_state=456)

    # Instantiate Pipeline object: pl
    pl = Pipeline([
        ('vec', CountVectorizer()),
        ('clf', OneVsRestClassifier(LogisticRegression()))
    ])

    # Fit to the training data
    pl.fit(X_train, y_train)

    # Compute and print accuracy
    accuracy = pl.score(X_test, y_test)
    print("\nAccuracy on sample data - just text data: ", accuracy)


def fnFunctionTransformer():
    sample_df = getSampleDF()

    # Import FunctionTransformer
    from sklearn.preprocessing import FunctionTransformer

    # Obtain the text data: get_text_data
    get_text_data = FunctionTransformer(lambda x: x['text'], validate=False)

    # Obtain the numeric data: get_numeric_data
    get_numeric_data = FunctionTransformer(lambda x: x[['numeric', 'with_missing']], validate=False)

    # Fit and transform the text data: just_text_data
    just_text_data = get_text_data.fit_transform(sample_df)

    # Fit and transform the numeric data: just_numeric_data
    just_numeric_data = get_numeric_data.fit_transform(sample_df)

    # Print head to check results
    print('Text Data')
    print(just_text_data.head())
    print('\nNumeric Data')
    print(just_numeric_data.head())

def fnFeaturesUnion():
    sample_df = getSampleDF()

    # Import the CountVectorizer
    from sklearn.feature_extraction.text import CountVectorizer

    # Import the Imputer object
    from sklearn.preprocessing import Imputer

    # Import FunctionTransformer
    from sklearn.preprocessing import FunctionTransformer

    # Obtain the text data: get_text_data
    get_text_data = FunctionTransformer(lambda x: x['text'], validate=False)

    # Obtain the numeric data: get_numeric_data
    get_numeric_data = FunctionTransformer(lambda x: x[['numeric', 'with_missing']], validate=False)


    # Import FeatureUnion
    from sklearn.pipeline import FeatureUnion

    # Split using ALL data in sample_df
    X_train, X_test, y_train, y_test = train_test_split(sample_df[['numeric', 'with_missing', 'text']],
                                                        pd.get_dummies(sample_df['label']),
                                                        random_state=22)

    # Create a FeatureUnion with nested pipeline: process_and_join_features
    process_and_join_features = FeatureUnion(
        transformer_list=[
            ('numeric_features', Pipeline([
                ('selector', get_numeric_data),
                ('imputer', Imputer())
            ])),
            ('text_features', Pipeline([
                ('selector', get_text_data),
                ('vectorizer', CountVectorizer())
            ]))
        ]
    )

    # Instantiate nested pipeline: pl
    pl = Pipeline([
        ('union', process_and_join_features),
        ('clf', OneVsRestClassifier(LogisticRegression()))
    ])

    # Fit pl to the training data
    pl.fit(X_train, y_train)

    # Compute and print accuracy
    accuracy = pl.score(X_test, y_test)
    print("\nAccuracy on sample data - all data: ", accuracy)

def fnFunctionTransformer():
    df = getTrainingData()

    # Import the CountVectorizer
    from sklearn.feature_extraction.text import CountVectorizer

    # Import the Imputer object
    from sklearn.preprocessing import Imputer

    # Import FunctionTransformer
    from sklearn.preprocessing import FunctionTransformer

    # Import FeatureUnion
    from sklearn.pipeline import FeatureUnion

    # Get the dummy encoding of the labels
    dummy_labels = pd.get_dummies(df[LABELS])

    # Get the columns that are features in the original df
    NON_LABELS = [c for c in df.columns if c not in LABELS]

    # Split into training and test sets
    X_train, X_test, y_train, y_test = multilabel_train_test_split(df[NON_LABELS],
                                                                   dummy_labels,
                                                                   0.2,
                                                                   seed=123)

    # Preprocess the text data: get_text_data
    get_text_data = FunctionTransformer(combine_text_columns, validate=False)

    # Preprocess the numeric data: get_numeric_data
    get_numeric_data = FunctionTransformer(lambda x: x[NUMERIC_COLUMNS], validate=False)

    # Complete the pipeline: pl
    pl = Pipeline([
        ('union', FeatureUnion(
            transformer_list=[
                ('numeric_features', Pipeline([
                    ('selector', get_numeric_data),
                    ('imputer', Imputer())
                ])),
                ('text_features', Pipeline([
                    ('selector', get_text_data),
                    ('vectorizer', CountVectorizer())
                ]))
            ]
        )),
        ('clf', OneVsRestClassifier(LogisticRegression()))
    ])

    # Fit to the training data
    pl.fit(X_train, y_train)

    # Compute and print accuracy
    accuracy = pl.score(X_test, y_test)
    print("\nAccuracy on budget dataset: ", accuracy)

fnFunctionTransformer()

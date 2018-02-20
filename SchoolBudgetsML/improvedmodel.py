from multilabel import  multilabel_train_test_split
import pandas as pd
import numpy as np
import random

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

def getTrainingData():
    df = pd.read_csv("TrainingDataSample.csv")
    del df['Unnamed: 0']
    df.drop(df[df['FTE'] > 1.04].index, inplace=True)
    return df

def fnInstantiatePipeline():
    # Import Pipeline
    from sklearn.pipeline import Pipeline

    # Import other necessary modules
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression
    from sklearn.multiclass import OneVsRestClassifier

    # Split and select numeric data only, no nans
    X_train, X_test, y_train, y_test = train_test_split(____,
                                                        pd.get_dummies(sample_df['label']),
                                                        random_state=22)

    # Instantiate Pipeline object: pl
    pl = Pipeline([
        (____, ____)
    ])

    # Fit the pipeline to the training data
    pl.fit(____, ____)

    # Compute and print accuracy
    accuracy = pl.score(____, ____)
    print("\nAccuracy on sample data - numeric, no nans: ", accuracy)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

def fnInit():
    df = pd.read_csv('gm_2008_region.csv')

    # Create dummy variables with drop_first=True: df_region
    df_region = pd.get_dummies(df, drop_first=True)
    y = df_region['life']
    del df_region['life']
    X = df_region
    return X,y

def fnExploring():

    # Read 'gapminder.csv' into a DataFrame: df
    df = pd.read_csv('gm_2008_region.csv')

    # Create a boxplot of life expectancy per region
    df.boxplot('life', 'Region', rot=60)

    # Show the plot
    plt.show()

def fnCreateDummies():
    # Read 'gapminder.csv' into a DataFrame: df
    df = pd.read_csv('gm_2008_region.csv')

    # Create dummy variables: df_region
    df_region = pd.get_dummies(df)

    # Print the columns of df_region
    print(df_region.columns)

    # Create dummy variables with drop_first=True: df_region
    df_region = pd.get_dummies(df, drop_first=True)

    # Print the new columns of df_region
    print(df_region.columns)

def fnRidgeRegression():
    X,y= fnInit()

    # Import necessary modules
    from sklearn.linear_model import Ridge
    from sklearn.model_selection import cross_val_score

    # Instantiate a ridge regressor: ridge
    ridge = Ridge(alpha=0.5, normalize=True)

    # Perform 5-fold cross-validation: ridge_cv
    ridge_cv = cross_val_score(ridge, X, y, cv=5)

    # Print the cross-validated scores
    print(ridge_cv)


def fnDroppingMissingData():
    df = pd.read_csv('house-votes-84.csv')
    print(df.head())

    # Convert '?' to NaN
    df[df == '?'] = np.nan

    # Print the number of NaNs
    print(df.isnull().sum())

    # Print shape of original DataFrame
    print("Shape of Original DataFrame: {}".format(df.shape))

    # Drop missing values and print shape of new DataFrame
    df = df.dropna()

    # Print shape of new DataFrame
    print("Shape of DataFrame After Dropping All Rows with Missing Values: {}".format(df.shape))


def fnImputingMissingInPipeline():
    # Import the Imputer module
    from sklearn.preprocessing import Imputer
    from sklearn.svm import SVC

    # Setup the Imputation transformer: imp
    imp = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)

    # Instantiate the SVC classifier: clf
    clf = SVC()

    # Setup the pipeline with the required steps: steps
    steps = [('imputation', imp),
             ('SVM', clf)]

def fnInitVotes():
    df_votes = pd.read_csv('house-votes-84.csv')
    y = df_votes.iloc[:,0]

    X = df_votes.drop(df_votes.columns[[0]], axis=1)

    X.replace(
        to_replace=['y'],
        value=1,
        inplace=True
    )

    X.replace(
        to_replace=['n'],
        value=0,
        inplace=True)

    X.replace(
        to_replace=['?'],
        value=np.nan,
        inplace=True)
    return X,y

def fnVotesPipeline():
    X,y = fnInitVotes()

    # Import necessary modules
    from sklearn.preprocessing import Imputer
    from sklearn.pipeline import Pipeline
    from sklearn.svm import SVC

    # Setup the pipeline steps: steps
    steps = [('imputation', Imputer(missing_values='NaN', strategy='most_frequent', axis=0)),
             ('SVM', SVC())]

    # Create the pipeline: pipeline
    pipeline = Pipeline(steps)

    # Create training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Fit the pipeline to the train set
    pipeline.fit(X_train, y_train)

    # Predict the labels of the test set
    y_pred = pipeline.predict(X_test)

    print("X original format: {}".format(X.shape))
    # Compute metrics
    print(classification_report(y_test, y_pred))

def fnInitWhiteWineQuality():
    df = pd.read_csv('white-wine.csv')

    # if 'quality' is less than 5 then the target variable is 1
    df.loc[df['quality'] < 5, 'quality'] = 1
    df.loc[df['quality'] >= 5, 'quality'] = 0

    y = df['quality']
    del df['quality']

    X = df

    return X,y

def fnCenteringAndScaling():
    X,y = fnInitWhiteWineQuality()

    # Import scale
    from sklearn.preprocessing import scale

    # Scale the features: X_scaled
    X_scaled = scale(X)

    # Print the mean and standard deviation of the unscaled features
    print("Mean of Unscaled Features: {}".format(np.mean(X)))
    print("Standard Deviation of Unscaled Features: {}".format(np.std(X)))

    # Print the mean and standard deviation of the scaled features
    print("Mean of Scaled Features: {}".format(np.mean(X_scaled)))
    print("Standard Deviation of Scaled Features: {}".format(np.std(X_scaled)))

def fnCenteringAndScalingInPipeline():
    X, y = fnInitWhiteWineQuality()

    # Import the necessary modules
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import Pipeline

    # Setup the pipeline steps: steps
    steps = [('scaler', StandardScaler()),
             ('knn', KNeighborsClassifier())]

    # Create the pipeline: pipeline
    pipeline = Pipeline(steps)

    # Create train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=42)

    # Fit the pipeline to the training set: knn_scaled
    knn_scaled = pipeline.fit(X_train,y_train)

    # Instantiate and fit a k-NN classifier to the unscaled data
    knn_unscaled = KNeighborsClassifier().fit(X_train, y_train)

    # Compute and print metrics
    print('Accuracy with Scaling: {}'.format(knn_scaled.score(X_test, y_test)))
    print('Accuracy without Scaling: {}'.format(knn_unscaled.score(X_test, y_test)))

def fnPipelineForClassification():
    from sklearn.svm import SVC
    from sklearn.preprocessing import StandardScaler

    X,y = fnInitWhiteWineQuality()

    # Setup the pipeline
    steps = [('scaler', StandardScaler()),
             ('SVM', SVC())]

    pipeline = Pipeline(steps)

    # Specify the hyperparameter space
    parameters = {'SVM__C': [1, 10, 100],
                  'SVM__gamma': [0.1, 0.01]}

    # Create train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=21)

    # Instantiate the GridSearchCV object: cv
    cv = GridSearchCV(pipeline, parameters)

    # Fit to the training set
    cv.fit(X_train, y_train)

    # Predict the labels of the test set: y_pred
    y_pred = cv.predict(X_test)

    # Compute and print metrics
    print("Accuracy: {}".format(cv.score(X_test, y_test)))
    print(classification_report(y_test, y_pred))
    print("Tuned Model Parameters: {}".format(cv.best_params_))


def fnPipelineForRegression():
    from sklearn.preprocessing import Imputer
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import ElasticNet

    X,y = fnInit()

    # Setup the pipeline steps: steps
    steps = [('imputation', Imputer(missing_values='NaN', strategy='mean', axis=0)),
             ('scaler', StandardScaler()),
             ('elasticnet', ElasticNet())]

    # Create the pipeline: pipeline
    pipeline = Pipeline(steps)

    # Specify the hyperparameter space
    parameters = {'elasticnet__l1_ratio': np.linspace(0, 1, 30)}

    # Create train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4, random_state=42)

    # Create the GridSearchCV object: gm_cv
    gm_cv = GridSearchCV(pipeline, parameters)

    # Fit to the training set
    gm_cv.fit(X_train, y_train)

    # Compute and print the metrics
    r2 = gm_cv.score(X_test, y_test)
    print("Tuned ElasticNet Alpha: {}".format(gm_cv.best_params_))
    print("Tuned ElasticNet R squared: {}".format(r2))


fnPipelineForRegression()

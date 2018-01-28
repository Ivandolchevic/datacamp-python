import pandas as pd
import matplotlib.pyplot as plt

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


fnRidgeRegression()
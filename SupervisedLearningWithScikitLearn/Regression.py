
print("---------------------------------------------------")
print("  Importing data for supervised learning ")
print("---------------------------------------------------")

def fnZero():
    import pandas as pd

    # load the datas
    df = pd.read_csv('gapminder.csv')
    y = df['life'].values.reshape(-1, 1)
    del df['life']
    del df['Region']
    X = df.values
    return X,y

def fnOne():
    # Import numpy and pandas
    import numpy as np
    import pandas as pd

    # Read the CSV file into a DataFrame: df
    df = pd.read_csv('gapminder.csv')

    # Create arrays for features and target variable
    y = df['life']
    X = df['fertility']

    print("y type: ", type(y))
    print("X type: ", type(X))


    # Print the dimensions of X and y before reshaping
    print("Dimensions of y before reshaping: {}".format(y.shape))
    print("Dimensions of X before reshaping: {}".format(X.shape))

    # Reshape X and y
    y = y.values.reshape(-1, 1)
    X = X.values.reshape(-1, 1)

    print("y type: ", type(y))
    print("X type: ", type(X))


    # Print the dimensions of X and y after reshaping
    print("Dimensions of y after reshaping: {}".format(y.shape))
    print("Dimensions of X after reshaping: {}".format(X.shape))

    print("\n")

print("---------------------------------------------------")
print("  Exploring the Gapminder data ")
print("---------------------------------------------------")

def fnTwo():
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

    # load the dataframe
    df = pd.read_csv('gapminder.csv')
    sns.heatmap(df.corr(), square=True, cmap='RdYlGn')
    plt.show()

    print(df.info())
    print(df.head())
    print(df.describe())


def fnThree():
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import seaborn as sns

    df = pd.read_csv('gapminder.csv')

    sns.lmplot(x='fertility', y='life', data=df)
    plt.show()

def fnFour():
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    # Import LinearRegression
    from sklearn.linear_model import LinearRegression

    # Create the regressor: reg
    reg = LinearRegression()

    # load the datas
    df = pd.read_csv('gapminder.csv')
    X_fertility = df['fertility'].values.reshape(-1, 1)
    y = df['life'].values.reshape(-1, 1)

    # Create the prediction space
    prediction_space = np.linspace(min(X_fertility), max(X_fertility)).reshape(-1,1)

    print('type of prediction_space:', type(prediction_space))
    print('shape of prediction_space:', prediction_space.shape)
    print('prediction_space:', prediction_space.shape)

    # Fit the model to the data
    reg.fit(X_fertility,y)

    # Compute predictions over the prediction space: y_pred
    y_pred = reg.predict(prediction_space)

    # Print R^2
    print(reg.score(X_fertility, y))

    # Plot regression line
    plt.plot(prediction_space, y_pred, color='black', linewidth=3)
    plt.plot(X_fertility, y,  'ro')
    plt.show()

def fnFive():
    # Import necessary modules
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error
    from sklearn.model_selection import train_test_split
    import pandas as pd
    import numpy as np

    # load the datas
    df = pd.read_csv('gapminder.csv')
    y = df['life'].values.reshape(-1, 1)
    del df['life']
    del df['Region']
    X = df.values

    # Create training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Create the regressor: reg_all
    reg_all = LinearRegression()

    # Fit the regressor to the training data
    reg_all.fit(X_train, y_train)

    # Predict on the test data: y_pred
    y_pred = reg_all.predict(X_test)

    # Compute and print R^2 and RMSE
    print("R^2: {}".format(reg_all.score(X_test, y_test)))
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    print("Root Mean Squared Error: {}".format(rmse))

def fnSix():
    import numpy as np
    import pandas as pd
    # load the datas
    df = pd.read_csv('gapminder.csv')
    y = df['life'].values.reshape(-1, 1)
    del df['life']
    del df['Region']
    X = df.values

    # Import the necessary modules
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import cross_val_score

    # Create a linear regression object: reg
    reg = LinearRegression()

    # Compute 5-fold cross-validation scores: cv_scores
    cv_scores = cross_val_score(reg, X, y, cv=5)

    # Print the 5-fold cross-validation scores
    print(cv_scores)

    print("Average 5-Fold CV Score: {}".format(np.mean(cv_scores)))

def fnSeven():
    import timeit
    setup = '''
import numpy as np
import pandas as pd
df = pd.read_csv('gapminder.csv')
y = df['life'].values.reshape(-1, 1)
del df['life']
del df['Region']
X = df.values
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
reg = LinearRegression()
'''
    print(timeit.timeit(stmt="cross_val_score(reg, X, y, cv=3)", setup=setup,number=100))
    print(timeit.timeit(stmt="cross_val_score(reg, X, y, cv=10)", setup=setup, number=100))



def fnHeight():
    import numpy as np
    import pandas as pd
    # load the datas
    df = pd.read_csv('gapminder.csv')
    y = df['life'].values.reshape(-1, 1)
    del df['life']
    del df['Region']
    X = df.values

    # Import necessary modules
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import cross_val_score

    # Create a linear regression object: reg
    reg = LinearRegression()

    cvscores_3 = cross_val_score(reg, X, y, cv=3)
    print(np.mean(cvscores_3))

    # Perform 10-fold CV
    cvscores_10 = cross_val_score(reg, X, y, cv=10)
    print(np.mean(cvscores_10))

def fnNine():
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.read_csv('gapminder.csv')
    df_columns = df.drop(labels=['life','Region'], axis=1).columns

    X,y = fnZero()

    # Import Lasso
    from sklearn.linear_model import Lasso

    # Instantiate a lasso regressor: lasso
    lasso = Lasso(alpha=0.4, normalize=True)

    # Fit the regressor to the data
    lasso.fit(X, y)

    # Compute and print the coefficients
    lasso_coef = lasso.coef_
    print(lasso_coef)

    # Plot the coefficients
    from matplotlib import rcParams
    rcParams.update({'figure.autolayout': True})
    plt.plot(range(len(df_columns)), lasso_coef)
    plt.xticks(range(len(df_columns)), df_columns.values, rotation=60)
    plt.margins(0.02)
    plt.show()

def display_plot(cv_scores, cv_scores_std, alpha_space):
    import matplotlib.pyplot as plt
    import numpy as np

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(alpha_space, cv_scores)

    std_error = cv_scores_std / np.sqrt(10)

    ax.fill_between(alpha_space, cv_scores + std_error, cv_scores - std_error, alpha=0.2)
    ax.set_ylabel('CV Score +/- Std Error')
    ax.set_xlabel('Alpha')
    ax.axhline(np.max(cv_scores), linestyle='--', color='.5')
    ax.set_xlim([alpha_space[0], alpha_space[-1]])
    ax.set_xscale('log')
    plt.show()

def fnTen():
    import numpy as np
    X,y = fnZero()

    # Import necessary modules
    from sklearn.linear_model import Ridge
    from sklearn.model_selection import cross_val_score

    # Setup the array of alphas and lists to store scores
    alpha_space = np.logspace(-4, 0, 50)
    ridge_scores = []
    ridge_scores_std = []

    # Create a ridge regressor: ridge
    ridge = Ridge(normalize=True)

    # Compute scores over range of alphas
    for alpha in alpha_space:
        # Specify the alpha value to use: ridge.alpha
        ridge.alpha = alpha

        # Perform 10-fold CV: ridge_cv_scores
        ridge_cv_scores = cross_val_score(ridge, X, y, cv=10)

        # Append the mean of ridge_cv_scores to ridge_scores
        ridge_scores.append(np.mean(ridge_cv_scores))

        # Append the std of ridge_cv_scores to ridge_scores_std
        ridge_scores_std.append(np.std(ridge_cv_scores))

    # Display the plot
    display_plot(ridge_scores, ridge_scores_std, alpha_space)

fnTen()